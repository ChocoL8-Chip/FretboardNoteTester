import random
import os
import time

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRINGS = {
"E": ["E", "F", "F#", "G", "G#", "A", "A#", "B" "C", "C#", "D", "D#"],
"A": ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
"D": ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#"],
"G": ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"],
"B": ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#"],
}
list_of_strings = []
for string in STRINGS:
    list_of_strings.append(string)
ANSWERED_CORRECTLY = 0
NUMBER_OF_TURNS = 0

def startGame():
    global NUMBER_OF_TURNS
    global ANSWERED_CORRECTLY
    NUMBER_OF_TURNS+=1
    random_note = random.choice(NOTES)
    random_string = STRINGS[random.choice(list_of_strings)]

    difference = random_string.index(random_note)
    # print(random_note, random_string, difference)
    # print(difference)
    print(f"Where is {random_note} on the {random_string[0]} string?")
    user_input = input()
    if int(user_input) == difference or int(user_input) % 12 == difference:
        ANSWERED_CORRECTLY+=1
        print(f"Correct! ({ANSWERED_CORRECTLY}/{NUMBER_OF_TURNS})")
        time.sleep(1)
    elif user_input != difference:
        print(f"Incorrect; {random_note} is located on fret {difference}. ({ANSWERED_CORRECTLY}/{NUMBER_OF_TURNS})")
        time.sleep(1)
while True:
    startGame()
    os.system("cls" if os.name == "nt" else "clear")
