title: Install Multiple Python Versions In Ubuntu With Pyenv
slug: pyenv-python-tool
meta: An article about pyenv 
date: 2019-04-11 10:53
modified: 2019-04-11 10:53
tags: python, ubuntu
note: no notes


The python default installation in Ubuntu is a stripped down version. It does not 
include pip or venv. The pyenv tool allows programmers to install multiple
versions of python in Ubuntu system. 

This recent 
[realpython article](https://realpython.com/intro-to-pyenv/) 
includes everything from pyenv installation to pyenv configuration. 

The only thing to note is that a user needs to install some dependencies
in Ubuntu before running pyenv.  If you omit this step, python
building process will fail without warnings or errors. 

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl 
```

I usually change the global python to a more recent version with `pyenv global` 
command and simply use `venv` to manage virtual environment. 

```
pyenv global 3.7.3
python -m venv ~/.venv/pelican
``` 
