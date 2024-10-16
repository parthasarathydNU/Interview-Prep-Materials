Considerations :
- Network bandwidth - Large image sizes are slower to load 
- Memory - Images once downloaded are stored in memory

#### General ideas

- Biggest and easiest improvement to image loading is implementing `lazy loading`
- Picking the right format
- A new format - Progressive JPEGs - here, first a blurred image is loaded on the UI and the image becomes clearer as the image is downloaded from the servers

### Making images adaptable 

https://www.smashingmagazine.com/2014/05/picturefill-2-0-responsive-images-and-the-perfect-polyfill/

The three pillars, 
- screen size
- pixel density of the screen 
- internet bandwidth

### `srcset`

The Responsive Images Community Group (RICG), got together and worked on the new attribute called `srcset`
```html
<img alt="dog" src="dog.jpg" srcset="dog-HD.jpg 2x, dog-narrow.jpg 300w, dog-narrow-HD.jpg 600w 2x">  
```

Here we notice that in the srcset, we have the following syntax:
`image-path width-of-the-source optimal-pixel-ratio`

### `<picture>`

One step further than just using the `srcset` attribute, is to use the picture tag. 

This allows us to control images for various breakpoints better:
```html
<picture>
  <source media="(min-width: 600px)" srcset="large-1.jpg, large-2.jpg 2x">
  <img alt="A fat dog" src="small-1.jpg">
</picture>  

<picture>
  <source srcset="extralarge.jpg, extralarge.jpg 2x" media="(min-width: 1000px)">
  <source srcset="large.jpg, large.jpg 2x" media="(min-width: 800px)">
  <source srcset="medium.jpg">
  <img srcset="medium.jpg" alt="Cambodia Map">
</picture>  

```
Here, the `img` tag is used as the default fallback image, while the source attribute is used for defining media queries along with the `srcset` attribute

