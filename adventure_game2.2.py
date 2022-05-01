import time
import random


weapon = ("Shiny-bat", " sword", "nunchaku", "battle-ax")
s = random.choice(weapon)


def print_time(message, pause=0):
    print(message)
    time.sleep(pause)


def valid_input(prompt, options):
    output = input(prompt)
    if output not in options:
        print_time("Wrong choice, please try again")
        return valid_input(prompt, options)
    return output


def intro():
    print()
    print()
    print()
    print("     #########################")
    print("     #                       #")
    print("     #      CROSS ROADS      #")
    print("     #                       #")
    print("     #########################")
    print()
    print()
    name = input("\nHello what is your name?\n")
    print("Hello", name, "!")
    while True:
        startgame = valid_input("Do you want to play a game? (Yes or No)\n",
                                ["yes", "no"]).lower()
        if "no" == startgame:
            print("Sorry to hear that. GAME OVER!!")
            exit()
        elif "yes" == startgame:
            game_start()


def game_start():
    print_time("IT HAS BEGUN!\n")
    print_time("It's 10 pm and you found yourself on a long dark\n"
               "road in the counrty.")
    print_time("Your car is making strange noises before the"
               " engine\nsuddenly stops.")
    print_time("Your stuck on the side of the road in the dark.\n\n")
    print_time("What would you like to do?")
    print_time("1. Stay in the car\n"
               "2. Get out of the car")
    destiny1 = valid_input("Choose your destiny", ["1", "2"])
    if "1" == destiny1:
        print_time("")
        course_1()
    elif "2" == destiny1:
        course_2()
    else:
        print_time("You had one job and failed! Enter 1 or 2.\n")
        print_time("What would you like to do?")
        print_time("1. Stay in the car\n"
                   "2. Get out of the car")
        print_time("Choose your destiny")
        print("Oh no thats not right. Let's try this again from"
              "   the beginning.\n")


def course_1():
    print_time("Your in the car and you remembered that you have a")
    print_time("cell phone. You picked up the cell phone to call\nfor help"
               " and realize you have no signal.\n")
    print_time("What would you like to do?")
    print_time("1. Stay in the car\n"
               "2. Get out of the car")
    print_time("Choose your destiny")
    while True:
        destiny1 = input("")
        if "1" == destiny1:
            print_time("")
            course_1()
        elif "2" == destiny1:
            print_time("")
            course_2()
        else:
            print_time("")
            print_time("You had one job and failed! Enter 1 or 2.\n")
            print_time("What would you like to do?")
            print_time("1. Stay in the car\n"
                       "2. Get out of the car")
            print_time("Choose your destiny")


def course_2():
    print_time("Its very dark outside but you have no choice but to\nwalk.")
    print_time("As you begin walking you notice the faint glow of a\nstreet"
               "light.")
    print_time("You head towards the light for fear of what might\nbe"
               " lurking in the dark.")
    print_time("Your getting closer and the light is getting\nbrighter.")
    print_time("You can see what looks like a pay phone.")
    print_time("Relieved you hastened your pace to reach the light and"
               " the pay phone.")
    print_time("When you finally arrive at the pay phone you\nnoticed a"
               " well dressed man standing on the other\nside smoking a"
               " cigarette.\n")
    print_time("What would you like to do?")
    print_time("1.Use the pay phone\n"
               "2 Talk to the strange well dressed man")
    print_time("Choose your destiny")
    while True:
        destiny2 = input("")
        if "1" == destiny2:
            print_time("")
            course_3()
        elif "2" == destiny2:
            print_time("")
            course_4()
        else:
            print_time("")
            print_time("You had one job and failed! Enter 1 or 2.\n")
            print_time("What would you like to do?")
            print_time("1.Use the pay phone\n"
                       "2 Talk to the strange well dressed man")
            print_time("Choose your destiny")


def course_3():
    print_time("As your putting the quarter in the pay phone you\n noticed"
               " the strange well dressed man has turned to\n your direction.")
    print_time("Quickly you begin dialing the number for a tow\n truck"
               " to help.")
    print_time("Then realized the phone is currently out of order.")
    print_time("Frustrated and scared you turn towards the strange"
               " man who seemed to be looking at you.\n")
    print_time("What would you like to do?")
    print_time("1.Use the pay phone\n"
               "2 Talk to the strange well dressed man")
    print_time("Choose your destiny 1 or 2")


def course_4():
    print_time("Hey! you said to the man. He replied in a voice\n"
               "that seemed demonic.")
    print_time("Help you can I, Said the strange man as The"
               " Seagull song began to play in the bacKground. THATS WEIRD"
               "  You could not make out his face.")
    print_time("He seemed to glide across the ground closer to you"
               " making a noise like the Predator from the movies.")
    print_time("You said to him, how far and in which direction is"
               " the closest town.")
    print_time("My car is not working and I need to call a tow\n truck.")
    print_time("The Strange well dressed man said.")
    print_time("Demon of crossroad I am, here to make"
               " deal I will, the Demon said in this weird Yoda voice.")
    print_time("New car for you, your Soul for me.")
    print_time("Startled realizing what the man was, you turned to run"
               "away but realized your in the middle of\n nowhere"
               " and he can glide.")
    print_time("Thinking to yourself, he has a car and all he wants is"
               " your soul.")
    print_time("Out of the corner of your eye you see the glint"
               " of a " + s + '.\n')
    print_time("What would you like to do?")
    print_time("1 Agree to the deal.\n"
               "2 Dash towards the " + s + ".")
    print_time("Choose your destiny")
    while True:
        destiny3 = input("")
        if "1" == destiny3:
            print_time("")
            course_5()
        elif "2" == destiny3:
            print_time("")
            course_6()
        else:
            print_time("")
            print_time("You had one job and failed! Enter 1 or 2.\n")
            print_time("What would you like to do?")
            print_time("1 Agree to the deal.\n"
                       "2 Dash towards the " + s + ".")
            print_time("Choose your destiny")


def course_5():
    print_time("You can have my soul for the car. What do I need a soul"
               " for anyway.")
    print_time("I'm not currently using it, and I need to get to\n town.")
    print_time("With one quick touch on the forehead.")
    print_time("YOU DIED!!!. If you choose this path again then you are"
               " doomed to repeat this mistake FOR EVER!!!!")
    print_time("The body can't live with out a soul.")
    print_time("What would you like to do?")
    print_time("1 Agree to the deal.\n"
               "2 Dash towards the " + s + ".")
    print_time("Choose your destiny")


def course_6():
    print_time("You look down and realized that your standing on a land mine.")
    print_time("With every ounce of strength you have, you leap off the land"
               "mind towards the " + s + ".")
    print_time("BOOM! goes the land mine wounding the Demon.")
    print_time("The Demon shrieks AHHHHHHH!!!!! MINE YOUR SOUL IS\n Yelled"
               " the Demon!!")
    print_time("You grab the " + s + " and with one very hard swing you"
               " chop off the Demon's head.")
    print_time("The Demon hits the ground and you search his\n pockets.")
    print_time("Excited, you find the keys to the car and drive off to town.")
    print_time("YOU WIN\n")
    play_again()


def play_again():
    print_time("Do you want to play again?")
    play_again = valid_input("Enter Yes or No:", ["yes", "no"]).lower()
    if "yes" == play_again:
        global s
        s = random.choice(weapon)
        intro()
    if "no" == play_again:
        print_time("GAME OVER")
        exit()
    else:
        print_time("")
        print_time("You had one job and failed! Enter yes or no.\n")
        print_time("What would you like to do?")


def adventure_game2():
    print_time("", pause=0)
    intro()


adventure_game2()
