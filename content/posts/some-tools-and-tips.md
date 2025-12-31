title: Some Tools and Tips
slug: some-tools-and-tips
date: 2025-12-31 05:24
modified: 2025-12-31 05:24
tags: software utility
note: 2025 year end summary about win32 tools
no: 94

I recently discovered some new Windows tools that I’d like to share. The first one is 
[AutoHotkey v2](https://www.autohotkey.com/docs/v2/), a powerful automation tool for Windows.

With AutoHotkey, you can write simple scripts that run in the background to create global keyboard shortcuts and 
automate repetitive tasks. Below is an example of a basic script. It’s relatively easy to set up and can 
significantly boost your productivity.

Notice that the *Ctrl + Alt + A* shortcut invokes a [WinPython](https://winpython.github.io/) script. 
One nice aspect of this approach is that you don’t need to install Python to run the script. 
You only need to extract WinPython and save it in a local folder.

```
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  Auto reload the current script Ctrl + Alt + R
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

^!r::{
    try Reload()
    catch
        MsgBox("Failed to reload the script.", "Error", 16)
}


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  AkelPad Win + A
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

#a:: {
    Run(
        ".\APPS\akelpad-x64\AkelPad.exe",
        "",
        ""
    )
}

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  OPEN x86 Book  Ctrl + Alt + X
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
^!x:: {
    SumatraPDF := ".\APPS\SumatraPDF.exe"
    mutcd := ".\APPS\Files\x86_book.pdf"
    cmd := Format('"{1}" "{2}"', SumatraPDF, mutcd)
    Run(cmd, "", "")
}

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  FOR TIME SHEET APPROVAL Ctrl + Alt + A
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
^!a:: {
    python := ".\APPS\WPy64-31280\python\python.exe"
    script := ".\APPS\approve_timesheet.py"
    cmd := Format('"{1}" "{2}"', python, script)
    Run(cmd, "", "Hide")
}


::pwo::Please work on this request, thank you{!}{Enter}{Enter}George

```

I reread one of my favorite books *Programming Windows, 5th Edition* by Charles Petzold in October. With the help of 
ChatGPT, I also discovered several useful tools and tips for Win32 programming.

The typical recommendation for developing Win32 applications is to use Visual Studio 2022 Community Edition. However, 
there is a very nice tool called [PortableBuildTools](https://github.com/Data-Oriented-House/PortableBuildTools) on 
GitHub that makes it easy to set up a Windows development environment. This approach allows you to avoid the bloated 
Visual Studio interface while still having the essential build tools needed for Win32 development. 

I tried several ways to compile the Win32 example programs from the book, including CMake and NMAKE. The easiest 
approach I found was to write a generic Windows batch file and use the Command Prompt to compile the program. Below is 
the `build.bat` file I created. You’ll need to modify it if a project contains multiple `.c` or `.rc` files.

```
ECHO Call devcmd.bat to setup environment
SET DEV_CMD_PATH=C:\BuildToolsx86\devcmd.bat

REM Check if the file exists at the specified path
IF EXIST "%DEV_CMD_PATH%" (
    ECHO Found build environment script. Calling it now...
    CALL "%DEV_CMD_PATH%"
) ELSE (
    ECHO Error: Build environment script not found at "%DEV_CMD_PATH%"
    EXIT /B	
)

ECHO Starting compilation...

SET CC_FLAGS=/c /W3 /O2 /MD /EHsc /D "UNICODE" /D "_UNICODE"
SET RC_FLAGS=/l 0x409 /d "UNICODE" 
SET LINK_FLAGS=kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib ^
               advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib ^
               odbc32.lib odbccp32.lib /nologo /subsystem:windows /machine:I386 

FOR %%f IN (*.c *.cpp) DO (
    ECHO Compiling %%f...
    
    REM /Fo      = Specify output file/dir.
    REM %%~nf    = The filename part of %%f (e.g., "main" from "main.c")
    REM %%~nf.obj = The output filename (e.g., "main.obj")
    REM %%f      = The full input filename (e.g., "main.c")
    
    cl %CC_FLAGS% /Fo%%~nf.obj %%f
)
ECHO C Files Compile Done.


ECHO Compiling resources (*.rc to *.res)...

FOR %%f IN (*.rc) DO (
    ECHO Compiling resource file: %%f
    
    REM Run the Resource Compiler (rc)
    REM %%f     = The full input filename (e.g., "app.rc")
    REM /fo     = Specify the output filename
    REM %%~nf   = The filename part of %%f (e.g., "app" from "app.rc")
    REM %%~nf.res = The output filename (e.g., "app.res")
    
    rc %RC_FLAGS% /fo %%~nf.res %%f
)

ECHO Resource compilation complete.


REM Get the full path (e.g., C:\Path\To\MyFolder\)
SET SCRIPT_FULL_PATH=%~dp0

REM Remove the trailing backslash to make substitution easier
SET FOLDER_NAME=%SCRIPT_FULL_PATH:~0,-1%

FOR %%i IN ("%FOLDER_NAME%") DO SET FOLDER_NAME=%%~nxi


ECHO Linking object and resource files...

link %LINK_FLAGS% *.obj *.res /OUT:%FOLDER_NAME%.exe

ECHO Link command is complete


ECHO Deleting all generated build files (*.obj, *.res)...
del /Q /F *.obj *.res
ECHO Clean up complete.

ECHO Build complete.

PAUSE
```

When developing Win32 programs, the Hex Editor [HxD](https://mh-nexus.de/en/hxd/) can be quite helpful for inspecting 
binaries and debugging low-level details.

This post is not finished yet, and I plan to add more content in the future. 
