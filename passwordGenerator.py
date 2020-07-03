import random

lowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","\"","£","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",";",":","@","\'","#","<",">","?","/"]

bools = []

charNum = int(input("Number of characters: "))
bools.append(input("Lowercase letters: "))
bools.append(input("Uppercase letters: "))
bools.append(input("Numbers: "))
bools.append(input("Symbols: "))

acceptedCharacters = []

if bools[0] == "yes":
    acceptedCharacters.append(1)

if bools[1] == "yes":
    acceptedCharacters.append(2)

if bools[2] == "yes":
    acceptedCharacters.append(3)

if bools[3] == "yes":
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
print(password)
