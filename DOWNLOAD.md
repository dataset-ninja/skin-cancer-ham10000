Dataset **Skin Cancer: HAM10000** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEzMThfU2tpbiBDYW5jZXI6IEhBTTEwMDAwL3NraW4tY2FuY2VyOi1oYW0xMDAwMC1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJ0MG9heU0xaGQrQSs1ZnBDMjc5ei9ncCt5REJDYVBPS1RXeFQ4dkRKZzBVPSJ9)

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