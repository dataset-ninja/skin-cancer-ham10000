Dataset **Skin cancer HAM10000** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/V/E/dt/75rc87P55oAclezZFCrmeuYzsHikpfh9QblTpRQlsnW6gV16MUTnCgJWkCa9VvbzP64OP25aIR9ExNtITfk0gapm2IbS2qWA97lHLlM5m4V8dsAhjtHUqgenluIW.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Skin cancer HAM10000', dst_path='~/dtools/datasets/Skin cancer HAM10000.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification/download?datasetVersionNumber=2)