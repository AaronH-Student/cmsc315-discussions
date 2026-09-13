# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


## Implementation

My first instinct was to use the Python list index method which is already a linear search algorithm but decided that would likely defeat the purpose of the exercise. Instead, I just used a for loop to iterate over each element in the lst argument and compared it against the target value, returning the index when a match was found or -1 if the algorithm went through each element without finding a match. I tested the list.index method out of curiosity and left it commented out under linear_search. Comparing runtime of the final linear search algorithm and the index method showed that the base index method is considerably faster, probably becaue it is implemented in C.

The binary search algorithm is just like it was in our reading material, establish the lower and upper bounds of the search range and narrow it down each time there is no match to the target value at the middle index of said search range. If the lower bound exceeds the upper bound then the target value is not present and the function returns -1. The binary search method requires the data to be ordered otherwise the location of the target values would be random and impossible for the algorithm to accurately narrow down the search range.

For the real-world scenario, I generated a simplified list of product IDs in a list I called inventory. The inventory is ordered which makes it so I can use binary search to find objects as necessary. I used the time library to show how the runtime differs between linear and binary searches. Testing on a smaller inventory showed that linear search took approximately 4 times longer than the binary search when looking for the same value in the same list. The difference was almost exactly the same with the larger inventory of 10000 product IDs. Edge case testing yielded no surprises and the functions worked exactly as expected.


## Reflection

1. This was my first time implementing a binary search algorithm on a list in python, I can see how it would be useful. I also learned what the list.index implementation looks like in C which was interesting.
2. I did not really run into any significant challenges, the logic behind the binary search algorithm took a few reads to make sure I understood exactly what was happening but is quite clear now.
3. Binary search cannot be used on unordered data, linear search would have to be used in such a case where order cannot be guaranteed. When data is ordered, linear search is likely more useful on smaller datasets as it makes fewer comparisons per step. Binary search is far more efficient for larger datasets. There are some tradeoffs for each. Binary search takes longer to find the first element in a list. I ran a test to see how they both did when finding the first object of the larger inventory and linear search was obviously much quicker as it was its best case scenario. Binary search took considerably longer in that case, but was much faster in the majority of other cases.