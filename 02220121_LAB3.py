'''#stack implementation using array
#task 1
class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._data = [None] * capacity
        # Variable to track the top of the stack
        self._top = -1
        # Store capacity
        self._capacity = capacity
        # Output
        print(f"Created new ArrayStack with capacity: {capacity}")
        print("Stack is empty:", self.is_empty())
    # Method to check if stack is empty
    def is_empty(self):
        return self._top == -1
# Testing
if __name__ == "__main__":
    stack = ArrayStack() '''''
''''#Task 2
class ArrayStack:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._top = -1
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
        print("Stack is empty:", self.is_empty())
    # 1. Push operation
    def push(self, element):
        if self._top == self._capacity - 1:
            print("Stack Overflow")
            return
        self._top += 1
        self._data[self._top] = element
        print(f"Pushed {element} to the stack")
    # 2. Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None

        element = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        print(f"Popped element: {element}")
        return element
    # 3. Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        print(f"Top element: {self._data[self._top]}")
        return self._data[self._top]
    # 4. Check if empty
    def is_empty(self):
        return self._top == -1
    # 5. Size of stack
    def size(self):
        size = self._top + 1
        print(f"Stack size: {size}")
        return size
     # 6. Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self._data[:self._top + 1])
# Testing Task 2
if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(10)
    stack.display()
    stack.push(20)
    stack.display()
    stack.push(30)
    stack.display()
    stack.peek()
    stack.pop()
    stack.size()
    stack.display()'''


'''#TAsk 3
# Node Class
class Node:
    def __init__(self, data):
        self.data = data      # Store element
        self.next = None      # Reference to next node
# LinkedStack Class
class LinkedStack:
    def __init__(self):
        self.top = None       # Top (head) of stack
        self._size = 0        # Size counter

        print("Created new LinkedStack")
        print("Stack is empty:", self.is_empty())
     # Check if stack is empty
    def is_empty(self):
        return self.top is None
# Testing Task 3
if __name__ == "__main__":
    stack = LinkedStack()'''

#TASK 4
# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
 # 1. Push operation
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Pushed {element} to the stack")
# 2. Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Popped element: {popped}")
        return popped
# 3. Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data
# 4. Check if empty
    def is_empty(self):
        return self.top is None
# 5. Size of stack
    def size(self):
        print(f"Stack size: {self.count}")
        return self.count
# 6. Display stack
    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty")
            return
        
        print("Display stack:", end=" ")
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        print(elements)
# Display in linked format
    def display_linked(self):
        current = self.top
        print("Current stack:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")
# Example Usage
s = Stack()
s.push(10)
s.display()
s.push(20)
s.display()
s.push(30)
s.display()
s.peek()
s.pop()
s.display_linked()
s.size()