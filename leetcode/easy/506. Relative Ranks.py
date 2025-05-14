import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        print(f"score : {score}")
        
        heap = []
        position = 1
        for i in range(len(score)):
            heapq.heappush(heap, (score[i]* -1, i))
        while heap:
            x = heapq.heappop(heap)
            print(x)
            runs = x[0] *-1
            index = x[1]
            if position == 1:
                score[index] = "Gold Medal"
            elif position == 2:
                score[index] = "Silver Medal"
            elif position == 3:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(position)
            position +=1
        return score
