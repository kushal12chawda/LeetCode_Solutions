# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.make(1, n)

    def make(self, start, end):
        if start > end:
            return [None]
        
        all_tree = []
        for i in range(start, end + 1):
            left = self.make(start, i - 1)
            right = self.make(i + 1, end)

            for l in left:
                for r in right:
                    root = TreeNode(i, l, r)
                    all_tree.append(root)
        
        return all_tree
        