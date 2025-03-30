from typing import List
# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0 #start at  zero
        highest_altitude = 0 

        for current_gain in gain:
            current_altitude += current_gain
            highest_altitude = max(current_altitude, highest_altitude)

        return highest_altitude