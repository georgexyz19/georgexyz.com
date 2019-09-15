#!/bin/bash

# commit_change.sh : commit git changes for georgexyz.com
# see stackoverflow question 6565357 to set git credential caching
# $git config credential.helper store
# $git push origin master

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
pipenv run invoke clean build # see stack overflow 48056606
git status
git add -A
git commit -m "$1"
git push origin master # update source code

pipenv run ghp-import output -b gh-pages
git push origin gh-pages
