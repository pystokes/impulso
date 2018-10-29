# __impulso__

## Description
Framework for object detection (Ex. faces, captions)  

## Data format
### Structure

```
{IMPULSO_HOME}
  └─org
     ├─train
     │  ├─{image}.jpg
     │  ├─{image}.jpg
     │  ├─...
     │  ├─{image}.jpg
     │  └─bbox.json
     └─train
        ├─{image}.jpg
        ├─{image}.jpg
        ├─{image}.jpg
        ├─...
        ├─{image}.jpg
        └─bbox.json
```

### Input
Locate images in `train` and `test` directories in the above structure.  

### Ground Truth
Ground truth (GT) is defined with `bbox.json` in `train` and `test` directories.  
GT's structure is as follows.  
"BBox" indicates regions of objects.

```
[
    {
        "FileName": "IMAGE_NAME.jpg",
        "BBox": [
            {"Left": 449, "Top": 330, "Width": 122, "Height": 149},
            ...,
            {"Left": 104, "Top": 59, "Width": 235, "Height": 55}
        ]
    },
    ...,
    {
        "FileName": "IMAGE_NAME.jpg",
        "BBox": [
            {"Left": 33, "Top": 20, "Width": 222, "Height": 382},
            ...,
            {"Left": 131, "Top": 151, "Width": 42, "Height": 76}
        ]
    }
]
```

## Output examples
This is the case of face detection.  

![Sample1](https://github.com/pystokes/impulso/blob/master/tmp/output/figures/hamabe_minami_1.jpg)
![Sample2](https://github.com/pystokes/impulso/blob/master/tmp/output/figures/hamabe_minami_2.jpg)
![Sample3](https://github.com/pystokes/impulso/blob/master/tmp/output/figures/hamabe_minami_3.jpg)

## Requirement
Python3.6  
tensorflow-gpu==1.4.0  
Keras==2.1.4  

## Install
```
https://github.com/pystokes/impulso.git
```

## Usage
### Create dataset
```
python impulso.py dataset
```

### Prepare
```
python impulso.py prepare -d DATA-ID
```

### Train
To resume training, specify MODEL-ID.
```
python impulso.py train -e EXPERIMENT-ID [-m MODEL-ID]
```

### Test
```
python impulso.py test -e EXPERIMENT-ID -m MODEL-ID
```

### Predict
```
python impulso.py predict -e EXPERIMENT-ID -m MODEL-ID -x INPUT_DIR -y OUTPUT_DIR
```

## About IDs
`DATA-ID`  
- Published when execute `python impulso.py dataset`

`EXPERIMENT-ID`  
- Published when execute `python impulso.py prepare -d DATA-ID`

`MODEL-ID`  
- Published in saving model
  - MODEL-ID is 70 for sample model (model.00070-0.02-0.00-0.03-0.00.hdf5)

## License
- Permitted: Private Use  
- Forbidden: Commercial Use  

## Specification
### Data to be created with [aggregator.py](https://github.com/pystokes/impulso/blob/master/src/aggregator.py)
- IMPULSO_HOME: Absolute path to directory [impulso.py](https://github.com/pystokes/impulso/blob/master/impulso.py) exists

|Usage phase|Type|Path|
|:---|:---|:---|
|Train|Input|IMPULSO_HOME/datasets/{DATA-ID}/train/x/x.npy
|Train|Ground Truth|IMPULSO_HOME/datasets/{DATA-ID}/train/t/t.npy
|Test|Input|IMPULSO_HOME/datasets/test/x/x.npy
|Test|Ground Truth|IMPULSO_HOME/datasets/test/t/t.npy
|Test|Image file name|IMPULSO_HOME/datasets/test/x/filename.npy

## Limitations
- Train data are splitted to train and validation data
- Make all images one numpy.array (npy file), so can not deal with large-scale datasets
- Detect just one kind of objects
  - Can not multi kind of objects like detecting cat and dog

## Author
[LotFun](https://github.com/pystokes)
