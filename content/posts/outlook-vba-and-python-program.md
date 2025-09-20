title: Outlook VBA and Python Program
slug: outlook-vba-and-python-program
date: 2025-09-20 00:19
modified: 2025-09-20 00:19
tags: ai, python
note: working on vba and python interactions
no: 93


I am trying to automate some of my Outlook tasks and have found something interesting. 
Some of the emails I receive from a system include a line with latitude and longitude 
coordinates, like this:

```
Lat/Lon: 37.83635720,-76.17577260
```

I want to write a Python program to read the coordinate and determine whether it falls 
within a specific county. If the coordinate is inside the county boundary, the 
program will perform certain actions.

My first thought was to try accessing Outlook emails using Python. Python has a win32com 
package that can be used to interact with Outlook. However, I discovered that my Outlook 
has a security setting that does not allow third-party programs to read email messages. 
As a result, the following piece of code does not work:

```python
outlook = win32com.client.Dispatch("Outlook.Application")
explorer = outlook.ActiveExplorer()

selection = explorer.Selection # selected msgs
if selection.Count == 0:
    print("No item selected.")
    return

item = selection.Item(1)
body = item.Body # no access to body
```

Interestingly, if the email message has a PDF attachment, the Python program can save it 
to disk and read from the PDF. The code below actually works fine.

```python
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
selected_items = outlook.ActiveExplorer().Selection

for mail in selected_items:
    for attachment in mail.Attachments:
        if attachment.FileName.lower().endswith(".pdf"):
            # Generate a unique temp file path
            temp_dir = tempfile.gettempdir()
            unique_filename = f"{uuid.uuid4()}.pdf"
            temp_path = os.path.join(temp_dir, unique_filename)

            # Save the attachment
            attachment.SaveAsFile(temp_path)
            print(f"Saved: {temp_path}")

            # Extract text from the PDF
            extracted_text = extract_text_from_pdf(temp_path)
```

The next step is to write an Outlook VBA program that saves the email as a .msg file. 
The VBA program can then call a Python script to process the file. The Python script 
can write the result to a second file, which the VBA program can read to retrieve the 
result. The steps may sound complicated, but the code itself is actually quite straightforward.

Below are the VBA and Python code files:

[VBA program in txt form](/files/InCounty_Check.vba.txt)

[Python program in txt form](/files/extract_latlon.py.txt)


Another interesting point is that we can use the pdfplumber Python package to read PDF 
files and extract text from them. As mentioned earlier, win32com can save email attachments. 
So, if you only need to extract information from a PDF email attachment, you can write a 
pure Python program to handle it. If the Python program includes a GUI built with tkinter, 
you can convert the script into a Windows executable file using PyInstaller. The command is:

```
pyinstaller --onefile --windowed textbox_copy.py
```

Note that the generated executable can be quite large. In my case, the .exe file is 
around 65 MB, even though the original Python script is relatively small.
