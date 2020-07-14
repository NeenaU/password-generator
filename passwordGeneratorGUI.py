import random
import tkinter as tk

class passwordGenerator():

    def __init__(self, master):
        self.master = master
        master.title = ("Password Generator")
        
        self.lowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.uppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.symbols = ["!","\"","£","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",";",":","@","\'","#","<",">","?","/"]
        
        self.lowercase = tk.IntVar()
        self.uppercase = tk.IntVar()
        self.numbers = tk.IntVar()
        self.symbols = tk.IntVar()
        self.acceptedCharacters = []

        self.titleLabel = tk.Label(text="Password Generator").grid(sticky='W')
        self.charactersLabel = tk.Label(text="Number of characters:").grid(sticky='W')
        self.characterEntry = tk.Entry(width=10)
        self.characterEntry.grid(row=1,column=1)

        self.lowercaseCheckbutton = tk.Checkbutton(master, text="Lowercase letters", variable=self.lowercase).grid(sticky='W')
        self.uppercaseCheckbutton = tk.Checkbutton(master, text="Uppercase letters", variable=self.uppercase).grid(sticky='W')
        self.numbersCheckbutton = tk.Checkbutton(master, text="Numbers", variable=self.numbers).grid(sticky='W')
        self.symbolsCheckbutton = tk.Checkbutton(master, text="Symbols", variable=self.symbols).grid(sticky='W')

        self.generateButton = tk.Button(text="Generate", command=self.generatePassword).grid(sticky='W')
        self.resultLabel = tk.Label(text="Result:").grid(sticky='W')

        self.resetButton = tk.Button(text="Reset", command=self.reset).grid(sticky='W')
        self.exitButton = tk.Button(text="Exit", command=self.exit).grid(row=8,column=1)

    def generatePassword(self):

        charNum = 0

        if len(self.characterEntry.get()) > 0:
            charNum = int(self.characterEntry.get())

        if self.lowercase.get() == 1:
            self.acceptedCharacters.append(1)
            
        if self.uppercase.get() == 1:
            self.acceptedCharacters.append(2)

        if self.numbers.get() == 1:
            self.acceptedCharacters.append(3)

        if self.symbols.get() == 1:
            self.acceptedCharacters.append(4)

        password = []

        for i in range(charNum):

            typeOfChar = random.choice(self.acceptedCharacters)

            if typeOfChar == 1:
                password.append(random.choice(self.lowercaseLetters))

            elif typeOfChar == 2:
                password.append(random.choice(self.uppercaseLetters))

            elif typeOfChar == 3:
                password.append(random.choice(self.numbers))

            else:
                password.append(random.choice(self.symbols))

        password = "".join(password)
        text = "Result: " + password
        print(text)
        setattr(self, 'resultLabel.text', text)
     
    def reset(self):
        setattr(self, 'resultLabel.text', "Result:")
        if len(self.characterEntry.get()) > 0:
            characterEntry.delete()

    def exit(self):
        self.master.destroy()

def main():
    window = tk.Tk()
    window.geometry("300x300")
    generator = passwordGenerator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
