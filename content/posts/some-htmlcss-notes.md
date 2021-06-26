title: Some HTML/CSS Notes
slug: some-htmlcss-oddities
date: 2021-06-26 16:56
modified: 2021-06-26 16:56
tags: web development
note: some html/css notes
no: 76

###HTML/CSS Editor Layout

I am reviewing the [HTML & CSS Is Hard](https://www.internetingishard.com/html-and-css/) website, which is 
an awesome resouce for studying HTML and CSS. It is easy to work through the examples with this window layout. 
The left window opens the website, the right top window is the Vim editor, and the right bottom browser window 
is a preview of the HTML file.  

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/html-editor.png" alt="HTML editor">
</div>

###HTML/CSS Notes

Some HTML/CSS rules are strange (at least to me). This post records some of them for future reference.  

####CSS Descendant Selector

The CSS descendant selector is a blank between two selectors. For example, the code below `p a ` selects 
an `a` element inside `p`.  The second example below selects three elements with classes social, logo, and 
subscribe. 

```
p a {
  color: #DAABCE;
}
```

```
.social, 
.logo,
.subscribe {
  border: 1px solid #5995DA;
}
```
This just feels odd. If you do not pay attention, you would think they work the same, but they are 
totally different things. The CSS has a child selector like this `li>a`. It feels more natural than 
the descendant selector. 



