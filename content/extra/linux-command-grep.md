title: Linux Command Grep
slug: linux-command-grep
meta: Discuss grep
date: 2019-07-11 23:57
modified: 2019-07-11 23:57
tags: linux, software utility
status: draft
note: I completed this article on 7/11/2019, but messed up during git process. NEED TO BE EXTRA CAREFUL WHEN DEALING WITH GIT.
no: 18

Brian Kernighan Youtube talk link: https://www.youtube.com/watch?v=NTfOnGZUZDk

Corey Schafer Linux Terminal Tutorial for Grep:  https://youtu.be/VGgTmxXp7xQ

Nick Parlante's Python RE Video:  https://youtu.be/kWyoYtvJpe4


Grep command searches file contents to find lines that contain a pattern.  The pattern is described 
in Regular Expression language. 

Ryan's Tutorials website has [a nice introduction](https://ryanstutorials.net/linuxtutorial/grep.php) 
to **Grep and Regular Expression**.  Note egrep is a shortcut to `grep -E` in Ubuntu: 

```
$which egrep
/bin/egrep
$file /bin/egrep
/bin/egrep: POSIX shell script, ASCII text executable
$vim /bin/egrep  # file content is
#!/bin/sh
exec grep -E "$@"
```

This is a very simple grep example:

$grep "Jane Williams" filename.txt

The command has many options. A few common ones are:

* -w  Whole word
* -i  ignore case
* -n  line number
* -B 4  4 lines before

The `filename.txt` in the above example could be either ./* or ./*.txt. 

For example, this command will search current directory and subdirectories. 

$grep -winr "Jane Williams" ./

Here are a few more options:

* -r  recursive
* -l  file name only
* -c  count, print a count

You can use pipes to search the results of another command.

$history | grep "git commit"

