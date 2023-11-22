# input = array of int V, array of pairs of int (i, j)
# output = array of int, where each element is the sum of the elements of V in the range [i, j]

# Example:
# input=5 0 3 1 13 7 5
# 0 6 2 4 3 6 # [0:6] [2:4] [3:6]
# output=34 17 26

def sumIntervals(V, pairs):
    sums = [None] * len(pairs)
    for i in range (len(pairs)):
        sums[i] = 0
        for j in range (pairs[i][0], pairs[i][1] + 1): # pairs[i][0] è il primo elemento della coppia, pairs[i][1] è il secondo elemento della coppia
            sums[i] += V[j]
    return sums
       
V = [int(x) for x in input().split(" ") if x] 
inputPairs = list(map(int, input().split()))
pairs = [(inputPairs[i], inputPairs[i+1]) for i in range(0, len(inputPairs), 2)]

# print(sumIntervals(V, pairs))
print(' '.join(str(x) for x in sumIntervals(V, pairs))) # join() prende una lista di stringhe e le concatena in una stringa unica, separandole con lo spazio.