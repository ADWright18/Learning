/*
Problem Description:
  Implement a function named factorial that has one parameter: an integer, n.
  It must return the value of n! (i.e., n factorial)

  Constraints:
    - 1 <= n <= 10

Example
Input:
4

Output:
24
*/
function factorial(n) {

    // Base Case
    if (n == 0) {
        return 1
    }
    // Recursive Case
    else {
        return n * factorial(n-1)
    }

}
