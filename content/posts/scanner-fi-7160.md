title: Fujitsu Scanner Fi-7160 Software
slug: scanner-fi-7160
date: 2020-05-14 12:46
modified: 2020-05-14 12:46
tags: software utility
note: Tips on fujitsu scanner fi-7160
no: 46

A few years ago I purchased a Fujitsu fi-7160 document scanner for home use. Occasionally I 
use it to scan a few pages at home and I only use very basic function. The scanner is used much often 
in the past few weeks since I start working from home. 

The scanner itself is excellent, however the software coming with it and instructions are 
horrible. Yesterday I spent a few hours trying to figure out the software. The Fijitsu website 
has a list of drivers and applications to download. Here is a screenshot of the list. 
 
<div style="max-width: 800px">
  <img class="img-fluid pb-3" src="/images/fi-7160/fi7160-software-list.png" alt="fi software list"> 
</div>

My computer still has very old version of software that was installed from a CD in the original 
package. The last item on the above list "fi Series Online Update 1.2.23" 
will automatically update several software to latest version and updated firmware of
the scanner. After trying out items on the list and doing some Google searches, 
here are my understanding on how they work. 

PaperStream Capture
: main scan software provided by Fujitsu. You can configure the scanner such as resolution,
paper size, punch hole removal etc. in this software. 

PaperStream IP (TWAIN and ISIS)
: scanner driver for Windows, needed for scanner to work.

ScanSnap Manager
: this software configures how the Scan/Enter button work. Need reboot computer after installation
for it to work.

ABBYY FineReader
: third party OCR software, which work with *ScanSnap Manager*.

ScandAll PRO
: third party software which is similar to a strip down version of Adobe Acrobat, 
not as powerful as *PaperStream Capture*. 

Scanner Central Admin (agent and console)
: this software seems to upload scanned documents to a network location, not useful
for me. 

Scan to Microsoft SharePoint
: it is also network related. 

I found a [youtube video](https://youtu.be/PgW-ILyIVik) on how to configure ABBYY FineReader 
with ScanSnap Manager and use the OCR function.  You can configure the scan button to automatically
scan the document, perform OCR, and save it to a specified folder. 

<div style="max-width: 350px">
  <img class="img-fluid pb-3" src="/images/fi-7160/fi7160-software-scansnap.png" alt="scansnap"> 
</div> 

The tricky part is that the ScanSnap Manager software is disabled if PaperStream Capture is open. 
You need to exit PaperStream Capture before enable Scansnap Manager. It takes me sometime to figure 
that out.
