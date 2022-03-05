# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        mono_stack = []

        for num in nums2:
            if not mono_stack:
                mono_stack.append(num)
                continue

            while mono_stack and num>mono_stack[-1]:
                d[mono_stack.pop()] = num

            mono_stack.append(num)

        return [(d[num] if num in d.keys() else -1) for num in nums1]
