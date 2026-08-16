"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
class Sailor:
    sea_legs = True

    def __init__(self, name: str, ship: str):
        self.name = name
        self.ship = ship

    def display_info(self):
        print(f"Name: {self.name}\nShip: {self.ship}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
class Pirate(Sailor):
    flag = "Jolly Roger"

    def __init__(self, name: str, ship: str, job: str, experience={'raids': 0, 'boardings': 0}):
        super().__init__(name, ship)
        self.job = job
        self.experience = experience

    def change_job(self, job):
        if job != self.job:
            self.job = job
        else:
            print(f"{self.name} is already a {self.job}.")

    def change_experience(self, raids=0, boardings=0):
        if not raids:
            raids = input(f"How many raids has {self.name} been on? ")
            self.experience['raids'] = int(raids)
        else:
            self.experience['raids'] = raids
        if not boardings:
            boardings = input(f"How many ships has {self.name} boarded? ")
            self.experience['boardings'] = int(boardings)
        else:
            self.experience['boardings'] = boardings

    def display_info(self):
        print(f"Name: {self.name}\nShip: {self.ship}\nJob: {self.job}\nExperience:\n\t{'\n\t'.join([f"{k}: {v}" for k, v in self.experience.items()])}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # - Create at least two objects of the child class.
    pirate_one = Pirate("Edward Thatch", "Queen Anne's Revenge", "Captain")
    pirate_two = Pirate("Edward Kenway", "Jackdaw", "Captain")

    # - Access a class variable through the class itself.
    print(f"Demonstration of accessing a class variable through the class: {Pirate.flag}")
    # - Access the same class variable through an object.
    print(f"Demonstration of accessing a class variable through an object: {pirate_one.flag}")

    # - Add a new attribute to only one object after it is created.
    pirate_one.change_experience(3, 40)

    # - Display each object's namespace using __dict__.
    print(pirate_one.__dict__)
    print(pirate_two.__dict__)

    # - Display information about the class namespace.
    print(Pirate.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # - Create an object that contains nested mutable data.
    pirate_one = Pirate("Edward Thatch", "Queen Anne's Revenge", "Captain")
    pirate_one.change_experience(3, 40)

    # - Create a shallow copy.
    shallow_copy = copy(pirate_one)

    # - Create a deep copy.
    deep_copy = deepcopy(pirate_one)

    # - Modify the original object's nested data.
    pirate_one.change_experience(5, 50)

    # - Display the original object, shallow copy, and deep copy.
    pirate_one.display_info()
    shallow_copy.display_info()
    deep_copy.display_info()

    # - Use comments to explain the difference between shallow and deep copying.
    # The shallow copy shares a reference to the same experience dictionary object as the original thus changes
    # when I made a modification to the dictionary with the change_experience method to the original. The deep copy
    # made a completely new object including the experience dictionary when I used the deepcopy function so it
    # was unchanged when I made modifications to the original.


# TODO 5:
# Complete the main function.
#
def main():
    print("=== Unit 1 OOP Assignment ===\n")

    # - Create at least one object from the parent class.
    sailor = Sailor("John Paul Jones", "Bonhamme Richard")

    # - Create at least one object from the child class.
    pirate = Pirate("Calico Jack Rackham", "William", "Captain")

    # - Demonstrate inheritance by calling methods.
    print("Parent class (Sailor) method demonstration using display_info:")
    sailor.display_info()
    print("\nChild class (Pirate) method demonstration using display_info:")
    pirate.display_info()

    # - Call your namespace demonstration function.
    # - Call your copy demonstration function.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()