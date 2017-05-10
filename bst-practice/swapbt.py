"""
	>>> n5 = Node(5)
	>>> n4 = Node(4)
	>>> n3 = Node(3, n4, n5)
	>>> n2 = Node(2)
	>>> n1 = Node(1, n2, n3)

	>>> n1.ptree()
	 1
	   2
	   3
	     4
	     5

	>>> n1.rev()
	>>> n1.ptree()
	 1
	   3
	     5
	     4
	   2
	   

"""

class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def ptree(self, indent=0):
		print "  " * indent, self.data

		if self.left:
			self.left.ptree(indent + 1) 
		
		if self.right:
			self.right.ptree(indent + 1)

	def rev(self):
		if self.left:
			self.left.rev()

		if self.right:
			self.right.rev()

		self.left, self.right = self.right, self.left

		# temp = self.left
		# self.left = self.right
		# self.right = self.left



class GNode(object):
	"""Same idea, but for a general (ie, nonbinary tree)"""

	def __init__(self, data, children=[]):
		self.data = data
		self.children = children

	def ptree(self, indent=0):
		print "  " * indent, self.data

		for c in self.children:
			c.ptree(indent + 1)

	def rev(self):
		for c in self.children:
			c.rev()

		self.children.reverse()

		# temp = self.left
		# self.left = self.right
		# self.right = self.left


import doctest
print doctest.testmod().failed