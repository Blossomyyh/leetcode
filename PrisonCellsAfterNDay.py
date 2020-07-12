from typing import List


class Solution:
    # All states between two repetitive states form a cycle, which would repeat itself over the time.
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        remem = []
        remem.append(cells)
        i = N
        while i > 0:
            cell = cells.copy()
            cell[0], cell[-1] = 0, 0
            for i in range(1, len(cell) - 1):
                if cells[i - 1] == cells[i + 1]:
                    cell[i] = 1
                else:
                    cell[i] = 0
            if cell not in remem:
                remem.append(cell)
            else:
                break
            cells = cell
            i -= 1
        return remem[N - 1] if N <= len(remem) else remem[N % len(remem) - 1]
# #     In other words, if the remaining steps is NN, at least we could fast-forward to the step of N \mod.

list = [0,1,0,1,1,0,0,1]

Solution().prisonAfterNDays(list, 7)