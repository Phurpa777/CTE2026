'''#Task1
def indexed_search(arr, key, block_size):
    n = len(arr)
    # create index table
    index_table = []
    for i in range(0, n, block_size):
        index_table.append((arr[i], i))
    
    # search index table
    start = 0
    for i in range(len(index_table)):
        if key < index_table[i][0]:
            break
        start = index_table[i][1]

    # sequential search in block
    end = min(start + block_size, n)

    for i in range(start, end):
        if arr[i] == key:
            return i

    return -1
# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80]
key = 50
result = indexed_search(arr, key, 3)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")'''

#Task 2
def selection_sort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
# Example
data = [30, 10, 20, 80, 5]
sorted_data = selection_sort(data)
print("Sorted List:", sorted_data)