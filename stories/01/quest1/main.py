import time
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
    
    def eni(self, N, exp, mod):
        num = 1
        res = []
        for _ in range(exp):
            num = (num * N) % mod
            res.append(str(num))
        
        return int("".join(reversed(res)))
    
    def eni_2(self, N, exp, mod):
        num = self.mod_exp(N, exp - 4, mod)
        res = [str(num)]
        for _ in range(4):
            num = (num * N) % mod
            res.append(str(num))
        
        return int("".join(reversed(res)))
    
    def eni_3(self, N, exp, mod):
        num = N
        res = N
        seen = [N]
        for _ in range(exp-1):
            num = (num * N) % mod
            if num in seen:
                loop_start = seen.index(num)
                loop = seen[loop_start:]
                loops = (exp - loop_start) // len(loop)
                left = exp - loop_start - (loops * len(loop))
                return sum(seen[0:loop_start]) + sum(loop) * loops + sum(loop[0:left])
            
            seen.append(num)
            res += num
        
        return res
    
    def mod_exp(self, a, b, m):
        result = 1
        a %= m
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            b //= 2
        return result
        
    def part1(self):
        data = self.read_data(1)
        best = 0
        for line in data.split("\n"):
            a, b, c, x, y, z, m = map(int, re.findall(r"\d+", line))
            best = max(best, self.eni(a, x, m) + self.eni(b, y, m) + self.eni(c, z, m))
        return best
    
    def part2(self):
        data = self.read_data(2)
        best = 0
        for line in data.split("\n"):
            a, b, c, x, y, z, m = map(int, re.findall(r"\d+", line))
            best = max(best, self.eni_2(a, x, m) + self.eni_2(b, y, m) + self.eni_2(c, z, m))
        return best
    
    def part3(self):
        data = self.read_data(3)
        best = 0
        for line in data.split("\n"):
            a, b, c, x, y, z, m = map(int, re.findall(r"\d+", line))
            best = max(best, self.eni_3(a, x, m) + self.eni_3(b, y, m) + self.eni_3(c, z, m))
        return best
    
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