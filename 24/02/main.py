import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        words, text = open(filename).read().split("\n\n")
        words = words[6:].split(",")
        return words, text
        
    def part1(self):
        words, text = self.read_data(1)
        return sum(text.count(word) for word in words)
    
    def part2(self):
        words, text = self.read_data(2)
        all_words = list(words)
        for word in words:
            all_words.append(word[::-1])
        text = text.split("\n")
        s = 0
        for line in text:
            used = set()
            for word in all_words:
                for i in range(len(line)):
                    if line[i:].startswith(word):
                        used.update(range(i, i + len(word)))
            s += len(used)
        return s
    
    def part3(self):
        words, text = self.read_data(3)
        text = text.split("\n")
        all_words = list(words)
        for word in words:
            all_words.append(word[::-1])
            
        used = set()
        for word in all_words:
            
            #horizontal
            for y in range(len(text)):
                for x in range(len(text[y])):
                    if all(text[y][(x + i) % len(text[y])] == word[i] for i in range(len(word))):
                        used.update(((x + i) % len(text[y]), y) for i in range(len(word)))
            
            #vertical
            for x in range(len(text[0])):
                for y in range(len(text) - len(word) + 1):
                    if all(text[y + i][x] == word[i] for i in range(len(word))):
                        used.update((x, y + i) for i in range(len(word)))
                            
        return len(used)
                              
    
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