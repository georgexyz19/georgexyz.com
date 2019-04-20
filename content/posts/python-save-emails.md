title: Python Code to Save Emails in Gmail to PDF Files
slug: python-save-emails
meta: Python code to save emails in Gmail to PDF files using pyautogui. 
date: 2019-04-03 13:02
modified: 2019-04-03 13:02
tags: Python


One of my work tasks requires me to save hundreds of emails in my work Gmail 
account to PDF files in local hard drive.  I could do it manually spending hours 
saving emails, or I could write a python program to do the work. 
No doubt I prefer the second approach. 

A google search finds several online articles discussing how to do it.  A typical 
method is to install a Chrome plugin for the browser, and the plugin will do the work. 
But granting permission to a plugin to read my work emails is not acceptable. 

After reading some articles, I settled on two methods. The first one is to select and 
export emails in Gmail to a .mbox file, then write a python program to read the .mbox file 
and save emails.  The second one is discovered when I was reading the
last chapter of Al Sweigart's wonderful book 
[Automate The Boring Stuff With Python](https://automatetheboringstuff.com/). 
This method uses the pyautogui module and involves writing a python program to simulate 
mouse button clicks and keyboard key presses to save emails.  The program is like a person is 
clicking the mouse button and typing on the keyboard. 

Let's look at the first method. 
[An article on Lifwire.com](https://www.lifewire.com/how-to-export-your-emails-from-gmail-as-mbox-files-1171881) 
has step by step guide on how to save emails to a .mbox file.  The python standard
library modules _mailbox_ and _email_ can read emails in the .mbox file.  I spent
some time writing a python program, which also parses email content and extracts 
useful information from emails. The code structure looks like this. 

```python
import mailbox
import email.header
import email.utils 

import time, datetime, argparse
import re, csv, copy, os  # for os.path.exists

def parse_html(message):
    '''parse a message and return html_content'''
    if message.is_multipart():
        content = ''.join(part.get_payload(decode=True).decode(
            'utf-8') for part in message.get_payload())
        html_content = content
    else:
        content = message.get_payload(decode=True)
        html_content = content.decode('utf-8')
    return html_content

def parse_date(message):
    '''return a date of message of format datetime'''
    date = message['Date']
    dt_parse = email.utils.parsedate(date)
    timestamp = time.mktime(dt_parse)
    dt = datetime.datetime.fromtimestamp(timestamp)  # dt of the message
    dt = dt + datetime.timedelta(hours=3) # email time has an offset
    return dt

def parse_subject(message):
    subj = message['Subject']
    s1 = ' '.join(subj.strip().splitlines()) # remove multiple \n or ' '
    s2 = ' '.join(s1.split())
    return s2

# ... other methods for parsing email contents
    
if __name__ == '__main__':
    mbox = mailbox.mbox(path)
    save = True # flag for parse emails, not save them
    for message in mbox:
        # code to parse emails
        html = parse_html(message)
        # ...
        if save:
            fn = '{}'.format( ... )
            f = open(fn, 'w')
            f.write(html)
            f.close()            

```

I find a major flaw in this approach a few days later.  The Google archive 
system has a limit on the number of time a user is allowed to export emails to .mbox files. Once 
the daily limit (3 times on my account) is reached, it does not allow a user to export 
emails that day.  The system simply gives a message "Please try to create your 
archive again".

When I am reading the last chapter of Al Sweigart's book, I realize that
the pyautogui module can be used for this task.  Here is the code to save emails, 

```python
# save_emails.py by Geroge Zhang on 2/1/2019
# The GMail window should be in a status shown in SaveEMails.png
# The EMails should be in a folder(label), the program clicks next button
# This program only works on my laptop

# Chrome settings -> Advanced -> Privacy and security -> Content settings ->
# pop-ups and redirects -> allow => add https://mail.google.com

# setup the program
import pyautogui # this requires installation
import time

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

TOTALEMAILS = 10
START = 1

nextButton = (1229, 189)
printButton = (1230, 247)
saveButton = (202, 167)
filenameBox = (878, 443)
saveDialog = (788, 503)

closeButton = (470, 15)
centerWindow = (683, 7)

print('>>> 5 Seconds to start <<<')
time.sleep(5)

##print('Click window center to activate Gmail')
##pyautogui.click(centerWindow[0], centerWindow[1])

print('Please click the first email in a label group')
print('>>> 5 Seconds to start <<<')
time.sleep(5)

for i in range(START, TOTALEMAILS + START):
    print('\nNow click the print button')
    pyautogui.click(printButton[0], printButton[1])
    time.sleep(5)

    print('Click the Save email button')
    pyautogui.click(saveButton[0], saveButton[1])
    time.sleep(1)

    print('Click filename field')
    pyautogui.click(filenameBox[0], filenameBox[1])
    time.sleep(.5)

    pyautogui.press('home')
    filename_prefix = '{0:03}'.format(i) + ' - '
    pyautogui.typewrite(filename_prefix)
    time.sleep(.5) 

    print('Click the Save file button')
    pyautogui.click(saveDialog[0], saveDialog[1])
    time.sleep(.5)

    print('Close the second window')
    pyautogui.click(closeButton[0], closeButton[1])
    time.sleep(.5)

    print('Click next button')
    pyautogui.click(nextButton[0], nextButton[1])
    time.sleep(.5)

print(' >>> Done <<< ')
```

The program is able to save 1500 emails in about four hours.  Depending on the network speed, the
sleep seconds between tasks can be adjusted. Sometime the program may abort for 
some reason.  Change the variables `TOTALEMAILS` and `START` at the beginning of the program
to resume running. 

You need to manually save a few emails in Chrome browser to understand what the
program is doing.  How do I get the coordinates of the buttons on Gmail interface?  The 
Al Sweigart book includes a `mouseNow.py` program.  I simple write down the coordinates
on a piece of paper and then type those coordinates into the program. 

<div style="max-width:450px">
  <img class="img-fluid" src="/images/save-emails-notes.png" alt="save emails"> 
</div>
