
# def binary_search(arr, key):
#     """
#     Perform binary search on a sorted array of integers.

#     Args:
#     - arr: a sorted array of integers
#     - key: the integer to search for in the array

#     Returns:
#     - the index of the key in the array, if it exists (0-indexed)
#     - -1 if the key is not present in the array
#     """
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


def binary_search(a, low, high, key):
    if high - low <= 0:
        return -1
    m = (low + high) // 2 
    if a[m] == key:
        return m
    elif a[m] < key:
        return binary_search(a, m + 1, high, key)
    else:
        return binary_search(a, low, m, key)
    
a = [int(x) for x in input().split(" ") if x]

binary_search(a, 0, len(a), int(input()))   