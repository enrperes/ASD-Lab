
def find_pair(V, S):
    i = 0
    j = len(V) - 1
    while i < j:
        if V[i] + V[j] == S:
            return i, j
            exit()
        elif V[i] + V[j] < S:
            j -= 1
        else:
            i += 1
    return -1, -1

V = list(map(int, input().split()))
S = int(input())

i, j = find_pair(V, S)
print(i, j)
