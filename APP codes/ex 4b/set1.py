
import tkinter as tk
from tkinter import *

#from tkinter import messagebox
root = tk.Tk()
root.geometry("750x1000")
root.configure(bg='purple')


def submit_value():
    print("Your information has been saved successfully")


def reset():
    h.set("")


l1 = tk.Label(root, text="FIRST NAME")
l1.configure(bg='purple', foreground="white")
l1.grid(row=0, column=0)
l2 = tk.Label(root, text="LAST NAME")
l2.configure(bg='purple', foreground="white")
l2.grid(row=1, column=0)
l3 = tk.Label(root, text="DATE OF BIRTH")
l3.configure(bg='purple', foreground="white")
l3.grid(row=2, column=0)
l4 = tk.Label(root, text="EMAIL ID")
l4.configure(bg='purple', foreground="white")
l4.grid(row=3, column=0)
l5 = tk.Label(root, text="MOBILE NUMBER")
l5.configure(bg='purple', foreground="white")
l5.grid(row=4, column=0)
l6 = tk.Label(root, text="GENDER")
l6.configure(bg='purple', foreground="white")
l6.grid(row=5, column=0)
l7 = tk.Label(root, text="ADDRESS")
l7.configure(bg='purple', foreground="white")
l7.grid(row=6, column=0)
l16 = tk.Label(root, text="")
l16.configure(bg='purple', foreground="white")
l16.grid(row=7, column=0)
l17 = tk.Label(root, text="")
l17.configure(bg='purple', foreground="white")
l17.grid(row=8, column=0)
l18 = tk.Label(root, text="")
l18.configure(bg='purple', foreground="white")
l18.grid(row=9, column=0)
l19 = tk.Label(root, text="")
l19.configure(bg='purple', foreground="white")
l19.grid(row=10, column=0)
l20 = tk.Label(root, text="")
l20.configure(bg='purple', foreground="white")
l20.grid(row=11, column=0)
l8 = tk.Label(root, text="CITY")
l8.configure(bg='purple', foreground="white")
l8.grid(row=11, column=0)
l9 = tk.Label(root, text="PIN CODE")
l9.configure(bg='purple', foreground="white")
l9.grid(row=12, column=0)
l10 = tk.Label(root, text="STATE")
l10.configure(bg='purple', foreground="white")
l10.grid(row=13, column=0)
l11 = tk.Label(root, text="COUNTRY")
l11.configure(bg='purple', foreground="white")
l11.grid(row=14, column=0)
l12 = tk.Label(root, text="HOBBIES")
l12.configure(bg='purple', foreground="white")
l12.grid(row=15, column=0)
l13 = tk.Label(root, text="QUALIFICATION")
l13.configure(bg='purple', foreground="white")
l13.grid(row=17, column=0)
l14 = tk.Label(root, text="COURSES")
l14.configure(bg='purple', foreground="white")
l14.grid(row=23, column=0)
l15 = tk.Label(root, text="APPLIED FOR")
l15.configure(bg='purple', foreground="white")
l15.grid(row=24, column=0)
l16 = tk.Label(root, text="")
l16.configure(bg='purple', foreground="white")
l16.grid(row=16, column=0)
l17 = tk.Label(root, text="Sl.No.Examination")
l17.configure(bg='purple', foreground="white")
l17.grid(row=17, column=1)
l18 = tk.Label(root, text="")
l18.configure(bg='purple', foreground="white")
l18.grid(row=18, column=0)
l19 = tk.Label(root, text="")
l19.configure(bg='purple', foreground="white")
l19.grid(row=19, column=0)
l20 = tk.Label(root, text="")
l20.configure(bg='purple', foreground="white")
l20.grid(row=20, column=0)
l21 = tk.Label(root, text="")
l21.configure(bg='purple', foreground="white")
l21.grid(row=21, column=0)
l22 = tk.Label(root, text="")
l22.configure(bg='purple', foreground="white")
l22.grid(row=22, column=0)
l23 = tk.Label(root, text="1          Class X")
l23.configure(bg='purple', foreground="white")
l23.grid(row=18, column=1)
l24 = tk.Label(root, text="2        Class XII")
l24.configure(bg='purple', foreground="white")
l24.grid(row=19, column=1)
l25 = tk.Label(root, text=" 3     Graduation")
l25.configure(bg='purple', foreground="white")
l25.grid(row=20, column=1)
l26 = tk.Label(root, text="4          Masters")
l26.configure(bg='purple', foreground="white")
l26.grid(row=21, column=1)
l27 = tk.Label(root, text="Board")
l27.configure(bg='purple', foreground="white")
l27.grid(row=17, column=2)
l28 = tk.Label(root, text="Percentage")
l28.configure(bg='purple', foreground="white")
l28.grid(row=17, column=3)
l16 = tk.Label(root, text="Year of Passing")
l16.configure(bg='purple', foreground="white")
l16.grid(row=17, column=4)

list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
         '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
d = StringVar()
droplist = OptionMenu(root, d, *list1)
d.set('Date')
droplist.configure(bg='white', foreground="black")
droplist.grid(row=2, column=1)

list2 = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
f = StringVar()
droplist = OptionMenu(root, f, *list2)
f.set('Month')
droplist.grid(row=2, column=2)
droplist.configure(bg='white', foreground="black")

list3 = ['2000', '2001', '2002', '2003', '2004',
         '2005', '2006', '2007', '2008', '2009', '2010']
g = StringVar()
droplist = OptionMenu(root, g, *list3)
g.set('Year')
droplist.configure(bg='white', foreground="black")
droplist.grid(row=2, column=3)


c = Checkbutton(root, text="Drawing")
c.place(x=100, y=324, width=60, height=25)
c.configure(bg='purple', foreground="black")

c1 = Checkbutton(root, text="Singing")
c1.place(x=161, y=324, width=60, height=25)
c1.configure(bg='purple', foreground="black")
c2 = Checkbutton(root, text="Dancing")
c2.place(x=222, y=324, width=60, height=25)
c2.configure(bg='purple', foreground="black")
c3 = Checkbutton(root, text="Sketching")
c3.place(x=283, y=324, width=80, height=25)
c3.configure(bg='purple', foreground="black")
c4 = Checkbutton(root, text="Others")
c4.place(x=95, y=343, width=60, height=25)
c4.configure(bg='purple', foreground="black")

var = IntVar()
r = Radiobutton(root, text="Male", padx=1, variable=var, value=1)
r.grid(row=5, column=1)
r.configure(bg='purple', foreground="black")

r1 = Radiobutton(root, text="Female", padx=1, variable=var, value=2)
r1.grid(row=5, column=2)
r1.configure(bg='purple', foreground="black")

var1 = IntVar()
r2 = Radiobutton(root, text="BCA", padx=1, variable=var, value=1)
r2.grid(row=23, column=1)
r2.configure(bg='purple', foreground="black")
r3 = Radiobutton(root, text="B.Com", padx=1, variable=var, value=2)
r3.grid(row=23, column=2)
r3.configure(bg='purple', foreground="black")
r4 = Radiobutton(root, text="B.Sc", padx=1, variable=var, value=3)
r4.grid(row=23, column=3)
r4.configure(bg='purple', foreground="black")
r5 = Radiobutton(root, text="B.A", padx=1, variable=var, value=4)
r5.grid(row=23, column=4)
r5.configure(bg='purple', foreground="black")

h = Entry(root)
h.grid(row=0, column=1)
t = tk.Entry(root)
t.grid(row=1, column=1)
t = tk.Entry(root)
t.grid(row=3, column=1)
t = tk.Entry(root)
t.grid(row=4, column=1)
t = tk.Entry(root)
t.grid(row=11, column=1)
t = tk.Entry(root)
t.grid(row=12, column=1)
t = tk.Entry(root)
t.grid(row=13, column=1)
t = tk.Entry(root)
t.grid(row=14, column=1)
t = tk.Entry(root)
t.grid(row=18, column=2)
t = tk.Entry(root)
t.grid(row=19, column=2)
t = tk.Entry(root)
t.grid(row=20, column=2)
t = tk.Entry(root)
t.grid(row=21, column=2)
t = tk.Entry(root)
t.grid(row=18, column=3)
t = tk.Entry(root)
t.grid(row=19, column=3)
t = tk.Entry(root)
t.grid(row=20, column=3)
t = tk.Entry(root)
t.grid(row=21, column=3)
t = tk.Entry(root)
t.grid(row=18, column=4)
t = tk.Entry(root)
t.grid(row=19, column=4)
t = tk.Entry(root)
t.grid(row=20, column=4)
t = tk.Entry(root)
t.grid(row=21, column=4)
t = tk.Entry(root)

t.place(x=155, y=345, width=125, height=20)
t = tk.Entry(root)

t.grid(row=6, column=1)
t.place(x=99, y=137, width=200, height=100)

Button(text="Submit", command=submit_value).grid(row=25, column=1)

Button(text="Reset", command=reset).grid(row=25, column=2)

root.mainloop()