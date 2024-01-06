class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        nums = [-1 for i in range(n)]
        cur = -1
        i = n - 1
        while i >= 0:
            nums[i] = cur
            cur = max(cur, arr[i])
            i -= 1
        return nums