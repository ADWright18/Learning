# 2.1 - Hello, World!

Section 2.1 of javascript.info tutorial

## The "script" Tag
* Javascript programs can be inserted in any part of an HTML document with the
help of the ```<script>``` tag.
* For instance:
```html
<!DOCTYPE HTML>
<html>

<body>

  <p>Before the script...</p>

  <script>
    alert( 'Hello, world!' );
  </script>

  <p>...After the script.</p>

</body>

</html>
```
* The ```<script>``` tag contains JavaScript code which is automatically executed
when the browser meets the tag

## External Scripts
* JavaScript code can be located in a different file.
* The script file is attached to HTML with the ```src``` attribute:
```html
<script src="/path/to/script.js"></script>
```
* Here ```/path/to/script.js``` is an absolute path to the file with the script
(from the site root)
* We can give a full URL as well, for instance:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.2.0/lodash.js0">
</script>
```
* To attach several scripts, use multiple tags:
```html
<script src="/js/script1.js"></script>
<script src="/js/script2.js"></script>
```

## Summary
* We can use a ```<script>``` tag to add JavaScript code to the page
* The ```type``` and ```language``` attributes are not required
* A script in an external file can be inserted with  
```html
html <script src="path/to/script.js">
```
