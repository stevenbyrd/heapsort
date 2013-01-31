from heapsort import Heap

class Main:
	def __init__(self):
		comparator	= lambda root, child: root > child
		heap		= Heap(comparator)
		
		heap.push(10)
		heap.push(4)
		heap.push(8)		
		heap.push(2)
		heap.push(5)
		
		print heap.pop()
		print heap.pop()
		print heap.pop()
		print heap.pop()
		print heap.pop()



if __name__ == "__main__":
	Main()
