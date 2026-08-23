"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # list.append adds value to the end of the list
        self.stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Using pop on list already removes and returns the most recent element.
        # Lists raise an IndexError when pop is called on an empty list.
        if len(self.stack):
            return self.stack.pop()
        print("Stack is empty.")
        return False

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Returns the last element in list stack without removing the element from stack.
        # Normal list behavior will raise IndexError when calling index 0 of empty list.
        if len(self.stack):
            return self.stack[len(self.stack) - 1]
        print("Stack is empty.")
        return False

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # If the length of stack is greater than 0, it is not empty.
        if len(self.stack):
            return False
        return True


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Deque.append adds value to the end of the queue.
        self.queue.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Popleft removes and returns the left most element in the queue.
        # Popleft raises an IndexError when called on an empty queue.
        if len(self.queue):
            return self.queue.popleft()
        print("Queue is empty.")
        return False

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # The first index of queue will always be the front of the queue.
        # Looking at index 0 of an empty queue raises an IndexError.
        if len(self.queue):
            return self.queue[0]
        print("Queue is empty.")
        return False

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Return False if queue has any length, True otherwise.
        if len(self.queue):
            return False
        return True


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    print("Creating Stack object.")
    test_stack = Stack()
    print("Pushing integers 10, 20, 30, 40.")
    test_stack.push(10)
    test_stack.push(20)
    test_stack.push(30)
    test_stack.push(40)

    print(f"Stack: {[_ for _ in test_stack.stack]}")
    print("Popping from end of stack:")
    print(f"Last element of stack: {test_stack.pop()}")
    print(f"Stack after pop: {[_ for _ in test_stack.stack]}")

    print(f"Emptying stack: {test_stack.pop()} {test_stack.pop()} {test_stack.pop()}")
    print(f"Testing pop on empty stack: {test_stack.pop()}")
    print(f"Testing peek on empty stack: {test_stack.peek()}")

    print(f"Pushing 10 to stack.")
    test_stack.push(10)
    print(f"Testing that stack is not empty using is_empty: {test_stack.is_empty()}")
    print(f"Popping last element in stack: {test_stack.pop()}")
    print(f"Testing that stack is empty after pop: {test_stack.is_empty()}")


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

    print("Creating Queue object.")
    test_queue = Queue()
    print("Enqueueing integers 10, 20, 30, 40.")
    test_queue.enqueue(10)
    test_queue.enqueue(20)
    test_queue.enqueue(30)
    test_queue.enqueue(40)

    print(f"Queue: {[_ for _ in test_queue.queue]}")
    print("Dequeueing first item in queue:")
    print(f"First element of queue: {test_queue.dequeue()}")
    print(f"Queue after dequeue: {[_ for _ in test_queue.queue]}")

    print(f"Emptying queue: {test_queue.dequeue()} {test_queue.dequeue()} {test_queue.dequeue()}")
    print(f"Testing dequeue on empty queue: {test_queue.dequeue()}")
    print(f"Testing front on empty queue: {test_queue.front()}")

    print(f"Queueing 10.")
    test_queue.enqueue(10)
    print(f"Testing that queue is not empty using is_empty: {test_queue.is_empty()}")
    print(f"Dequeueing first element in queue: {test_queue.dequeue()}")
    print(f"Testing that queue is empty after dequeue: {test_queue.is_empty()}")

if __name__ == "__main__":
    main()
