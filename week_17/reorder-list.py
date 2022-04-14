# https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = {}
        temp = head
        while temp and temp.next and temp.next.next:
            prev[temp.next] = temp
            temp = temp.next

        first_left = head
        second_left = head.next
        first_right = temp
        second_right = temp.next

        while first_left != first_right:
            first_right.next = None
            first_left.next = second_right
            second_right.next = second_left

            first_left = second_left
            second_left = first_left.next
            if first_left == first_right:
                break
            first_right = prev[first_right]
            second_right = first_right.next
