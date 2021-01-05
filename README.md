# This is the source code of my personal website

[georgexyz.com](https://www.georgexyz.com)

The shell script *commit_change.sh* automates the blog publishing.  After
writing a new post or editing an existing post, run command `source
commit_change.sh "git commit msg"` to make git commit and push it to github. The
website is hosted on Github Pages, and it will be automatically updated. 

Run those commands to setup the environment on a new computer.

```
pip install pipenv  # install it globally
pipenv install  # install from Pipfile, 
    # or use --ignore-pipfile to install from Pipfile.lock
pipenve shell   # launch virtual env
# write or edit articles
invoke livereload  # preview website in a browser
source commit_change.sh "msg" # publish
```

If you do not want to use `pipenv`, you can use the `venv` to manage virtual 
environment. 

```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# write or edit articles
invoke livereload  # preview website in a browser
source commit_change_venv.sh "msg" # to publish
```
