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

def quickselect(a, h, i = 0, j = None):
    if j == None:
        j = len(a)
    # invariante: h dovrebbe sempre essere compreso tra i (incluso) e j (escluso)
    if j - 1 == 1 and h == i: 
        return a[i]
    elif i == j:
        return None
    
    # caso induttivo
    k = partition(a, i, j)

    if i <= h < k:
        quickselect(a, h, i, k)
    elif k <= h < j:
        quickselect(a, h, k, j) 


def heap_select(a, h):
    heap = MinHeap()           # todo
    heap.buildheap(a) # tempo O(n)
    for i in range(0, h):
        r = heap.get_min()
        heap.exract()
    return heap.getmin()


def heap_select2(a, h):
    main_heap = MinHeap()
    main_heap.buidheap(a)
    aux_heap = MinHeapAux()
    aux_heap.insert((main_heap.heap[0], 0))

    for i in range(0, h): 
        (x, j) = aux_heap.getmin()
        aux_heap.extract()
        
        l = main_heap.left(j)
        r = main_heap.right(j)
        if l != None:
            aux_heap.insert((main_heap.heap[l], l))
        if r != None:
            aux_heap.insert((main_heap.heap[r], r))
    (x, j) = aux_heap
    return x
        


a = [int(x) for x in input().split(" ") if x]
h = int(input()) - 1
print(quickselect(a, h))
print("HeapSort:  ")
print(heap_select(a, h))