/*
Problem Description:
  1. Declare a constant variable, PI, and assign if the value Math.PI.
  2. Read a number, r, denoting the radius of a circle from stdin
  3. Use PI and r to calculate the area and perimeter of a circle having radius r
  4. Print area as the first line of output and print perimeter as the second line
  of output

  Constraints:
    - 0 <= r <= 100
    - r is a floating-point number scaled to at most 3 decimal places

Example
Input:
2.6

Output:
21.237166338267002
16.336281798666924
*/
function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const PI = Math.PI;
    let r = readLine();

    // Print the area of the circle:
    console.log(PI * r * r);

    // Print the perimeter of the circle:
    console.log(2 * PI * r);
