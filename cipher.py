from tkinter import messagebox, simpledialog
from random import choice

def receiveTask():
    task = simpledialog.askstring("Task", "Do you want to CIPHER or DECIPHER? Type 'exit' to exit the program.")
    return task

def receiveMessage():
    message = simpledialog.askstring("Message", "Input your message here. ")
    return message

def isEven(number):
    return number % 2 == 0

def receiveEvenLetters(message):
    evenLetters = []
    for counter in range(0, len(message)):
        if isEven(counter):
            evenLetters.append(message[counter])
    return evenLetters

def receiveOddLetters(message):
    oddLetters = []
    for counter in range(0, len(message)):
        if not isEven(counter):
            oddLetters.append(message[counter])
    return oddLetters

def cipher(message):
    cipheredList = []
    fakeLetters = ["a", "b", "c", "d", "e", "f", "g", "i", "r", "s", "t", "u", "v"]
    for counter in range(0, len(message)):
       cipheredList.append(message[counter])
       cipheredList.append(choice(fakeLetters))
    fakeMessage = "".join(cipheredList)
    switchedMessage = switchLetters(fakeMessage)
    cipheredMessage = "".join(reversed(switchedMessage))
    return cipheredMessage

def decipher(message):
    evenLetters = receiveEvenLetters(message)
    unfakeMessage = "".join(evenLetters)
    decipheredMessage = "".join(reversed(unfakeMessage))
    #switchedMessage = switchLetters(decipheredMessage)
    return decipheredMessage

def switchLetters(message):
    letterList = []
    if not isEven(len(message)):
        message += "x"
    evenLetters = receiveEvenLetters(message)
    oddLetters = receiveOddLetters(message)
    for counter in range(0, int(len(message)/2)):
        letterList.append(oddLetters[counter])
        letterList.append(evenLetters[counter])
    newMessage = "".join(letterList)
    return newMessage

while True:
    task = receiveTask()
    if task == None:
        break
    if task.lower() == "cipher":
        message = receiveMessage()
        cipherMessage = cipher(message)
        print(cipherMessage)
        messagebox.showinfo("Ciphered message (copy from shell/terminal output): ", cipherMessage)
    elif task.lower() == "decipher":
        message = receiveMessage()
        decipherMessage = decipher(message)
        print(decipherMessage)
        messagebox.showinfo("Deciphered message (copy from shell/terminal output): ", decipherMessage)
    elif task.lower() == "exit":
        break
    else:
        messagebox.showinfo("OOOPS!", "I didn't understand what you want to do. Type 'cipher' or 'decipher'.")
        break
    
