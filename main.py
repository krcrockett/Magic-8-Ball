#imports
from tkinter import *
from tkinter import messagebox
import random

root = Tk()
#the window
root.geometry("190x100")
root.title('Magic 8 Ball')

frame = Frame(root)
frame.grid()
root.configure(bg="blue")

#centering frame
frame.place(relx=.5, rely=.5, anchor="center")

#8 ball answers
answer = ["probably not", "Yes", "probably", "No", "Ask again"]

def showans():
    result = int(random.random() * len(answer))
    messagebox.showinfo('Answer!', f'Magic 8 Ball answers {answer[result]}',)

#window appearance and buttons
button = Button(frame, text="Exit", fg="red", command=quit)
button.grid(row=4, column=0)
slogan = Button(frame, text="Click here for 8Ball's Answer", command=showans)
slogan.grid(row=1, column=0)
label1 = Label(frame, text="Ask the Magic Ball a question")
label1.grid(row=0, column=0)

root.mainloop()
