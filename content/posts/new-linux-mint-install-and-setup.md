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

### Steps

Here is a list of things to do:

1. Remove vim-tiny and install vim-gtk3.
   Add a ~/.vimrc, copy code from previous blog post.

2. Map the Synology Network Drive.

3. Install git, this step is need for pyenv install. 
   Do not forget to set user email and user name. 

4. Install pyenv and latest python 3.9.1.

5. Setup SSH keys and upload to github.

6. Download github repos with `git clone`.

7. Chrome, VS Code (download deb packages). 
   Chrome will ask for a keyring password, leave it blank.
   Check out 
   [this post](https://askubuntu.com/questions/867/how-can-i-stop-being-prompted-to-unlock-the-default-keyring-on-boot) 
   for more info.  

8. Install other apps like Node, Inkscape, GIMP, etc.

9. Copy Roboto font and Fira Code font. Font Selection 
   tool to set default font (Ubuntu). 

### Add New Fonts

[This tutorial](https://community.linuxmint.com/tutorial/view/29) 
has information on how to add new fonts to Linux Mint. 

The easy way is to copy file truetype font files to this directory. 

```
/usr/share/fonts/truetype/
```

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
The print function of Chrome is much better than Mozilla Firefox 
that comes with Linux Mint installation.  

### Printer Driver

[Canon website](https://www.usa.canon.com/internet/portal/us/home/support/details/printers/color-laser/canon-color-imageclass-mf642cdw) 
provides printer drivers for Debian Linux.  You can use the 
deb package. After you download the driver file, upzip it, and run 
`sudo ./install.sh` to install it.  

### Script

Here are the output of `history` bash command (after edit). 

```bash
# update the system
sudo apt-get update
sudo apt-get upgrade

# update vim
sudo apt-get remove vim-tiny
sudo apt-get update
sudo apt-get install vim-gtk3
vim ~/.vimrc

# mount synology network drive
sudo vim /etc/fastab
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
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev 
 libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
 libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl 
curl https://pyenv.run | bash
vim .bashrc 
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