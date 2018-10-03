# Variables
* Most of the time, a JavaScript application needs to work with information. Here
are two examples:
  * An online shop - the information might include goods being sold and a shopping
  cart
  * A chat application - the information might include users, messages, and much
  more.
* Variables are used to store this information

## A Variable
* A variable is a "named storage" for data
* To create a variable in JavaScript, we need to use the ```let``` keyword
* Example:

```JavaScript
let message;
```

* Now we can put some data into it by using the assignment operator ```=```:

```JavaScript
let message;
message = 'Hello'; // store a string

alert(message); // show the variable content
```

* Note: ```var``` is slightly different than ```let```

## Variable Naming
* There are two limitations for a variable name in JavaScript:
  * The name must contain only letters, digits, symbols ```$``` and ```_```.
  * The first character must not be a digit.
* Valid names, for instance:

```javascript
let userName;
let test123;
```

* Invalid names:

```javascript
let 1a = 1; // cannot start with a digit
let my-name = 2; // a hyphen '-' is not allowed in the name
```

* Note: Letter case matters

## Constants
* To declare a constant (unchanging) variable, one can use ```const``` instead
of ```let```:

```javascript
const myBirthday = '18.04.1982';
```

* Variables declared using ```const``` are called "constants". They cannot be
changed.

### Uppercase Constants
* There is a widespread practice to use constants as aliases for difficult-to-remember
values that are known prior to execution
* For instance:

```javascript
const COLOR_RED = "#F00"
const COLOR_GREEN = "#0F0"
const COLOR_ORANGE = "FF7F00"

// ...when we need to pick a color
let color = COLOR_ORANGE;
alert(color); // #FF7F00
```

* In other words, capital-named constants are only used as aliases for "hard-coded"
values

## Summary
* We can declare variables to store data. That can be done using ```var``` or ```let```
or ```const```
* ```let``` - is a modern variable declaration. The code must be in strict mode
to use ```let``` in Chrome (V8)
* ```var``` - is an old-school variable declaration.
* ```const``` - is like ```let```, but the value of the variable can't be changed
