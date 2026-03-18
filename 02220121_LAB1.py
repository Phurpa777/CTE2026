"""##Task 1
class CustomList:
    def __init__(self, capacity=10):
        self._elements = [None] * capacity
        self._capacity = capacity
        self._size = 0

        print("Created new CustomList with capacity:", self._capacity)
        print("Current size:", self._size)
        
my_list = CustomList()"""

## Task 2
class CustomList:

    def __init__(self, capacity=10):
        self._elements = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def append(self, element):
        if self._size < self._capacity:
            self._elements[self._size] = element
            self._size += 1
            print("Appended", element, "to the list")
        else:
            print("List is full")

    def get(self, index):
        if 0 <= index < self._size:
            print("Element at index", index, ":", self._elements[index])
            return self._elements[index]
        else:
            print("Index out of range")

    def set(self, index, element):
        if 0 <= index < self._size:
            self._elements[index] = element
            print("Set element at index", index, "to", element)
        else:
            print("Index out of range")

    def size(self):
        print("Current size:", self._size)
        return self._size

my_list = CustomList()

my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()