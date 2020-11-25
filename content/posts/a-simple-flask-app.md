title: A Simple Flask App - Temperature Converter
slug: a-simple-flask-app
meta: How to develop and deploy a simple flask app
date: 2020-03-21 10:19
modified: 2020-03-21 10:19
tags: python, flask
note: 30


I have been studying Flask web framework for some time.  Today I decide to 
write a simple app and deploy it to a Digital Ocean web server under my 
control.  The Flask app itself is very simple. It is a temperature converter which 
converts temperature in fahrenheit to celsius. The source code is on github and the 
[link is here](https://github.com/georgexyz19/temperature_converter). You can access the live app via 
[this link](https://gotrafficsign.com/convert). 

The flask app follows the guidance on Miguel Grinberg's *Flask Web Development* book. 
The only difference is that I used Flask-BS4 instead of Flask-Bootstrap package 
because Flask-Bootstrap is still based on Bootstrap 3.  It does not have a database 
backend. 

The web server already have a nginx server installed and configured for a static website. 
I followed [this medium article](https://medium.com/@jgefroh/a-guide-to-using-nginx-for-static-websites-d96a9d034940) 
to setup the nginx server and letsencrypt certification. At the time I set up 
the server, I did not really understand what I was doing.  A few weeks ago I found 
[this nginx setting article](http://www.patricksoftwareblog.com/how-to-configure-nginx-for-a-flask-web-application/) 
which details nginx settings very well. I added a location block to pass along (so called reverse 
proxy) http requests to the gunicorn WSGI server. 

```
location /convert {
    proxy_pass http://localhost:8001;
    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

The setting code above is from Miguel Grinberg's 
[Flask Mega-Tutorial Chapter 17](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux). 
I followed step-by-step guides in this Chapter to set up tools on the server. 
I thought about setting up Docker containers, but decided not to do so 
after reading the chapter a few times.  The main reason is that the Docker containers will 
incur a significant overhead on a $5/mo Digital Ocean server. 

William Shotts' book [The Linux Command Line](http://linuxcommand.org/tlcl.php) 
has a section on ssh, scp and sftp. It has a sentence "the SFTP protocol 
is supported by many of the graphical file managers found in Linux distributions." I found 
[FileZilla](https://filezilla-project.org/) is easy to setup and easy to transfer files between 
a local computer and the server. 

