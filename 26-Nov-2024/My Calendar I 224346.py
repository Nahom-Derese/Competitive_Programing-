# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class Node:
    def __init__(self, l, r):
        self.range = (l,r)
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, start: int, end: int) -> bool:
        if self.root == None:
            self.root = Node(start, end)
            return True
        
        def rec(node):
            if node.range[0] < start:

                if node.range[1] > start:
                    return False

                if not node.right:
                    node.right = Node(start, end)
                    return True

                return rec(node.right)
            
            if node.range[0] > start:

                if node.range[0] < end:
                    return False

                if not node.left:
                    node.left = Node(start, end)
                    return True

                return rec(node.left)
                    
            return False
            
        return rec(self.root)            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)