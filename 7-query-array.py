def input_array(): 
    return [int(x) for x in input().split(" ") if x]

def range_sum(a, i, j):
    s = 0
    for k in range(i, j+1):
        s += a[k]
    return s

a = input_array()
b = input_array()
c = [(i, j) for (i, j) in zip(b[0::2], b[1::2])]

for (i, j) in c:
    print(range_sum(a, i, j), end=" ")


