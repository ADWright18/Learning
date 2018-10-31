# Stacks and Queue Interview Questions
Compilation of stack and queue related questions and answers.

## 3.1 - Three in One
* Q - Describe how you could use a single array to implement three stacks.
  * A - You can split the array space into 3 arrays with a length of
  len(array) / 3. The first stack would have index 0 to len(array) / 3, second
  stack would have index len(array) / 3 to 2 * len(array) / 3, and third would
  have 2 * len(array) / 3 to len(array) - 1

## 3.2 - Stack Min
* Q - How would you design a stack which, in addition to push and pop, has a
function min which returns the minimum element? Push, pop, and min should
operate in O(1) time.
  * A - You can add an instance variable, min, that stores the current min of
  the stack. Every time an element is pushed onto the stack, we compare that
  element to the current min. If the pushed element in less than the current min,
  then the pushed element becomes the min of the stack.

## 3.3 - Stack of Plates
* Q - Imagine a (literal) stack of plates. If the stack gets too high, it might
topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure SetOfStacks
that mimics this. SetO-fStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity. SetOfStacks.push()
and SetOfStacks.pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a
single stack).
