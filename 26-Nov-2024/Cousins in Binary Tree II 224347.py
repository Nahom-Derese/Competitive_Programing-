# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([(root, 0)])

        while queue:
            for _ in range(len(queue)):
                node, _ = queue.popleft()

                if node:
                    siblings = 0
                    if node.left:
                        siblings += node.left.val
                    if node.right:
                        siblings += node.right.val
                    
                    if node.left:
                        queue.append((node.left, siblings))
                    if node.right:
                        queue.append((node.right, siblings))

                
            cousins = 0
            for node, _  in queue:
                if node:
                    cousins += node.val
            
            for node, siblings  in queue:
                node.val = cousins - siblings
                
        root.val = 0
        return root
