title: Copy SSH Keys to A New Computer
slug: copy-ssh-keys
date: 2020-06-07 10:24
modified: 2020-06-07 10:24
tags: software utility
note: How to copy ssh keys to a new computer
no: 48

I followed 
[Miguel Grinberg's tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux) 
setting up an SSH key on my desktop using `ssh-keygen`. I thought I could simply copy the 
private key `id_rsa` and public key `id_rsa.pub` to `~/.ssh` directory on a new computer 
and SSH would work as on the first computer. 

It does not work. I googled and found a 
[Q&A](https://askubuntu.com/questions/4830/easiest-way-to-copy-ssh-keys-to-another-machine) 
on askubuntu.com. There are many answers to the question but only an answer by Victor Timoftil 
is related to what I am looking for. The simple answer is that, 

>    Move `~/.ssh` to the new machine and run `ssh-add`. DONE!

The long answer is that, 


>    1. In the old machine, take the folder ~/.ssh to an USB drive, or to any other storage you like.
>    2. On the new machine, put the folder under ~ aka /home/$USER.
>    3. Run ssh-add, on the new machine done.


I copy the two SSH keys files to a flash drive that is formatted as ntfs format. The key files 
are having new permission `777`. The `ssh-add` command will show an error for that. I have to 
use `chmod 500` command to change file permissions. Also the `ssh-add` will ask a passphrase 
which is entered when you create the keys. 




