/*
Problem Description:
  Complete the following functions in the editor below:
    1. getArea(length, width): Calculate and return the area of a rectangle having
    sides "length" and "width".
    2. getPerimeter(length, width): Calculate and return the perimeter of a rectangle
    having sides "length" and "width"

    Constraints:
      - 1 <= length, width <= 1000
      - length and width are scaled to at most three decimal places

Example
Input:
3
4.5

Output:
13.5
15
*/
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}
/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;

    area = length * width;

    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;

    perimeter = 2 * (length + width);

    return perimeter;
}
