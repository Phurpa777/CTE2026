'''# ===============================
# PART 1: Queue using Array
# ===============================
class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._queue = [None] * capacity
        # Variables to track front and rear
        self._front = 0
        self._rear = -1
        self._capacity = capacity
        self._size = 0

        print("Created new Queue with capacity:", capacity)
        print("Queue is empty:", self.is_empty())

    def is_empty(self):
        return self._size == 0
# Testing
q = ArrayQueue()'''
''''##task 2
class ArrayQueue:
    def __init__(self, capacity=10):
        self._queue = [None] * capacity
        self._front = 0
        self._rear = -1
        self._capacity = capacity
        self._size = 0

        print("Created new Queue with capacity:", capacity)
        print("Queue is empty:", self.is_empty())

    def is_empty(self):
        return self._size == 0

    # 1. Enqueue
    def enqueue(self, element):
        if self._size == self._capacity:
            print("Queue Overflow!")
            return
        
        self._rear = (self._rear + 1) % self._capacity
        self._queue[self._rear] = element
        self._size += 1
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None
        
        element = self._queue[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        print(f"Dequeued element: {element}")
        return element

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._queue[self._front]

    # 4. Size
    def size(self):
        return self._size

    # 5. Display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        items = []
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            items.append(self._queue[index])
        
        print("Display queue:", items)

# Testing

q = ArrayQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

print("Front element:", q.peek())

q.dequeue()
q.display()

print("Queue size:", q.size())'''''
'''#task 3
# Node Class
class Node:
    def __init__(self, data):
        self.data = data      # stores the value
        self.next = None      # reference to next node


# LinkedQueue Class
class LinkedQueue:
    def __init__(self):
        self.front = None     # first node
        self.rear = None      # last node
        self._size = 0        # size counter

        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())

    def is_empty(self):
        return self.front is None

# Testing
q = LinkedQueue()'''
##task 4
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedQueue Class
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())

    # 1. Check if empty
    def is_empty(self):
        return self.front is None

    # 2. Enqueue
    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self._size += 1
        print(f"Enqueued {element} to the queue")

    # 3. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        print(f"Dequeued element: {temp.data}")
        return temp.data

    # 4. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    # 5. Size
    def size(self):
        return self._size

    # 6. Display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        print("Current queue:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")
# Testing (Example Output)
q = LinkedQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

print("Front element:", q.peek())

q.dequeue()
q.display()

print("Queue size:", q.size())