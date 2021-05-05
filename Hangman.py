import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
attempt = 8

rand_num = random.randint(0, len(words)-1)

guess = words[rand_num]
show_guess = "-" * len(guess)
prev_guess = list()

keep_ask = True

while keep_ask:
    print('Type "play" to play the game, "exit" to quit:>')
    user_choice = input()
    if user_choice == "play":
        while attempt > 0:
            print()
            print(show_guess)
            if show_guess == guess:
                print("You guessed the word!")
                print("You survived!")
                break
            print("Input a letter:>")
            user_input = input()
            if len(user_input) != 1:
                print("You should input a single letter")
                continue
            if user_input.isupper() or not user_input.isalpha():
                print("Please enter a lowercase English letter")
                continue
            if user_input in prev_guess:
                print("You've already guessed this letter")
                continue
            else:
                prev_guess.append(user_input)
            if user_input in guess:
                for index, elem in enumerate(guess):
                    if elem == user_input:
                        show_guess = show_guess[:index] + user_input + show_guess[index + 1:]

            else:
                print("That letter doesn't appear in the word")
                attempt -= 1

        if attempt == 0 and show_guess != guess:
            print("You lost!")
            quit()
    if user_choice == "exit":
        keep_ask = False
        quit()