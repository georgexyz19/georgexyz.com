title: Setup Linux Mint on a New Computer
slug: linux-mint
meta: This post has two tips about how to setup linux mint on a new computer. 
date: 2019-06-26 12:32
modified: 2019-06-26 12:32 
tags: linux, linux mint
note: None
no: 15


I have been using Xubuntu since version 17.10. This week I read some articles on 
Linux Mint and I decided to give it a try. It is not a big change because Linux 
Mint is an ubuntu based distro. 

Linux Mint has a very nice user interface built on 
Cinnamon desktop system. It definitely looks better than Xubuntu which is known 
for its lightweight Xfce desktop environment. 

Omg!ubuntu website has an article about 
[Wine 4.0 in Linux Mint 19](https://www.omgubuntu.co.uk/2019/06/linux-mint-19-wine-4-available). 
Linux developers backported Wine 4.0 to the Linux Mint repositories.  It becomes 
very easy for users to install Wine 4. Here is the single command to install: 

```
$sudo apt install --install-recommends wine-installer
```

I find two issues when setting up Linux Mint. The first one is that when I run 
`sudo apt upgrade` command after installation, the system reports an error like this:

```
Fetched 902 kB in 3s (247 kB/s)
Preconfiguring packages ...
dpkg: dependency problems prevent processing triggers for gconf2:
 gconf2 depends on dbus-x11; however:
  Package dbus-x11 is not configured yet
```

A Google search finds 
[a solution](https://forums.linuxmint.com/viewtopic.php?t=276119) 
posted on Linxu Mint forum.  Running 
two commands below solves the issue. 

```
$sudo dpkg --configure -a
$sudo apt-get install -f
```

The man pages of dpkg and apt-get have the following paragraphs about those two 
commands:

```
dpkg
   --configure package...|-a|--pending
    Configure  a  package  which  has  been  unpacked  but  not  yet
    configured.  If -a or --pending is given instead of package, all
    unpacked but unconfigured packages are configured.

    To  reconfigure a package which has already been configured, try
    the dpkg-reconfigure(8) command instead.

    Configuring consists of the following steps:

    1. Unpack the conffiles, and at the same time back  up  the  old
    conffiles, so that they can be restored if something goes wrong.

    2. Run postinst script, if provided by the package.

apt-get
  -f, --fix-broken
    Fix; attempt to correct a system with broken dependencies in place.
    This option, when used with install/remove, can omit any packages
    to permit APT to deduce a likely solution. If packages are
    specified, these have to completely correct the problem. The option
    is sometimes necessary when running APT for the first time; APT
    itself does not allow broken package dependencies to exist on a
    system. It is possible that a system's dependency structure can be
    so corrupt as to require manual intervention (which usually means
    using dpkg --remove to eliminate some of the offending packages).
    Use of this option together with -m may produce an error in some
    situations. Configuration Item: APT::Get::Fix-Broken.
```

The other issue I encountered is that the system does not respond 
to logitech wireless mouse and keyboard after going into suspend (sleep). 


<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/logitech-k375s-m585.jpg" alt="keyboard mouse"> 
</div>

[An article](https://askubuntu.com/questions/848698/wake-up-from-suspend-using-wireless-usb-keyboard-or-mouse-for-any-linux-distro) 
on askubuntu.com provides a working solution.  Here are the commands to make it 
work:

```
george@STK2M3:~$ grep . /sys/bus/usb/devices/*/product
/sys/bus/usb/devices/1-3/product:USB Receiver     # PORT !!!
/sys/bus/usb/devices/1-5/product:USB2.0 Hub
/sys/bus/usb/devices/2-3.1/product:Flash Drive
/sys/bus/usb/devices/2-3/product:USB3.0 Hub
/sys/bus/usb/devices/usb1/product:xHCI Host Controller
/sys/bus/usb/devices/usb2/product:xHCI Host Controller

george@STK2M3:~$ grep . /sys/bus/usb/devices/*/power/wakeup
/sys/bus/usb/devices/1-3/power/wakeup:disabled    # DEFAULT DISABLED  !!!
/sys/bus/usb/devices/1-5/power/wakeup:disabled
/sys/bus/usb/devices/1-7/power/wakeup:disabled
/sys/bus/usb/devices/2-3/power/wakeup:disabled
/sys/bus/usb/devices/usb1/power/wakeup:disabled
/sys/bus/usb/devices/usb2/power/wakeup:disabled

george@STK2M3:~$ lsusb
Bus 002 Device 003: ID 090c:1000 Silicon Motion, Inc. 
Bus 002 Device 002: ID 2109:0813 VIA Labs, Inc. 
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 004: ID 8087:0a2b Intel Corp. 
Bus 001 Device 003: ID 2109:2813 VIA Labs, Inc. 
Bus 001 Device 002: ID 046d:c52b Logitech, Inc. Unifying Receiver  # DEVICE !!!
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

george@STK2M3:~$ sudo vim /etc/udev/rules.d/10-wakeup.rules 
[sudo] password for george: 
```

Add the contents below to the 10-wakeup.rules file.  The idVendor and idProduct 
values are from the `lsusb` command, and the path `/sys/bus/...` is from the first 
grep command.

```
ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="c52b" 
RUN+="/bin/sh -c 'echo enabled > /sys/bus/usb/devices/1-3/power/wakeup'"
```

After the above steps, the logitech mouse and keyboard wake up the Linxu Mint just fine. 
I never got the sleep/wakeup function working properly in Xubuntu system. So, this is 
a large improvement for me. 
