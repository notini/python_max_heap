# python_max_heap
Python implementation of a Max Heap based on Cormen's 'Introduction to Algorithms' book for educational purposes.

# Usage

First, import the MaxHeap class and declare an object:
```python
from maxHeap import MaxHeap
max_heap = MaxHeap()
```
The max_heapify() function guarantees the heap condition will always hold. In order to heapify an existing array:
```python
values = [4,1,3,2,16,9,10,14,8,7]
for idx in range(math.floor(len(values) / 2), 0, -1):
	max_heap.max_heapify(values, len(values), idx - 1)
```
 You can also start you heap by inserting values with the insertKey() function.
```python
values = [4,1,3,2,16,9,10,14,8,7]
heap = []
for value in values:
	max_heap.insertKey(heap, value)
```
Inserting a new key on an existing heap:
```python
max_heap.insertKey(heap, 20)
```
In order to sort the heap:
```python
max_heap.heapsort(heap)
print('Heap is now sorted:', heap)
```

## Example

example.py provides examples for the conditions mentioned above. To run it, run `python example.py` inside the project folder.

Any doubts/suggestions, feel free to contact me.
