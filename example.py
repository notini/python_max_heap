import math
import random
from maxHeap import MaxHeap

max_heap = MaxHeap()

values = [random.randint(0,20) for i in range(10)]
heap = []

#Initializing heap with values from a random array. 
print('Values inserted to the heap:')
for value in values:
	max_heap.insertKey(heap, value)
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