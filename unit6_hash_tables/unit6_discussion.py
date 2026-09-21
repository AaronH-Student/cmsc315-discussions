"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    pokedex = {}

    # Python dictionaries allows a program to look up information by a unique key
    # Under the hood, python dictionaries are hash tables, the keys are hashed
    # and then the key-value pairs are assigned to a bucket
    pokedex['Bulbasaur'] = {'type': ['Grass', 'Poison'], 'height': 2.3}
    pokedex['Charmander'] = {'type': ['Fire'], 'height': 2.0}
    pokedex['Squirtle'] = {'type': ['Water'], 'height': 1.6}
    pokedex['Pikachu'] = {'type': ['Electric'], 'height': 1.3}
    pokedex['Evee'] = {'type': ['Normal'], 'height': 1.0}

    for pokemon, entry in pokedex.items():
        print(pokemon)
        print('-' * 15)
        print('Type: ' + ', '.join(entry['type']))
        print('Height: ' + str(entry['height']))
        print()

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # The keys (Bulbasaur and Pikachu in the examples below) are hashed and looked up directly
    # in the pokedex dictionary, retrieving the value
    print(f"Get 'Bulbasaur': {pokedex['Bulbasaur']}")
    print(f"Get 'Pikachu': {pokedex['Pikachu']}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Updating the value of a pre-existing key overwrites the original value
    # with the new one, in this case I just added some information to Bulbasaur
    print(f"Bulbasaur value before: {pokedex['Bulbasaur']}")
    pokedex['Bulbasaur'] = {'type': ['Grass', 'Poison'], 'height': 2.3, 'id': 1}
    print(f"Bulbasaur value before: {pokedex['Bulbasaur']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Pokedex before: {pokedex}")
    pokedex.pop('Evee')
    print(f"Pokedex after: {pokedex}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # The key does not exist so get returns None
    print(f"Lookup missing key (Mew): {pokedex.get('Mew')}")

    # Cannot remove a key that does not exist, pop returns nothing
    to_remove = 'Mew'
    print(f"Delete missing key (Mew): {pokedex.pop(to_remove, f'Key \"{to_remove}\" not found...')}")

    # Updating a missing key updates the dictionary/hash table with
    # the new key-value pair
    print(f"Pokedex before update to missing key: {pokedex}")
    pokedex['Mew'] = {'type': ['Psychic'], 'height': 1.3}
    print(f"Pokedex after update to missing key: {pokedex}")

    empty_pokedex = {}
    # Attempting to retrieve a key from an empty dictionary is similar to retrieving a
    # non-existent key from a populated dictionary
    print(f"Looking up Pikachu in empty pokedex: {empty_pokedex.get('Pikachu', 'No pokemon, explore more!')}")



if __name__ == "__main__":
    main()