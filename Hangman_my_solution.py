import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
char = 0
chosen_word_list = []
for char in range(len(chosen_word)):
    chosen_word_list.append(chosen_word[char])
print(chosen_word_list)
print(chosen_word_list[0])
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in range(len(chosen_word_list)):
     
     if chosen_word_list[letter] == guess :
        print("Right")
    
     else:
        print("Wrong")