class Node:
	def __init__(self, elem):
		self.elem = elem 
		self.next = next

	def __repr__(self):
		return "Node(%s)" % str(self.elem)

class OrderedList:
	def __init__(self):
		self.head = None

	def insert(self, elem):
		"""
		Takes a number, creates a new Node containing that number, and adds it to the list in the correct position, returning the Node that was created. A number that already exists in the list should be inserted before the first existing Node with that value.

		>>> mylist = OrderedList()
		>>> mylist.insert(1)
		>>> mylist
		[1]

		>>> mylist.insert(5)
		>>> mylist
		[1, 5]

		>>> mylist.insert(3)
		>>> mylist
		[1, 3, 5]

		>>> mylist.insert(7)
		>>> mylist
		[1, 3, 5, 7]

		>>> mylist.insert(6)
		>>> mylist
		[1, 3, 5, 6, 7]

		"""
		current = self.head
		previous = None

		while current != None:
			if current.elem > elem:
				break
			previous = current
			current = current.next

		temp = Node(elem)
		# adds Node to tail
		if previous == None:
			temp.next, self.head = self.head, temp
		# assigns new Node's next pointer to 
		else:
			temp.next, previous.next = current, temp

	def find(self, elem):
		"""
		Takes a number and finds the first Node in the list whose elem is that number. If no such node exists, returns null.
		
		>>> mylist = OrderedList()
		>>> mylist.insert(1)
		>>> mylist.insert(3)
		>>> mylist.insert(5)
		>>> mylist.insert(6)
		>>> mylist.insert(7)
		>>> mylist
		[1, 3, 5, 6, 7]

		>>> mylist.find(6)
		6

		>>> mylist.find(4) is None
		True
		
		>>> mylist.find(8) is None
		True

		"""
		current = self.head

		while current is not None:
			if current.elem == elem:
				return elem
			
			if current.elem > elem:
				return None
			
			current = current.next
		
		return None

	def remove(self, elem):
		"""
		Takes a number and removes the first Node in the list whose elem is that number. If no such node exists, does nothing.
		
		>>> mylist = OrderedList()
		>>> mylist.insert(1)
		>>> mylist.insert(3)
		>>> mylist.insert(5)
		>>> mylist.insert(6)
		>>> mylist.insert(7)

		>>> mylist
		[1, 3, 5, 6, 7]

		>>> mylist.remove(6)
		>>> mylist
		[1, 3, 5, 7]

		>>> mylist.remove(4)
		>>> mylist
		[1, 3, 5, 7]

		>>> mylist.remove(27)
		>>> mylist
		[1, 3, 5, 7]

		"""
		current = self.head
		previous = None

		while True:
			if current is None:
				return
			if current.elem == elem:
				break
			previous, current = current, current.next

		if previous == None:
			self.head = current.next
		else:
			previous.next = current.next

	def insert_pt(self, elem):
		"""
		Takes a number and finds the Node in the list after which the number would be inserted. Used as a helper function to implement the step "find where [X] would be" in each of the other operations.

		>>> mylist = OrderedList()
		>>> mylist.insert(1)
		>>> mylist.insert(3)
		>>> mylist.insert(5)
		>>> mylist.insert(7)

		>>> mylist
		[1, 3, 5, 7]

		>>> mylist.insert_pt(6)
		5

		>>> mylist.insert_pt(8)
		7
		>>> mylist.insert_pt(0)

		
		>>> mylist.insert_pt(3) is None
		True

		"""

		current = self.head
		previous = None

		while current is not None:
			# if insert pt is at beginning
			print(current)

			if current.elem < elem:
				previous, current = current, current.next
			# if insert pt is at end
			if current is None:
				return previous.elem
			# if insert pt exists
			if current.elem == elem:
				return None

			if current.elem > elem:
				return previous.elem




	def list_to_data(self):
		elem_list = []
		current = self.head

		while current != None:
			elem_list.append(current.elem)
			current = current.next
		return elem_list

	def data_to_list(self, elem_list):
		self.head = Node(elem_list[0])
		current = self.head

		for elem in elem_list[1:]:
			current.next = Node(elem)
			current = current.next

	def __repr__(self):
		elem_list = self.list_to_data()
		return "%s" % str(elem_list)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"