#ES
def decorator(func):
    def wrapper():
        print("Hi")
        func()
        print("hurry up")
    return wrapper

@decorator
def greet():
    print("bru")
greet()

@decorator
def add():
    print(6+7)
add()