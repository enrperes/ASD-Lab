# input: array int V non ordinato 
# output: coppia (i, j) di posizioni in V tali che i<=j e la differenza v[j] - v[i] sia massima
# Esempio: 
# V = 14 16 1 5 13 0 3
# output: 2 4

def findMaxDiff(V):
    mins = [float("+inf")] * (len(V) + 1)
    argMins = [None] * (len(V) + 1)
    # mins[j] = min a[0:j] j esclusa!
    for j in range(len(V)):
        if V[j] < mins[j]:
            mins[j + 1] = V[j]
            argMins[j + 1] = j
        else: 
            mins[j + 1] = mins[j]
            argMins[j + 1] = argMins[j]

        # calcolo escursione massima
        maxDiff = float("-inf")
        argMaxDiff = None
        for j in range(len(V)):
            diff = V[j] - mins[j]
            if diff > maxDiff:
                maxDiff = diff
                argMaxDiff = (argMins[j] , j)

        return argMaxDiff

V = [int(x) for x in input().split(" ") if x]
i, j = findMaxDiff(V)
print(i, j)