# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Implementation

Starting with insert, I opted to check if the root was None, setting the root node if it was empty before using the recursive helper method. I later refactored this to be more in line with what I think the intent of the assignment, calling the helper method on root and checking for None within the recursive method to establish the new node.

The search method also relied on a recursive helper method that took a node and the target value. Each node is checked for None, returning False when true, otherwise returning True on a match or traversing down the appropriate direction.

The inorder method was interesting as it required multiple recursive calls to traverse each child for every node. I set up a values variable to contain all values, only appending once the left most node was established, then zig-zagging its way back around the whole tree.

For the main function, I tried to set up a balanced tree to showcase all test methods. I leaned heavily on formatted strings to explain what was happening at each test stage. The edge cases did not post an issue. I did have to think for a bit to come up with a suitable real-world example that wasn't just accounts again. I went with a spell checker. Spell checker programs have to potentially crosscheck thousands of words in a document and make comparison to dictionaries containing tens of thousands of words in the English language. Array based search algorithms would be too slow and inefficient, so a BST would significantly reduce the time complexity for the program. To implement my use-case, I just set up a small "dictionary" or words and made a couple of test strings. The spell_check helper cleans up the string, removing punctuation and making the words lowercase for easier comparison. Then the BST spelling_tree search method is called for each word in the string, printing a message to inform the user if a word seems to be spelled incorrectly.

## Reflection

This was my first time building and implementing a BST, it was definitely an interesting exercise and I like the benefits that the structure affords. Recursive functions have been a source of frustration for me in the past but this unit's use cases were easy enough to digest.

I only came across one issue while working on the code and it wasn't related to the learning objectives. I had initially tried to implement a decorator around the recursive insert method to demonstrate how the tree was being traversed and values inserted, but it would print statements in reverse order due to the recursion so I ended up breaking it out in the method itself instead. It unnecessarily complicated the method, but I liked the output better for this discussion post.

For the real-world example, I ended up making a simple spell checker with a tiny dictionary and some small test strings. It searches the dictionary BST for each word in the string and prints a simple statement when a word (that is present in the dictionary) is spelled incorrectly. BSTs are a good way to keep the number of traversals down when looking through the tens of thousands of words in the English language.

The innate ordered structure of BSTs allows quick and efficient ordering and access to elements regardless of where they are in the tree as long as it is well balanced. Issues can arise in unbalanced trees where it is only as efficient as a list, so the root is crucial.
