def mergeSort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])
    return merge(left, right)

def merge(left, right):
    new = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    
    # Use extend to add all remaining elements from left or right
    new.extend(left[i:])
    new.extend(right[j:])
    return new

li = [5, 8, 1, 6, 4, 3, 2, 7, 9]
print("Before sorting:")
print(li)
sorted_li = mergeSort(li)
print("After sorting:")
print(sorted_li)
