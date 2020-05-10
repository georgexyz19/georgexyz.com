title: GIMP Tips
slug: gimp-tips
date: 2020-05-10 10:54
modified: 2020-05-10 10:54
tags: software utility
note: Some tips on how to use GIMP
no: 45

GIMP is a free and open source image manipulation software. I only use a small subset of functions 
of the software.  Here are some tips I keep a record for myself. 

### Move Pixels In An Area

`Ctrl + Alt + Move Selection` is the shortcut to move selected area of an image.  GIMP adds a 
"Floating selection" temporary layer in the layer dialog.  After you make the change, click the 
mouse in another area to confirm the move. The temporary layer merges onto the main layer. 

### Add White Background After Deleting An Area

Sometimes GIMP leaves a hole on an image when you delete the pixels in an area. Choose menu 
item `Layer` > `Transparency` > `Remove Alpha Channel` and the area will show white background.

### Remove Background Grey Hue

Some scanned image file has a grey hue on the background. The `Colors` > `Curves` tool can be 
used to remove the background. 


<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/gimp/gimp-curve-r.png" alt="gimp curve"> 
</div>

<p class="text-muted">This article will be continuously updated (last update: 5/10/2020). <p>
