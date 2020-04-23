=================================
Print Python Source Code on Paper
=================================

:slug: print-source-code-paper
:date: 2020-04-23 09:29
:modified: 2020-04-23 09:29
:tags: python, pelican, software utility
:meta: Show how to print pelican source code
:note: python program to print pelican source code
:no: 38

I am reading Pelican source code. Sometimes I do not have a computer nearby, a I want to 
print out the source code on paper. The current release of Pelican is version 4.2.0. The 
source code is `available on github`_. 

.. _available on github: https://github.com/getpelican/pelican

After you :code:`git clone` the code to local drive, you can run the following Linux 
command to have a basic idea of the code base. The number of lines of Pelican 4.2 code is 
5,530, which is actually a litter shorter than version 4.0.1 (5,670).  The file 
:code:`generators.py` is the longest with 936 lines. The main code base has 
14 python files. 

.. code-block:: command

    $ find . -maxdepth 1 -name '*.py' -exec wc -l '{}' + | sort -n
    9 ./__main__.py
    92 ./rstdirectives.py
    129 ./urlwrappers.py
    136 ./cache.py
    140 ./server.py
    160 ./paginator.py
    226 ./log.py
    271 ./writers.py
    560 ./__init__.py
    607 ./contents.py
    662 ./settings.py
    748 ./readers.py
    854 ./utils.py
    936 ./generators.py
    5530 total

A Google search finds this article `Print Out Your Code On Paper`_ on medium.com. The 
author made some good points in the article. It also introduces
a piece of Unix/Linux command line software called :code:`enscript`, which can covert 
text code to postscript file. A typical command looks like this, 

.. code-block:: command

    enscript -1rG --line-numbers -p out.ps --highlight=python \
        -c inputfile.py

.. _Print Out Your Code On Paper: https://medium.com/@tashian/print-out-your-code-on-paper-7c760a376bca

A furthur Google search finds `an online man page`_ for :code:`enscript`. The page has 
detailed detailed infomation regarding the software options and configuration files. 

.. _an online man page: http://manpages.ubuntu.com/manpages/precise/en/man1/enscript.1.html

The default fancy header configuration file :code:`enscript.hdr` is stored in the directory 
:code:`/usr/share/enscript/`. I want to change the date and time on the left corner to 
current date/time. Also I want to change the page number on the right corner to "number 
of pages processed so far" rather than the default "current page numbers". An easy way 
is to copy the :code:`enscript.hdr` to a new :code:`enscript_mod.hdr` file and copy back 
the modified file to the directory. I only change three lines of code in 
:code:`enscript_mod.hdr` file. 

.. code-block:: command

    %Format: moddatestr	%W
    %Format: modtimestr	%C
    %Format: pagenumstr	$p

After that, I write a short python script to call the :code:`enscript` command. The 
python code is shown below. 

.. code-block:: python

    #! python3
    #
    # sudo cp enscript_mod.hdr /usr/share/enscript/
    # the mod hdr file change the file mod date/time to current date/time
    # 
    # note that the hdr file should be in configuration dir
    # see ubuntu manpage
    # http://manpages.ubuntu.com/manpages/precise/en/man1/enscript.1.html
    #
    # convert ps to pdf
    # ps2pdfwr pelican.ps pelican_print.pdf

    import os
    import subprocess

    # result of $ls -S -l *.py
    files ='''
    -rw-r--r-- 1 george george 38063 Apr 18 14:56 generators.py
    -rw-r--r-- 1 george george 28171 Apr 18 14:56 utils.py
    -rw-r--r-- 1 george george 27331 Apr 18 14:56 readers.py
    -rw-r--r-- 1 george george 25748 Apr 18 14:56 settings.py
    -rw-r--r-- 1 george george 22680 Apr 18 14:56 contents.py
    -rw-r--r-- 1 george george 21857 Apr 18 14:56 __init__.py
    -rw-r--r-- 1 george george 11161 Apr 18 14:56 writers.py
    -rw-r--r-- 1 george george  6453 Apr 18 14:56 log.py
    -rw-r--r-- 1 george george  5385 Apr 18 14:56 paginator.py
    -rw-r--r-- 1 george george  5133 Apr 18 14:56 server.py
    -rw-r--r-- 1 george george  4992 Apr 18 14:56 cache.py
    -rw-r--r-- 1 george george  3803 Apr 18 14:56 urlwrappers.py
    -rw-r--r-- 1 george george  2951 Apr 18 14:56 rstdirectives.py
    -rw-r--r-- 1 george george   126 Apr 18 14:56 __main__.py
    '''

    def fnlist(files):
        filenames = []
        fns = files.split('\n')
        for fn in fns:
            if fn:
                filename = fn[46:]
                if filename.startswith('__'):
                    filenames.insert(0, filename)
                else:
                    filenames.append(filename)
        # print(filenames)
        return filenames


    def main():
        cwd = os.getcwd()
        os.chdir('./pelican/pelican')
        filenames = ' '.join(fnlist(files))
        p1 = subprocess.run(
            'enscript --fancy-header=enscript_mod --line-numbers ' + \
            '-p ../../pelican_code_print.ps ' + \
            '--highlight=python ' + \
            f'--color=1 -c {filenames}', 
            shell = True,
            capture_output = True
        )
        print(p1.stdout.decode())
        os.chdir(cwd)

        
    if __name__ == '__main__':
        main()


After those steps. the final pdf file of Pelican 4.2 source code can be downloaded here_.

.. _here: /files/pelican_code_print.pdf


