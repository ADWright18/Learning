# CSS Basics

Basics and essentials for CSS from freeCodeCamp.

## Change the Color of Text
* The property that is responsible for the color of an element's text is the ```color```
style property
* Example:
```html
<h2 style="color: blue;">CatPhotoApp</h2>
```

## Use CSS Selectors to Style Elements
* At the top of your code, create a ```style``` block like this:
```html
<style>
</style>
```
* Inside the style block, you can create a ```CSS selector``` for all ```h2```
elements
* Example:
```html
<style>
  h2 {color: red;}
</style>
```

## Use a CSS Class to Style an Element
* Classes are reusable styles that can be added to HTML elements
* Example:
```html
<style>
  .blue-text {
    color: blue;
  }
</style>

<h2 class="blue-text">CatPhotoApp</h2>
```
* Classes allow you to use the same CSS styles on multiple HTML elements.

## Change the Font Size of an Element
* Font size is controlled by the ```font-size``` CSS property
* Example:
```css
h1 {
  font-size: 30px;
}
```

## Set the Font Family of an Element
* You can set which font an element should use, by using the ```font-family``` property
* Example:
```css
h2 {
  font-family: sans-serif;
}
```

## Import a Google Font
* To import a Google Font, you can copy the font(s) URL from the Google Fonts library
and then paste it in your HTML.
* Example:
```html
<link href="https://fonts.googleapis.com/css?family-lobster" rel="stylesheet" type="text/css">
```

## Specify How Fonts Should Degrade
* When one font isn't available, you can tell the browser to "degrade" to another font
* Example:
```css
p {
  font-family: Helvetica, sans-serif;
}  
```

## Size Your Images
* CSS has a property called ```width``` that controls an element's width.
* Just like fonts, we'll use ```px```(pixels) to specify the image's width.
* Example:
```html
<style>
  .large-image {
    width: 500px;
  }
</style>
```

## Add Borders Around Your Elements
* CSS borders have properties like ```style```, ```color``` and ```width```
* Example:
```html
<style>
  .thin-red-border {
    border-color: red;
    border-width: 5px;
    border-style: solid;
  }
</style>
```

## Add Rounded Corners with border-radius
* You can specify a ```border-radius``` with pixels.
* Example:
```css
.thick-green-border {
  border-radius = 10px;
}
```

## Make Circular Images with a border-radius
* In addition to pixels, you can also specify the ```border-radius``` using a percentage
* Example:
```css
.thick-green-border {
  border-radius: 50%;
}
```

## Give a Background Color to a div Element
* You can set an element's background color with the ```background-color``` property
* Example:
```css
.green-background {
  background-color: green;
}
```

## Set the id of an Element
* In addition to classes, each HTML element can also have an ```id``` attribute
* There are several benefits to using ```id``` attributes: You can use an ```id```
to style a single element and also modify it with JavaScript
* Example:
```html
<h2 id="cat-photo-app">
```

## Use an id Attribute to Style an Element
* You can use the ```id``` attribute to style elements with CSS
* Example:
```css
#cat-photo-element {
  background-color: green;
}
```

## Adjust the Padding of an Element
* Three important properties control the space that surrounds each HTML element: ```padding```
, ```margin```, and ```border```.
* Refer to css-box-model.png for a visual representation of the CSS Box Model
* Example:
```css
.red-box {
  background-color: crimson;
  color: #fff;
  padding: 20px;
  margin: 20px;
}
```

## Adjust the Margin of an Element
* An element's ```margin``` controls the amount of space between an element's ```border```
and surrounding elements

## Add a Negative Margin to an Element
* You can set an element's ```margin``` to a negative value, the element will grow
larger

## Add Different Padding to Each Side of an Element
* CSS allows you to control the ```padding``` of all four individual sides of an element
with the ```padding-top```, ```padding-right```, ```padding-bottom```, and ```padding-left``` properties
* Example:
```css
.red-box {
  padding-top: 40px;
  padding-right: 20px;
  padding-bottom: 20px;
  padding-left: 40px;
}
```

## Add Different Margins to Each Side of an Element
* CSS also allows you to control the ```margin``` of all four individual sides of an element
with the ```margin-top```, ```margin-right```, ```margin-bottom```, and ```margin-left``` properties
* Example:
```css
.blue-box {
  padding-top: 40px;
  padding-right: 20px;
  padding-bottom: 20px;
  padding-left: 40px;
}
```
## Use Clockwise Notation to Specify the Padding of an Element
* Instead of specifying an element's padding on each side individually, you can specify
them all in one line, like this:
```css
h1 {
  padding: 10px 20px 10px 20px;
}
```

## Use Clockwise Notation to Specify the Margin of an Element
* Refer to Clockwise Notation for Padding
* Example:
```css
h1 {
  margin: 10px 20px 10px 20px;
}
```

## Use Attribute Selectors to Style Elements
* There are other CSS Selectors you can use to select custom groups of elements to style
* Example:
```css
[type='radio'] {
  margin: 20px 0px 20px 0px;
}
```

## Understanding Absolute versus Relative Units
* The two main types of length units are absolute and relative. Absolute units tie
to physical units of length (i.e., in and mm)
* Relative units, such as ```em``` or ```rem```, are relative to another length value
(i.e., ```em``` is based on the size of an element's font)

## Style the HTML Body
