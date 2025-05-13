from collections import Counter
from typing import List
import heapq

class Pair: 
    def __init__(self, str, freq): 
        self.str = str 
        self.freq = freq

    #define  a custom comparator. 
    # heapq uses __lt__ operator to compare elements
    def __lt__(self, other):
        # prioritize lexicographically smaller strings
        if self.freq == other.freq:
            return self.str < other.str
        # otherwise, prioritize higher frequency
        return self.freq > other.freq

def k_most_frequent_strings_max_heap(strs: List[str], k: int) -> List[str]:
    freqs = Counter(strs)
    max_heap = [Pair(str, freq) for str, freq in freqs.items()]
    heapq.heapify(max_heap)
    # pop the most frequent k elements
    return [heapq.heappop(max_heap).str for _ in range(k)], max_heap

#k_most_frequent_strings_max_heap(["a", "b", "c", "a", "b", "a"], 2)
result, h = k_most_frequent_strings_max_heap(["a", "b", "c", "a", "b", "a"], 2)
result = k_most_frequent_strings_max_heap(["x", "y", "z", "x", "y", "x", "z", "z", "z", "y"], 2) # needs lt operator
print(result)  # Output: ['a', 'b']
