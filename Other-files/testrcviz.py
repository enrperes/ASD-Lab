# from rcviz import callgraph, viz
from recviz import recviz

@recviz
def quicksort(items):
    if len(items) <= 1: 
        return items
    else:
        pivot = items[0]
        lesser = quicksort([x for x in items[1:] if x < pivot])
        greater = quicksort([x for x in items[1:] if x >= pivot])
        return lesser + [pivot] + greater
