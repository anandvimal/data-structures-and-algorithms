import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, stone * -1)
        while heap:
            if len(heap) == 1:
                result = abs(heapq.heappop(heap)) 
                print(result)
                return result
            stone_big = abs(heapq.heappop(heap)) 
            stone_small = abs(heapq.heappop(heap))
            
            leftover = stone_big - stone_small
            print(f" big: {stone_big}   small: {stone_small}  leftover:{leftover}")
            if leftover > 0 :
                heapq.heappush(heap, -leftover)
        return 0 # no stones left