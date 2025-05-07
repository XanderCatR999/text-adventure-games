import os
import time

# Setup Functions, Sets up the game.

# just intializes some variables.
# In Lua, require can load libraries. We'll simulate the 'computer' library
# with a dummy class as its actual implementation is external to the provided code.
class Computer:
    def beep(self, frequency, duration):
        # This simulates the beep function call structure.
        # Actual sound output requires platform-specific libraries or external commands,
        # which are not part of the original Lua code provided.
        # print(f"Simulating beep: freq={frequency}, duration={duration}")
        pass # Do nothing to avoid external dependencies/assumptions

    def shutdown(self, force):
        # This simulates the shutdown function call structure.
        # Actual system shutdown requires platform-specific calls,
        # which are not part of the original Lua code provided.
        # print(f"Simulating computer shutdown: force={force}")
        pass # Do nothing to avoid external dependencies/assumptions

computer = Computer()

# Global variables
mr = 0
ln = 0
end1 = 0
end2 = 0
end3 = 0
booted = 0 # Initialize booted as 0

# Checks if the game has been played before.
# The original Lua code checks if booted ~= 1, which is true if booted is nil or 0.
# Since we initialize booted to 0, this block will run on the first execution.
if booted != 1:
    end1 = 0
    end2 = 0
    end3 = 0
    booted = 1

def Intro():
    # This is the bit that adds the intro.
    print("Max Rowland (C)opyright 2025")

    print("ZORKOID")

def sleep(n):
    # This pauses the code without the use of an external API.
    # Using time.sleep is the standard Python way.
    # The original uses os.execute("sleep ..."), which is platform-dependent.
    # time.sleep is a more portable equivalent in Python.
    # tonumber(n) is handled by Python's float conversion for time.sleep.
    time.sleep(float(n))

def EndMelody01():
    # This is the end melody of ending 1.
    computer.beep(500, 0.15)
    computer.beep(750, 0.15)
    computer.beep(1000, 0.15)
    computer.beep(500, 0.15)

def EndMelody02():
    # This is the end melody of ending 2.
    computer.beep(1000, 0.15)
    computer.beep(750, 0.15)
    computer.beep(500, 0.15)

def EndMelody03():
    # This is the end melody of ending 3.
    computer.beep(500, 0.15)
    computer.beep(750, 0.15)
    computer.beep(1000, 1)

def Newline(x):
    # Prints a new line as many times as X is set to.
    # Lua's repeat/until loop runs the body *before* checking the condition.
    # Python's while True with a break simulates this.
    global ln # Need to declare ln as global to modify it
    ln = 0 # Reset ln for each call, matching the Lua behavior
    while True:
        ln = ln + 1
        print(" ")
        if ln == x:
            break

def PortalAuth():
    # this code check if all the endings are completed.
    global end1, end2, end3 # Need to declare globals to access them
    if end1 == 1 and end2 == 1:
        print("You opened the portal and you are now out of Zork, Michigan.")
        Newline(3)
        print("Ending 3/3 /// True Ending")
        EndMelody03()
        # The original Lua code doesn't set end3 here, preserving that behavior.
    else:
        print("You attempted to open the portal and failed, you are now cosmic spaghetti.")

# Actual Gameplay code
# os.execute("cls") clears the screen. Use os.system for this.
# Use 'cls' for Windows, 'clear' for Linux/macOS.
os.system('cls' if os.name == 'nt' else 'clear')

Intro()

sleep(3)

# This is the main gameplay code.

print("You find yourself at an abandoned house in Zork, Michigan.")
# io.write prints without a newline, io.read reads a line.
# Use print(..., end='') and input() in Python.
print('Do you go into the house or leave? ', end='')
input_val = input() # Use a different variable name to avoid shadowing the built-in input function

# Lua's if/elseif/end structure
if input_val == "Artanium":
    print("Github.vom")
elif input_val == "Xander":
    print("Creator of XORKOID")
elif input_val == "Max":
    print("Creator of ZORKOID")

# Separate if blocks in Lua are independent checks.
# Translate them as separate if blocks in Python.
if input_val == "house":
    print("You were eaten by a grue and taken to the shadow realm...")
    print('You are in the shadow realm, do you open a portal back to reality? ', end='')
    input_val = input()
    if input_val == "yes":
        PortalAuth()
    else:
        print("You are now stuck in the shadow realm forever.")

if input_val == "RESET":
    global booted # Need to declare booted as global to modify it
    booted = 0
    # os.execute("computer.shutdown(true)") calls the shutdown function.
    # Translate to the call on our dummy computer object.
    computer.shutdown(True) # Pass boolean True

if input_val == "leave":
    print('You leave the house, do you go to the town, gas station or your car? ', end='')
    input_val = input()
    if input_val == "town":
        print("You go up to a local wizard, but he gets angry and initiates a battle!")
        print("Mad Wizard Draws Near!")
        print('what attack do you use? Bash, Zap or Madjick? ', end='')
        input_val = input()
        if input_val == "bash":
            print("The wizard dodges! You are swiftly zapped!")
        if input_val == "zap":
            print("You try to tase the wizard but he reflects the attack!")
        if input_val == "madjick":
            print("You cast magic machine-gun and the wizard is defeated!")
            print("However, your crime is not unwitnessed, and you are jailed.")
            Newline(3)
            print("Ending 2/3 /// Imprisoned")
            # Lua's repeat/until loop for melody
            global mr, end2 # Need to declare globals to modify them
            mr = 0 # Reset mr for this loop
            while True:
                mr = mr + 1
                EndMelody02()
                if mr == 4:
                    break
            # These beeps are outside the loop in the original
            computer.beep(1000, 0.15)
            computer.beep(750, 0.15)
            computer.beep(500, 0.15)
            if end2 == 0:
                end2 = 1
    if input_val == "gas station":
        print('You go to the gas station, but you get mistaken as an armed criminal and you are tased.')
    if input_val == "car":
        print("You get in and start the car. You drive away from this dump known as Zork, Michigan.")
        Newline(3)
        print("Ending 1/3 /// Highway from hell.")
        # Lua's repeat/until loop for melody
        global mr, end1 # Need to declare globals to modify them
        mr = 0 # Reset mr for this loop
        while True:
            mr = mr + 1
            EndMelody01()
            if mr == 4:
                break
        # These beeps are outside the loop in the original
        computer.beep(500, 0.15)
        computer.beep(750, 0.15)
        computer.beep(1000, 0.15)
        if end1 == 0:
            end1 = 1

