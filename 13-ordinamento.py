def partition(a, i, j):
    pivot = a[j-1]
    k = i
    h = i
    while 0 <= k <= h < j:
        if a[h] <= pivot:
            a[k], a[h] = a[h], a[k]
            k += 1
        h += 1
    return k-1


def quicksort(a, i=0, j=None):
    if j == None:
        j = len(a)
    
    #caso base 
    if j-i <= 1:
        return
    # caso induttivo
    k = partition(a, i, j)
    # 
    quicksort(a, i, k)
    quicksort(a, k+1, j)


a = [int(x) for x in input().split(" ") if x]
quicksort(a)
print(a)