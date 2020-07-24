import random
import tkinter as tk

class passwordGenerator():

    def __init__(self, master):
        self.master = master
        master.title = ("Password Generator")
        
        self.lowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.uppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.numbersList = ["0","1","2","3","4","5","6","7","8","9"]
        self.symbolsList = ["!","\"","£","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",";",":","@","\'","#","<",">","?","/"]
        
        self.lowercase = tk.IntVar()
        self.uppercase = tk.IntVar()
        self.numbers = tk.IntVar()
        self.symbols = tk.IntVar()
        self.acceptedCharacters = []

        self.titleLabel = tk.Label(text="Password Generator", font=("Courier", 16)).grid(sticky='W', columnspan=3)
        self.charactersLabel = tk.Label(text="Number of characters:").grid(sticky='W')
        self.characterEntry = tk.Entry(width=3)
        self.characterEntry.grid(row=1,column=1)

        self.lowercaseCheckbutton = tk.Checkbutton(master, text="Lowercase letters", variable=self.lowercase).grid(sticky='W')
        self.uppercaseCheckbutton = tk.Checkbutton(master, text="Uppercase letters", variable=self.uppercase).grid(sticky='W')
        self.numbersCheckbutton = tk.Checkbutton(master, text="Numbers", variable=self.numbers).grid(sticky='W')
        self.symbolsCheckbutton = tk.Checkbutton(master, text="Symbols", variable=self.symbols).grid(sticky='W')

        self.generateButton = tk.Button(text="Generate", command=self.verifyCheckboxes).grid(sticky='W')
        self.resultLabel = tk.Label(text="Result:")
        self.resultLabel.grid(sticky='W')

        self.errorLabel = tk.Label(text="")
        self.errorLabel.grid(sticky='W')

        self.resetButton = tk.Button(text="Reset", command=self.reset).grid(sticky='W')
        self.exitButton = tk.Button(text="Exit", command=self.exit).grid(row=9,column=1)

    def verifyCheckboxes(self):

        self.errorLabel["text"] = ""    #reset error label
        self.acceptedCharacters = []
        
        if len(self.characterEntry.get()) > 0:

            try:
                if int(self.characterEntry.get()) >= 0:
                    if self.lowercase.get() == 1 or self.uppercase.get() == 1 or self.numbers.get() == 1 or self.symbols.get() == 1:

                        if self.lowercase.get() == 1:
                            self.acceptedCharacters.append(1)
                            
                        if self.uppercase.get() == 1:
                            self.acceptedCharacters.append(2)

                        if self.numbers.get() == 1:
                            self.acceptedCharacters.append(3)

                        if self.symbols.get() == 1:
                            self.acceptedCharacters.append(4)
                            
                        self.generatePassword()

                    else:
                        self.errorLabel["text"] = "Select at least one of the checkboxes"

                else:
                    self.errorLabel["text"] = "Choose a number that is greater than zero"
                
            except:
                self.errorLabel["text"] = "Please enter a number"
                

        else:
            self.errorLabel["text"] = "Enter a number in the box"

    def generatePassword(self):
        charNum = int(self.characterEntry.get())
        password = []

        for i in range(charNum):

            typeOfChar = random.choice(self.acceptedCharacters)

            if typeOfChar == 1:
                password.append(random.choice(self.lowercaseLetters))

            elif typeOfChar == 2:
                password.append(random.choice(self.uppercaseLetters))

            elif typeOfChar == 3:
                password.append(random.choice(self.numbersList))

            else:
                password.append(random.choice(self.symbolsList))

        password = "".join(password)
        password = "Result: " + password
        self.resultLabel["text"] = password
     
    def reset(self):
        self.acceptedCharacters = []
        self.resultLabel["text"] = "Result:"
        self.errorLabel["text"] = ""
        
        if len(self.characterEntry.get()) > 0:
            self.characterEntry.delete(0, 'end')

        self.lowercase.set(0)
        self.uppercase.set(0)
        self.numbers.set(0)
        self.symbols.set(0)

    def exit(self):
        self.master.destroy()

def main():
    window = tk.Tk()
    window.geometry("300x300")
    generator = passwordGenerator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
