# Input: Sorted array and target value
# Output: Index of target value in array, -1 if not found. 

raw_input = input

#Implementare in l'algoritmo di ricerca dicotomica su array ordinati di interi.
#Il programma deve ricevere
#- un array ordinato di interi, rappresentato da una sequenza di numeri separati da spazi e terminata da "end of line",  
#- una chiave, rappresentata da un numero su una nuova riga
#e deve ritornare
#- la posizione della chiave nell'array, se esiste (0 = prima posizione)
#- oppure -1 se la chiave non e' presente nell'array

#Lettura dell'array in input
def letturaArray():
    tokens = raw_input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

#Funzione di ricerca binaria ricorsiva
def binarySerchRec(array, leftIndex, rightIndex, item):
    
    i = int(item)
    
    if rightIndex >= leftIndex:
        
        middle = leftIndex + (rightIndex - leftIndex) //2

        if (i == array[middle]):
            
            return middle
        
        elif (array[middle] > i):
            
            return binarySerchRec(array, leftIndex , middle - 1,  itemToFind)
        
        else:
            
            return binarySerchRec(array, middle + 1, rightIndex,  itemToFind)

    else:
        
        return -1
        
def binarySearch(array, item):
    
    return binarySerchRec(array, 0, len(array)-1, item)


a = letturaArray()
itemToFind = raw_input()

pos = binarySearch(a, itemToFind)
 
print(pos)
