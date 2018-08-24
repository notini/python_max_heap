import random
import math 
import copy

class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
class MaxHeap:
	
	def parent(self, idx):
		return math.floor((idx - 1)/2)
	
	def left(self, idx):
		return idx * 2 + 1
		
	def right(self, idx):
		return (idx * 2) + 2
		
	#Exchanges values on indexes a and b.
	def exchange(self, heap, a, b):
		aux = heap[a]
		heap[a] = heap[b]
		heap[b] = aux
		
	#Base function that guarantees that the heap property will hold.
	def max_heapify(self, heap, heapsize, idx):
		l = self.left(idx)
		r = self.right(idx)
		swap = False
		if l <= heapsize - 1:
			if heap[l] > heap[idx]:
				largest = l; swap = True
			else:
				largest = copy.deepcopy(idx); swap = True
		if r <= heapsize - 1:
			if heap[r] > heap[largest]:
				largest = r; swap = True
		if swap:
			if largest != idx:
				self.exchange(heap, idx, largest)
				self.max_heapify(heap, heapsize, largest)
				
	#Inserts a new key onto the heap.
	def insertKey(self, heap, key):
		heap.append(float('-inf'))
		self.increaseKey(heap, len(heap) - 1, key)
				
	#Increases value on 'idx' to the 'key' value, unless 'key' is smaller than current heap[idx] value.
	def increaseKey(self, heap, idx, key):
		if key < heap[idx]:
			print('Error: key is smaller than current key')
			return
		heap[idx] = key
		while idx > 0 and heap[self.parent(idx)] < heap[idx]:
			par = self.parent(idx)
			self.exchange(heap, idx, par)
			idx = copy.deepcopy(par)
			
	#Sorts the max heap.
	def heapsort(self, heap):
		heapsize = len(heap)
		for i in range(len(heap), 1, -1):
			self.exchange(heap, 0, i - 1)
			heapsize -= 1
			self.max_heapify(heap, heapsize, 0)