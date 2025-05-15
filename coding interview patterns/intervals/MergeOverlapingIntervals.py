from typing import List, Tuple

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def merge_overlapping_intervals(intervals: List[Interval] ) -> List[Interval]: 
    intervals.sort(key= lambda x: x.start)
    merged = [intervals[0]]
    for B in intervals[1:]:
        A = merged[-1]
        # if A and B dont overlap, add B to the merged List.
        if A.end < B.start:
            merged.append(B)
        # if A and B overlap, merge A with B
        else:
            merged[-1] = Interval(A.start, max(A.end, B.end))
    return merged

intervals1 = [[1,6] , [2,4], [5,7], [8,9]]
for i in range(len(intervals1)):
    intervals1[i] = Interval(intervals1[i][0], intervals1[i][1])

merged_result = merge_overlapping_intervals(intervals1)

print("Merged intervals:", merged_result)
            