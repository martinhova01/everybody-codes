import time
import copy 

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8


class Solution():
    def __init__(self, test=False, do_print=False):
        self.test = test
        self.do_print = do_print
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return [list(x) for x in open(filename).read().split("\n")]
    
    def print_grid(self, grid):
        res = ""
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] >= 10:
                    res += "X"
                else:
                    
                    res += str(grid[y][x])
            res += "\n"
        print(res)
        
    def solve(self, org_grid, use_diagonal=False):
        adjacent_function = adjacent8 if use_diagonal else adjacent4
        
        grid = [[0 if org_grid[y][x] == "." else 1 for x in range(len(org_grid[y]))] for y in range(len(org_grid))]
        dept = 2
        changed = True
        while changed:
            new_grid = copy.deepcopy(grid)
            changed = False
            for y in range(1, len(grid) - 1):
                for x in range(1, len(grid[y]) - 1):
                    num = grid[y][x]
                    if num <= dept - 2:
                        continue
                    
                    if all(grid[ny][nx] == num for (nx, ny) in adjacent_function(x, y)):
                        new_grid[y][x] += 1
                        changed = True
            grid = new_grid
            dept += 1
            
        if self.do_print: 
            self.print_grid(grid)
            
        return sum(grid[y][x] for x in range(len(grid[y])) for y in range(len(grid)))
        
    def part1(self):
        return self.solve(self.read_data(1))
        
    
    def part2(self):
        return self.solve(self.read_data(2))
        
    
    def part3(self):
        grid = self.read_data(3)
        
        #add a padding of "." around the edges of the grid
        for y in range(len(grid)):
            grid[y].insert(0, ".")
            grid[y].append(".")
        row = ["." for _ in range(len(grid[0]) + 2)]
        grid.insert(0, row)
        grid.append(row)
        
        return self.solve(grid, use_diagonal=True)
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True, )
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()