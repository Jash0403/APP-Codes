from tkinter import *
master = Tk()
v = IntVar()
options = []
for i in range(10, 31):
    options.append(i)
Label(master, text="Movie Booking id").grid(row=0)
Label(master, text="Person Name").grid(row=1)
Label(master, text="Movie Name").grid(row=2)
Label(master, text="Class").grid(row=3)
Label(master, text="Time of Show").grid(row=3, column=3)
Label(master, text="No of Tickets").grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
r1 = Radiobutton(master, text="A", variable=v, value=1)
r2 = Radiobutton(master, text="B", variable=v, value=2)
r3 = Checkbutton(master, text="7.15 pm", variable=v)
r4 = Checkbutton(master, text="9 am")
b1 = Button(master, text="Insert")
b2 = Button(master, text="Update")
b3 = Button(master, text="Delete")
b4 = Button(master, text="Select")
s1 = Scale(master, from_=0, to=10, orient=HORIZONTAL)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
r1.grid(row=3, column=1)
r2.grid(row=3, column=2)
r3.grid(row=3, column=4)
r4.grid(row=3, column=5)
s1.grid(row=4, column=1)
b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
b3.grid(row=6, column=0)
b4.grid(row=6, column=1)
mainloop()
