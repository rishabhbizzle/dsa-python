class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sortedCount = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        for num, count in sortedCount:
            if len(ans) == k:
                break
            ans.append(num)
        return ans
