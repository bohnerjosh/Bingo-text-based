from random import choice
from sys import exit

def clearscreen():
    for i in range(10):
        print("")
        
def bingo(called_numbers):
    print("Enter the numbers one at a time in the prompt when it comes up below. Hit enter only when you want")
    print("the program to check the numbers.")
    inputnumbers = True
    numslst = []
    goodbingo = False
    checkindex = 0
    while inputnumbers:
        numstocheck = input("Enter number to check. ")
        if not numstocheck == "":
            checkindex += 1
            numslst.append(numstocheck)
        else:
            break
    for num in numslst:
        if num in called_numbers:
            print("%s was called." % num)
            continue
            goodbingo = True
            break
        else:
            print("%s was NOT called." % num)
            numslst = []
            break
        goodbingo = True
        break
    if len(numslst) == checkindex:
        goodbingo = True
    if goodbingo:
        print("That is a good bingo!")
    else:
        print("That is NOT a good bingo!")
    while True:
        ask = input("Keep playing or end game? ").lower()
        if ask == "keep playing":
            return
        elif ask == "end game":
            exit()
        else:
            print("Invalid.")
# Lists
numbers = {
"BB" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
"II" : [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
"NN" : [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
"GG" : [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
"OO" : [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75],
}

letters = ["B", "I", "N", "G", "O"]
called_numbers = []

done = False

print("Welcome to my bingo caller! To use, every time you want a new number, press enter!")
print("If you want to pause the game, type 'pause'.")
print("If you want to check for a bingo, type 'bingo'.")
print("")

while not done:
    column = choice(letters)
    tempcolumn = column + column
    if len(numbers[tempcolumn]) == 0:
        continue
    else:
        row = choice(numbers[tempcolumn])
        strrow = str(row)
        picked = column + " " + strrow
        print("")
        numbers[tempcolumn].remove(row)
        called_numbers.append(picked)
        print(picked)
    stop = input("").lower()
    if stop == "stop":
        break
    elif stop == "pause":
        while True:
            check = input("Type 'unpause' when ready to continue, or 'bingo' if there is a bingo.").lower()
            if check == "unpause":
                break
            elif check == "bingo":
                bingo(called_numbers)
                break
    elif stop == "bingo":
        bingo(called_numbers)
        
