title: Linux Command Grep
slug: linux-command-grep
meta: Discuss grep
date: 2019-07-19 15:07
modified: 2019-07-19 16:00
tags: linux, software utility
note: I completed this article on 7/11/2019, but messed up during git process. 
no: 20

Grep command searches file contents to find lines that contain a pattern.  The 
pattern is described in Regular Expression (regex) language. Here are three 
youtube vidio links about Grep and regular expressions. 

* [Brian Kernighan Youtube Talk on Grep](https://www.youtube.com/watch?v=NTfOnGZUZDk)
* [Corey Schafer Linux Terminal Tutorial for Grep](https://youtu.be/VGgTmxXp7xQ)
* [Nick Parlante's Python Regex Video](https://youtu.be/kWyoYtvJpe4)

Ryan's Tutorials website has [a nice introduction](https://ryanstutorials.net/linuxtutorial/grep.php) 
to *Grep and Regular Expression*.  Note egrep is a shortcut to `grep -E` in 
Ubuntu. The man page of grep describes that "in GNU grep there is no difference 
in available functionality between basic and  extended syntaxes".  

```
$which egrep
/bin/egrep
$file /bin/egrep
/bin/egrep: POSIX shell script, ASCII text executable
$vim /bin/egrep  # file content is
#!/bin/sh
exec grep -E "$@"
```

Here is a very simple grep example:

```
$grep "Jane Williams" filename.txt
```

The grep command has many options. A few common ones are:

* -w : Whole word
* -i : ignore case
* -n  : line number
* -B 4 : 4 lines before
* -A 4 : 4 lines after
* -C 4 : 2 lines before, 2 lines after

The `filename.txt` in the above example could be either ./* or ./*.txt. 

For example, this command will search current directory and subdirectories. 

```
$grep -winr "Jane Williams" ./
```

Here are a few more options:

* -r : recursive
* -l : file name only
* -c : count, print a count

You can use pipes to search the results of another command.

```
$history | grep "git commit"
```

The grep `-P` option interprets the pattern as a Perl-compatible regex. The 
Python and Perl "essentially has the same regex syntax".  So with the `-P` 
option turned on, the grep command will accept Python style special characters 
in pattern. Here is a list of common regex special characters in Python:

* \.(dot) : any char
* \\w : word char 'A-Za-z0-9_'
* \\d : digit
* \\s : white sapce
* \* : zero or more
* \+ : one or more




