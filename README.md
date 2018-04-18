# AngleBasedOutlierDetection [![Build Status](https://travis-ci.org/ITU-2019/AngleBasedOutlierDetection.svg?branch=master)](https://travis-ci.org/ITU-2019/AngleBasedOutlierDetection)

Dependencies:

```bash
python -m pip install --upgrade pip
pip install numpy
pip install scipy
pip install matplotlib
```

To run the code. go into the fht_repo folder run:

```bash
cd fht_repo
python setup.py build
```

Go into the build folder generated inside the fht_repo folder and then into the lib folder, and move the folder called fht to the build folder in root.
All generated files should be git ignored.

To run the files:
```bash
cd build
# fx.
python DataTest.py data/somefile.txt 
```
