from tkinter import *
master = Tk()
master.geometry("550x360")
v = IntVar()

l1 = Label(master, text="Contact List")
l2 = Label(master, text="Last Name:")
l3 = Label(master, text="New Contact")
l4 = Label(master, text="First Name:")
l5 = Label(master, text="Last Name:")
l6 = Label(master, text="Phone #:")
l7 = Label(master, text="Email:")
l8 = Label(master, text="Birthday:")


# entry fields
e1 = Listbox(master, height=12, width=20)
e2 = Entry(master)
b1 = Button(master, text="Display Contact")
b2 = Button(master, text="Search")
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
c1 = Checkbutton(master, text="Friend", variable=v)
e7 = Entry(master)
e8 = Entry(master)

# Place fields
l1.place(x=100, y=0)
e1.place(x=50, y=20)
b1.place(x=75, y=230)
l2.place(x=0, y=280)
e2.place(x=75, y=278)
b2.place(x=125, y=330)

l3.place(x=350, y=0)
l4.place(x=280, y=20)
l5.place(x=280, y=50)
l6.place(x=295, y=80)
e4.place(x=355, y=20)
e5.place(x=355, y=50)
e6.place(x=355, y=80)
c1.place(x=370, y=110)
l7.place(x=310, y=140)
e7.place(x=355, y=140)
l8.place(x=295, y=170)
e8.place(x=355, y=170)


mainloop()
