#!/bin/bash

# pipenv_commit_change.sh : commit git changes for georgexyz.com
# How to execute the script:
# $pipenv shell
# $source commit_change.sh "git commit message"

# need pipenv installed
# $pip install pipenv
# pipenv install pelican Markdown invoke ghp-import2

PROGNAME="$(basename "$0")" # or = "${0##*/}"

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
pipenv run invoke publish # see stack overflow 48056606
git status
git add -A
git commit -m "$1"
git push origin master # update source code

pipenv run ghp-import output -b gh-pages
git push origin gh-pages
