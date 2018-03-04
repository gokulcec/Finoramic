class Node:

	def __init__(self,x):
		self.val = x
		self.right = None
		self.left = None

class Tree:
	
	def TreeTraversal(self,root,sum):

		result = []

		def pathsum(root,tempsum,temp):
			
			if root == None:
				return 

			else:
				if root.left is None and root.right is None:
					if root.val == tempsum:
						result.append(temp+[root.val])
						return
			pathsum(root.left,tempsum-root.val,temp+[root.val])
			pathsum(root.right,tempsum-root.val,temp+[root.val])	
		pathsum(root,sum,[])

		return result
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(2)
    root.left.right = Node(3)
    root.right = Node(4)
    result = Tree().TreeTraversal(root, 5)
    print (result)		
