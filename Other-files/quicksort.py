# from rcviz import callgraph, viz
from recviz import recviz

@recviz
def partition(a, low, high):
    p = a[high-1]
    i = low
    for j in range(low, high -1):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high-1] = a[high-1], a[i]
    return i


def quicksort(a, low, high):
    if high - low <= 1:
        return
    middle = partition(a, low, high)
    quicksort(a, low, middle)
    quicksort(a, middle + 1, high)

a = [43, 1, 5, 7, 5, 8, 29, 11]
quicksort(a, 0, len(a))
print (a)

# callgraph.render("sort.png")