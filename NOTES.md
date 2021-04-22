# Update notes for the blog site

[georgexyz.com](https://www.georgexyz.com)

## 4/22/2021

Added a new article template article-2.html for *Book List* article. 
Add a line on the blog post header `template: article-2` to activate 
the new template. This template changes the article width from 8 columns 
to 12 columns in Bootstrap. 

Here is code to link internal articles (grep command results)

```
george@T420s:~/Code/georgexyz.com$ grep -winr "{filename}" ./content/posts/
./content/posts/python-calendar-app.md:12:[PDFXChange-Viewer]({filename}/posts/pdfxchange-viewer.md) 
```
