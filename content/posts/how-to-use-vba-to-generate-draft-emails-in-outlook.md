title: How to Use VBA to Generate Draft Emails in Outlook
slug: how-to-use-vba-to-generate-draft-emails-in-outlook
date: 2025-03-29 03:29
modified: 2025-03-29 03:29
tags: other
note: Chatgpt VBA code
no: 89

Every Friday, I need to send two emails to other teams at work. Although the emails 
are straightforward, drafting them each week is time-consuming and prone to errors. Below 
are some requirements for these emails:

1. The email subject must include Friday's date (e.g., "Files for the Week of 3-28-2025").
2. The email will contain several attached PDF files.
3. The body of the email lists the filenames of the attachments.

After repeating this task for several weeks, I sought a way to automate the process. Chatgpt 
helped me generate the following VBA code to streamline the workflow,

[VBA program to draft emails](/files/vba_email_draft.txt)

Now, with the click of a button in Outlook, the VBA code automatically generates the email, 
and I simply click the Send button. This automation saves me approximately 30 minutes each 
week.
