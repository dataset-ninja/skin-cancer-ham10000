from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Skin Cancer (HAM10000)"
PROJECT_NAME_FULL: str = "Skin Cancer: HAM10000"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Medical()]
CATEGORY: Category = Category.Medical(is_original_dataset=False, sensitive_content=True)

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2021

HOMEPAGE_URL: str = (
    "https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1532721
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/skin-cancer-ham10000"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification/download?datasetVersionNumber=2"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = [
    "https://www.nature.com/articles/sdata2018161",
    "https://www.nature.com/articles/s41591-020-0942-0",
]
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"Original Data":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T", "GitHub":"https://github.com/ptschandl/HAM10000_dataset"}

CITATION_URL: Optional[str] = "https://github.com/ptschandl/HAM10000_dataset#cite"
AUTHORS: Optional[List[str]] = [
    "Tschandl, Philipp",
    "Cliff Rosendahl",
    "Harald Kittler",
    "Suraj Ghuwalewala",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["ghuwalewalasuraj@gmail.com" ,"philipp.tschandl@meduniwien.ac.at", "harald.kittler@meduniwien.ac.at"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "ViDIR Group in Medical University of Vienna, Austria",
    "University of Queensland, Austria",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.meduniwien.ac.at/vidir",
    "https://www.uq.edu.au/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,        
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
