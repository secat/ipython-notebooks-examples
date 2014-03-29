ipython-notebooks-examples
==========================

Collections of IPython notebooks examples


## install submodules

In order to retrieve the submodules used by this repository, please run the following git commands:

```shell
git submodule init
git submodule update
```

## mac osx requirements

In order to install all Python requirements on mac osx, please install the following homebrew formulas:

```shell
brew install readline
brew install zeromq
brew install gfortran
brew install pkg-config
brew install freetype
```

## python virtual environment

```shell
python -m virtualenv vpydata
source vpydata/activate
pip install -r requirements.txt
```
