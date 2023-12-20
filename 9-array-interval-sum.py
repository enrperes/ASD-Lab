
# input: array di int V > 0, non ordinato. 
# int S > 0
# output: intervallo [i, j] di posizioni in V con i <= j, tale che: 
# V[i] + V[i+1] + ... + V[j] = S

# Esempio: 
# V = 5 0 3 1 13 7 5 
# S = 17
# Output: 2 4

# Implementare versione di O(n^3) e Theta(n) (c'è un errore, da correggere.)

def findInterval_slow(V, S):
    for i in range(len(V)):
        for j in range(i, len(V)):
            if sum(V[i:j+1]) == S:
                return (i, j)
    return (-1, -1)

def findInterval_fast(V, S):
    i = 0
    j = 0
    sum = 0
    while i < len(V):
        if sum == S:
            return (i+1, j-1)
        elif sum < S:
            sum += V[j]
            j += 1
        else:
            sum -= V[i]
            i += 1
    return (-1, -1)

# get input
V = [int(x) for x in input().split(" ") if x]
S = int(input())
i, j = findInterval_slow(V, S)
print(i, j)






