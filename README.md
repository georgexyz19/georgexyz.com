# This is the source code of my personal website

[georgexyz.com](https://www.georgexyz.com)

The shell script *commit_change.sh* automates the blog publishing.  After
writing a new post or editing an existing post, run command `source
commit_change.sh "git commit msg"` to make git commit and push to github. The
website is hosted on github, and it will be automatically updated. 

To setup the environment in a new computer, run those commands

```
pip install pipenv  # install it globally
pipenv install  # install from Pipfile, 
    # or use --ignore-pipfile to install from Pipfile.lock
pipenve shell   # launch virtual env
# write or edit articles
invoke livereload  # preview website in a browser
source commit_change.sh "msg" # publish
```

