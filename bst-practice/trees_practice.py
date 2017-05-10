class Node():
	def __init__(self, data, children = None):
		self.data = data
		self.children = children or []

	def find_dfs(self, data):
		to_visit = [self]

		while to_visit:
			current = to_visit.pop()

			if current.data == data:
				return current

			to_visit.extend(current.children)

#DFS searches children (and children of those children, etc) of current node before moving onto searching siblings of current node. Uses stack() for [to visit] => [].pop() pops the last item in the array and adds children of last item => DFS! Last item in array first to be evaluated. 

	def find_bfs(self, data):
		to_visit = [self] 

		while to_visit:
			current == to_visit.pop(0)

			if current.data == data:
				return current

			to_visit.extend(current.children)

#pop(0):  uses a QUEUE for [to_visit] => [].pop(0) pops the first item off the list, and adds children to end of the array => Bc children are at the end of the array, the siblings at start of array are evaluated first => BFS!

class Tree():
	def __init__(self, root):
		self.root = root

	def __repr__(self):
		return "<Tree root = %s>" % self.root

	def find_in_tree(self, data):
		"""return node object w this data. 
		Start at root.
		Return None if not found
		"""
		return self.root.find(data)


class BinarySearchNode():
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

	def __repr__(self):
		return "<BinaryNode %s>" % self.data

	def find(self, sought):
		current = self

		while current: 
			print "checking", current.data

			if current.data == sought:
				return current

			elif sought < current.data:
				current = current.left
			elif sought > current.data:
				current = current.right




