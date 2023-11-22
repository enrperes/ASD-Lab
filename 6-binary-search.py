raw_input = input

def getArray():
	tokens = raw_input().split(" ")
	return [int(x) for x in tokens if x]  # "if x" filters out empty tokens

def binarySearchRec(array, left, right, item):
	i = int(item)
	if right >= left:
		middle = left + (right - left) //2
		if (i == array[middle]):
			return middle
		elif (array[middle] > i):
			return binarySearch(array, left , middle - 1,  itemToFind)
		else:
			return binarySearch(array, middle + 1, right,  itemToFind)
	else:
		return -1
	
def binarySearch(array, item):
	return binarySearchRec(array, 0, len(array)-1, item)

V = getArray()
itemToFind = raw_input()

pos = binarySearch(V, itemToFind) + 1

print(pos)