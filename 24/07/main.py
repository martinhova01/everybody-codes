import time
import itertools
from collections import deque
from tqdm import tqdm
import numpy as np

import sys
sys.path.append("../..")
from utils import adjacent4


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = self.read_data(1)
        res = {}
        for line in data.split("\n"):
            device, plan = line.split(":")
            plan = [c for c in plan.split(",")]
            s = 0
            curr = 10
            for i in range(10):
                c = plan[i % len(plan)]
                if c == "+":
                    curr += 1
                elif c == "-":
                    curr -= 1
                s += curr
            res[device] = s
        
        return "".join([x[0] for x in sorted(res.items(), key=lambda x: x[1], reverse=True)])

    
    def part2(self):
        data = self.read_data(2)
        plans, track = data.split("\n\n")
        track = [[x for x in line] for line in track.split("\n")]
        track = np.array(track)
        track_string = ""
        for _ in range(4):
            for i in range(1, len(track[0])):
                track_string += track[0][i]
            track = np.rot90(track)
        
        res = {}
        for line in plans.split("\n"):
            device, plan = line.split(":")
            plan = [c for c in plan.split(",")]
            s = 0
            curr = 10
            for i in range(len(track_string) * 10):
                op_track = track_string[i % len(track_string)]
                op_plan = plan[i % len(plan)]
                if op_track == "+":
                    curr += 1
                elif op_track == "-":
                    curr =  max(0, curr - 1)
                elif op_plan == "+":
                    curr += 1
                elif op_plan == "-":
                    curr =  max(0, curr - 1)
                s += curr
            res[device] = s
        return "".join([x[0] for x in sorted(res.items(), key=lambda x: x[1], reverse=True)])
    
    def find_track(self, track):
        track_string = ""
        visited = set()
        visited.add((0, 0))
        q = deque()
        q.append((1, 0))
        while q:
            x, y = q.popleft()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            c = track[y][x]
            if c == " ":
                continue
            track_string += c
            
            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= len(track[0]) or ny < 0 or ny >= len(track):
                    continue
                q.append((nx, ny))
                
        return track_string + "=" # the 'S' behaves like a '='
    
    def simulate(self, plan, track_string) -> int:
        s = 0
        curr = 10
        for i in range(len(track_string) * 2024):
            op_track = track_string[i % len(track_string)]
            op_plan = plan[i % len(plan)]
            if op_track == "+":
                curr += 1
            elif op_track == "-":
                curr =  max(0, curr - 1)
            elif op_plan == "+":
                curr += 1
            elif op_plan == "-":
                curr =  max(0, curr - 1)
            s += curr
        return s
                
    
    def part3(self):
        data = self.read_data(3)
        opponent_plan, track = data.split("\n\n")
        track = [[x for x in line] for line in track.split("\n")]
        
        track_string = self.find_track(track)
        opponent_plan = "".join(opponent_plan[2:].split(","))
        opponent_score = self.simulate(opponent_plan, track_string)
        
        res = 0
        for plan in tqdm(itertools.product("+-=", repeat=11)):
            plan = "".join(plan)
            if plan.count("+") != 5 or plan.count("-") != 3 or plan.count("=") != 3:
                continue
            if self.simulate(plan, track_string) > opponent_score:
                res += 1
        return res
    
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