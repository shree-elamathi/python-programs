'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())

        for candidate in candidates:
            for t in range(target, candidate - 1, -1):
                for comb in dp[t - candidate]:
                    dp[t].add(comb + (candidate,))

        return list(map(list, dp[target]))