# class Data:
#     def __init__(self, *info):
#         self.info = list(info)
#
#     def __getitem__(self, i):
#         return self.info[i]
#
#     def __str__(self):
#         return self.info[0]
#
#
# class Teacher:
#     def __init__(self):
#         self.work = 0
#
#     def teach(self, info, *pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1
#
#
# class Pupil:
#     def __init__(self):
#         self.knowledge = []
#
#     def take(self, info):
#         self.knowledge.append(info)
#
#
# data = Data('qwe', 'sfd', 'asd')
# data2 = Data('sfd', 'fgh', 'djn')
# teacher = Teacher
# pupil1 = Pupil()
# pupil2 = Pupil()
# for i in [data, data2]:
#     teacher.teach(i, pupil1, pupil2)


class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.value = width * height

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        if self.value >= other.value:
            return self.value - other.value
        else:
            raise ArithmeticError

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.value != other.value


class Rectangle:
    def __init__(self, width, height, color='black'):
        self.area = Area(width, height)
        self.color = color

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        if self.area >= other.area:
            return self.area - other.area
        else:
            raise ArithmeticError

    def __eq__(self, other):
        return self.area == other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __ne__(self, other):
        return self.area != other.area


r1 = Rectangle(12, 5)
r2 = Rectangle(3, 4)
r3 = Rectangle(3, 4)
print(f'r1 + r2 ----> {r1 + r2}')
print(f'r1 - r2 ----> {r1 - r2}')
print(f'r1 == r2 ----> {r1 == r2}')
print(f'r2 == r3 ----> {r2 == r3}')
print(f'r1 > r2 ---->{r1 > r2}')
print(f'r1 >= r2 ---->{r1 >= r2}')
print(f'r1 < r2 ---->{r1 < r2}')
print(f'r1 <= r2 ---->{r1 <= r2}')
print(f'r1 != r2 ---->{r1 != r2}')
