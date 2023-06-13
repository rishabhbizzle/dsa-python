class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0, 0
        high = len(nums) - 1

        for i in range(len(nums)):
            if nums[mid] == 0:
                # swap
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                # swap
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1