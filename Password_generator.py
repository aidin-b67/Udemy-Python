#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:


#get random letter by creating loop
random_letters = []
for letter in range(nr_letters):
    random_letters.append(random.choice(letters))

print(random_letters)

#get random symbols by creating loop
random_symbols = []
for symbol in range(0, nr_symbols):
    random_symbols.append(random.choice(symbols))
print(random_symbols)
#get random numbers by creating loop for lenght user_input
random_numbers = []
for number in range(0, nr_numbers):
    random_numbers.append(random.choice(numbers))
print(random_numbers)

generated_password_not_random = random_letters + random_symbols + random_numbers
lenght_generated_password_not_random = len(generated_password_not_random)

print(*(generated_password_not_random), sep="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(generated_password_not_random)
print('You password is: ', end="")
print(*(generated_password_not_random), sep="")

# generated_random_pass = []
# for password in range(0, lenght_generated_password_not_random):
#   generated_random_pass.append(random.choice(generated_password_not_random))
# print(*generated_random_pass)
