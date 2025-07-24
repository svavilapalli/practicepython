# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

# Get the XOR of all the values of the nodes for each of the three components respectively.
# The difference between the largest XOR value and the smallest XOR value is the score of the pair.
# For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
# Return the minimum score of any possible pair of edge removals on the given tree.

# Example:


# Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
# Output: 0
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
# - The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
# - The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
# The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
# We cannot obtain a smaller score than 0.


class Solution:
    
    def __init__(self):
        self.time = 0

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        ans = 1e9
        xo = 0
                
        n = len(nums)
        adj = [[] for _ in range(n)]
        for val in nums:
            xo ^= val
        for i in range(n-1):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        sub = [0]*n
        ins = [-1]*n
        out = [-1]*n

        def dfs(node, par):
            ins[node] = self.time
            self.time += 1
            sub[node] = nums[node]
            for child in adj[node]:
                if child == par:
                    continue
                dfs(child, node)
                sub[node] = sub[node] ^sub[child]
            out[node] = self.time
            self.time += 1


        dfs(0,0)
        for i in range(1,n):
            for j in range(1,n):
                if i==j:
                    continue
                elif ins[i]<ins[j] and out[i]>out[j]:
                    x = sub[j]
                    y = sub[i] ^ sub[j]
                    z = xo ^ sub[i]
                    mn = min(x, min(y,z))
                    mx = max(x, max(y,z))
                    ans = min(ans, mx-mn)
                elif ins[i]>ins[j] and out[i]<out[j]:
                    x = sub[i]
                    y = sub[i] ^ sub[j]
                    z = xo ^ sub[j]
                    mn = min(x, min(y,z))
                    mx = max(x, max(y,z))
                    ans = min(ans, mx-mn)
                else:
                    x = sub[i]
                    y = sub[j]
                    z = xo ^ sub[i] ^ sub[j]
                    mn = min(x, min(y,z))
                    mx = max(x, max(y,z))
                    ans = min(ans, mx-mn)
        
        return ans


if __name__=="__main__":
    nums = [5,5,2,4,4,2]
    edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
    print("Expected Output: 0")
    s = Solution()
    print("Actual Output: ",s.minimumScore(nums, edges))
