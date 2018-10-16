# ArrayList and Resizable Arrays
* An ArrayList is an array that resizes itself as needed while still providing O(1)
access.
* A typical implementation is that when the array is full, the array doubles in
size. Each doubling takes O(n) time, but happens so rarely that its amortized
insertion time is still O(1).
* Example:

```java
ArrayList<String> merge(String[] words, String[] more) {
  ArrayList<String> sentence = new ArrayList<String>();
  for (String w : words) sentence.add(w);
  for (String w : more) sentence.add(w);
  return sentence;
}
```

* Note: Resizing factor for Java is 2
* Question: Why is the amortized insertion runtime O(1)?
  * Answer: The total number of copies to insert N elements is roughly
  N/2 + N/4 + N/8 + ... + 2 + 1, which is just less than N. Therefore, inserting
  N elements takes O(N) work total each. Each insertion is O(1) on average, even
  though some insertions take O(N) time in the worst case
