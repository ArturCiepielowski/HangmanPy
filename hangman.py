import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, 2)]

guess = input("Guess a letter\n").lower()

print(chosen_word)

display = []
for y in range(len(chosen_word)):
    display.append("_")
    # print(y)


for x, z in enumerate(chosen_word):
    # print(x)
    if z == guess:
        display[x] = guess


print(display)
