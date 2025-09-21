import sys

def choices():
    print('"You have decided to find computer components in order to build a PC.')
    choice_1 = input("""Do you browse 'Ebay' or 'Amazon'?""")
    if choice_1 == 'Ebay':
        print("You Find a AMD Ryzen 9950x3d for 500 Dollars. However you end up getting scammed.")
        with open("Fails.txt", "a") as file:
            file.write("You Got Scammed On Ebay. \n")
        sys.exit("""GAME OVER""")
    elif choice_1 == 'Amazon':
        print("""You find an AMD Ryzen 9950x3d and Buy it for 699.99. """)
    else:
        sys.exit("INVALID ANSWER")
    choice_2 = input("""do you buy the '5090' or the '5080' Super?""")
    if choice_2 == '5090':
        print("You ended up getting a 5090.")
    elif choice_2 == '5080':
        print('You get scammed since the 5080 Super has not released')
        with open('Fails.txt', "a") as file:
            file.write("You Got scammed from buying a 5080 Super. \n")
        sys.exit("""GAME OVER""")
    else:
        sys.exit("INVALID ANSWER")
    choice_3 = input("What power supply do you get, the '1000' Watt or the '650' Watt power supply?")
    if choice_3 == '1000':
        print("""you get the 1000 watt power supply""")
    elif choice_3 == '650':
        print("""You get an under powered power supply.""")
        with open('Fails.txt', 'a') as file:
            file.write("You got an under powered power supply. \n")
        sys.exit("""GAME OVER""")
    else:
        sys.exit("INVALID ANSWER")
    choice_4 = input("""Now you need to choose an 'aio' or a 'fan' cooler""")
    if choice_4 == 'aio':
        print("""You decide to go with an AIO cooler.""")
    elif choice_4 == 'fan':
        print('You put a under powered fan with a powerful cpu.')
        with open("Fails.txt", 'a') as file:
            file.write("""You put a under powered fan with a powerful cpu.\n""")
        sys.exit('GAME OVER')
    else:
        sys.exit("INVALID ANSWER")
    choice_5 = input("""do you get a 'AM4' or an 'AM5' Motherboard?""")
    if choice_5 == 'AM5':
        print("""you chose the correct the mobo""")
    elif choice_5 == 'AM4':
        print("""You chose the incorrect mobo""")
        with open("Fails.txt", 'a') as file:
            file.write("You chose the incorrect mobo \n")
        sys.exit("""GAME OVER""")
    else:
        sys.exit("INVALID ANSWER")
    choice_6 = input("""do you 'hire' someone to build the pc or do you it 'yourself'""")
    if choice_6 == 'hire':
        print("You Hire someone at MicroCenter to build for you. GOOD ENDING")
        with open("Endings.txt", 'a') as file:
            file.write("""GOOD ENDING \n""")
        sys.exit("""THE END""")
    elif choice_6 == 'yourself':
        print("""You attempt to build it yourself and break the mobo""")
        with open("Endings.txt", 'a') as file:
            file.write("""BAD ENDING \n""")
        sys.exit("""THE END""")


start = input("""if you want to start, type 'start' if not type 'exit' :    """)

if start == 'start':
    choices()
elif start == 'exit' or 'Exit':
    sys.exit()
else:
    sys.exit('INVALID ANSWER')