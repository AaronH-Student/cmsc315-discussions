"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""
import string


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Use recursion to traverse the BST and find where value goes
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If node is None then return a new node with the value.
        if node is None:
            print(f"Established new node {value}.")
            return Node(value)

        # If value is less than current Node, traverse left.
        if value < node.value:
            print(f"Value {value} is less than node {node.value}, traversing left.")
            node.left = self._insert_recursive(node.left, value)

        # If value is greater than current Node, traverse right.
        elif value > node.value:
            print(f"Value {value} is greater than node {node.value}, traversing right.")
            node.right = self._insert_recursive(node.right, value)

        # No duplicates
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search improves upon the worst case scenarios, especially in longer arrays.
        # An array of 255 elements has a complexity of O(N) whereas BST is O(logN)
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # None means there was no node
        if node is None:
            return False

        # Value found
        if value == node.value:
            return True
        # Traverse left
        elif value < node.value:
            return self._search_recursive(node.left, value)
        # Traverse right
        else:
            return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    #     # 2. Insert at least 7 values.
    #     # 3. Include values that go into both left
    #     #    and right subtrees.
    #     # 4. Display the values inserted.
    #     # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # BSTs are efficient at reducing search space because it reduces complexity to O(logN) over the
    # linear search which is O(N). That means fewer hops to find elements in a well-balanced tree.
    bst = BST()
    bst.insert(12)
    bst.insert(10)
    bst.insert(8)
    bst.insert(14)
    bst.insert(11)
    bst.insert(15)
    bst.insert(13)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # The search method recursively traverses the tree's left nodes until it finds
    # the left most leaf, then up to the parent, then down right, and back up again
    # until each node has been visited. Values are congregated in a list as it goes.
    print(bst.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # The values 8 and 14 are present in the tree, search recursively traverses the
    # tree until they are found and returns True.
    print(f"Searching for value 8 in BST. Present: {bst.search(8)}")
    print(f"Searching for value 14 in BST. Present: {bst.search(14)}")

    # The values 22 and 117 are not present in the tree, search recursively traverses
    # the tree until they are found absent and returns False.
    print(f"Searching for value 22 in BST. Present: {bst.search(22)}")
    print(f"Searching for value 117 in BST. Present: {bst.search(117)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")


    empty = BST()
    # The root in an empty BST is set to None, recursive search returns
    # False when a node is equal to None.
    print(f"Searching for value 100 in empty BST. {empty.search(100)}")

    dup = BST()
    # The only comparison made is whether the value to be inserted is less than the current node.
    # When they are equal, it follows the same route as values greater than the node.
    print("Adding duplicate values to BST.")
    dup.insert(100)
    dup.insert(100)

    print("Adding a single node to BST.")
    single = BST()
    single.insert(100)
    print(f"Resulting tree: {single.inorder()}")

    print("\n=== REAL WORLD EXAMPLE ===")
    print("BSTs can be used to do things like spell checking.")
    spelling_tree = BST()
    print("\nAdding words into a spell checker \"dictionary\".")
    # BSTs can be used to efficiently look up words in a dictionary.
    words = ['hello', 'spelling', 'keyboard', 'verify', 'world', ' checker', 'trees']
    for word in words:
        spelling_tree.insert(word)

    test_string_one = "Hello, World!"
    test_string_two = "Helloo, Wourld!"

    # Helper function to turn a string into a friendlier and cleaner list of strings.
    def spell_check(sentence):
        # Make a list of words in lower case to check against the words BST.
        # The str.translate receives a translation table to remove all punctuation. The resulting string
        # is split into a list by spaces.
        broken_sentence = [word.lower() for word in sentence.translate(str.maketrans('', '', string.punctuation)).split(' ')]

        right = True
        for word in broken_sentence:
            # Returns False if word is not in dictionary, print a warning. Text editors would underline the word in red.
            if not spelling_tree.search(word):
                print(f"The word \"{word}\" appears to be misspelled.")
                right = False

        print(f"Spelled correctly? {right}")

    print(f"\n\nTesting first string: {test_string_one}")
    spell_check(test_string_one)
    print(f"\nTesting second string: {test_string_two}")
    spell_check(test_string_two)



if __name__ == "__main__":
    main()