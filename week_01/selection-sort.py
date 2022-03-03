# https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution:
    def select(self, arr_trunc, i):
        return arr_trunc.index(min(arr_trunc)) + i

    def selectionSort(self,arr,n):
        for i in range(n):
            selected = self.select(arr[i:],i)
            arr[i], arr[selected] = arr[selected], arr[i]
        return arr
