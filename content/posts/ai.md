title: AI Is Exciting
slug: ai
date: 2025-03-01 00:37
modified: 2025-03-08 07:34
tags: other
note: AI is a revolutionary tech
no: 87

It’s been over a year since I last updated this website. Recently, I've been using 
ChatGPT more and more, so it would be a good time to update the wesite and write 
something about AI.

AI is the most exciting technology I've seen in recent years. Here are a few examples:

When I ask a question on Google, the AI provides a very good answer. This level of 
 response probably wouldn’t be possible before the ChatGPT.

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/ai/whirlpool.png" alt="whirlpool question"> 
</div>

Here’s a question about Outlook. ChatGPT can give a solid answer in a few seconds.

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/ai/outlook.png" alt="outlook question"> 
</div>

AI can help with writing code. I know a bit of VBA, and here’s a relatively complex VBA
 program that copies data from Outlook to Excel.

[VBA program in txt form](/files/vba_code.txt)

Here is another example of AI writing a short command-line script to list file names in a 
directory without their extensions. Manually writing this type of code can be challenging 
for a person.

```
@echo off
for %%f in (*.*) do (
    if /I "%%~xf" neq ".bat" echo %%~nf >> filelist.txt
)
```