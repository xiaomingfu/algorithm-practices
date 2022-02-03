class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # O(n), O(n)
        dic = {}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = True
        return False
    
    #second solution
    def containsDuplicate(self, nums: List[int]) -> bool:
      # On(log(n)), O(1)
        nums.sort()
        for i in range(0, len(nums) - 1):
          if nums[i] == nums[i + 1]:
            return True
        return False