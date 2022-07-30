# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False
        
        h = list(Counter(hand).items())
        heapq.heapify(h)
        
        while h:
            s, sv = h[0]
            arr = []
            for i in range(groupSize):
                if not h:
                    return False
                k, v = heapq.heappop(h)
                if k != s + i or v < sv:
                    return False
                if v > sv:
                    arr.append((k, v - sv))
            for k, v in arr:
                heapq.heappush(h, (k,v))
        return True