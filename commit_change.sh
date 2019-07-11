if [ -z "$1" ]  # if no command line arg, exit
then
    echo "\$1 is empty"
    exit
fi

source venv.sh  # load virtual env
invoke clean build
git status
git add -A
#echo $1
git commit -m "$1"
git push origin master # update source code

ghp-import output -b gh-pages
git push origin gh-pages
