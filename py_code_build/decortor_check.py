def decor(func):
    def wrapper():
        print("wrapping started")
        func()
        print("wrapping finished")
    return wrapper

@decor
def greet():
    print("hello")

greet()