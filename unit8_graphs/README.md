# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

## Implementation
Implemented a BFS algorithm using an adjacency list represented by a dictionary with string keys and list values.
The example graph used shows Wikipedia pages (vertices) and their links (edges). The BFS algorithm uses a deque
as a FIFO queue to traverse connected pages level by level. The traversal tracks visited nodes and records each
node and its degree from the starting node. This was done to for the sake of demonstrating the BFS behavior rather
than for any algorithmic requirement.

Also added nodes and edges to the graph to show how it changes the traversal. Tested several edge cases including
trying to traverse using incorrect nodes or traverse empty graphs.

## Reflection
1. What concepts or skills did you learn while completing this assignment?
I learned how to use BFS to traverse a graph, the biggest help was using the deque to maintain FIFO order when
traversing the levels of the graph.
2. What challenges did you encounter, and how did you overcome them?
I ran into a small issue when I was using pop on the deque instead of popleft which was messing up the traversal
order. Once that was done I needed a better way to show the degrees of each node so I refactored some of the code
to keep track of each node's degree from the start node which made explaining and demonstrating the BFS behavior a
lot easier.
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.
BFS explores a graph one level at a time, visiting each adjacent node before reaching out to their adjacent nodes on the next level. DFS follows a path until it reaches the end before backing up and exploring the next possible path. DFS will often use recursion as well. BFS is useful for finding the shortest path possible while DFS is better for finding more complete branching paths.

