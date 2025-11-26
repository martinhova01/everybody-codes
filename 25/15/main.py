import time
import itertools
import functools
from collections import Counter, defaultdict, deque
# import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy
import heapq
from functools import cache

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist

@cache
def point_on_line(x, y, x1, y1, x2, y2):
    if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
        return False
    
    return (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2))


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = self.read_data(1)
        
        walls = set()
        
        x, y = 0, 0
        dir = [0, -1]
        for instruction in data.split(","):
            direction = instruction[0]
            n = int(instruction[1:])
            if direction == "L":
                dir = [-dir[1], dir[0]]
            else:
                dir = [dir[1], -dir[0]]
                
            for _ in range(0, n):
                x, y = x + dir[0], y + dir[1]
                walls.add((x, y))
                
        goal = (x, y)
        walls.remove((x, y)) # goal is not a wall
        
        visited = set()
        q = deque([(0, 0, 0)]) # x, y, step
        while q:
            x, y, step = q.popleft()
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            if (x, y) == goal:
                return step
            
            for nx, ny in adjacent4(x, y):
                if (nx, ny) in walls:
                    continue
                q.append((nx, ny, step + 1))
        
    
    def part2(self):
        data = self.read_data(2)
        
        walls = set()
        
        x, y = 0, 0
        dir = [0, -1]
        for instruction in data.split(","):
            direction = instruction[0]
            n = int(instruction[1:])
            if direction == "L":
                dir = [-dir[1], dir[0]]
            else:
                dir = [dir[1], -dir[0]]
                
            for _ in range(0, n):
                x, y = x + dir[0], y + dir[1]
                walls.add((x, y))
                
        goal = (x, y)
        walls.remove((x, y)) # goal is not a wall
        
        visited = set()
        q = deque([(0, 0, 0)]) # x, y, step
        while q:
            x, y, step = q.popleft()
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            if (x, y) == goal:
                return step
            
            for nx, ny in adjacent4(x, y):
                if (nx, ny) in walls:
                    continue
                q.append((nx, ny, step + 1))
    
    def part3(self):
        data = self.read_data(3)
        
        walls = set()
        
        x, y = 0, 0
        dir = [0, -1]
        for instruction in data.split(","):
            direction = instruction[0]
            n = int(instruction[1:])
            if direction == "L":
                dir = [dir[1], -dir[0]]
            else:
                dir = [-dir[1], dir[0]]
            
            start = (x, y)
            x, y = x + dir[0] * (n - 1), y + dir[1] * (n - 1)
            stop = (x, y)
            walls.add((start, stop))
            
            x, y = x + dir[0], y + dir[1]
    
        print(walls)
        
        goal = (x, y)
        print(goal)
        # walls.remove(goal)  # goal is not a wall
    
        visited = set()
        q = []  # heap: (f, steps, x, y)
        
        start_x, start_y = 0, 0
        h0 = manhattanDist(start_x, start_y, x, y)
        heapq.heappush(q, (h0, 0, start_x, start_y))

        while q:
            f, steps, x, y = heapq.heappop(q)
            # print(x, y)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if (x, y) == goal:
                return steps

            for nx, ny in adjacent4(x, y):
                if any(point_on_line(nx, ny, x1, y1, x2, y2) for ((x1, y1), (x2, y2)) in walls):
                    continue
                
                new_steps = steps + 1
                new_f = new_steps + manhattanDist(nx, ny, goal[0], goal[1])
                heapq.heappush(q, (new_f, new_steps, nx, ny))
        
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
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