print(""" hello this is Xander an this text adventure game is dedicated to My Dad who has 53,000 comic give or take""")
print("""Warning: This is unfinished and a free version""")
print("""GAME BY XANDERCATR999 or simply XANDER""")
print("""welcome to Comic Quest (TM) (C) : The Text Adventure.""")
print("""Your Goal is to find the holy grail of holy grails:  Action Comics #1, the first appearance of Superman!!!!""")
print("""However it will be a difficult journey with lots of other comic enthusiasts!!!""")
print("""You must fight your way through many other like minded individuals!""")
print("""it will start very soon!!!""")
comic_holy_grail_1 = 'Action Comics #1'
comic_holy_grail_2 = 'Action Comics #27'
choice1 = input("""as you leave your somehow acquired house you see a estate sale two houses down and a yard sale two house down the other way do you go to the 'estate' sale or the 'yard' sale? :   """)
pummel_damage = '0 damage'
magic_damage = 'you cast the rage of a thousand comic collectors and deal 1,870,000,000 damage!'


if choice1 == 'yard':
    print(f"""you see that there is a {comic_holy_grail_2} in pristine condition, however you already have that comic from your late father, who was a comic writer. and you do not see {comic_holy_grail_1}.""")
elif choice1 == 'estate':
    print(f"""as you walk to the estate sale you get mugged by other comic enthusiasts. GAME OVER: YOU LOST YOUR OTHER HOLY GRAIL: {comic_holy_grail_2}.     :(""")
    exit()
else:
    print("""INVALID CHOICE TRY 'yard' or 'estate'""")
    exit()

choice2 = input("""as you walk away from the yard sale you see a comic shop that you have never been in somehow. Do you go in? 'yes' or 'no'?""")

if choice2 == 'yes':
    print("""you walk in and see that they have overpriced comics and before you can do anything you walk out with $13,000 worth of comics from there which are worth at market value are $50. GAME OVER YOU LOST YOUR LIFE'S SAVINGS.""")
    exit()
elif choice2 == 'no':
    print("""before you go in you use some binoculars to investigate the prices on the comics and see that they are massively over priced and bad quality comics. you decide to not go in.""")
else:
    print("""INVALID CHOICE TRY 'yes' OR 'no' """)
    exit()

choice3 = input("""as you walk away from the comic shop you bump in to someone. as you walk away you notice that you are missing your copy of {comic_holy_grail_2}. Do you chase after the person you bumped into? 'yes' or  'no'?""")

if choice3 == 'yes':
    print("""you catch up to the person you bumped into and realize that he is a notorious comic stealer in your community.""")
elif choice3 == 'no':
    print("""you decide not to chase after the person you bumped into and end up losing $1,870,000 from your comic being stolen. GAME OVER : YOU LOST YOUR OTHER HOLY GRAIL: {comic_holy_grail_2}""")
    exit()
else:
    print("""INVALID CHOICE TRY 'yes' OR 'no' """)
    exit()

choice4 = input("""you engage in a comic fight with 'Bob the comic baron'. do you 'pummel', cast 'magic', or 'run'? """)

if choice4 == 'pummel':
    print(f"""you punch Bob The Comic Baron with all your might but break your hand and deal{pummel_damage}. then bob attacks dealing 1 damage. you have failed. GAME OVER : YOU LOST YOUR OTHER HOLY GRAIL: {comic_holy_grail_2}""")
    exit()
elif choice4 == 'magic':
    print(f"""{magic_damage} thus beating Bob The Comic Baron. You Earned 1 experience!!!! you are 1,869,999 exp from leveling up!!! :)""")
elif choice4 == 'run':
    print("""you run from Bob The Comic Baron but without your late fathers favourite comic book. GAME OVER : YOU LOST YOUR OTHER HOLY GRAIL: {comic_holy_grail_2}""")
    exit()
else:
    print("""INVALID CHOICE TRY 'pummel', 'magic', or 'run'.""")
    exit()

print("""hello this is the end of the demo sorry about that but you can recive the full game if you email 'xanderrowland2011@gmail.com' you might get full access""")
