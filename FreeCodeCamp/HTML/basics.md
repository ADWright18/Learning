# HTML Basics

Basics and essentials for HTML from freeCodeCamp.

## Commenting
* Commenting in HTML starts with ```<!--```, and ends with a ```-->```
* Example:
```html
<!--
<h1>Hello World</h1>
-->
<h2>CatPhotoApp</h2>
<!--
<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack
your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
-->
```

## HTML5 Elements
* HTML5 introduces more descriptive HTML tages. These include ```header```,
 ```footer```, ```nav```, ```video```, ```article```, ```section```, and others
* These tags make your HTML easier to read, and also help with Search Engine Optimization (SEO)
and accessibility
* The ```main``` HTML5 tag helps search engines and other developers find the
main content of your page
* Example:
```html
<h2>CatPhotoApp</h2>

<main>
  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack
  your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>

  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the
  couch sleep in the sink fluffy fur catnip scratched.</p>
</main>
```

## Adding Images
* Add images to your site by using the ```img``` element, and point to a specific
image's URL using the ```src``` attribute
* Example:
```html
<img src="https://www.your-image-source.com/your-image.jpg">
```
* Note: All ```img``` elements are self-closing
* All ```img``` elements **must** have an ```alt``` attribute. The text inside
an ```alt``` attribute is used for screen readers to improve accessibility and is
displayed if the image fails to load

### Turn an Image into a Link
* You can make elements into links by nesting them within an ```a``` element
```html
<a href="#"><img src="https://bit.ly/fcc-running-cats" alt="Three kittens running
towards the camera."></a>
```

### Link to External Pages with Anchor Elements
* You can use ```anchor``` elements to link to content outside of your web page
* ```anchor``` elements need a destination web address called an ```href```
attribute and an archor text
* Example:
```html
<a href="https://freecodecamp.org">this links to freecodecamp.org</a>
```

### Nest an Anchor Element within a Paragraph
* You can nest links within other text elements
* Example:
```html
<p>
Here's a <a target="_blank" href="http://freecodecamp.org"> link to freecodecamp.org</a>
for you to folow
</p>
```

### Make Dead Links Using Hash Symbol (#)
* Sometimes you want to add ```a``` elements to your website before you know where
they will link
Example:
```html
href="#"
```

## Link to Internal Sections of a Page
* Anchor elements can also be used to create internal links to jump to different
sections within a webpage
* To create an internal link, you assign a link's ```href``` attribute to a hash
symbol ```#``` plus the value of the ```id``` attribute
* Example:
```html
<a href="#contacts-header">Contacts</a>
...
<h2 id="contacts-header">Contacts</h2>
```
* When you click the Contacts link, you'll be taken to the section of the webpage
with the **Contacts** header element

## Create a Bulleted Unordered List
* Unordered lists start with an opening ```<ul>``` element, followed by any number
of ```<li>``` elements
* Unordered lists close with a ```</ul>```
* Example:
```html
<ul>
  <li>milk<li>
  <li>cheese</li>
</ul>
```

## Create an Ordered List
* Ordered lists start with an opening ```<ol>``` element, followed by any number
of ```<li>``` elements
* Ordered lists close with a ```</ol>```
* Example:
```html
<ol>
  <li>Garfield</li>
  <li>Sylvester</li>
</ol>
```

## Create a Text Field
* You can create a text input like this:
```html
<input type="text">
```
* Note that ```input``` elements are self-closing

### Add Placeholder Text to a Text Field
* Placeholder text is what is displayed in your ```input``` element before your
user has inputted anything.
* Example:
```html
<input type="text" placeholder="this is placeholder text">
```

## Create a Form Element
* You can build web forms that actually submit data to a server using nothing
more than pure HTML.
* You can do this by specifying an action on your ```form``` element
* Example:
```html
<form action="/url-where-you-want-to-submit-form-data"></form>
```

### Add a Button to a Form
* Adding a button to a form will allow us to send data from the form to the URL specified
* Example:
```html
<button type="submit">this button submits the form</button>
```

### Use HTML5 to Require a Field
* You can require specific form fields so that your user will not be able to submit
your form until the field is filled out
* Example:
```html
<input type="text" required>
```

### Create a Set of Radio Buttons
* You can use ```radio buttons``` for questions where you want the user to only
give you one answer out of multiple options
* Radio buttons are a type of ```input```
* Example:
```html
<label>
  <input type="radio" name="indoor-outdoor">Indoor
</label>
```
* It is considered best practice to set a ```for``` attribute on the ```label```
element, with a value that matches the value of the ```id``` attribute of the```input```
element
* Example:
```html
<label for="indoor">
  <input id="indoor" type="radio" name="indoor-outdoor">Indoor
</label>
```

### Create a Set of Checkboxes
* Checkboxes are a type of ```input```
* Each of your checkboxes can be nested with its own ```label``` element.
* All related checkbox inputs should have the same ```name``` attribute
* Example:
```html
<label for="loving">
  <input id="loving" type="checkbox" name="personality">Loving
</label>
```

### Check and Radio Buttons and Checkboxes by Default
* You can set a checkbox or radio button to be checked by default using the
```checked``` attribute
* Example:
```html
<input type="radio" name="test name" checked>
```

## Nest Many Elements within a Single div Element
* The ```div``` element, also known as division element, is a general purpose
container for other elements.
* Just like any other non-self-closing element, you can open a ```div``` element
with ```<div>``` and close it on another line with ```</div>```

## Declare the Doctype of an HTML Document
* You can tell the browser the version of an HTML document by adding the ```<!DOCTYPE ...>
tag on the first line, where the "```...```" part is the version of HTML. For HTML5,
you use ```<!DOCTYPE html>.
* Example:
```html
<!DOCTYPE html>
<html>
  <!-- Your HTML code goes here -->
</html>
```

## Define the Head and Body of an HTML Document
* You can add another level of organization in your HTML document within the ```html```
tags with the ```head``` and ```body``` elements.
* Example:
```html
<!DOCTYPE html>
<html>
  <head>
    <!-- metadata elements -->
  </head>
  <body>
    <!-- page contents -->
  </body>
</html>
```
