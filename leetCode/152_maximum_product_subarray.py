class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #   #o(n^2), O(1)
    #   res = float("-inf")
    #   for i in range(len(nums)):
    #       p = 1
    #       for j in range(i, len(nums)):
    #           p *= nums[j]
    #           res = max(res, p)
    #   return res


  def maxProduct(self, nums: List[int]) -> int:
    cur_max = nums[0]
    cur_min = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        temp1 = cur_max
        temp2= cur_min
        cur_max = max(temp1 * nums[i], temp2 * nums[i], nums[i])
        cur_min = min(temp1 * nums[i], temp2 * nums[i], nums[i])
        res = max(cur_max, res)
    return res
        