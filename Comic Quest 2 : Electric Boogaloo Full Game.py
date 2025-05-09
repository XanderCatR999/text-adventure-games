print("""Welcome to Comic Quest 2: Electric Boogaloo! the sequal to Comic Quest: The Text Adventure!""")
print("""This is a Game By XanderCatR999 on Github.""")
print("""your goal is to get an autograph from Stan Lee via time travel.""")
print("""Context: you have found a working time machine in a comics shop's trash bin and have decided to get an autograph from Stan Lee""")

stan_lee_area = """on the board at the 2014 Phoenix Comicon"""
choice1 = input("""you have two time periods that the time machine supports: a one way trip to the '1990s' or a one way trip to '2014' which do you choose?""")

if choice1 == "1990s":
    print("""you go to the year of 1996 and find stan lee on the street heading towards an apartment.""")
    print(""" as you ask him for a autograph he declines and leaves. GAME OVER YOU FOUND THE WRONG PERSON""")
    exit()
elif choice1 == "2014":
    print("""you travel to the year 2014 and see that you are outside of the  2014 Phoenix Comicon!!!""")
elif choice1 == "idk":
    print("""you throw the time machine away and buy an autograph from ebay. ENDING 1 OF 2: STAN LEE'S AUTOGRAPH FROM EBAY""")
    print("""THX FOR PLAYING""")
    exit()
elif choice1== "both":
    print("""you decide to try doing both""")
    print("""you go to NYC in the 1990s and get an autograph from the real stan lee.""")
    print("""then you go to 2014 at the Phoenix Comicon on July 8th and get a second autograph. SECRET ENDING!!! The Thinker...""")
    print("""THX FOR PLAYING""")
    exit()
else:
    print("""INVALID OPTION TRY '1990s' OR '2014' """)
    exit()

choice2 = input("""As You check a newspaper you see that it is July 7th 2014. Do you go to 'Comicon' or rent a 'room' at a hotel?   :   """)

if choice2 == 'room':
    print("""you go to bed and wake up at 8:00 AM on July 8th.""")
elif choice2 == 'Comicon':
    print("""As you exit Comicon you realize that you have 19 cents to your name. GAME OVER : YOU HAVE NO MONEY              """)
    exit()
else:
    print("""INVALID OPTION TRY 'Comicon' OR 'room' """)
    exit()

choice3 = input("""as you wake up on July 8th and realize that stan lee is at the Comicon today do you goto a 'writer's board' or the 'floor' of Comicon?""")

if choice3 == "writer's board":
    print(f"""'you see that stan lee is {stan_lee_area} and ask him for an autograph. ENDING 2 of 2 :  GOOD ENDING STAN LEE'S AUTOGRAPH FRENZY""")
    print("""THX FOR PLAYING""")
elif choice3 == "floor":
    print("""GAME OVER YOU MISSED STAN LEE AT THE WRITER'S BOARD""")
    exit()
else:
    print("""INVALID OPTION TRY 'writer's board' or 'floor'""")
    exit()
















