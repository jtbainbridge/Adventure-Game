import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself in the lobby of a dark dingy dungeon, "
                "trying to escape.")
    print_pause("In front of you are three passageways.")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response
        print_pause("Sorry, I don't understand.")


def weapons_menu(items, weapon, beast):
    del weapon[:]
    weapon_select = valid_input("Pick up: (Enter number)\n"
                                "1. Sword\n"
                                "2. Crossbow\n"
                                "3. Spear\n"
                                "4. Axe \n", ["1", "2", "3", "4"])
    if "1" in weapon_select:
        weapon.append('sword')
        print_pause("You have taken the Sword.")
    elif "2" in weapon_select:
        weapon.append('Crossbow')
        print_pause("You have taken the Crossbow.")
    elif "3" in weapon_select:
        weapon.append('Spear')
        print_pause("You have taken the Spear.")
    elif "4" in weapon_select:
        weapon.append('Axe')
        print_pause("You have taken the Axe.")
    print_pause("Returning to the dungeon lobby.")
    main_menu(items, weapon, beast)


def attack(items, weapon, beast):
    health = 100
    print_pause(beast + " current health: " + str(health))
    for fight in range(2):
        damage = random.randint(30, 70)
        print_pause("\nHIT " + str(fight + 1))
        print_pause("Damage inflicted: " + str(damage))
        health = health - damage
    if health <= 0:
        print_pause("\nThe " + beast + " has been defeated.")
        print_pause("It looks like it was protecting a key. "
                    "You take the key.")
        items.append("key")
        print_pause("Returning to the dungeon lobby.")
        main_menu(items, weapon, beast)
    else:
        print_pause(beast + " remaining health: " + str(health))
        print_pause("Unfortunately, the " + beast +
                    " is too strong and defeated you.")
        print_pause("GAME OVER!")
        play_again()


# CONTAINS A WEAPONS CRATE
def center(items, weapon, beast):
    print_pause("You have decided to enter the center passageway.")
    if weapon != []:
        confirm = valid_input("Do you want to change your weapon? (y/n)\n",
                              ["y", "n"])
        if "y" in confirm:
            weapons_menu(items, weapon, beast)
        elif "n" in confirm:
            print_pause("Returning to the dungeon lobby.")
            main_menu(items, weapon, beast)
    else:
        print_pause("Looks like there is a weapons crate inside.")
        weapons_menu(items, weapon, beast)


# LOCATED INSIDE IS A KEY PROTECTED BY A BEAST. DEFEAT THE BEAST, GET THE KEY!
def left(items, weapon, beast):
    print_pause("You have decided to enter the left passageway.")
    if "key" in items:
        print_pause("You have already been in here and found a key.")
        print_pause("Returning to the dungeon lobby.")
        main_menu(items, weapon, beast)
    else:
        print_pause("Whats the noise? It sounds like a " + beast)
        print_pause("It is! And it looks like it is guarding something.")
        print_pause("Doesn't look like it will let you past without a fight.")
        attack_choice = valid_input("Do you want to attack? (y/n)\n",
                                    ["y", "n"])
        if attack_choice == "y":
            print_pause("You have courage!")
            if weapon != []:
                print_pause("Using your " + "".join(weapon) +
                            " you fight the " + beast + ".")
                attack(items, weapon, beast)
            else:
                print_pause("Without any weapons you fight "
                            "with your barehands.")
                print_pause("Unfortunately, the " + beast +
                            " is too strong and it defeats you.")
                print_pause("GAME OVER!")
                play_again()
        elif attack_choice == "n":
            print_pause("Wise move...")
            print_pause("Returning to the dungeon lobby.")
            main_menu(items, weapon, beast)


# CONTAINS A LOCKED DOOR TO ESCAPE
def right(items, weapon, beast):
    print_pause("You have decided to enter the right passageway.")
    print_pause("It looks like there is a big locked door in the way.")
    if "key" in items:
        print_pause("Hang on... You found a key earlier. Let's try it.")
        print_pause("Yes! The door has unlocked and "
                    "you have managed to esacape.")
        print_pause("Well done! GAME OVER")
        play_again()
    else:
        print_pause("Hmm. There must be a way to unlock the door!")
        print_pause("Try going down another passageway.")
        print_pause("You return to the dungeon lobby.")
        main_menu(items, weapon, beast)


def main_menu(items, weapon, beast):
    choice = valid_input("Enter 1 to head down the left passage.\n"
                         "Enter 2 to head down the right passage.\n"
                         "Enter 3 to head down the center passage.\n",
                         ["1", "2", "3"])
    if choice == '1':
        left(items, weapon, beast)
    elif choice == '2':
        right(items, weapon, beast)
    elif choice == '3':
        center(items, weapon, beast)


def play_again():
    restart = valid_input("\nWould you like to play again? (y/n):\n",
                          ["y", "n"])
    if restart == "y":
        print_pause("Great stuff! Resetting the game...\n\n")
        time.sleep(2)
        print("--NEW GAME--\n")
        play_game()
    elif restart == "n":
        print_pause("Thank you for playing. Goodbye.")


def play_game():
    items = []
    weapon = []
    beast = random.choice(['Dragon', 'Troll', 'Amarok'])
    intro()
    main_menu(items, weapon, beast)


play_game()
