"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Compare each element of lst to the target, return index when there is a match
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 when target is not found
    return -1
    '''
    # The block below happens to be more faster than the implementation above,
    # likely due to the python list index method being implemented in C
    try:
        return lst.index(target)
    except ValueError:
        return -1
    '''


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low, high = 0, len(lst) - 1

    # Continue to iterate and adjust the search range as long as the searched index is within the range
    while low <= high:
        # Find the middle index of the search range
        index = int((high + low) / 2)
        if lst[index] < target:
            # Target must be in the upper half
            low = index + 1
        elif lst[index] > target:
            # Target must be in the lower half
            high = index - 1
        else:
            return index

    # Lower search bound exceeded the upper bound, target was not found
    return -1




def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Generate a list of ordered product IDs in list inventory
    inventory = list(range(10)[::2])
    print(f"Sorted inventory of product IDs: {inventory}\n")

    # Using time to record the actual runtime for each search
    # Checking for target value 4 returns the index 2
    # Checking for the non-existent value 5 returns -1
    t = time.time_ns()
    print(f"Searching for 4 using linear search: found at index {linear_search(inventory, 4)} in {time.time_ns() - t} ns")
    t = time.time_ns()
    print(f"Searching for 5 using linear search: returned {linear_search(inventory, 5)} in {time.time_ns() - t} ns\n")

    # Checking for target value 4 returns the index 2
    # Checking for the non-existent value 5 returns -1
    t = time.time_ns()
    print(f"Searching for 4 using binary search: found at index {linear_search(inventory, 4)} in {time.time_ns() - t} ns")
    t = time.time_ns()
    print(f"Searching for 5 using binary search: returned {linear_search(inventory, 5)} in {time.time_ns() - t} ns")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Generate a larger list of ordered product IDs in list inventory
    inventory = list(range(10000))
    print("Generated a large inventory of product IDs from 0 to 9999.")

    # Using time to record the actual runtime for each search
    # Checking for target value 3672 returns the index 3672 in both cases
    # The runtime comparison shows a clear advantage for the binary search algorithm
    t = time.time_ns()
    print(f"Searching for product ID 3672 using linear search: found at index {linear_search(inventory, 3672)} in {time.time_ns()-t} ns.")
    t = time.time_ns()
    print(f"Searching for product ID 3672 using binary search: found at index {binary_search(inventory, 3672)} in {time.time_ns()-t} ns.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Empty list for edge case testing
    edge_list = []
    print(f"Testing on empty list: {edge_list}")
    # Both algorithms will return -1 as the target value is not present in the empty list
    # The linear search algorithm will not iterate through its for loop due to the length of the list being 0
    # The binary search algorithm will not iterate through its while loop due to the low (0) being greater than -1 (len(lst)-1)
    print(f"Linear search for 0: {linear_search(edge_list, 0)}")
    print(f"Binary search for 0: {binary_search(edge_list, 0)}\n")

    # Single element list for edge case testing
    edge_list = [1]
    print(f"Testing on single-element list: {edge_list}")
    # Both algorithms will return -1 when searching for target value 0 which is not present
    print(f"Linear search for 0: {linear_search(edge_list, 0)}")
    print(f"Binary search for 0: {binary_search(edge_list, 0)}\n")

    # Both algorithms will return index 0 which is the first (and last) index in edge_list
    print(f"Linear search with target value (1) at first (and last) position: {linear_search(edge_list, 1)}")
    print(f"Binary search with target value (1) at first (and last) position: {binary_search(edge_list, 1)}")


if __name__ == "__main__":
    main()