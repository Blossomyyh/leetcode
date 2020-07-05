from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        remem = []
        while True:
            cell = cells
            cell[0], cell[-1] = 0,0
            for i in range(1, len(cell)-1):
                if cells[i-1] == cells[i+1]:
                    cell[i] = 1
            if cell in remem: break
            else:
                remem.append(cell)
                cells = cell
        return remem[(N % len(cells)) - 1]




Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7)

