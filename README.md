# This is the source code of my personal website

[georgexyz.com](https://www.georgexyz.com)


The shell script *commit_change.sh* automates the blog publishing.  After
writing a new post or editing an existing post, run command `source
commit_change.sh "git commit msg"` to make git commit and push it to github. The
website is hosted on Github Pages, and it will be automatically updated. 

If you use `venv` to manage your virtual environment, run those commands 
to setup the environment on a new computer. 

```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# write or edit articles
invoke livereload  # preview website in a browser
source commit_change.sh "git msg" # to publish
```

If you use `pipenv`, here are the commands. 

```
pip install pipenv  # install it globally
pipenv install  # install from Pipfile, 
    # or use --ignore-pipfile to install from Pipfile.lock
pipenve shell   # launch virtual env
# write or edit articles
invoke livereload  # preview website in a browser
source pipenv_commit_change.sh "msg" # publish
```

*Last update:* 3/5/2021
