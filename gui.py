import tkinter as tk
from main import GeneratePassword
from pyperclip import copy

app = tk.Tk()
app.title('Password Generator')
app.geometry('400x600')

copyCount = 0
warningCount = 0

def OnSubmit():
    global copyCount
    global warningCount
    pLength = length.get()
    pAlphanumeric = var1.get()
    pSpecialCharacters = var2.get()

    try:
        pLength = int(pLength)
        try:
            password = GeneratePassword(length=pLength, alphanumeric=pAlphanumeric, specialChars=pSpecialCharacters, copyToClipboard=False, messages=False)
            copyBtn = tk.Button(app, text='Copy Password', command=copy(password))
            pwdLabel = tk.Label(app, text=password)
            if copyCount == 0: 
                copyBtn.pack()
                copyCount = 1

            pwdLabel.pack()
        except TypeError:
            if warningCount == 0:
                tk.Label(app, text='Invalid Password Length').pack()
                warningCount = 1
    except ValueError:
        if warningCount == 0:
            tk.Label(app, text='Invalid Password Length').pack()
            warningCount = 1

tk.Label(app, text='').pack() # Spacer

# Title Label
title = tk.Label(app, text='Password Generator', font=('Arial', 30))
title.pack()

tk.Label(app, text='').pack() # Spacer

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

# Parameters
lengthLabel = tk.Label(app, text='Password Length (6-32):')
length = tk.Entry(app, textvariable='Length')
alphanumeric = tk.Checkbutton(app, text='Alphanumeric', variable=var1, onvalue=True, offvalue=False)
specialChars = tk.Checkbutton(app, text='Special Characters', variable=var2, onvalue=True, offvalue=False)
generateBtn = tk.Button(app, text='Generate Password', command=OnSubmit)

lengthLabel.pack()
length.pack()
alphanumeric.pack()
specialChars.pack()
tk.Label(app, text='').pack() # Spacer
generateBtn.pack()

app.mainloop()