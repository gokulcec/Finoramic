# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        
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
		pathsum(A,B,[])
		return result