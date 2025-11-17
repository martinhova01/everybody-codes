import time


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def parse(self, data: str):
        names, instructions = data.split("\n\n")
        names = names.split(",")
        instructions = instructions.split(",")
        return names, instructions

    def part1(self):
        names, instructions = self.parse(self.read_data(1))

        i = 0
        N = len(names)
        for instruction in instructions:
            dir, n = instruction
            if dir == "R":
                i = min(i + int(n), N - 1)
            else:
                i = max(0, i - int(n))

        return names[i]

    def part2(self):
        names, instructions = self.parse(self.read_data(2))

        i = 0
        N = len(names)
        for instruction in instructions:
            dir = instruction[0]
            n = int(instruction[1:])
            if dir == "R":
                i = (i + n) % N
            else:
                i = (i - n) % N

        return names[i]

    def part3(self):
        names, instructions = self.parse(self.read_data(3))

        N = len(names)
        for instruction in instructions:
            dir = instruction[0]
            n = int(instruction[1:])
            if dir == "R":
                names[0], names[n % N] = names[n % N], names[0]
            else:
                names[0], names[-n % N] = names[-n % N], names[0]

        return names[0]


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
