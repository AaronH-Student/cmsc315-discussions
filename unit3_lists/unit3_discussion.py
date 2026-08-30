"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert puts the value at the given index and pushes all values at or above the index to the right
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate index is between 0 and list length
    if 0 <= index < len(lst):
        return(lst.pop(index))
    # Return None instead of raising IndexError when calling delete_at on an invalid index
    return(None)

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # try block to account for raised ValueErrors when searching for value that is not in list
    try:
        # lst.index returns the index of the given value
        return(lst.index(value))
    # Value was not present in lst
    except ValueError:
        return(-1)


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    test_list = [1, 22, 87, -10]
    print(f"Original list: {test_list}")
    insert_at(test_list, 0, 'beginning')
    print(f"List with insertion at the beginning: {test_list}")
    insert_at(test_list, int(len(test_list)/2)+1, 'middle')
    print(f"List with insertion in the middle: {test_list}")
    insert_at(test_list, len(test_list), 'end')
    print(f"List with insertion at the end: {test_list}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    print(f"Deleting item from the beginning of {test_list}.")
    print(f"Removed {delete_at(test_list, 0)}, list is now: {test_list}")
    print(f"Deleting item from the middle of {test_list}.")
    print(f"Removed {delete_at(test_list, int(len(test_list)/2)-1)}, list is now: {test_list}")
    print(f"Deleting item from the end of {test_list}.")
    print(f"Removed {delete_at(test_list, len(test_list)-1)}, list is now: {test_list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    print(f"Searching for \"87\" in list: {test_list}")
    print(f"Search result: {search_value(test_list, 87)}")
    print(f"Searching for \"0\" in list: {test_list}")
    print(f"Search result: {search_value(test_list, 0)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    print(f"Deleting at invalid index (10): {delete_at(test_list, 10)}")
    print(f"Searching for missing value (0): {delete_at(test_list, 0)}")
    empty_list = []
    print(f"Inserting value (1) into an empty list ({empty_list}): {insert_at(empty_list, 0, 1)}")
    print(f"Result: {empty_list}")
    empty_list = []
    print(f"Deleting index 0 from an empty list ({empty_list}): {delete_at(empty_list, 0)}")

    # ===============================
    # TODO (Student): REAL WORLD SCENARIO
    # ===============================
    #
    # Demonstrate a real world scenario.
    #
    # Create a list of accounts.
    accounts = ['00123', '03417', '32905', '00001']
    print(f"List of accounts: {accounts}")
    print("Adding account 01234 to the end of the list.")
    insert_at(accounts, len(accounts), '01234')
    print(f"Accounts is now: {accounts}")
    print("Removing account 00001 from accounts using search_value to find index.")
    print(f"Found account 00001 at accounts index {search_value(accounts, '00001')}.")
    print("Using search_value derived index to remove account from accounts.")
    delete_at(accounts, search_value(accounts, '00001'))
    print(f"Resulting accounts index: {accounts}")



if __name__ == "__main__":
    main()