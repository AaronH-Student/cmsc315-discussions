# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## Reflection

The merge sort was initially a little difficult for me to grasp, but completing the discussion post work helped me figure how the algorithm works. The recursive element was not as challenging as usual, so I ended up struggling with the bubble_sort algorithm. I forgot to make a copy of the list and ended up sorting the original list which affected some of the testing later on. I went back and made it a copy later which fixed the issue.

The two sorting methods are both quite interesting. The bubble sort algorithm is fairly intuitive, the merge sort takes a little bit more time to get used to but ultimately it is just comparing values one by one. The merge sort has a lot more overhead than the bubble sort, it recursively instantiates new lists at each level. I added timing to my tests to see where the actual crossover in efficiency happens for the two different algorithms, it ended up being around ~20 elements when merge sort started to be more efficient than bubble sort. So it may be beneficial to use bubble sort on shorter lists and merge sort on larger lists.

