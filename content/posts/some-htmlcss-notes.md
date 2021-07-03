title: Some HTML/CSS Notes
slug: some-htmlcss-notes
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

###CSS Property Names

Some CSS property names are not easy to remember. Here are a list of some confusing names. 

```
box-sizing: border-box;  /* I remember this rule as BSBB*/
justfy-content: center;
align-items: center;     /* really odd items vs content */
position, display, float /* remember them as PDF */
  display: flex;         /* this is for flexbox  */
  flex: 1 (or auto);     /* flex itself is a property name */
```

The responsive design mainly relies on media queries.  The media query syntax is not very intuitive. 

```
@media only screen and (max-width: 400px) {
  body { ... }
}
```

The logic behind `width` and `max-width` properties is interesting. The code below is an example. 
The element with `box` class will be 100% if it is less than 900px. The width will be 900px 
if it is larger than 900px.    

```
.box {
  width: 100%;
  max-width: 900px;
}
```

The oddest terms in HTML/CSS probably are "art direction".  The author explains that "(you can) 
think of art direction as responsive image optimization for designers."

###CSS Frameworks

The web book is awesome and the examples are easy to follow.  However, CSS itself is not easy to 
understand and write.  The *Web Typography* chapter has a simple page which includes a *typo.css* 
file. It only contains some basic stuff, but it has 201 lines of code. Some lines are difficult 
to write if you are not very skilled at CSS. 

That's probably why the CSS frameworks are popular. 
Here is a list of [awesome css frameworks](https://github.com/troxler/awesome-css-frameworks). 
This website is itself built on the Bootstrap CSS framework. 

