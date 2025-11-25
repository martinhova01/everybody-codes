import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = list(map(int, self.read_data(1).split("\n")))
        nums = list(data)
        
        round = 1
        while round <= 10:
            
            
            done = True
            for i in range(len(nums) - 1):
                if nums[i] == 0:
                    continue
                if nums[i] > nums[i + 1]:
                    done = False
                    nums[i] -= 1
                    nums[i + 1] += 1
            if done:
                break
                    
            round += 1
                    
        
        while round <= 10:
            for i in range(len(nums) - 1):
                if nums[i + 1] == 0:
                    continue
                if nums[i] < nums[i + 1]:
                    nums[i + 1] -= 1
                    nums[i] += 1
            
            round += 1
        
        print(nums)
                
        s = 0
        for i, n in enumerate(nums):
            s += (i + 1) * n
        
        return s
    
    def part2(self):
        data = list(map(int, self.read_data(2).split("\n")))
        nums = list(data)
        
        round = 0
        while True:
            
            
            done = True
            for i in range(len(nums) - 1):
                if nums[i] == 0:
                    continue
                if nums[i] > nums[i + 1]:
                    done = False
                    nums[i] -= 1
                    nums[i + 1] += 1
            if done:
                break
                    
            round += 1
                    
        
        while True:
            done = True
            for i in range(len(nums) - 1):
                if nums[i + 1] == 0:
                    continue
                if nums[i] < nums[i + 1]:
                    done = False
                    nums[i + 1] -= 1
                    nums[i] += 1
            
            if done:
                break
            
            round += 1
            
        return round
    
    def part3(self):
        data = list(map(int, self.read_data(3).split("\n")))
        nums = list(data)
        
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    # print(f"part 3: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()