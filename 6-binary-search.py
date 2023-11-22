# input = Sorted int array and target value
# output = index of target value in the array. -1 if not found

# Example:
# input: 3 7 8 11 15 24
# 15
# output: 4

def binarySearchRec(array, left, right, item):
	i = int(item)
	if right >= left:
		middle = left + (right - left) //2
		if (i == array[middle]):
			return middle
		elif (array[middle] > i):
			return binarySearchRec(array, left , middle - 1,  target)
		else:
			return binarySearchRec(array, middle + 1, right,  target)
	else:
		return -1
	
def binarySearch(array, item):
	return binarySearchRec(array, 0, len(array)-1, item)

V = [int(x) for x in input().split(" ") if x] # "if x" filters out empty tokens. 
target = int(input())

pos = binarySearch(V, target)

print(pos)