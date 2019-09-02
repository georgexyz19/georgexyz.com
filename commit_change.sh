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
