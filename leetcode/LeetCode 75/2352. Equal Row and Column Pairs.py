
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        columns = []

        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                row.append(grid[i][j])
            rows.append(row)
            print(f"row : {row}")

        for i in range(len(grid)):
            column = []
            for j in range(len(grid[i])):
                column.append(grid[j][i])
            columns.append(column)
            print(f"column : {column}")

        count = 0
        for row in rows:
            for column in columns:
                if row == column:
                    count +=1
        
        return count