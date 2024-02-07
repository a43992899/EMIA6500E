# Install vscode on mac
You can install Visual Studio Code on Mac by following the instructions on the [Visual Studio Code website](https://code.visualstudio.com/docs/setup/mac).

# Install Miniconda on Mac and Linux
Mac users can install Miniconda by running the following commands in the terminal:
If you are arm64 Mac user, you can run the following commands in the terminal:
```bash
mkdir -p ~/miniconda3
# arm64 is for M1 Macs
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

If you are x86_64 Mac user, you can run the following commands in the terminal:
```bash
mkdir -p ~/miniconda3
# x86_64 is for Intel Macs
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Linux users can install Miniconda by running the following commands in the terminal:
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

After running the commands, you can activate the Miniconda environment by running the following command:
```bash
source ~/miniconda3/bin/activate
```

You can verify the installation by running the following command:
```bash
conda --version
```
It should display the version of Miniconda you installed. e.g.`conda 23.11.0`
```

# Install EMIA6500E Environment


Now create a new environment and install the `requirements.txt` by running the following command:
```bash
conda create --name emia6500 python=3.8
conda activate emia6500
pip install -r requirements.txt
```
You can refer to the [Miniconda installation guide](https://docs.anaconda.com/free/miniconda/) for more information.

If you don't know how to open a terminal, you can refer to the [Terminal on Mac](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) guide.

To test your package is correctly installed, you can run the following command:
```bash
conda activate emia6500
cd code1_install_env
python import_env.py
```