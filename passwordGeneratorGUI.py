import random
import tkinter as tk
import pyperclip

class passwordGenerator():

    def __init__(self, master):
        self.master = master
        master.title = ("Password Generator")

        #Lists of characters
        self.lowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.uppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.numbersList = ["0","1","2","3","4","5","6","7","8","9"]
        self.symbolsList = ["!","\"","£","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",";",":","@","\'","#","<",">","?","/"]
        self.acceptedCharacters = []

        #Title
        self.titleLabel = tk.Label(text="Password Generator", font=("Times",16), bg='#aaabb8').grid(sticky='NW',columnspan=11,pady=15)

        #Widgets for the options
        
        self.optionsLabel = tk.Label(text="Character Options", font=("Times", 11), bg='#aaabb8').grid(sticky='W')
        self.charactersLabel = tk.Label(master, text="Number of characters:", bg='#aaabb8').grid(sticky='W')
        self.characterEntry = tk.Entry(master, width=3)
        self.characterEntry.grid(row=2,column=1,pady=10,sticky='W')
        
        self.lowercase = tk.IntVar()
        self.uppercase = tk.IntVar()
        self.numbers = tk.IntVar()
        self.symbols = tk.IntVar()
        self.lowercaseCheckbutton = tk.Checkbutton(master, text="Lowercase letters", variable=self.lowercase, bg='#aaabb8').grid(sticky='W')
        self.uppercaseCheckbutton = tk.Checkbutton(master, text="Uppercase letters", variable=self.uppercase, bg='#aaabb8').grid(sticky='W')
        self.numbersCheckbutton = tk.Checkbutton(master, text="Numbers", variable=self.numbers, bg='#aaabb8').grid(sticky='W')
        self.symbolsCheckbutton = tk.Checkbutton(master, text="Symbols", variable=self.symbols, bg='#aaabb8').grid(sticky='W')

        self.resetButton = tk.Button(text="Reset Options", command=self.reset).grid(row=7,column=0,sticky='W',pady=10)

        #Widgets for the result
        self.resultLabel = tk.Label(text="", font=("Times",10), bg='#aaabb8')
        self.resultLabel.grid(row=3,column=12,sticky='W',padx=10)
        self.generateButton = tk.Button(text="Generate Password", command=self.verify).grid(row=5,column=12,sticky='W',padx=10)
        
        #Widget for displaying errors
        self.errorLabel = tk.Label(text="", bg='#aaabb8')
        self.errorLabel.grid(row=6,column=12,sticky='W',padx=10)


    #Error handling of checkboxes and entry box for number of characters
    def verify(self):

        self.errorLabel["text"] = ""    #reset error label and list of accepted characters
        self.acceptedCharacters = []
        
        if len(self.characterEntry.get()) > 0:

            try:
                if int(self.characterEntry.get()) >= 0:
                    if self.lowercase.get() == 1 or self.uppercase.get() == 1 or self.numbers.get() == 1 or self.symbols.get() == 1:


                        #Numbers correspond to a type of character (1=lowercase, 2=uppercase, 3=number, 4=symbol)
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
                
            except Exception as e:
                self.errorLabel["text"] = "Please enter a number"
                print(e)
                

        else:
            self.errorLabel["text"] = "Enter a number in the box"

    #For each character: choose a random type of character, then a random character from the corresponding list
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
        passwordWithText = "Result: " + password
        self.resultLabel["text"] = passwordWithText

        #Copy password to clipboard
        pyperclip.copy(password)
        self.errorLabel["text"] = "Copied to clipboard!"

    #Reset everything to be empty/default values
    def reset(self):
        
        self.acceptedCharacters = []
        self.resultLabel["text"] = ""
        self.errorLabel["text"] = ""
        
        if len(self.characterEntry.get()) > 0:
            self.characterEntry.delete(0, 'end')

        self.lowercase.set(0)
        self.uppercase.set(0)
        self.numbers.set(0)
        self.symbols.set(0)

def main():
    window = tk.Tk()
    window.geometry("400x275")
    window.configure(bg='#aaabb8')  #window background colour
    generator = passwordGenerator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
