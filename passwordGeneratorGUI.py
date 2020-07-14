import random
import tkinter as tk

lowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","\"","£","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",";",":","@","\'","#","<",">","?","/"]
options = []

window = tk.Tk()

titleLabel = tk.Label(text="Password Generator")
charactersLabel = tk.Label(text="Number of characters:")
characterEntry = tk.Entry(width=10)

lowercaseCheckbutton = tk.Checkbutton(top, text="Lowercase letters", variable = )
uppercaseCheckbutton = tk.Checkbutton(top, text="Uppercase letters", variable = )
numbersCheckbutton = tk.Checkbutton(top, text="Numbers", variable = )
symbolsCheckbutton = tk.Checkbutton(top, text="Symbols", variable = )

generateButton = tk.Button(text="Generate", command=generatePassword())

resultLabelText = "Result:"
resultLabel = tk.Label(text=resultLabelText)

resetButton = tk.Button(text="Reset", command=reset())
exitButton = tk.Button(text="Exit")

def generatePassword():

    charNum = characterEntry.get()
    acceptedCharacters = []

    if options[0] == "yes":
        acceptedCharacters.append(1)

    if options[1] == "yes":
        acceptedCharacters.append(2)

    if options[2] == "yes":
        acceptedCharacters.append(3)

    if options[3] == "yes":
        acceptedCharacters.append(4)

    password = []

    for i in range(charNum):

        typeOfChar = random.choice(acceptedCharacters)

        if typeOfChar == 1:
            password.append(random.choice(lowercaseLetters))

        elif typeOfChar == 2:
            password.append(random.choice(uppercaseLetters))

        elif typeOfChar == 3:
            password.append(random.choice(numbers))

        else:
            password.append(random.choice(symbols))

    password = "".join(password)
    #print(password)

def reset():
    resultLabelText = "Result"
    characterEntry.delete()

window.mainloop()
