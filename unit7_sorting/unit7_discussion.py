"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""
import  random
import time


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    new_lst = lst.copy()
    for _ in range(len(new_lst)):
        for i in range(len(new_lst)-1):
            if new_lst[i] > new_lst[i+1]:
                new_lst[i], new_lst[i+1] = new_lst[i+1], new_lst[i]
    return new_lst


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # List of one element is already sorted
    if len(lst) <= 1:
        return lst

    # Floor div to find the middle of the list
    midpoint = len(lst) // 2
    # Left is from 0 to midpoint exclusive
    left = lst[:midpoint]
    # Right is from midpoint to the end
    right = lst[midpoint:]

    # Further subdivide the halves of the list until single elements are isolated
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # New list to hold the sorted results
    merged_list = []
    # Placeholders for the index in left and right as we compare values
    l = 0
    r = 0
    # As long as we are still working through either the left or right list,
    # compare values.
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1

    # Any values left over will be greater anything appended so far
    # Only the left or the right will be left over and they are already sorted
    while l < len(left):
        merged_list.append(left[l])
        l += 1

    while r < len(right):
        merged_list.append(right[r])
        r += 1

    return merged_list

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    scores = []
    for _ in range(5):
        scores.append(random.randint(45,100))

    print(f"Original scores list: {scores}")
    print(f"Bubble sorted scores list: {bubble_sort(scores)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    scores = []
    for _ in range(22):
        scores.append(random.randint(45,100))

    scores_copy = scores.copy()

    # Show that the scores lists are equal
    print(f"Original scores list: {scores}")
    print(f"Copied scores list: {scores_copy}")
    print(f"Score lists are equal: {scores == scores_copy}")

    # Added timing out of curiosity
    t = time.time_ns()
    bs = bubble_sort(scores)
    total = time.time_ns() - t
    print(f"Bubble sorted scores list: {bs[0:5]} ({total} ns)")

    t = time.time_ns()
    ms = merge_sort(scores_copy)
    total = time.time_ns() - t
    print(f"Merge sorted scores list: {ms[0:5]} ({total} ns)")
    print(f"Sorted scores lists are equal: {bs == ms}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Bubble sort makes a copy of the empty list and immediately
    # returns it since there are no elements to iterate through
    # and sort.
    empty_list = []
    print(f"Empty list sort: {bubble_sort(empty_list)}")

    # Bubble sort iterates through all elements, duplicate values are not
    # greater than one another so the swap never occurs during those
    # comparisons and the loop move on.
    duplicates_list = [97, 88, 68, 88, 91]
    print(f"Duplicates list: {bubble_sort(duplicates_list)}")



if __name__ == "__main__":
    main()