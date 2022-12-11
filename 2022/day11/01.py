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

    def take_turn(self, all_monkeys):
        current_items = self.items
        current_items.reverse()

        while len(current_items) > 0:
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

    def status(self):
        print('Monkey', self.num, ':', self.items)
        

# input
monkeys = []
monkeys.append(Monkey(0, [79, 98], ['old', 'mult', 19], 23, 2, 3))
monkeys.append(Monkey(1, [54, 65, 75, 74], ['old', 'add', 6], 19, 2, 0))
monkeys.append(Monkey(2, [79, 60, 97], ['old', 'mult', 'old'], 13, 1, 3))
monkeys.append(Monkey(3, [74], ['old', 'add', 3], 17, 0, 1))

# run program

monkeys[0].take_turn(monkeys)
monkeys[1].take_turn(monkeys)
monkeys[2].take_turn(monkeys)
monkeys[3].take_turn(monkeys)

for monkey in monkeys:
    monkey.status()

