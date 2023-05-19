local_var = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"


print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)

