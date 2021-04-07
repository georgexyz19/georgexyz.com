title: Git Command Reference
slug: git-command-reference
date: 2021-04-07 09:48
modified: 2021-04-07 09:48
tags: software utility
note: Git command ref
no: 71

This note is from [Corey Schafer's Youtube Git Tutorial](https://youtu.be/HVsySz-h9r4). 
A viewer posted the note under the video and I copied it as a starting point for this post. 
I will add more contents to this post over time. 

On initial install:

git --version 
: checks the version of the installed locally git

git config --global user.name "Your Name" 
: sets up the name of the user 

git config --global user.email "user@email.com" 
: sets email

git config --list 
: lists configurations


For help on commands:

git `<verb>` --help 
:  help info

git help `<verb>` (e.g. git help config)
: alternative help command

For initializing the project:

git init 
: initializes the git repo in the current folder

touch .gitignore 
: creates a git ignore file

git status 
: check working tree - both on the git and on local 


Add and remove from staging area:

git add -A 
: adds all files to staging area

git reset `<file>`
: removes file in staging area


Make a commit:

git commit -m "commit message" 
: -m is for message


Check log:

git log 
: renders commit ids, authors, dates

Clone a remote repo:

git clone `<url>` `<dir>`
: clone a repo from url to dir 

View info about the repo:

git remote -v 
: lists info about the repo

git branch -a 
: lists all branches


View changes:

git diff 
: shows the difference 

Pull and push:

git pull origin master
: pull before push

git push origin master 
: origin is remote repo, master is the branch


First time to push a branch:

git push -u origin `<branch name>` 
: `-u` has special meaning

git branch `<branch name>`
: create a branch:

git checkout `<branch name>`
: checkout a branch

git checkout master
: switch to master

Merge a branch:

git pull origin master
: pull from origin

git branch --merged 
: see which branches are merged 

git merge `<name of the branch to merge>`
: merge onto a branch

git push origin master 
: push to upstream


Delete a branch:

git branch -d `<name of the branch>`
: this deletes it locally

git branch -a 
: check the repo branches 

git push origin --delete `<name of the branch>`
: this deletes it from the repo

