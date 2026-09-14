class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_fruits = deque((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2)

        num_fruits = sum(1 for row in grid for item in row if item != 0)
        
        new_rotten_fruits = deque()

        num_steps = 0
        num_visited = 0

        while len(new_rotten_fruits) > 0 or num_steps == 0:
            new_rotten_fruits = deque()
            print(rotten_fruits)
            while len(rotten_fruits) > 0:
                i, j = rotten_fruits.popleft()
                num_visited += 1

                dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for di, dj in dirs:
                    new_i = i+di
                    new_j = j+dj
    
                    if new_i in range(len(grid)) and new_j in range(len(grid[0])) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        new_rotten_fruits.append((new_i, new_j))

            num_steps+=1
            
            for fruit in new_rotten_fruits:
                rotten_fruits.append(fruit)


        return num_steps-1 if num_fruits == num_visited else -1