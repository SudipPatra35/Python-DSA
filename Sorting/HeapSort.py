def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array is:", arr)
heapSort(arr)
print("Sorted array is:", arr)



### Explanation:

# 1. **Heapify Function:**
#    - `heapify` ensures the subtree rooted at index `i` is a heap.
#    - It compares the root with its left and right children, and swaps if the root is not the largest.
#    - This process is repeated for the subtree affected by the swap.

# 2. **HeapSort Function:**
#    - First, build a max heap from the input array.
#    - Then, repeatedly swap the first element of the array with the last element, reduce the heap size by one, and call `heapify` on the root.
   
# ### Example Usage:
# - The example demonstrates sorting an array `[12, 11, 13, 5, 6, 7]` using heap sort.
# - It first prints the original array, then sorts it using `heapSort`, and finally prints the sorted array.