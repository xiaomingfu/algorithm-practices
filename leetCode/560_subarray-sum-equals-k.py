# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        pre_s, cnt = 0, 0
        for n in nums:
            pre_s += n
            cnt += dic.get(pre_s - k, 0)
            dic[pre_s] = dic.get(pre_s, 0) + 1
        return cnt