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

The user registration process is simpler. It is a typical form collecting 
data from a user and saving the data in a database. Here are the steps. 

1. Add a link on the `login` template page for user registration.
2. Create a `register` view function.
    - The function needs a RegistrationForm class.
    - It needs a template to show the form.
    - It will initialize a `user` instance and commit it to the db.

User email confirmation logic is not very difficult. The system sends an email to a user 
during registration.  The email contains a link to a view function that changes a field of 
`User` model in the database. The interesting part is that user id is not passed around in 
text, instead it is encoded into tokens. Below are the steps. 

1. Modify the `User` model. 
    - Add a `confirm` boolean field.
    - Add two methods `generate_confirmation_token` and `confirm` 
2. Send an email in `register` view function. 
    - The email does not need forms, but it needs templates. 
    - Email has link to a `confirm` view function and contains token
3. Add a `confirm` view function
    - The function has a `<token>` as a variable. 
    - It calls `current_user.confirm` method to change db field. 

If the user confirms, everything is good. But the system needs to consider what happens 
when a user does not confirm. The idea is to check every request, and to show an 
`unconfirmed` page when necessary.  The pages has a link to resend the confirmation email. 


There is also a [flask-user](https://flask-user.readthedocs.io/en/latest/) 
plugin that is widely used.
