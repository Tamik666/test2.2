def my_decorator(func):
    def wrapper():
        print("******")
        func()
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

say_hello()
