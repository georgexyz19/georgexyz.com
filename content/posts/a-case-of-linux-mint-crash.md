title: A Case of Linux Mint Crash
slug: a-case-of-linux-mint-crash
date: 2020-09-21 13:54
modified: 2020-09-21 13:54
tags: linux, linux mint
note: record a case of linux mint crash
no: 54

Last night my main computer with Linux Mint 20 crashed and I was really worried
that I might lose the files I had been working on.  After many google searches,
I found a solution and knew why it happened.  

The computer did not respond to mouse or keyboard input so I had to hold down
the power key for a few seconds to shut it off.  When the computer restarted,
it showed the Linux Mint login screen but the system did not let me log in. I
tried a few times entering my password and also tried to restart the computer,
but still could not log in. 

After some google searches, I found this online post

[(SOLVED) Cannot Login (login loop)](https://forums.linuxmint.com/viewtopic.php?f=57&t=261704)

I followed the answer by Lohengrines, did the following steps, and logged 
into the system.

1. In login screen, switch to terminal by pressing "Ctrl + Alt + F2"
2. Run the command `sudo tune2fs -m0 /dev/sda2`
3. Switch back to login screen "Ctrl + Alt + F7"
4. Login with user name and password

There were previous discussions on the same topic on Linux Mint Forum.  This
post had more information.

[Disk full, unable to login. I need help (SOLVED)](https://forums.linuxmint.com/viewtopic.php?f=90&t=253502)

As suggested on the above post, when I ran the command 

```
df -h
sudo du -h -d 1 / | sort -n  
  # this is for 1 level of dir under root /
```

I found two huge files under /var/log directory.  It turned out that both
`syslog` and `kern.log` files were of 40GB+ sizes. And the disk was full and
that was the reason I could not login.  

Unfortunately I could not simply delete those two files.  How to remove them? 
There was another post for that. 

[Var/log file way too large](https://forums.linuxmint.com/viewtopic.php?t=233943)

The following command cleared the two files to 0 byte:

```
sudo su
> /var/log/syslog
> /var/log/kern.log
```

After that the disk showed a free space of 90GB. I also ran the command 
below to change the reserved disk blocks percent back to 5 percent. 

```
sudo tune2fs -m5 /dev/sda2
```

I have a large 30 inch Dell U3011 monitor I bought a few years ago. The desktop 
connects to the monitor via a displayport cable.  I also connect my laptop to 
the monitor through the same cable. I simply unplug the cable from desktop and 
plug it to the laptop. 

Last night, I did not turn off the desktop when unplugging the monitor cable.
Linux Mint 20 system started outputting the same error messages again and
again.  It eventually filled up the disk. That was the reason I could not log
into the system. Thought it was painful, I did learn something from this 
crash experience.


