from datetime import datetime

TREES_NUMBER = 100000


def getEfficiency(fruit):
    def outer(method):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            loot = method(*args, **kwargs)
            print(f'Robot spent {datetime.now() - start} time collecting {fruit}.')
            return loot
        return wrapper
    return outer


class Robot:
    def __init__(self, name):
        self.name = name

    @getEfficiency('apples')
    def collectApples(self):
        loot = [x for x in range(TREES_NUMBER) if x % 3 != 0]
        return loot

    @getEfficiency('grapes')
    def collectGrapes(self):
        loot = [x for x in range(TREES_NUMBER) if x % 12 != 0]
        return loot

    @getEfficiency('oranges')
    def collectOranges(self):
        loot = [x for x in range(TREES_NUMBER) if x % 6 != 0]
        return loot


lootie = Robot('Lootie')
collectedApples = lootie.collectApples()
collectedGrapes = lootie.collectGrapes()
collectedOranges = lootie.collectOranges()

def checkIfArgumentsAreIntegers(function):
    def wrapper(*args, **kwargs):
        # args = [self, num1, num2]
        if not isinstance(args[1], int) or not isinstance(args[2], int):
            print("This is not correct question! Give Lootie 2 integers!")
            raise TypeError('Arguments must be integers.')
        return function(*args, **kwargs)
    return wrapper


def check_second_argument(function):
    def wrapper(*args, **kwargs):
        if args[2] == 0:
            raise ZeroDivisionError('На ноль делить нельзя!')
        else:
            return function(*args, **kwargs)
    return wrapper


class Robot:
    def __init__(self, name):
        self.name = name

    @checkIfArgumentsAreIntegers
    def add(self, num1, num2):
        return num1 + num2

    @checkIfArgumentsAreIntegers
    def subtract(self, num1, num2):
        return num1 - num2

    @check_second_argument
    @checkIfArgumentsAreIntegers
    def divide(self, num1, num2):
        return num1 / num2

    @checkIfArgumentsAreIntegers
    def multiply(self, num1, num2):
        return num1 * num2


lootie = Robot('Lootie')
print(lootie.add(1, 5))
print(lootie.subtract(5, 3))
print(lootie.divide(4, 2))
# print(lootie.divide(4, 0))
print(lootie.multiply("Lootie", "the Robot"))
