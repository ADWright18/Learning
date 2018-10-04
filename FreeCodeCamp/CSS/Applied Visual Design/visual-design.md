# Applied Visual Design

Applied Visual Design with CSS from freeCodeCamp

## Create Visual Balance Using the text-align Property
* CSS has several options for how to align it with the ```text-align``` property
* ```text-align: justify;``` causes all lines of text except the last line to meet
the left and right edges of the line box.
* ```text-align: center;``` centers the text
* ```text-align: right;``` right-aligns the text
* ```text-align: left;``` (the default) left-aligns the text

## Adjust the Width of an Element Using the width Property
* You can specify the width of an element using ```width``` property in CSS
* Values can be given in relative length units (such as em), absolute length
units (such as px), or as a percentage of its containing parent element
* Example:

```css
img {
  width: 220px;
}
```

## Adjust the Height of an Element Using the height Property
* You can specify the height of an element using the ```height``` property in CSS,
similar to the ```width``` property.
* Example:

```css
img {
  height: 20px;
}
```

## Use the strong Tag to Make Text Bold
* To make text bold, you can use the ```strong``` tag.
* Example:

```html
<p>Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at <strong>Stanford University</strong>.</p>
```

## Use the u Tag to Underline Text
* To underline text, you can use the ```u``` tag.
* Example:

```html
<p>Google was founded by Larry Page and Sergey Brin while they were <u>Ph.D. students</u> at <strong>Stanford University</strong>.</p>
```

## Use the em Tag to Italicize Text
* To emphasize text, you can use the ```em``` tag.
* Example:

```html
<p><em>Google was founded by Larry Page and Sergey Brin while they were <u>Ph.D. students</u> at <strong>Stanford University</strong>.</em></p>
```

## Use the s Tag to Strikethrough Text
* To strikethrough text, which is when a horizontal line cuts across the characters,
you can use the ```s``` tag.
* Example:

```html
<h4><s>Google</s>Alphabet</h4>
```

## Create a Horizontal Line Using the hr Element
* You can use the  ```hr``` tag to add a horizontal line across the width of its
containing element.
* Example:

```html
<h4><s>Google</s>Alphabet</h4>
<hr> <!-- Underline Here -->
```

## Adjust the background-color Property of Text
* Instead of adjusting your overall background or the colors of the text to make
the foreground easily readable, you can add a ```background-color``` to the element
holding the text you want to emphasize
* Example:

```css
h4 {
  text-align: center;
  padding: 10px;
  background-color: rgba(45, 45, 45, 0.1)
}
```

## Adjust the Size of a Header Versus a Paragraph Tag
* You can use the ```font-size``` property to adjust the size of the text in an
element.
Example:

```css
h4 {
  text-align: center;
  background-color: rgba(45, 45, 45, 0.1);
  padding: 10px;
  font-size: 27px;
}
```

## Add a box-shadow to a Card-like Element
* The ```box-shadow``` property applies one or more shadows to an element
* Here's an example of the CSS to create multiple shadows with some blur, at
mostly-transparent black colors:

```css
p {
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
```

## Decrease the Opacity of an Element
* The ```opacity``` property in CSS is used to adjust the opacity, or conversely,
the transparency for an item
* Example:

```css
.links {
  text-align: left;
  color: black;
  opacity: 0.7;
}
```

## Use the text-transform Property to Make Text Uppercase
* The ```text-transform``` property in CSS is used to change the appearance of
text.
  * ```lowercase``` - "transform me"
  * ```uppercase``` - "TRANSFORM ME"
  * ```capitalize``` - "Transform Me"
  * ```initial``` - Use the default value
  * ```inherit``` - Use the ```text-transform``` value from the parent element
  * ```none``` - Default: Use the original text
* Example:

```css
h4 {
  text-align: center;
  background-color: rgba(45, 45, 45, 0.1);
  padding: 10px;
  font-size: 27px;
  text-transform: uppercase;
}
```

## Set the font-size for Multiple Heading Elements
* The ```font-size``` property is used to specify how large the text is in a given
element.

```html
<style>
  h1 {
    font-size: 68px;
  }
  h2 {
    font-size: 52px;
  }
  h3 {
    font-size: 40px;
  }
  h4 {
    font-size: 32px;
  }
  h5 {
    font-size: 21px;
  }
  h6 {
    font-size: 14px;
  }
</style>
```

## Set the font-weight for Multiple Heading Elements
* You set the ```font-size``` of each heading tag in the last challenge, here
you'll adjust the ```font-weight```.

```html
<style>
  h1 {
    font-size: 68px;
    font-weight: 800;
  }
  h2 {
    font-size: 52px;
    font-weight: 600;
  }
  h3 {
    font-size: 40px;
    font-weight: 500;
  }
  h4 {
    font-size: 32px;
    font-weight: 400;
  }
  h5 {
    font-size: 21px;
    font-weight: 300;
  }
  h6 {
    font-size: 14px;
    font-weight: 200;
  }
</style>
```

## Set the font-size of Paragraph Text
* The ```font-size``` property in CSS is not limited to headings, it can be applied
to any element containing text.
* Example:

```css
p {
  font-size: 16px;
}
```

## Set the line-height of Paragraphs
* CSS offers the ```line-height``` property to change the height of each line in
a block of text.
* Example:

```css
p {
  font-size: 16px;
  line-height: 25px;
}
```

## Adjust the Hover State of an Anchor Tag
* The styling of an anchor tag can be changed for its hover state using the ```:hover```
pseudo-class selector.
* Example:

```css
a:hover {
  color:red;
}
```

##
