title: Change Boot Order with GRUB 2
slug: change-boot-order-with-grub-2
date: 2020-08-28 03:17
modified: 2020-08-28 03:17
tags: linux, software utility
note: a post about grub 2
no: 52

My laptop has both Windows 10 and Linux Mint installed. Sometimes I want the laptop booting into 
Windows by default. After a little online research, I find that I need to change the settings of 
boot loader software GRUB 2. 

After reading the 
[online grub manual](https://www.gnu.org/software/grub/manual/grub/grub.html) 
for one hour or so, I am still not sure how to do it. Fortunately, I find 
[an excellent GRUB tutorial](https://www.dedoimedo.com/computers/grub-2.html) 
on dedoimedo.com, which explains the GRUB 2 very well. 

Basically, the GRUB 2 software reads the `grub.cfg` configuration file in `/boot/grub/` directory.
However you should not modify this file directly. Instead, the file is generated with a linux
command like this. 

```
sudo grub-mkconfig -o grub.cfg 
```

The `grub-mkconfig` tool will load setting files in `/etc/grub.d/` directory and setting 
file `/etc/default/grub`.  A user should change those files and run `grub-mkconfig` to 
generate the final `grub.cfg` file. 

Here is the file list under `/etc/grub.d` directory in my laptop.

```
george@T450:/etc/grub.d$ ls -la
total 108
-rwxr-xr-x   1 root root 10046 Mar 18  2019 00_header
-rwxr-xr-x   1 root root  6258 Mar 18  2019 05_debian_theme
-rwxr-xr-x   1 root root 12059 Aug  4 23:46 09_os-prober <-- added
-rwxr-xr-x   1 root root 12693 Mar 18  2019 10_linux
-rwxr-xr-x   1 root root 11298 Mar 18  2019 20_linux_xen
-rwxr-xr-x   1 root root  1992 Jan 28  2016 20_memtest86+
-rw-r--r--   1 root root 12059 Mar 18  2019 30_os-prober
-rwxr-xr-x   1 root root  1418 Mar 18  2019 30_uefi-firmware
-rwxr-xr-x   1 root root   214 Mar 18  2019 40_custom
-rwxr-xr-x   1 root root   216 Mar 18  2019 41_custom
-rw-r--r--   1 root root   483 Mar 18  2019 README
```

Reading the `/boot/grub/grub.cfg` file a little bit, I find the `30_os-prober` is the configuration
file to read the Windows. I made a copy the file and named the new copy `09_os-prober`, then I
turned the execution bit off for `30_os-prober`. Note the boot order is based on the first two
digits of file names in this directory.  The commands are like this, 

```
sudo cp 30_os-prober 09_os-prober
sudo chmod -x 30_os-prober
sudo grub-mkconfig -o /boot/grub/grub.cfg 
```
 
Now reboot the computer and the boot screen looks like this, 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/boot_order.jpg" alt="boot order"> 
</div>
