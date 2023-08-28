#functions with output

def format_name():
    return input("What is your name? ").capitalize()
def format_last():
    return input("What is your last name? ").capitalize()

f_name = format_name()
l_name = format_last()

print(f_name + " " + l_name)