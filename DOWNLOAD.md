Dataset **Skin Cancer: HAM10000** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/9/9/E6/KArHitfX9jzRrI4jx1bnTqZnqKftxaCm5Z4p30VqJg4EdhjgCB8QGj6kDr1YpM4mxbhA6pS4q6At09C1lZa588xIbbALzyPXkvYlnmfOMEsmcMFPNs7xLxtWgmOa.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Skin Cancer: HAM10000', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification/download?datasetVersionNumber=2).