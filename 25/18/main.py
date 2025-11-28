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


class Node:
    def __init__(self, thickness: int, edges: list):
        self.thickness = thickness
        self.edges = edges
    
    def __str__(self):
        return f"({self.thickness}, {self.edges})"
    
    def __repr__(self):
        return self.__str__()


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
    
    def parse(self, data: str):
        G: dict[int, Node] = {} # (node_id): (Node)
        
        for plant in data.split("\n\n"):
            lines = plant.split("\n")
            plant_id, thickness = tuple(map(int, re.findall(r"-?\d+", lines[0])))
            G[plant_id] = Node(thickness, [])
            
            for branch in lines[1:]:
                if "free" in branch:
                    G[plant_id].edges.append((0, 1))
                else:
                    from_plant, edge_thickness = tuple(map(int, re.findall(r"-?\d+", branch)))
                    G[plant_id].edges.append((from_plant, edge_thickness))
        return G
        
    def part1(self):
        G = self.parse(self.read_data(1))
        
        energies: dict[int, int] = {0: 1} # node_id: energy
        
        for plant_id in range(1, max(G.keys()) + 1):
            plant = G[plant_id]
            
            s = 0
            for u, u_thickness in plant.edges:
                if u in energies:
                    s += u_thickness * energies[u]
                    
            if s >= plant.thickness:
                energies[plant_id] = s
        
        
        return energies[max(G.keys())]
    
    def part2(self):
        data, test_cases = self.read_data(2).split("\n\n\n")
        self.G = self.parse(data)
        test_cases = [tuple(int(x) for x in line.split(" ")) for line in test_cases.split("\n")]
        
        res = 0
        for test_case in test_cases:
            res += self.get_energy(test_case)
        
        return res
    
    @functools.cache
    def get_energy(self, test_case):
        energies: dict[int, int] = {} # node_id: energy
        for i, flag in enumerate(test_case):
            energies[i + 1] = flag
            
        for plant_id in range(len(test_case) + 1, max(self.G.keys()) + 1):
            plant = self.G[plant_id]
            
            s = 0
            for u, u_thickness in plant.edges:
                if u in energies:
                    s += u_thickness * energies[u]
                    
            if s >= plant.thickness:
                energies[plant_id] = s
            else:
                energies[plant_id] = 0
        
        
        return energies[max(self.G.keys())]
                    
    
    def part3(self):
        data, test_cases = self.read_data(3).split("\n\n\n")
        self.G = self.parse(data)
        test_cases = [tuple(int(x) for x in line.split(" ")) for line in test_cases.split("\n")]
        
        best = 0
        for test_case in (tuple(map(int, p)) for p in itertools.product([0, 1], repeat=len(test_cases[0]))):
            best = max(best, self.get_energy(test_case))
            
            
        res = 0
        for test_case in test_cases:
            energy = self.get_energy(test_case)
            if not energy:
                continue
            res += best - energy
        
        return res
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()