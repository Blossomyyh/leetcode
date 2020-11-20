def almostTetris(n, m, figures):
    grid = [[0] * m for _ in range(n)]
    for i, f in enumerate(figures):
        done = False
        if f == 1:
            for row in range(n):
                for col in range(m):
                    if grid[row][col] == 0:
                        grid[row][col] = i + 1
                        done = True
                        break
                if done:
                    break
        if f == 2:
            for row in range(n):
                for col in range(m - 2):
                    if (grid[row][col] == 0 and grid[row][col + 1] == 0 and
                            grid[row][col + 2] == 0):
                        grid[row][col] = grid[row][col +
                                                   1] = grid[row][col + 2] = i + 1
                        done = True
                        break
                if done:
                    break
        if f == 3:
            for row in range(n - 1):
                for col in range(m - 1):
                    if (grid[row][col] == 0 and grid[row][col + 1] == 0 and
                            grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0):
                        grid[row][col] = grid[row][col + 1] = grid[row +
                                                                   1][col] = grid[row + 1][col + 1] = i + 1
                        done = True
                        break
                if done:
                    break
        if f == 4:
            for row in range(n - 2):
                for col in range(m - 1):
                    if (grid[row][col] == 0 and grid[row + 1][col] == 0
                            and grid[row + 2][col] == 0 and grid[row + 1][col + 1] == 0):
                        grid[row][col] = grid[row + 1][col] = grid[row +
                                                                   2][col] = grid[row + 1][col + 1] = i + 1
                        done = True
                        break
                if done:
                    break
        if f == 5:
            for row in range(n - 1):
                for col in range(m - 2):
                    if (grid[row][col + 1] == 0 and grid[row + 1][col] == 0
                            and grid[row + 1][col + 1] == 0 and grid[row + 1][col + 2] == 0):
                        grid[row][col + 1] = grid[row + 1][col] = grid[row +
                                                                       1][col + 1] = grid[row + 1][col + 2] == i + 1
                        done = True
                        break
                if done:
                    break
    return grid