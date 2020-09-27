title: Home File Sharing with Raspberry Pi
slug: home-file-sharing
date: 2020-09-26 23:27
modified: 2020-09-26 23:27
tags: hardware, linux
note: Turn a Raspberry Pi to a home file sharing NAS
no: 55

When reconfiguring my home WIFI router this week, I have a thought to setup a
home file sharing drive. The Raspberry Pi 3B+ and a case I bought one or two 
years ago has been collecting dust in a drawer for quite some time. It is 
time to bring them out and get some use out of them.

My original plan is to connect a retired SSD to the PI via an USB adapter. It would
be a little messy to handle the cable and the exposed SSD drive. So I decide to 
use a Samsung 64GB USB flash drive which is also retired. 


The two articles linked below are on the top of Google search.

[Pcmag.com - How to Turn a Raspberry Pi Into a NAS for Whole-Home File Sharing](https://www.pcmag.com/how-to/how-to-turn-a-raspberry-pi-into-a-nas-for-whole-home-file-sharing)

[Magpi - Build a Raspberry Pi NAS](https://magpi.raspberrypi.org/articles/build-a-raspberry-pi-nas)

After reading the two articles, it seems that the first one suites my needs 
better. The first tutorial is quite good but I still run into a few problems. 
Below are some notes I have when setting up the Pi. 

1. The Raspberry Pi 3B+ needs a 3A or 2.5A power supply. If the USB power charger
   does not provide enough voltage, the Pi will start and then automatically shut off.
2. The my cell phone quick charger has 3A voltage output and it 
   works well with Pi.
3. The USB stick does not work with `sudo mkfs` command in the tutorial. 
   I have to use Linux Mint desktop app *USB Stick Formatter* to format 
   it to EXT4 first and then connect it to Pi. 
4. I tried both full version desktop Raspberry Pi OS and Lite minimal version. 
   It seems that the full version is easy to setup WIFI, SSH, and 
   other settings.
5. Even though it is possible to setup the Pi without a monitor, it is much 
   easier to connect it to monitor and do initial setup. 
6. The network drive speed is not so fast and it is between 0.5M/s to 2M/s.
   But it is good enough for me to share files among computers and my phone. 
7. Android file manager app *Cx File Explorer* can access network drive with 
   SMB protocol. 
8. Use address `\\raspberrypi` in Windows and `smb://raspberrypi` in Linux 
   to access the shared drive. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/usb_formatter.png" alt="USB Formatter">
</div>

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/pi.jpg" alt="Raspberry pi">
</div>

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/pi_ac.jpg" alt="Raspberry adapter">
</div>
