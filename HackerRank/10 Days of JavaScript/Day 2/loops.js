/*
Problem Description:
  The vowelsAndConsonants function should do the following:
    1. First, print each vowel in s on a new line. [a,e,i,o,u]
    2. Second, print each consonant in s on a new line as it appeared in s.


Example
Input:
javascriptloops

Output:
a
a
.
.
.
l
p
s
*/
/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let v = ["a", "e", "i", "o", "u"]; // Vowel List

    let vowels = [];
    let consonants = [];


    for (var i = 0; i < s.length; i++) {
        for (var j = 0; j < v.length; j++) {
            if (s[i] == v[j]) {
                vowels.push(s[i]);
            } else {
                consonants.push(s[i]);
            }
        }
    }

    for (var i = 0; i < vowels.length; i++) {
        let m = vowels.length;
        console.log(vowels[m - i]);
    }

    for (var i = 0; i < consonants.length; i++) {
        let m = consonants.length;
        console.log(vowels[m - i]);
    }

}
