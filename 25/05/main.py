import time
from functools import cmp_to_key


def build_sword(nums):
    sword = []
    for num in nums:
        placed = False
        for i in range(len(sword)):
            left, mid, right = sword[i]
            if num < mid and not left:
                sword[i][0] = num
                placed = True
                break
            if num > mid and not right:
                sword[i][2] = num
                placed = True
                break

        if not placed:
            sword.append([None, num, None])
    return sword


def get_quality(sword):
    quality = list(map(lambda x: str(x[1]), sword))
    quality = int("".join(quality))
    return quality


def compare(a, b):
    id_a, sword_a = a
    id_b, sword_b = b
    q_a = get_quality(sword_a)
    q_b = get_quality(sword_b)

    if q_a != q_b:
        return q_b - q_a

    i = 0
    while i < len(sword_a) and i < len(sword_b):
        layer_a = int("".join(str(n) for n in sword_a[i] if n is not None))
        layer_b = int("".join(str(n) for n in sword_b[i] if n is not None))
        if layer_a != layer_b:
            return layer_b - layer_a
        i += 1

    return id_b - id_a


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def parse_line(self, line: str):
        id, nums = line.split(":")
        nums = list(map(int, nums.split(",")))
        return int(id), nums

    def parse(self, data: str):
        res = []
        for line in data.split("\n"):
            res.append(self.parse_line(line))
        return res

    def part1(self):
        _, nums = self.parse_line(self.read_data(1))
        return get_quality(build_sword(nums))

    def part2(self):
        data = self.parse(self.read_data(2))

        qualities = []

        for _, nums in data:
            qualities.append(get_quality(build_sword(nums)))

        qualities.sort()
        return qualities[-1] - qualities[0]

    def part3(self):
        data = self.parse(self.read_data(3))
        swords = []

        for id, nums in data:
            swords.append((id, build_sword(nums)))

        swords = sorted(swords, key=cmp_to_key(compare))

        checksum = 0
        for i, (id, _) in enumerate(swords):
            checksum += (i + 1) * id

        return checksum


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
