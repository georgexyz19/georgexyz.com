title: Adding .vimrc Dotfile to Github
slug: adding-vimrc-dotfile-to-github
date: 2020-06-09 09:01
modified: 2020-06-09 09:01
tags: software utility, vim
note: version control .vimrc
no: 49


Youtube has a nice video [Learning Vim In A Week](https://youtu.be/_NUO4JEtkDw), and I watch it 
every few months to refresh my Vim skills. In the video the presenter suggests people to 
version control dotfiles such as `.vimrc`, which is the setting file Vim loads during startup. 
There is [a website](https://dotfiles.github.io/) 
dedicated to this topic. 

Dotfiles seem to be different than normal files in a regular github repo. I googled and found 
[a stackoverflow post](https://stackoverflow.com/questions/18197705/adding-your-vim-vimrc-to-github-aka-dot-files) 
which discusses the exact same issue. The accepted answer seems a reasonable start point, so I create 
[a github repo](https://github.com/georgexyz19/dotfiles) 
and start a directory containing `.vimrc` and `.simple` dot files.  The answer also suggests 
to create symbol links in home directory to the dot files. However, I find it does not work 
well. When I use `vim -u ~/.simple` command to load a specific dot file, Vim reports an error. 
Instead the hard links should be used here. You simply use `ln file link` command to create 
hard links instead of `ln -s ...` command.  

When adding files to git version control, the command `git add .` should be used. The command 
`git add *` will not work because `*` does not expand to include dot files. 


I also wrote a short python script `newlinks.py` to automatically create the hard links in the 
home directory. The program is not long and the source code is listed below. 

```python
#! python3

'''
Create hard links in ~/ or home directory.
The purpose is to track the .dot file by git and github

Use:

git add .
git commit -m "message"
git push origin master

to update git repo

After you git clone the repo
run $python3 newlinks.py to create hard links in home dir.

Written by George Zhang on 6/8/20
'''

import os
import subprocess

def main():
    abspath = os.path.abspath(__file__) 
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    filenames = os.listdir()

    for f in filenames:
        if os.path.isfile(f) and f.startswith('.') and not f.endswith('.swp'):
            # ln command
            # os module has link and symlink function
            p1 = subprocess.run(f'ln -f {f} ~/{f}', shell=True, capture_output=True) 
            print('running command: ', f'ln -f {f} ~/{f}', end=' --> ')
            if p1.returncode == 0:
                print('Success!')

    print('DONE!!!')   


if __name__ == '__main__':
    main()
```



