title: Click Python Package
slug: package-click
meta: Resources on learning python package click 
date: 2020-02-18 14:39
modified: 2020-02-18 14:39
tags: python, flask
related_posts: python-argparse
note: 28

I am reading Miguel Grinberg's 
[Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
and *Flask Web Development* book and converting OpenSignTool to a flask app. The 
[Click package](https://click.palletsprojects.com/en/7.x/) is one of the
tools created by Armin Ronacher and used by many developers as a standalone 
python package. I decided to read the Click documentation and build a 
simple command line interface for OpenSignTool. 

I found several resources to learn Click:

1. [Youtube Tutorial Video by Armin](https://youtu.be/kNke39OZ2k0). Armin speaks
fast, and I find 0.75 play speed is good for me. The video content is very good. 
2. [Writing Python Command-Line Tools With Click](https://dbader.org/blog/python-commandline-tools-with-click). 
Seb Vetter wrote two articles about Click on dbader.org.  This is the first one.
3. [Mastering Click: Writing Advanced Python Command Line Apps](https://dbader.org/blog/mastering-click-advanced-python-command-line-apps). 
This is Seb Vetter's second article on dbader.org. Both articles are fantastic. 

Here is what I come up with, 

```python
# signtool_cli.py

@click.command()
@click.option('--width', '-w', default=0, 
    help='Width of the sign in inches for output svg' )
@click.option('--ratio', '-r', default=1.0, 
    help='Ratio to true scale when drawing the sign, default 1.0')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('output_filename', type=click.Path(writable=True), 
    required=False)
def cli(width, ratio, filename, output_filename): 
    stream = open(filename, 'r')
    d = yaml.safe_load(stream)
    ......
    if output_filename is None:
        output_filename = pathlib.Path(filename).with_suffix('.svg')
    out_file = open(output_filename, 'w')
    out_file.write(output_stream.getvalue())
    click.echo(f'Write the file to {output_filename}')

if __name__ == '__main__':
    cli()
```

This is the help message and command to run the app. 

```
(dev_cli) george@STK2M3:~/dev_cli$ python signtool_cli.py --help
Usage: signtool_cli.py [OPTIONS] FILENAME [OUTPUT_FILENAME]

Options:
  -w, --width INTEGER  Width of the sign in inches for output svg
  -r, --ratio FLOAT    Ratio to true scale when drawing the sign, default 1.0
  --help               Show this message and exit.

(dev_cli) ... $ python signtool_cli.py --ratio 0.1 R2-1.yaml 
Write the file to R2-1.svg

```

I also created a second python file to read all files under a directory and 
write results to another directory. 

```python
# signtool_dir.py

@click.command()
@click.option('--width', '-w', default=0, 
    help='Width of the sign in inches for output svg' )
@click.option('--ratio', '-r', default=1.0, 
    help='Ratio to true scale when drawing the sign, default 1.0')
@click.argument('input_dir', type=click.Path(exists=True, dir_okay=True, 
    file_okay=False))
@click.argument('output_dir', type=click.Path(dir_okay=True), required=False)
def cli(width, ratio, input_dir, output_dir):
    pathlist = pathlib.Path(input_dir).glob('**/*.yaml')
    for filename in pathlist:
        stream = open(filename, 'r')
        d = yaml.safe_load(stream)
        arg = dict_to_obj(d)
        ......
        if output_dir is None:
            output_dir = input_dir
        output_filename = output_dir + pathlib.Path(filename).stem + '.svg'
        out_file = open(output_filename, 'w')
        out_file.write(output_stream.getvalue())
        click.echo(f'Write the file to {output_filename}')

if __name__ == '__main__':
    cli()

```

Here is how to call this Click app.

```
(dev_cli) george@STK2M3:~/dev_cli$ python signtool_dir.py --help
Usage: signtool_dir.py [OPTIONS] INPUT_DIR [OUTPUT_DIR]

Options:
  -w, --width INTEGER  Width of the sign in inches for output svg
  -r, --ratio FLOAT    Ratio to true scale when drawing the sign, default 1.0
  --help               Show this message and exit.

(dev_cli) george@STK2M3:~/dev_cli$ python signtool_dir.py ./yaml/ ./svg/
Write the file to ./svg/W8-5P.svg
Write the file to ./svg/R2-1.svg
......
```


