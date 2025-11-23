import time


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def parse(self, data):
        names, rules_string = data.split("\n\n")

        names = list(names.split(","))

        rules = []
        for line in rules_string.split("\n"):
            first, last = line.split(" > ")
            last = list(last.split(","))
            rules.append((first, last))
        return names, rules

    def is_valid(self, name, rules):
        for rule in rules:
            first, last = rule
            for i, c in enumerate(name[:-1]):
                if c != first:
                    continue
                if name[i + 1] not in last:
                    return False

        return True

    def part1(self):
        names, rules = self.parse(self.read_data(1))

        for name in names:
            if self.is_valid(name, rules):
                return name

    def part2(self):
        names, rules = self.parse(self.read_data(2))

        s = 0
        for i, name in enumerate(names):
            if self.is_valid(name, rules):
                s += i + 1
        return s

    def extend(self, prefix):
        if len(prefix) > 11:
            return

        if len(prefix) >= 7:
            self.names.add(prefix)

        last_c = prefix[-1]
        if prefix[-1] not in self.rules:
            return

        for next_c in self.rules[last_c]:
            self.extend(prefix + next_c)

    def part3(self):
        prefixes, rules_org = self.parse(self.read_data(3))

        self.rules = {}
        for first, last in rules_org:
            self.rules[first] = last

        self.names = set()
        for prefix in prefixes:
            if not self.is_valid(prefix, rules_org):
                continue
            self.extend(prefix)

        return len(self.names)


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
