#Part-1 
import os
import time

map = {0: '^', 1: 'v', 2: '<', 3: '>', 4: '#', 5: '.', 6: 'X', 7: '|', 8:'|', 9: '-', 'a': '-', 'b':'+'}

class Engine:
    def __init__(self):
        self.data = []
        with open(os.path.dirname(__file__) + "/input.txt", "r") as f:
            lines = f.read().split('\n')
            for c in range(len(lines)):
                d = []
                for r in range(len(lines[c])):
                    if lines[c][r] in ['^', 'v', '<', '>']:
                        self.player = (c, r)
                        self.direction = list(map.keys())[list(map.values()).index(lines[c][r])]
                    d.append(list(map.keys())[list(map.values()).index(lines[c][r])])
                self.data.append(d)
        self.fps = 60
        self.debug = False

    def clear(self):
        os.system('cls')

    def draw(self):
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.player == (r, c):
                    print(map[self.direction], end="")
                else:
                    print(map[self.data[r][c]], end="")
            print()
        print()

    def update(self) -> bool:
        print("This method should be overridden.")
        return True
    
    def game_over(self):
        self.draw()
        
        count = 1
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == 6:
                    count += 1
        print(f"Simlation ended. Guard has visited {count} different loations.")

    def loop(self):
        while True:
            if self.debug: self.clear()
            if self.update(): 
                self.game_over()
                break
            if self.debug: 
                self.draw()
                time.sleep(1 / self.fps)

print("Advent of Code 2024 - Day 6")
print("Guard Gallivant")
print("--- Part 1 ---")

class Part1(Engine):
    def __init__(self):
        super().__init__()
        self.loop()
    
    def update(self):

        # end of game
        if self.direction == 0 and self.player[0] == 0: return True
        if self.direction == 1 and self.player[0] == len(self.data)-1: return True
        if self.direction == 2 and self.player[1] == 0: return True
        if self.direction == 3 and self.player[1] == len(self.data[0])-1: return True

        # movement
        if self.direction == 0:
            if self.data[self.player[0]-1][self.player[1]] == 4:
                self.direction = 3
            else:
                self.data[self.player[0]][self.player[1]] = 6
                self.player = (self.player[0]-1, self.player[1])
        elif self.direction == 1:
            if self.data[self.player[0]+1][self.player[1]] == 4:
                self.direction = 2
            else:
                self.data[self.player[0]][self.player[1]] = 6
                self.player = (self.player[0]+1, self.player[1])
        elif self.direction == 2:
            if self.data[self.player[0]][self.player[1]-1] == 4:
                self.direction = 0
            else:
                self.data[self.player[0]][self.player[1]] = 6
                self.player = (self.player[0], self.player[1]-1)
        elif self.direction == 3:
            if self.data[self.player[0]][self.player[1]+1] == 4:
                self.direction = 1
            else:
                self.data[self.player[0]][self.player[1]] = 6
                self.player = (self.player[0], self.player[1]+1)
    
        return False

input("Press Enter to start simulation...")
E = Part1()

#Part-2 
print("--- Part 2 ---")

class Part2(Engine):
    def __init__(self):
        super().__init__()
        self.obstacles = 0
        self.loop()
    
    map = {0: '^', 1: 'v', 2: '<', 3: '>', 4: '#', 5: '.', 6: 'X', 7: '|', 8:'|', 9: '-', 'a': '-', 'b':'+'}

    def check_cols_rows(self):

        if self.direction == 0:
            for r in range(self.player[1]+1, len(self.data[0])):
                if self.data[self.player[0]][r] == 'a': return True
                if self.data[self.player[0]][r] == 'b' and self.data[self.player[0]][r+1] == 4: return True
                if self.data[self.player[0]][r] == 4: break
        elif self.direction == 1:
            for r in range(self.player[1]-1, -1, -1):
                if self.data[self.player[0]][r] == 9: return True
                if self.data[self.player[0]][r] == 'b' and self.data[self.player[0]][r-1] == 4: return True
                if self.data[self.player[0]][r] == 4: break
        elif self.direction == 2:
            for c in range(self.player[0]-1, -1, -1):
                if self.data[c][self.player[1]] == 7: return True
                if self.data[c][self.player[1]] == 'b' and self.data[c-1][self.player[1]] == 4: return True
                if self.data[c][self.player[1]] == 4: break
        elif self.direction == 3:
            for c in range(self.player[0]+1, len(self.data)):
                if self.data[c][self.player[1]] == 8: return True
                if self.data[c][self.player[1]] == 'b' and self.data[c+1][self.player[1]] == 4: return True
                if self.data[c][self.player[1]] == 4: break

        return False


    def update(self):

        # end of game
        if self.direction == 0 and self.player[0] == 0: return True
        if self.direction == 1 and self.player[0] == len(self.data)-1: return True
        if self.direction == 2 and self.player[1] == 0: return True
        if self.direction == 3 and self.player[1] == len(self.data[0])-1: return True

        # movement
        if self.direction == 0:
            if self.data[self.player[0]-1][self.player[1]] == 4:
                self.data[self.player[0]][self.player[1]] = 'b'
                self.direction = 3
                self.player = (self.player[0], self.player[1]+1)
            else:
                if self.data[self.player[0]][self.player[1]+1] in ('a','b'): self.obstacles += 1
                elif self.check_cols_rows(): self.obstacles += 1
                self.data[self.player[0]][self.player[1]] = 7 if self.data[self.player[0]][self.player[1]] not in (9,'a') else 'b'
                self.player = (self.player[0]-1, self.player[1])
        elif self.direction == 1:
            if self.data[self.player[0]+1][self.player[1]] == 4:
                self.data[self.player[0]][self.player[1]] = 'b'
                self.direction = 2
                self.player = (self.player[0], self.player[1]-1)
            else:
                if self.data[self.player[0]][self.player[1]-1] in (9,'b'): self.obstacles += 1
                elif self.check_cols_rows(): self.obstacles += 1
                self.data[self.player[0]][self.player[1]] = 8 if self.data[self.player[0]][self.player[1]] not in (9,'a') else 'b'
                self.player = (self.player[0]+1, self.player[1])
        elif self.direction == 2:
            if self.data[self.player[0]][self.player[1]-1] == 4:
                self.data[self.player[0]][self.player[1]] = 'b'
                self.direction = 0
                self.player = (self.player[0]-1, self.player[1])
            else:
                if self.data[self.player[0]-1][self.player[1]] in (7,'b'): self.obstacles += 1
                elif self.check_cols_rows(): self.obstacles += 1
                self.data[self.player[0]][self.player[1]] = 9 if self.data[self.player[0]][self.player[1]] not in (7,8) else 'b'
                self.player = (self.player[0], self.player[1]-1)
        elif self.direction == 3:
            if self.data[self.player[0]][self.player[1]+1] == 4:
                self.data[self.player[0]][self.player[1]] = 'b'
                self.direction = 1
                self.player = (self.player[0]+1, self.player[1])
            else:
                if self.data[self.player[0]+1][self.player[1]] in (8,'b'): self.obstacles += 1
                elif self.check_cols_rows(): self.obstacles += 1
                self.data[self.player[0]][self.player[1]] = 'a' if self.data[self.player[0]][self.player[1]] not in (7,8) else 'b'
                self.player = (self.player[0], self.player[1]+1)

        if self.debug:
            self.draw()
            print(f"Obstacles: {self.obstacles}")
            input()

        return False

input("Press Enter to start simulation...")
E = Part2()
print(f"Guard has encountered {E.obstacles} obstacles.")
