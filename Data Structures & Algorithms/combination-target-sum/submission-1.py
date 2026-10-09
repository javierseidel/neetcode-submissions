class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        def dfs(temp, runTot, curEl):

            if runTot == target:
                res.append(temp.copy())
                return
            
            for i in range(curEl, len(nums)):
                if runTot + nums[i] > target:
                    return
                temp.append(nums[i])
                dfs(temp, runTot+nums[i], i)
                temp.pop()

        dfs([], 0, 0)
        return res