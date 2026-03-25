'''##node class
class Node:
    def __init__(self, data):
        self.data = data      # Store element
        self.next = None      # Reference to next node


## LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None      # First node(initially none)
        self.tail = None      # Last node (optional)
        self._size = 0        # Size counter(Number of element start from 0)

        ##Output message
        print("Created new LinkedList")
        print("Current size:", self._size)
        print("Head:", self.head)
##Testing Task 1
if __name__ == "__main__":
    ll = LinkedList()'''
##Task 2
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

        print("Created new LinkedList")
        print("Current size:", self._size)
        print("Head:", self.head)

    # Append
    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"Appended {element} to the list")

    # Prepend
    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1
        print(f"Prepend {element} to the list")

    # Get
    def get(self, index):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for i in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # Set
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for i in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # Size
    def size(self):
        print("Current size:", self._size)
        return self._size

    # Print list
    def print_list(self):
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print("Print Linked list :[" + " ".join(elements) + "]")


# IMPORTANT: This prevents duplicate execution in VS Code
if __name__ == "__main__":
    ll = LinkedList()

    ll.append(5)
    ll.get(0)

    ll.set(0, 10)
    ll.get(0)

    ll.size()

    ll.prepend(10)

    ll.print_list()