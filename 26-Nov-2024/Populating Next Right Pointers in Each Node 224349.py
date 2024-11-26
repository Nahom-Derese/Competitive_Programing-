# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])

        while queue:
            LEN = len(queue)
            for i in range(LEN):
                node = queue.popleft()
                
                if node:
                    if queue and LEN != i+1:
                        node.next = queue[0]
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root