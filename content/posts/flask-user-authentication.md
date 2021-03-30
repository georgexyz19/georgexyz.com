title: Flask User Authentication Steps
slug: flask-user-authentication
date: 2021-03-30 09:37
modified: 2021-03-30 09:37
tags: flask
note: note to be added
no: 70

The user authentication process described in Chapter 8 of Miguel Grinberg's book is quite 
complicated. The flask-login plugin makes it a little simpler. Here are the steps it takes 
to create a basic login and logout system. 

1. Add `password_hash` field to `User` model, and add a `@password.setter` property and 
   a `verify_password` method to the `User` model. 
2. Add `UserMixin` to `User` model. The `UserMixin` is defined in flask-login plugin. 
3. Initialize `login_manager` in `app/__init__.py` like any other flask plugin.
4. In `base.html` template file, add links for login and logout. The links will show up 
   for all pages of the site. 
5. Add `login` view function. 
    - It needs a LoginForm form class.
    - And it needs a `auth/login.html` template file. 
    - It calls `login_user` of flask-login to do the actual log in work. 
6. The `logout` view function is simpler.  It calls `logout_user` to do the work and no 
   template is need. 

Page 113 of the book has an excellent description on how flask-login works. 

The login for user registration is simpler. This is a typical form which is collecting 
some data from a user and saving the data in a db. The steps is simple. 

1. Add a link on the `login` template page for user registration.
2. Create a `register` view function.
    - The function needs a RegistrationForm class.
    - It needs a template to show the form.
    - It will initialize a `user` instance and commit it to the db.

There is also a [flask-user](https://flask-user.readthedocs.io/en/latest/) 
plugin that is widely used.
