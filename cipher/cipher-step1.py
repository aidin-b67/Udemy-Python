alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
x = alphabet[:len(alphabet)-1]
print(x)
y=alphabet[len(alphabet)-1:]
print(y)
y.extend(x)

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# Wrote the pattern of code just need to define function
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift = int(input("Type the shift number:\n"))
text = input("Type your message:\n").lower()
print(text)
x = alphabet[:len(alphabet)-shift]

y = alphabet[len(alphabet)-shift:]

y.extend(x)


new_word=[]
print(alphabet)
print(y)
for letter in text:
  index = alphabet.index(letter)
  new_word . append(y[index])
print(*new_word)

#wrote the code just need to define function for it
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift = int(input("Type the shift number:\n"))
text = input("Type your message:\n").lower()
print(text)
x = alphabet[:len(alphabet)-shift]

y = alphabet[len(alphabet)-shift:]

y.extend(x)


new_word=[]
print(alphabet)
print(y)
for letter in text:
  index = alphabet.index(letter)
  new_word . append(y[index])
print(*new_word)