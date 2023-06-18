class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        n = len(nums)
        ans = []
        for i in range(n):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        for key, val in hashMap.items():
            if val > n//3:
                ans.append(key)
        return ans