import math
from maxHeap import MaxHeap

max_heap = MaxHeap()

#Initializing heap. You decide what to use, this is just an example.
#heap = [random.randint(0,20) for i in range(10)]
heap = [4,1,3,2,16,9,10,14,8,7]
for idx in range(math.floor(len(heap) / 2), 0, -1):
	max_heap.max_heapify(heap, len(heap), idx - 1)
	
print('Values inserted to the heap:')
print(heap)

print('Value on index 6 (if 6 is a valid index) now equals 15')
max_heap.increaseKey(heap, 6, 15)
print(heap)

print('Inserting new key: 20')
max_heap.insertKey(heap, 20)
print(heap)

print('Sorted heap:')
max_heap.heapsort(heap)
print(heap)