title: Django Model and Form Validation
slug: django-model-form-validation
meta: Discuss Django Validation
date: 2019-08-15 00:59
modified: 2019-08-15 00:59
tags: django
note: I wrote this article in an afternoon. I will update it as I read more on this topic. 
no: 21
 

Django model and form validation is a somewhat complicated and 
confusing topic in Django app development.  A developer needs to understand 
several basic concepts such as model, model field, form, model form, etc. to 
have a good understanding of validation.  Most Django books and online tutorials 
do not have a good discussion on validation. 

Django official documentation has detailed descriptions on validation. 
However, the contents are dispersed on several places.  This post describes the 
materials I have read on this topic. 

### Validator Function

The 
[validator official documentation page](https://docs.djangoproject.com/en/2.2/ref/validators/#django.core.validators.EmailValidator) 
is a good starting point to study model and form validation. 

The validator function is a callable that takes a value and raises a 
ValidationError if not validated. Here is an example from the page:

```
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

from django.db import models

class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
```

The subsection *how validators are run* on the validator
page has three links. 

* The second link *validating objects* is about 
*model validation*.  The link points to a subsection on the 
[model instance reference](https://docs.djangoproject.com/en/2.2/ref/models/instances/#validating-objects) 
page. 
* The first link *form validation* points 
to a separate page about 
[*form validation*](https://docs.djangoproject.com/en/2.2/ref/forms/validation/). 
* The third link goes to the ModelForm page. 

### Model Validation

A model's `full_clean()` method performs model validation. The method calls 
three other methods:

* `clean_fields()` method
* `clean()` method, as a whole
* `validate_unique()` method

The model `save()` method does NOT call `full_clean()` method automatically. 
A programmer needs to call it manually to trigger model validation like 
the below code.

```
try:
    article.full_clean()
except ValidationError as e:
    ...
    # handle the error
``` 

[A stack overflow answer](https://stackoverflow.com/questions/7366363/adding-custom-django-model-validation) 
shows a typical pattern to conduct custom model validation. The model class overrides the 
`clean()` method to provide custom model validation and the `save()` method 
to call `full_clean` method.  The example code is shown below:

```
class BaseModel(models.Model):
    # model fields 

    def clean(self, *args, **kwargs):
        # add custom validation here
        super(BaseModel, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BaseModel, self).save(*args, **kwargs)
```

[Another stack overflow answer](https://stackoverflow.com/questions/42003866/django-validation-at-model-not-forms-level) 
shows how to use custom model validation or simply use model field's built-in 
validator.

Model field's validation will not kick in unless the `full_clean()` method 
is explicitly called. For example, the `p2.save()` below would not raise an 
exception when called. 

```
class PageModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

>>> from page.models import PageModel #page app name
>>> p1 = PageModel(name='Page1', slug='page1')
>>> p1.save()
>>> p2 = PageModel(name='Page2', slug='page2#$%')
>>> p2.save()        # no error
>>> p2.full_clean()  # raise exception
```

Checking `clean_fields()` method source code, it has the following lines. 
The `f.clean(...)` method calls validation method on a model field.

```
try:
    setattr(self, f.attname, f.clean(raw_value, self))
except ValidationError as e:
    errors[f.name] = e.error_list
```

### Form Validation

While model validation is a subsection on a Django documentation page, the 
[form validation](https://docs.djangoproject.com/en/2.2/ref/forms/validation/) 
is on a separate page. Form validation is normally executed when the `is_valid()` 
method is called on a form. A programmer can also trigger form validation 
by accessing `errors` attribute or call `full_clean()` method of a form.

Form validation has a series of steps:

* `to_python()` method on a field, correct data type
* `validation()` method on a field
* `run_validators()` method on a field
* `clean()` method on a Field subclass, which calls above three methods and returns the clean data
* `clean_<fieldname>()` method has access to cleaned\_data Python object and returns value that replaces data in cleaned\_data
* `clean()` method of form, for multiple fields

The same documetation page has several nice examples, which are based on the 
model shown below:

```
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = MultiEmailField()
    cc_myself = forms.BooleanField(required=False)
```

The same page points out that "there are special considerations when overriding 
the `clean()` method of a ModelForm subclass."

Chapter 7 of Andrew Pinkham's *Django Unleashed* book, titled *allowing user 
input with forms*, has good example on how to override `clean_<fieldname>` 
method. The discussion on model validation and form validation in this chapter 
is better than other Django books I have read. 

### ModelForm Validation

The form validation steps described in the previous section also apply to 
ModelForm validation.  In addition to that, `Model.full_clean()` method is 
triggered after the form's `clean()` method is called. So, model validation 
methods are not triggered by model `save()` method, but model validation methods 
are triggered by ModelForm validation. 
[This stack overflow question](https://stackoverflow.com/questions/40881708/django-model-validator-not-working-on-create) 
discusses this exact issue. The accepted answer also has code example on 
model validation. 

Error messages at the form field level take precedence over the error messages 
defined at the model field level. 

