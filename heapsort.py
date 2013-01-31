NULL = 'NULL'

class Heap:
	def __init__(self, comparator):
		self.collection	= []
		self.comparator	= comparator	# returns true if comparator(root, child) needs to swap
		
		
	def push(self, objectToPush):
		self.collection.append(objectToPush)
		
		newLeaf	= len(self.collection) - 1
		
		if newLeaf > 0:
			parentIndex	= (newLeaf - 1) / 2
			parentValue	= self.collection[parentIndex]
			
			while self.comparator(parentValue, objectToPush):
				self.collection[parentIndex]	= objectToPush
				self.collection[newLeaf]	= parentValue
				newLeaf				= parentIndex
				parentIndex			= (newLeaf - 1) / 2
				parentValue			= self.collection[parentIndex]
				
				if parentIndex < 0:
					break
		
		
	def pop(self):
		if len(self.collection) == 0:
			return NULL
				
		retVal = self.collection[0]
		
		if len(self.collection) == 1:
			self.collection = []
		else:
			lastLeaf		= self.collection.pop()
			self.collection[0]	= lastLeaf
			
			if len(self.collection) > 2:
				current		= 0
				leftChild	= 1
				rightChild	= 2
				swapCheck	= (lambda left, right: 
							(left < len(self.collection) and self.comparator(lastLeaf, self.collection[left])) or 
							(right < len(self.collection) and self.comparator(lastLeaf, self.collection[right])))
				
				#chose which branch to swap with
				while swapCheck(leftChild, rightChild):
					left		= self.collection[leftChild]
					right		= self.collection[rightChild]
					swapIndex	= current
					swapValue	= NULL
					
					if self.comparator(right, left):
						swapIndex	= leftChild
						swapValue	= left
					else:
						swapIndex	= rightChild
						swapValue	= right
						
					self.collection[swapIndex]	= lastLeaf
					self.collection[current]	= swapValue
					current				= swapIndex
					rightChild			= 2 + (current * 2)
					leftChild			= 1 + (current * 2)
					
					if len(self.collection) <= leftChild:
						break
					elif len(self.collection) <= rightChild:
						if self.comparator(lastLeaf, self.collection[leftChild]):
							self.collection[current]	= self.collection[leftChild]
							self.collection[leftChild]	= lastLeaf
						
		return retVal
	
	
	def printHeap(self):
		print self.collection
