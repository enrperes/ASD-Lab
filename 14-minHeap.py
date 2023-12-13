class MinHeap: 
    heap = []

    def length(self):
        return len(heap) 
    
    def getmin(self):
        assert len(heap) > 0
        return heap[0]
    
    def extract(self):
        assert len(heap) > 0
        return heap.pop(0)
    
    def insert(self, value):
        heap.append(value)
        self._bubbleup(len(heap)-1)

    def change(self, index, value):
        assert index < len(heap)
        heap[index] = value
        self._bubbleup(index)
        self._bubbledown(index)

    def buildheap(self, array):
        heap = array
        for i in range(len(heap)-1, -1, -1):
            self._bubbledown(i)

    def heapify(self, array):
        heap = array
        for i in range(len(heap)-1, -1, -1):
            self._bubbledown(i)

    def moveup(self, index):
        self._bubbleup(index)

        