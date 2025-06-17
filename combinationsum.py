# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getcombo(start,t):
            if t ==0:
                return[[]]
            if t < 0:
                return []
            if sum(candidates[start:]) <t:
                return []
            res = []
            for i  in range(start, len(candidates)):
                n = candidates[i]
                nr = getcombo(i+1, t-n)
                for r in nr:
                    r.append(n)
                    r.sort()
                    if r not in res:
                        res.append(r)
            return res
    
        return getcombo(0,target)


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print("Expected Output: [[1,1,6], [1,2,5], [1,7], [2,6] ]")
print("Actual Output:",s.combinationSum2(candidates, target))
