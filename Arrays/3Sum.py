class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for l in range(len(nums) - 2):
            m = l + 1
            h = len(nums) - 1

            while m < h:
                summ = nums[l] + nums[m] + nums[h]
                if (summ == 0):
                    ans.add((nums[l] , nums[m] , nums[h]))
                    m += 1
                    h -= 1
                elif summ > 0:
                    h -= 1
                else:
                    m += 1

        return ans