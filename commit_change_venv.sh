#!/bin/bash

# commit_change_venv.sh : commit git changes for georgexyz.com 11/10/2020
# This is venv version of the script
# How to execute the script:
# $source venv/bin/activate
# $source commit_change_venv.sh "git commit message"
# I will start to use venv on new computers with this script
# basename prompts an error, change it back to ${...}
PROGNAME="${0##*/}"

usage () {
  cat << EOF
Usage: $PROGNAME "git commit message"
Where:
  git commit message: is a message passed to 'git commit -m' 
EOF
}

if [ -z "$1" ]; then 
    usage
    exit 1
fi

git pull

# pipenv shell # does not work
# publish is clean and build with publishconf.py
invoke publish 
git status
git add -A
git commit -m "$1"
git push origin master # update source code

ghp-import output -b gh-pages
git push origin gh-pages
