# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicated = {}

        temp = head
        while temp:
            if temp.val not in duplicated:
                duplicated[temp.val] = False

            elif not duplicated[temp.val]:
                duplicated[temp.val] = True

            temp = temp.next

        temp = head
        nodes = []
        while temp:
            if not duplicated[temp.val]:
                nodes.append(temp)
            temp = temp.next

        for node in nodes:
            node.next = None

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0] if nodes else None
