# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

def removeDuplicates(llist):
    head = llist
    while head and head.next:
        while head.next and head.data==head.next.data:
            head.next = head.next.next
        if not head.next:
            return llist

        head = head.next

    return llist
