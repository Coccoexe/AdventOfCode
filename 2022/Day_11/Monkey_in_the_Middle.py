import os, copy
print("Advent of Code 2022 - Day 11")
print("Monkey in the Middle")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

class Monkey:
    
    def __init__(self,items,operation,test,throw):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw = throw
        
    def __str__(self):
        s = ''
        s += 'Items: ' + str(self.items) + '\n'
        s += 'Operation: ' + str(self.operation) + '\n'
        s += 'Test: ' + str(self.test) + '\n'
        s += 'Throw: ' + str(self.throw) + '\n'
        return s
    
    def get_items(self):
        return self.items

def operations(a,b,operation):
    if b == 'old':
        b = a
    else:
        b = int(b)
    
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b

def cycle(dividing = True):
    global inspected
    
    modulo = 1
    for monkey in monkeys:
        modulo *= int(monkey.test)
    
    for monkey in monkeys:
        inspected[monkeys.index(monkey)] += len(monkey.items)
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            item = operations(item,monkey.operation[1],monkey.operation[0])
            if dividing:
                item = item//3
            else:
                item %= modulo
                #item = item - (item//int(monkey.test) * int(monkey.test))  
            if item % int(monkey.test) == 0:
                monkeys[int(monkey.throw[0])].items.append(item)
            else:
                monkeys[int(monkey.throw[1])].items.append(item)

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.strip() for line in file.read().splitlines()]
file.close()

monkeys = []

#parsing
for i in range(5,len(lines),+7):
    items = [int(item) for item in lines[i-4].split(': ')[1].split(', ')]
    operation = lines[i-3].split('old ')[1].split(' ')
    test = lines[i-2].split('by ')[1]
    throw = [lines[i-1].split('to monkey ')[1],lines[i].split('to monkey ')[1]]
    monkeys.append(Monkey(items,operation,test,throw))
    
#backup of monkeys
monkeys2 = copy.deepcopy(monkeys)

inspected = [0 for i in range(len(monkeys))]            
for i in range(20):
    cycle()

inspected.sort()
reslut = inspected[-1]*inspected[-2]
print("The level of monkey business is: " + str(reslut))
print()

print("--- Part 2 ---")

monkeys = copy.deepcopy(monkeys2)

inspected = [0 for i in range(len(monkeys))]            
for i in range(10000):
    cycle(dividing=False)

inspected.sort()
reslut = inspected[-1]*inspected[-2]
print("The level of monkey business is: " + str(reslut))
print()