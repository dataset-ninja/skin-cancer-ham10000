import csv
import os
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import file_exists, get_file_ext, get_file_name, get_file_size
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)
        fsize = get_file_size(local_path)
        with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer..", total=fsize) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = get_file_size(local_path)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer {local_path}...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/iwatkot/Downloads/ninja/datasets/skincancer"
    images_folder_name = "images"
    masks_folder_name = "masks"
    classes_data_file_name = "GroundTruth.csv"
    ds_name = "ds"
    batch_size = 30
    masks_ext = "_segmentation.png"
    images_ext = ".jpg"

    def create_ann(image_path):
        labels = []

        image_name = get_file_name(image_path)
        class_name = image_name_to_class[image_name]
        obj_class = name_to_class[class_name]
        mask_path = os.path.join(masks_path, image_name + masks_ext)

        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            img_height = mask_np.shape[0]
            img_wight = mask_np.shape[1]
            mask = mask_np == 255
            if len(np.unique(mask)) > 1:  # empty mask
                curr_bitmap = sly.Bitmap(mask)
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    name_to_class = {
        "AKIEC": sly.ObjClass("actinic keratoses", sly.Bitmap),
        "BCC": sly.ObjClass("basal cell carcinoma", sly.Bitmap),
        "BKL": sly.ObjClass("benign keratosis-like lesions", sly.Bitmap),
        "DF": sly.ObjClass("dermatofibroma", sly.Bitmap),
        "MEL": sly.ObjClass("melanoma", sly.Bitmap),
        "NV": sly.ObjClass("melanocytic nevi", sly.Bitmap),
        "VASC": sly.ObjClass("vascular lesions", sly.Bitmap),
    }

    index_to_class_name = {1: "MEL", 2: "NV", 3: "BCC", 4: "AKIEC", 5: "BKL", 6: "DF", 7: "VASC"}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(name_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, images_folder_name)
    masks_path = os.path.join(dataset_path, masks_folder_name)
    classes_file_path = os.path.join(dataset_path, classes_data_file_name)

    image_name_to_class = {}
    with open(classes_file_path, "r") as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx == 0:
                continue
            class_index = row.index("1.0")
            image_name_to_class[row[0]] = index_to_class_name[class_index]

    images_names = [
        im_name for im_name in os.listdir(images_path) if get_file_ext(im_name) == images_ext
    ]

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in img_names_batch
        ]
        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
