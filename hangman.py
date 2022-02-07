import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, 2)]

display = []
for y in range(len(chosen_word)):
    display.append("_")
    # print(y)

print(display)

for letter in display:
    if letter == "_":




guess = input("Guess a letter\n").lower()




for x, z in enumerate(chosen_word):
    # print(x)
    if z == guess:
        display[x] = guess
