# Install tensorflow (optional)

Given that you might all have configure the pytorch environment correctly in the past course, we will skip the installation of vscode, anaconda, etc.

```shell
# we encourage you to create another virtual environment for installation of the tensorflow, because we are not sure whether it will cause any undesirable error when 
# install both pytorch and tensorflow

# 1. create another virtual environment
conda create --name tensorflow python==3.9

# 2. activate it and navigate to current dira and install tensorflow
conda activate tensorflow
cd ./EMIA6500E/code1_install_env/
pip install -r tf_requirements.txt

# test it
python ./test_tensorflow.py

# it should give you the similar results of the `fit_quadratic.ipynb`

```