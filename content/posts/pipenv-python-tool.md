title: Python Pipenv Tool
slug: python-pipenv-tool
meta: Short discussion on pipenv
date: 2019-09-02 00:32
modified: 2020-02-27 15:40
tags: python
note: 22
 

Pyenv is the tool I use to install multiple versions of python in Linux, and I have 
[a short post on how to install pyenv]({filename}pyenv-python-tool.md). I simply 
use the python built-in tool venv to manage virtual environment. It works fine 
for most tasks. 

William Vicent recommends pipenv tool in his *Django for Beginners* book. Corey Schafer also 
favors pipenv in this youtube tutorials. I take a close look at the tool and I like it. 

Here are the links to two youtube videos and an article on real python website. 
Those are very nice resources to learn pipenv. 

* [Corey Schafer's Pipenv Tutorial](https://youtu.be/zDYL22QNiWk)
* [Pipenv Author Kenneth Reitz's Pycon Talk on Pipenv](https://youtu.be/GBQAKldqgZs)
* [Pipenv Tutorial on Realpython.com](https://realpython.com/pipenv-guide/) 

I will use pipenv to manage virtual environment and packages in my future projects. 
The shell script file for updating this website has been modified to like this:

```
# commit_change.sh
if [ -z "$1" ]  # if no command line arg, exit
then
    echo "\$1 is empty"
    exit
fi

# pipenv shell # does not work
pipenv run invoke clean build # see stack overflow 48056606
git status
git add -A
#echo $1
git commit -m "$1"
git push origin master # update source code

pipenv run ghp-import output -b gh-pages
git push origin gh-pages

```

The website is updated with the bash command:

```
source commit_change.sh "git commit message"
```

Here are some common pipenv commands:

```
$pip install pipenv      # global install
$pipenv install requests # virtualenv in ~/.local/share/virtualenvs/...
$pipenv shell

$pipenv run python ...   # no need to activate
>>> import requests

$pipenv install -r requirements.txt
$pipenv lock -r > requirements.txt   # create

$pipenv install pytest --dev
$pipenv uninstall requests

$pipenv --python 3.6
$pipenv --rm      # remove virtual env
$pipenv install   # from Pipfile
$pipenv --venv    # show path

$pipenv check
$pipenv graph     # show dependency
$pipenv install --ignore-pipfile
```

When I am reading Miguel Grinberg's Flask Mega Tutorial Chapter 15 
[A Better Application Structure](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure). 
He recommends to use a python package `python-dotenv` to load environment variables. 
Corey Schafer's tutorial video mentioned that pipenv can load environment variables as well. 

This [Pipenv documentation page](https://pipenv-fork.readthedocs.io/en/latest/advanced.html) 
has a section *Automatic Loading of .env*. If a project directory has a .env file, pipenv 
commands `$pipenv shell` and `$pipenv run` will automatically load it. You can set the 
`PIPENV_DOTENV_LOCATION` to change the file location or file name. You can also set 
`PIPENV_DONT_LOAD_ENV =1` to prevent pipenv from loading the .env file.
