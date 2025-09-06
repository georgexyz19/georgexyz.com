title: An Interesting WIFI Card Problem
slug: an-interesting-wifi-card-problem
date: 2025-09-05 20:01
modified: 2025-09-05 20:01
tags: hardware
note: note to be added
no: 92

I bought a new HP ZBook Firefly G10A last year with a Ryzen 7840HS CPU and 32GB RAM. It’s supposed to be much faster than my old 
laptop, an HP Firefly G8. However, I’ve found myself rarely using the new laptop, and I always pick up the old one as my first 
choice.

So, I started asking myself: what’s the reason? What’s the point of buying a new laptop if I still prefer the old one? There are 
probably two good reasons why the old Gen 8 Firefly feels better:

1. The Gen 8 version’s trackpad has two physical buttons. The new Gen 10 version removed the buttons, and I really like those 
physical buttons.

2. The Wi-Fi on the new laptop doesn’t work very well. Every time I turn on the laptop, I have to reconnect to my home network. 
Also, when I use the laptop in my living room, the signal is very weak. Sometimes the laptop doesn’t pick up any Wi-Fi signal at 
all. None of my other devices, like my phone or other laptops, have this problem. 

WIFI Status

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/WIFI1.PNG" alt="WIFI1"> 
</div>

WIFI Device Property 

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/WIFI2.PNG" alt="WIFI2"> 
</div>

After some digging, I found that the MediaTek MT7922 Wi-Fi card was the problem. There are many people complaining about MediaTek 
Wi-Fi cards online. So I asked ChatGPT what a good replacement card would be. The answer was the Intel AX210 Wi-Fi 6E card.

I spent about $17 on eBay and received the card today. It was quite easy to replace the Wi-Fi card, and the difference is 
obvious. The new card completely solved the two WIFI problems.

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/WIFI3.PNG" alt="WIFI2"> 
</div>

Interestingly, I found that the older driver (version 22.0.1.5) performs better than the newer drivers. The internet speed is 
faster, and the signal is stronger with this older driver. I’m not sure why, but I’ll stick with the old driver and hope it lasts 
for a while
