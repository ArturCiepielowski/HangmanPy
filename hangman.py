import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, 2)]

guess = input("Guess a letter\n").lower()

print(chosen_word)

if guess in chosen_word:
    print("Yes")

else:
    print("No")
