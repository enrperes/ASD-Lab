# input = Sorted int array and target value
# output = index (pair) of elements in the array that sum up to the target value. -1 -1 if not found.

# finxIndex_slowly is O(n^2)
# findIndex is O(n log n)
# findIndex_fast is O(n)

# Example:
# input: 3 7 8 11 15 20 24
# 23
# output: 0 5 

def findIndex_slowly(V, S):
    for i in range(len(V)):
        for j in range(i+1, len(V)):
            if V[i] + V[j] == S:
                return (i, j)
    return (-1, -1)

def findIndex_fast(V, S):
    i = 0
    j = len(V) - 1
    while i < j:
        if V[i] + V[j] == S:
            return (i, j)
        elif V[i] + V[j] < S:
            i += 1
        else:
            j -= 1
    return (-1, -1)

V = [int(x) for x in input().split(" ") if x] 
S = int(input())

print(' '.join(map(str, findIndex_slowly(V, S))))
print(' '.join(map(str, findIndex_fast(V, S))))

