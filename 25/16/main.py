import time


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = list(map(int, self.read_data(1).split(",")))

        return sum(self.generate_wall(data, 90))

    def generate_wall(self, spell, length):
        res = [0 for _ in range(length)]
        for n in spell:
            for i in range(n - 1, len(res), n):
                res[i] += 1
        return res

    def get_spell(self, wall):
        tmp = [0 for _ in range(len(wall))]

        res = []

        for i in range(len(wall)):
            if wall[i] > tmp[i]:
                res.append(i + 1)
                tmp = self.generate_wall(res, len(wall))
        return res

    def part2(self):
        data = list(map(int, self.read_data(2).split(",")))
        spell = self.get_spell(data)

        m = 1
        for n in spell:
            m *= n
        return m

    def length_to_blocks(self, length, spell):
        blocks = 0
        for s in spell:
            num = (length) // s
            blocks += num

        return blocks

    def part3(self):
        data = list(map(int, self.read_data(3).split(",")))
        spell = self.get_spell(data)

        left = 1
        right = 10**18

        while left <= right:
            mid = (left + right) // 2
            blocks = self.length_to_blocks(mid, spell)

            if blocks == 202520252025000:
                return mid
            elif blocks < 202520252025000:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1


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
