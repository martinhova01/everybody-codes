import time


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = int(self.read_data(1))
        bricks_needed = 1
        width = 1
        while True:
            width += 2
            bricks_needed += width
            if bricks_needed > data:
                break
        return width * (bricks_needed - data)
    
    def part2(self):
        data = int(self.read_data(2))
        mod = 5 if self.test else 1111
        available_blocks = 50 if self.test else 20240000
        thickness = 1
        blocks_needed = 1
        width = 1
        while True:
            width += 2
            thickness = (thickness * data) % mod
            blocks_needed += width * thickness
            if blocks_needed > available_blocks:
                return width * (blocks_needed - available_blocks)
            
    def calc_needed_blocks(self, layers, data, mod):
        thickness = 1
        blocks_needed = 1
        width = 1
        thicknesses = [1]
        
        # add blocks
        for _ in range(layers - 1):
            width += 2
            thickness = ((thickness * data) % mod) + mod
            thicknesses.append(thickness)
            blocks_needed += width * thickness
        
        thicknesses = thicknesses[::-1]
        heights = [sum(thicknesses[:i]) for i in range(1, len(thicknesses) + 1)]
        
        # remove bottom blocks
        empty = 0
        for height in heights[1:-1]:
            empty += 2 * ((data * width * height) % mod)
        empty += ((data * width * heights[-1]) % mod)
        return blocks_needed - empty
            
    
    def part3(self):
        data = int(self.read_data(3))
        mod = 5 if self.test else 10
        blocks_available = 160 if self.test else 202400000
        layer = 1
        while True:
            layer += 1
            blocks_needed = self.calc_needed_blocks(layer, data, mod)
            if blocks_needed > blocks_available:
                return blocks_needed - blocks_available
            
            
        
    
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