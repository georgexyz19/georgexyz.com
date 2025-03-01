title: Develop With WSL
slug: develop-with-wsl
date: 2025-03-01 13:15
modified: 2025-03-01 13:15
tags: linux, software utility
note: WSL how to
no: 88

I recently bought a new Windows 11 laptop and chose not to install Ubuntu. Instead, I’m using Windows Subsystem for Linux (WSL2) to update this blog site.

WSL is much more user-friendly than when I tried it a few years ago. The command below will install WSL and Ubuntu, and your system will be ready to go. Just remember to "Run as Administrator" when starting the Windows Command Prompt (cmd):


```
wsl --install
```

One issue I encountered is with Windows Terminal, and VIM doesn't work well in it. After some searching, I found that ConEmu works better. You’ll need to set the default window size to 150 x 40. I'm pretty happy with it so far.

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/wsl/wsl_conemu.png" alt="conemun"> 
</div>

To open the current directory in VS Code, use this command:

```
code .
```

Those last two blog posts were updated in WSL and ConEmu.  

