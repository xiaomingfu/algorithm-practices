from lib2to3.pgen2.token import LPAR


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # O(n^2)
      res = []
      for i in range(len(nums)):
        p = 1
        for j in range(len(nums)):
          if i != j:
            p *= nums[j]
        res.append(p)
      return res

      #second solution
      # O(n), O(1)
      res = [0 for _ in nums]
      lp = 1
      for i, n in enumerate(nums):
        res[i] = lp
        lp *= n
      rp = 1
      for i in range(len(nums) - 1, -1, -1):
        res[i] *= rp
        rp *= nums[i]
      return res
