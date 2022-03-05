# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        curr = start = ListNode()
        for i in range(len(lists)):
            if lists[i]:
                tup = (lists[i].val, i)
                heapq.heappush(heap,tup)

        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = lists[idx]

            curr = curr.next
            lists[idx] = lists[idx].next

            if lists[idx]:
                heapq.heappush(heap,(lists[idx].val,idx))

        return start.next
