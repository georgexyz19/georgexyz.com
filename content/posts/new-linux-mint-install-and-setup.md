title: New Linux Mint/Ubuntu System Install and Setup
slug: new-linux-mint-install-and-setup
date: 2021-01-15 11:03
modified: 2024-04-11 09:56
tags: linux, linux mint
note: note to be added
related_posts: home-file-sharing, a-case-of-linux-mint-crash, linux-mint, vim-tips
no: 67

I have been using Linux Mint since June 2019. Most times I am happy with it. 
It seems that version 19.x is more stable than 20.x at this time. My computer 
still has 19.3 installed, and eventually I will upgrade to 20.x or a newer version. 
Here is a short note to setup linux mint on a new computer. 

The system has been upgraded to Linux Mint 21.1 Cinnamon in May 2023, and  
the article has been modified to reflect that. 

### Steps

Here is a list of things to do:

1. Remove vim-tiny and install vim.
   Add a ~/.vimrc, copy code from previous blog post.

2. Map the Synology Network Drive.

3. Install git, this step is needed for pyenv install. 
   Do not forget to set user email and user name. 

4. Install pyenv and latest python 3.X. 

5. Setup SSH keys and upload to github.

6. Download github repos with `git clone`.

7. Install Chrome, VS Code (download deb packages).  

8. Install other apps like Node, Inkscape, GIMP, etc.

9. Copy Roboto font and Fira Code font. Font Selection 
   tool to set default font. 

### Add New Fonts

[This tutorial](https://community.linuxmint.com/tutorial/view/29) 
has information on how to add new fonts to Linux Mint. 

The easy way is to copy truetype font files into this directory. 

```
/usr/share/fonts/truetype/
```

Here is an excellent [online article](https://jichu4n.com/posts/how-to-set-default-fonts-and-font-aliases-on-linux/) about 
how to set default fonts and font aliases on Linux.

### VS Code

The VS code settings file is in this directory:

```
~/.config/Code/User/settings.json
```

The file has these lines:

```json
{
    "editor.fontFamily": "'Fira Code', 'monospace', monospace, 
      'Droid Sans Fallback'",
    "editor.fontSize": 16,
    "liveServer.settings.AdvanceCustomBrowserCmdLine": "google-chrome",
    "printcode.browserPath": "/usr/bin/google-chrome",
}
```
The print functionality of Chrome is much better than Mozilla Firefox 
that comes with Linux Mint installation.  

### Script

Here are the output of `history` bash command (with edit). 

```bash
# update the system
sudo apt-get update
sudo apt-get upgrade

# update vim
sudo apt-get remove vim-tiny
sudo apt-get update
sudo apt-get install vim
vim ~/.vimrc

# mount synology network drive
sudo vim /etc/fstab 
sudo vim /etc/samba/credentials
sudo mkdir /media/synology
sudo mount -a

# git install and config
sudo apt install git
git --version
git config --global user.email "<email address>"
git config --global user.name "<name>"


# Install pyenv
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev \ 
libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev


curl https://pyenv.run | bash

vim .bashrc 
# Add those 3 lines to .bashrc for new version of pyenv.run
# export PYENV_ROOT="$HOME/.pyenv"
# command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
# eval "$(pyenv init -)"


exec "$SHELL"
pyenv install --list | grep " 3\.[6789]"

# install python under pyenv
pyenv install --help
pyenv install 3.9.1
pyenv global 3.9.1

# ssh key generation
ssh-keygen -t rsa -b 4096 -C "<email address>"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

cat ~/.ssh/id_rsa.pub 
cd Desktop/
mkdir git-repo
cd git-repo/
git clone git@github.com:<repo address>

cd georgexyz.com/
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
invoke livereload
```

###Linux Mint/Windows Dual Bool Time Issue

When a computer has both Linux Mint and Windows system installed, the system time 
in Windows is wrong.  The issue is described in this 
[itsfoss.com article](https://itsfoss.com/wrong-time-dual-boot/). 

The easy way to fix the issue is to run the commands in Ubuntu, 

```
timedatectl set-local-rtc 1
timedatectl
```

### New Script

Here is an update script in April 2024 for ubuntu 22.04. The new ubuntu seems to 
solve the dual boot time issue mentioned above. 

```
sudo apt update
sudo apt upgrade
sudo apt remove vim-tiny
sudo apt install vim
sudo apt install git
git config --global user.email <email>
git config --global user.name "<name>"
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev \
      xz-utils tk-dev libxml2-dev libxmlsec1-dev \
      libffi-dev liblzma-dev
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null ||   \
      export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"
ssh-keygen -t rsa -b 4096 -C "<email>"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub 
mkdir git-repo
cd git-repo/
git clone git@github.com:georgexyz19/georgexyz.com.git
cd georgexyz.com/
python -V
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt 
code .
source commit_change.sh "minor change test"
pyenv --version
pyenv install --list
pyenv install 3.8.19
pyenv install 3.12.2
pyenv global 3.8.19
exit

```