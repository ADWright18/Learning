# Code Structure

## Statements
* Statements are syntax constructs and commands that perform actions
* Example:
```javascript
alert('Hello, world!')
```
* We can also have statments separated by a semicolon:
```javascript
alert('Hello, world!');
alert('World');
```

## Semicolons
* A semicolon can be omitted in most cases when a line break exists:
```javascript
alert('Hello')
alert('World')
```
* Here JavaScript interprets the line break as an "implicit" semicolon.
a.k.a. an automatic semicolon insertion
* There are cases when a newline does not mean a semicolon, for example:
```javascript
alert(3 +
1  
+ 2);
```
* The code outputs ```6```, because JavaScript does not insert semicolons here.
