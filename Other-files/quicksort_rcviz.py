from rcviz import callgraph, viz

@viz
def quicksort(items):
    if len(items) <= 1: 
        return items
    else:
        pivot = items[0]
        lesser = quicksort([x for x in items[1:] if x < pivot])
        greater = quicksort([x for x in items[1:] if x >= pivot])
        return lesser + [pivot] + greater

V = [43, 1, 5, 7, 5, 8, 29, 11, 2, 3, 52, 42, 69, 100]
V = [2, 3, 1, 0]
# print(quicksort( list("helloworld") ))
print(quicksort(V))
callgraph.render("sort.png")