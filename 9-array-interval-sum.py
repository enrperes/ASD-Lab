# input: array di int V > 0, non ordinato. 
# int S > 0
# output: intervallo [i, j] di posizioni in V con i <= j, tale che: 
# V[i] + V[i+1] + ... + V[j] = S

# Esempio: 
# V = 5 0 3 1 13 7 5 
# S = 17
# Output: 2 4

# Implementare versione di O(n^3) e Theta(n) (c'è un errore, da correggere.)

def findInterval(V, S):
    i = j = 0
    current_sum = V[i]
    while i <= j < len(V):
        # current_sum = sum a[i:j+1]
        if current_sum == S:
            return (i, j)
        elif current_sum < S:
            j += 1
            current_sum += V[j]
        else:
            current_sum -= V[i]
            i += 1
    return -1, -1

# get input
V = [int(x) for x in input().split(" ") if x]
S = int(input())
i, j = findInterval(V, S)
print(i, j)
