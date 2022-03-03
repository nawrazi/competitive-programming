# https://leetcode.com/problems/palindrome-linked-list/submissions/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = []
        length = 0

        while head:
            numbers.append(head.val)
            head = head.next
            length+=1

        i, j = 0, length-1
        while i<j:
            if numbers[i]!=numbers[j]:
                return False
            i+=1
            j-=1

        return True
