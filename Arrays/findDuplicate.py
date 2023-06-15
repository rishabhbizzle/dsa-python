class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # LL cycle method
        slow = nums[0]
        fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


'''--------------------------------------------------'''

        # hashing method
        n = len(nums)
        count = [0 for i in range(n+1)]

        for num in nums:
            if count[num] == 1:
                return num
            count[num] = 1
