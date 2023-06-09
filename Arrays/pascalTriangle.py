# not the best solution but came up with this on my own

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1,numRows):
            res = []
            res.append(1)

            for j in range(len(ans[-1])-1):
                curSum = ans[-1][j] + ans[-1][j+1]
                res.append(curSum)
                if len(res) == i:
                    break
                
            res.append(1)
            ans.append(res)

        return ans