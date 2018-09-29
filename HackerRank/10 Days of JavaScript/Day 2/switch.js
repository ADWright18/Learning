/*
Problem Description:
  Complete the getLetter(s) function in the editor, It has one parameter: a string,
  s, consisting of lowercase English alphabetic letters (i.e., a though z). It must
  return A, B, C, or D depending on the following criteria:
    - If the 1st character in string s is in the set {a,e,i,o,u}, then return A
    - If the 1st character in string s is in the set {b,c,d,f,g}, then return B
    - If the 1st character in string s is in the set {h,j,k,l,m}, then return C
    - If the 1st character in string s is in the set {n,p,q,r,s,t,v,w,x,y,z}, then return D

  Hint: You can get the letter at some index i in s using the syntax s[i] or s.charAt(i)

  Constraints:
    - 1 <= |s|<= 100, where |s| is the length of s
    - String s contains lowercase English alphabetic letters (i.e., a through z) only

Example
Input:
adfgt

Output
A

*/
function getLetter(s) {
    let letter;
    // Write your code here
    let n = s[0];

    switch (n) {
        case "a":
        case "e":
        case "i":
        case "o":
        case "u":
            letter = "A";
            break;
        case "b":
        case "c":
        case "d":
        case "f":
        case "g":
            letter = "B";
            break;
        case "h":
        case "j":
        case "k":
        case "l":
        case "m":
            letter = "C";
            break;
        default:
            letter = "D"
            break;
    }

    return letter;
