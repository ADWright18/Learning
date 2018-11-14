# Responsive Web Design Principles
This section will cover the basic ways to use CSS for Responsive Web Design

## Create a Media Query
* Media Queries are a new technique introduced in CSS3 that change the
presentation of content based on different viewport sizes.
* The viewport is a user's visible area of a web page, and is different
depending on the device used to access the site
* Examples:

```css
/*
Returns the content when the device's
width is less than or equal to 100px
*/
@media (max-width: 100px) {/* CSS Rules */}

/*
Returns the content when the device's
height is more than or equal to 350px
*/
@media (min-height: 350px) {/* CSS Rules */}
```

## Make an Image Responsive
* Making images responsive with CSS is very simple.
* Example:

```css
img {
  max-width: 100%;
  display: block;
  height: auto;
}
```

* The ```max-width``` property of 100% scales the image to fit the width of its
container, but the image won't stretch wider than its original width.
* Setting the ```display``` property to block changes the image from an inline
element (its default), to a block element on its own line
* The ```height``` property of auto keeps the original aspect ratio of the image

## Use a Retina Image for Higher Resolution Displays
* The simplest way to make way to make your images appear "retina" (and optimize
them for retina displays) is to define their ```width``` and ```height``` values
as only half of what the original file is.
* Example:

```html
<style>
  img {
    height
  }
</style>
```
