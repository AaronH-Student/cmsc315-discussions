# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Reflection
Design

I went with a simplified version of a Pokedex that I made for my sons. For this version, I used the names of a few pokemon as the keys and another dictionary with some basic information s the values for each pair. I mixed my approach to retrieving values, occasionally looking them up by key only and using the get method at other times. I'm most accustomed to just using the keys but the get method is less prone to exceptions.

Collisions

Collisions are when the hash of one key is the same as the hash of a different key. Python will find the hash of the key, go to the bucket where that key belongs, find the collision and compare the new key to the key that is already there. If the keys are not identical, then python proceeds through the hash table until it finds the next available empty bucket. This negatively impacts lookup and insertion performance, pulling it from O(1) towards O(n) in worst case scenarios.

Reflection

This was my first time taking a peek at what happens under the hood with python dictionaries. It was interesting to read about how the interpreter runs the hash table in C. The unit definitely deepened my understanding of how these deceptively simple data types actually work.

I did not experience any significant barriers or challenges, dictionaries are a very intuitive implementation of hash tables.

Hash tables mostly behave like a standard array with some extra logic about how to assign values to the available indexes. The key of a key-value pair is hashed which is then assigned to a given index or bucket. If/when two unique hash values share an index or bucket, it results in a collision where some follow-on logic is applied to ensure the key-value pair is added to the hash table.&nbsp; In chaining, the index or bucket will continue to append new key-value pairs to the same index. In python, the interpreter uses open addressing where the interpreter finds the&nbsp; next available empty index to add the new key-value pair.

The key is hashed again when seeks a specific value which tells the interpreter where to look in the array. If the key is not at the first position, the algorithm will check the next bucket in the hash table according to the probing logic until it finds the key or hits an empty-since-start bucket which will let the program know that the key is not in the hash table.