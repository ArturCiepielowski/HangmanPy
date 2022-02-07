import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, 2)]

guess = input("Guess a letter\n").lower()

print(chosen_word)
splitWord = list(chosen_word)
print(splitWord)

for x in splitWord:
    if x == guess:
        print("Right")
    else:
        print("Wrong")

# if guess in list(chosen_word):
#   print("Yes")

# else:
# print("No")
