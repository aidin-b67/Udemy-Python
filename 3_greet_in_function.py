def greet():
    print("Hello,")
    print("to my new functiion sample")
    print("Hope you enjoy it!")
greet()

def greet_with_name(name):
    print(f"Hello,{name}")
    print("to my new functiion sample")
    print("Hope you enjoy it!")

greet_with_name("Aidin")

def greet_with(name = input("What is your name?\n"),location = input("What is your location?\n")):
    print(f"Hello,{name}")
    print(f"to my new functiion sample in {location}")
    print("Hope you enjoy it!")
greet_with()
