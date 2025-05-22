import random
words= ("apple","banana","coconut","orange","pineapple")
#dictionary
hang_man = {0:("      ",
               "      ",
               "      "),

            1:("   o  ",
               "      ",
               "      "),


            2:("   o   ",
               "   |   ",
               "       "),

            3:("   o    ",
               "  /|    ",
               "        "),

            4:("   o    ",
               "  /|\\  ",
               "        "),

            5:("   o    ",
               "  /|\\  ",
               "  /     "),


            6:("   o    ",
               "  /|\\  ",
               "  / \\  ")}
def display_man(wrong_guesses):
    print("****************")
    for line in hang_man[wrong_guesses]:
        print(line)
    print("****************")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint= ["_"]*len(answer)
    wrong_guesses=0
    avoid_duplicate=set()
    max_attempt=6

    while True:

        display_hint(hint)
        display_man(wrong_guesses)


        guess=input("enter a letter to guess words:").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("______________________________________")
            print("invalid.don't guess with random number")
            print("______________________________________")
            continue


        if guess in avoid_duplicate:
            print("you have already entered guess.try differently")
            continue


        avoid_duplicate.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses +=1
            print("Wrong guess.try again")


        if "_" not in hint:
            print(f"you guessed correct answer.the answer was:{answer}")
            break


        if wrong_guesses >= max_attempt:
            print("You've run out of attempts! You lost the game.")
            display_answer(answer)
            break

if __name__=="__main__":
    main()
