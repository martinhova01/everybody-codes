import time
from collections import defaultdict, deque


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
    
    def find_all_paths(self, part):
        data = self.read_data(part)
        E = defaultdict(set)
        for line in data.split("\n"):
            source, dests = line.split(":")
            for dest in dests.split(","):
                E[source].add(dest)
        q = deque()
        q.append(("RR", ["RR"]))
        paths = []
        visited = set()
        while q:
            u, path = q.popleft()
            if u == "@":
                paths.append(path)
                
            if u in visited:
                continue
            visited.add(u)
            
            for v in E[u]:
                new_path = path + [v]
                
                q.append((v, new_path))
        return paths
        
    def part1(self):
        paths = self.find_all_paths(1)
        lengths = [len(p) for p in paths]
        unique = [length for length in set(lengths) if lengths.count(length) == 1][0]
        return "".join(paths[lengths.index(unique)])
    
    def part2(self):
        paths = self.find_all_paths(2)
        lengths = [len(p) for p in paths]
        unique = [length for length in set(lengths) if lengths.count(length) == 1][0]
        return "".join(p[0] for p in paths[lengths.index(unique)])
    
    def part3(self):
        paths = self.find_all_paths(3)
        lengths = [len(p) for p in paths]
        unique = [length for length in set(lengths) if lengths.count(length) == 1][0]
        return "".join(p[0] for p in paths[lengths.index(unique)])
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}")
    # print(f"part 3: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()