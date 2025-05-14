import heapq

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heap = []
        result = []
        for num in nums:
            heapq.heappush(heap, num)

        while heap:
            alice = heapq.heappop(heap)
            bob = heapq.heappop(heap)
            result.append(bob)
            result.append(alice)
        return result