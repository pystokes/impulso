# __impulso__

## Description
Framework for object detection (Ex. faces, captions)

## Data format
### Structure of original data
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
        └─bbox.json
```

### Input
Images in the above structure.

### Ground Truth
Ground truth data is defined with `bbox.json`. See `bbox.json` in `org` directory for example.

## Demo
The case of face detection.
```
python impulso.py predict -e 0912-0121-1904 -m 70 -x ./tmp/input -y ./tmp/output
```

## Output examples

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

## About DATA-ID, EXPERIMENT-ID and MODEL-ID
`DATA-ID`
- Published when execute `python impulso.py dataset`. See stdout.
`EXPERIMENT-ID`
- Published when execute `python impulso.py prepare -d DATA-ID`. See stdout.
`MODEL-ID`
- Published in saving model
  - MODEL-ID is 70 for sample model (model.00070-0.02-0.00-0.03-0.00.hdf5)

## License
- Permitted: Private Use  
- Forbidden: Commercial Use  

## Author
[LotFun](https://github.com/pystokes)

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

