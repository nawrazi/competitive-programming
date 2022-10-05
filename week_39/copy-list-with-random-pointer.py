# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {None: None}
        
        def copy(node):
            if node not in copied:
                copied[node] = Node(node.val)
                copied[node].random = copy(node.random)
                copied[node].next = copy(node.next)
                
            return copied[node]
        
        return copy(head)
    
