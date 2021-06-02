class CharField:
    def __init__(self, char, max_length):
        self.char = char
        self.max_length = max_length

    def __str__(self):
        return self.char


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


class Post:
    def __init__(self, title, body, author):
        self.title = CharField(title, 10)
        self.body = CharField(body, 140)
        self.author = author

    def __str__(self):
        return f'Author: {self.author}\nTitle: {self.title}\n{self.body}'


user = User('John', 18)
post = Post('Welcome!', 'Hi, my name is John.', user)
print(post)
