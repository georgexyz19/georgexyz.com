title: New Linux Mint Install and Setup
slug: new-linux-mint-install-and-setup
date: 2021-01-15 11:03
modified: 2021-01-15 11:03
tags: linux, linux mint
note: note to be added
related_posts: home-file-sharing, a-case-of-linux-mint-crash, linux-mint, vim-tips
no: 67

I have been using Linux Mint since June 2019. Most times I am happy with it. 
It seems that version 19.x is more stable than 20.x at this time. My computer 
still has 19.3 installed, and eventually I will upgrade to 20.x or a newer version. 
Here is a short note to setup linux mint on a new computer. 


```
Linux Mint 19.3

sudo apt-get update
sudo apt-get upgrade
// this step takes some time

1. Remove vim-tiny and install vim-gtk3
   Add a ~/.vimrc, copy code from previous blog post

2. Map the Synology Network Drive

3. Install git, this step is need for pyenv install
   Do not forget to set user email and user name. 

4. Install pyenv and latest python 3.9.1

5. Setup SSH keys and upload to github

6. Download github repos with 'git clone'

7. Chrome, VS Code (download deb packages)
   Chrome will ask for a keyring password, leave it blank.

8. Install other apps like Node, Inkscape, GIMP

9. Copy Roboto font and Fira Code font. Font Selection 
   tool to set default font (Ubuntu). 
   
```


