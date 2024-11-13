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
from utils import adjacent4, adjacent8, directions4, directions8


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = self.read_data(1)
        return None
    
    def part2(self):
        data = self.read_data(2)
        return None
    
    def part3(self):
        data = self.read_data(3)
        return None
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 2: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 2: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()