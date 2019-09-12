# commit_change.sh

# if no command line argument, exit
if [ -z "$1" ]; then 
    echo "$1 is empty"
    exit 1
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
