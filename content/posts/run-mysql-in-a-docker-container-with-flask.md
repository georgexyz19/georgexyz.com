title: Run MySql In A Docker Container With Flask
slug: run-mysql-in-a-docker-container-with-flask
date: 2021-04-28 13:25
modified: 2021-04-28 13:25
tags: docker, flask
note: Some notes on docker mysql and flask settings
no: 75

Miguel Grinberg's *Flask Web Development* book Chapter 5 shows how to run Flask with 
SqlAlchemy and a SQLite database. Because SQLite is included in Python, the settings 
are simple and easy. This post records the steps on how to run a MySQL database in a docker 
container with Flask (under a Linux Mint OS or Ubuntu). 

###Install Docker

The first step is to install docker and pull the MySQL container image. This 
[Docker Curriculum](https://docker-curriculum.com/) website has a nice Docker 
tutorial. 

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh 
sudo usermod -aG docker george  # restart after this step

# those steps installs docker-compose, optional
sudo curl -L "https://github.com/docker/compose/releases/download/\
              1.29.1/docker-compose-$(uname -s)-$(uname -m)"\ 
              -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose 
docker-compose

docker pull mysql:latest
docker images
```

###Run Container

How to start running the MySQL container is a little tricky. After some Google 
searching, I found that this 
[medium article](https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa) 
has nice practical examples. I simply create a bash script `start_mysql.sh` and 
bash command `source start_mysql.sh` will start the container. The script includes 
a `-v` volume option which maps a directory on a host to the mysql data directory 
in the container. So the database data files are saved on the host computer. 

```
# start_mysql.sh file
#!/bin/bash
docker run --name=test-mysql \
    --env="MYSQL_ROOT_PASSWORD=pw" \
    -p 3306:3306 \
    -v /home/george/Code/docker/test-mysql/data:/var/lib/mysql \
    -d  \
    mysql:latest
```

A second bash script `mysql-terminal.sh` starts a terminal session which runs 
`mysql` client inside the container. It will enter the `mysql` as a `root` user. 

```
# mysql-terminal.sh file
#!/bin/bash
docker exec -it test-mysql mysql -uroot -ppw
```

You can create a new db and a user once you are in the `mysql` client with 
those commands. 

```
CREATE DATABASE test_db;
USE test_db;
CREATE USER 'newuser'@'%' IDENTIFIED BY 'pw';
GRANT ALL PRIVILEGES ON test_db.* to 'newuser'@'%';
```

###Connect Flask App

Once you have the docker container running, you can connect a Flask app to it.
The first step is to install flask-sqlalchemy, pymysql, and cryptography packages 
in virtual environment. 

```
. venv/bin/activate
pip install flask-sqlalchemy pymysql cryptography
```

Note the pymysql and cryptography packages are required. I cannot make it working 
without those packages. 

In the flask app python file, have those db settings. 

```
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://newuser:pw@localhost:3306/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

Then you can run the `flask shell` and run those commands to test the db connections. 

```
>>>from hello import db
>>>db.create_all()
>>>db.metadata.tables.keys()  # show table names
```

