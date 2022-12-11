import math

class Monkey:
    def __init__(self, num, items, operation, test, true, false):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.value = 0
        self.inspections = 0

    def take_turn(self, all_monkeys):
        current_items = self.items
        current_items.reverse()

        while len(current_items) > 0:
            self.inspections += 1
            item = current_items.pop()
            worry = self.operate(item)

            worry = math.floor(worry / 3)

            if worry % self.test == 0:
                # give to monkey monkeys[true]
                all_monkeys[self.true].receive(worry)
            else:
                # give to monkeys[false]
                all_monkeys[self.false].receive(worry)

        self.items = []

    def operate(self, item):
        a = item if self.operation[0] == 'old' else int(self.operation[0])
        b = item if self.operation[2] == 'old' else int(self.operation[2])

        operator = self.operation[1]

        if operator == 'add':
            worry = a + b
        if operator == 'mult':
            worry = a * b

        self.value = worry

        return worry


    def receive(self, item):
        self.items.append(item)

    def getNumInspections(self):
        return self.inspections


    def status(self):
        print('Monkey', self.num, ':', self.items, self.inspections)
        

# input
test_monkeys = []
test_monkeys.append(Monkey(0, [79, 98], ['old', 'mult', 19], 23, 2, 3))
test_monkeys.append(Monkey(1, [54, 65, 75, 74], ['old', 'add', 6], 19, 2, 0))
test_monkeys.append(Monkey(2, [79, 60, 97], ['old', 'mult', 'old'], 13, 1, 3))
test_monkeys.append(Monkey(3, [74], ['old', 'add', 3], 17, 0, 1))

monkeys = []

monkeys.append(Monkey(0, [83, 97, 95, 67], ['old', 'mult', 19], 17, 2, 7))
monkeys.append(Monkey(1, [71, 70, 79, 88, 56, 70], ['old', 'add', 2], 19, 7, 0))
monkeys.append(Monkey(2, [98, 51, 51, 63, 80, 85, 84, 95], ['old', 'add', 7], 7, 4, 3))
monkeys.append(Monkey(3, [77, 90, 82, 80, 79], ['old', 'add', 1], 11, 6, 4))
monkeys.append(Monkey(4, [68], ['old', 'mult', 5], 13, 6, 5))
monkeys.append(Monkey(5, [60, 94], ['old', 'add', 5], 3, 1, 0))
monkeys.append(Monkey(6, [81, 51, 85], ['old', 'mult', 'old'], 5, 5, 1))
monkeys.append(Monkey(7, [98, 81, 63, 65, 84, 71, 84], ['old', 'add', 3], 2, 2, 3))


# run program

rounds = 0
while rounds < 20:
    monkeys[0].take_turn(monkeys)
    monkeys[1].take_turn(monkeys)
    monkeys[2].take_turn(monkeys)
    monkeys[3].take_turn(monkeys)
    monkeys[4].take_turn(monkeys)
    monkeys[5].take_turn(monkeys)
    monkeys[6].take_turn(monkeys)
    monkeys[7].take_turn(monkeys)

    rounds += 1


total_inspections = []
for monkey in monkeys:
    monkey.status()
    total_inspections.append(monkey.getNumInspections())

total_inspections.sort(reverse=True)

total_inspections = total_inspections[0:2]

print(math.prod(total_inspections))
