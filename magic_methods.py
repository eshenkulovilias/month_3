# class Test:
#     def __init__(self, name, num1, num2):
#         self.name = name
#         self.num1 = num1
#         self.num2 = num2
#
#     def __add__(self, other):
#         return self.num1 + self.num2 + other
#
#     def __str__(self):
#         return self.name
#
#
# t = Test('test1', 12, 5)
# print(t + 6)
# print(t)


class Phone:
    def __init__(self, name):
        self.name = name

    def __call__(self, new_name):
        self.name = new_name


a = Phone('qwe')
print(a.name)
a('rty')
print(a.name)
