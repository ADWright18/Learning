# StringBuilder
* Observe the following code to concatenate a list of strings

```java
String joinWords(String[] words) {
  String sentence = "";
  for (String w : words) {
    sentence = sentence + w;
  }
  return sentence;
}
```

* On each concatenation, a new copy of the string is created, and the two strings
are copied over, character by character.
  * The total time -> O(x + 2x + ... + nx). This reduces to O(xn^2)

* StringBuilder avoids this problem by creating a resizeable array of all the
strings copying them back to a string only when necessary.

```java
String joinWords(String[] words) {
  StringBuilder sentence = new StringBuilder();
  for (String w : words) {
    sentence.append(w)
  }
  return sentence.toString();
}
```
