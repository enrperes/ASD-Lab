# # from rcviz import callgraph, viz
# from recviz import recviz

# @recviz
# def quicksort(items):
#     if len(items) <= 1: 
#         return items
#     else:
#         pivot = items[0]
#         lesser = quicksort([x for x in items[1:] if x < pivot])
#         greater = quicksort([x for x in items[1:] if x >= pivot])
#         return lesser + [pivot] + greater

from rcviz import callgraph, viz

@viz

def fibonaccio(n):
    if n <= 1:
        return n
    else:
        return fibonaccio(n-1)+fibonaccio(n-2)
    
print(fibonaccio(6))
callgraph.render("fibonaccio.png")  
