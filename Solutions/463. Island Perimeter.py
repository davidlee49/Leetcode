class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimiter = 0
        grid.append([0]* len(grid[0]))
        for row in range(len(grid)):
            grid[row].append(0)
            for square in range(len(grid[row])-1):
                if grid[row][square] == 1:
                    if grid[row][square -1] == 0:
                        perimiter += 1
                    if grid[row -1][square] == 0:
                        perimiter += 1
                    if grid[row][square +1] == 0 and square < len(grid[row]):
                        perimiter += 1
                if grid[row][square] == 0 and grid[row -1][square] == 1:
                        perimiter += 1
        return perimiter