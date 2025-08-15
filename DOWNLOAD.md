Dataset **Skin Cancer: HAM10000** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTMxOF9Ta2luIENhbmNlcjogSEFNMTAwMDAvc2tpbi1jYW5jZXI6LWhhbTEwMDAwLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImQxazJseEQ2SUZCVUs2cFQ0Ym9lOXl0QW1hM1BuUFFBakJzWHFLOXhuakE9In0=?response-content-disposition=attachment%3B%20filename%3D%22skin-cancer%3A-ham10000-DatasetNinja.tar%22)

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