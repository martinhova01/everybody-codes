import time
from collections import defaultdict, deque


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
    
    def run(self, part, loop_limit, round_limit = float("inf")):
        data = self.read_data(part).rstrip()
        Qs: list[deque] = [deque(), deque(), deque(), deque()]
        for line in data.split("\n"):
            for i, elem in enumerate(line.split(" ")):
                Qs[i].append(int(elem))
        
        shouts = defaultdict(int)
        round = -1
        shout = None
        while round < round_limit:
            round += 1
            clapper = Qs[round % len(Qs)].popleft()
            q = (round + 1) % len(Qs)
            i = -1
            d = 1
            for _ in range(clapper):
                if i + d == len(Qs[q]):
                    d *= -1
                elif i + d == -1:
                    d *= -1
                else:
                    i += d
                    
            if d == 1:
                Qs[q].insert(i , clapper)
            elif d == -1:
                Qs[q].insert(i + 1, clapper)
                
            shout = "".join(map(str, [Qs[i][0] for i in range(len(Qs))]))
            shouts[shout] += 1
            if shouts[shout] == loop_limit:
                # part 2, 3
                return shouts, shout, round
        # part 1
        return shouts, shout, round
        
    def part1(self):
        return self.run(1, 10, 10)[1]
    
    def part2(self):
        _, shout, round = self.run(2, 2024)
        return (round + 1) * int(shout)
    
    def part3(self):
        # when we have seen the same number 10 times we probably are in a loop
        shouts, _, _ = self.run(3, 10)
        return max(int(x) for x in shouts.keys())
            
                
    
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