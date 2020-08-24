title: GIMP Tips
slug: gimp-tips
date: 2020-05-10 10:54
modified: 2020-05-10 10:54
tags: software utility
note: Some tips on how to use GIMP
no: 45

GIMP is a free and open source image manipulation software. I only use a small
subset of functions of the software.  Here are some tips I keep a record for
myself. 

### Move Pixels In An Area

`Ctrl + Alt + Move Selection` is the shortcut to move selected area of an image.
GIMP adds a "Floating selection" temporary layer in the layer dialog.  After you
make the change, click the mouse in another area to confirm the move. The
temporary layer merges onto the main layer. 

### Add White Background After Deleting An Area

Sometimes GIMP leaves a hole on an image when you delete the pixels in an area.
Choose menu item `Layer` > `Transparency` > `Remove Alpha Channel` and the area
will show white background.

### Remove Background Grey Hue

Some scanned image file has a grey hue on the background. The `Colors` >
`Curves` tool can be used to remove the background. 


<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/gimp/gimp-curve-r.png" alt="gimp curve"> 
</div>

### Resize Image to a Certain Size

If you want a scanned plan image file to be a certain size such as Arch D (36"
x 24") size, you can follow those steps. 

1. Click on menu `Image` > `Canvas Size` to resize image to be on a larger
   canvas (e.g., 36" x 24"), choose white background and center the image.
2. Select an area of image including the borders.  
3. Copy and paste the image pixels onto a new layer. 
4. Choose menu item `Layer` > `Scale Layer` to enlarge the layer to canvas
   size.  It seem that setting `Interpolation` to None works better for scanned
plans.
5. Merge down the image layer to the background layer. 

<p class="text-muted">This article will be continuously updated (last update: 8/24/2020). <p>
