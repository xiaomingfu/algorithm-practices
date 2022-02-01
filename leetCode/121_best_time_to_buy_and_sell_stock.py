'''
I: prices = [], prices[i] is the price of a given stock on the ith day
O: maximum profit, if cannot achieve profit return 0. 
single day to buy and a diff day in the future to sell
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      res = 0
      buy = float("inf")
      for sell in prices:
        buy = min(sell, buy)
        res = max(sell - buy, res)
      return res