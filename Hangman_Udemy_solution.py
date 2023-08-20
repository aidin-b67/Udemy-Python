#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display =[]
word_length = len(chosen_word)
for _ in chosen_word:
    display.append("_")
print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

end_of_game = False
while  not end_of_game:
    guess = input("Guess a letter: ").lower()
 

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# for step 2 we change above to the following to find position of the letter

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won")
