from tkinter import *
import calendar


# Function for Year Window
def show_year():
    top = Toplevel()
    top.geometry("1550x900")
    top['bg'] = '#77ab59'
    top.title("Year")

    label3 = Label(top, text="Year", font=('arial', 15, 'bold'), bg='#77ab59')
    label3.place(x=635, y=3)

    global ent1
    global txt1

    ent1 = Entry(top, width=6, bg='#f0f7da')
    ent1.place(x=700, y=10)

    btn1 = Button(top, text="Show", font=('arial', 13, 'normal'), bg='#c9df8a', command=show_year_bt)
    btn1.place(x=760, y=3)

    txt1 = Text(top, width=75, height=35, padx=50, pady=50, bg='#f0f7da')
    txt1.place(x=410, y=57)


# Function for Month Window
def show_month():
    top = Toplevel()
    top.geometry("300x300")
    top.resizable(0, 0)
    top['bg'] = '#77ab59'
    top.title("Month")
    
    label1 = Label(top, text="Month", font=('arial', 9, 'bold'), bg='#77ab59')
    label1.place(x=55, y=5)

    label2 = Label(top, text="Year", font=('arial', 9, 'bold'), bg='#77ab59')
    label2.place(x=155, y=5)

    global spin1
    global ent2
    global txt

    spin1 = Spinbox(top, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4, bg='#f0f7da')
    spin1.place(x=100, y=5)

    ent2 = Entry(top, width=5, bg='#f0f7da')
    ent2.place(x=190, y=5)

    btn = Button(top, text="Show", font=('arial', 9, 'bold'), bg='#c9df8a', command=show_month_bt)
    btn.place(x=125, y=30)

    txt = Text(top, width=20, height=7, padx=50, pady=58, bg='#f0f7da')
    txt.place(x=20, y=60)


# Function for Month Button
def show_month_bt():
    a = int(spin1.get())
    b = int(ent2.get())

    cal = calendar.month(b, a)

    txt.delete(0.0, END)
    txt.insert(INSERT, cal)


# Function for Year Button
def show_year_bt():
    c = int(ent1.get())

    cal = calendar.calendar(c)

    txt1.delete(0.0, END)
    txt1.insert(INSERT, cal)


# Main Window
root = Tk()
root['bg'] = '#89ABCD'
root.title("Calendar")
root.geometry("240x200")
root.resizable(0, 0)

lb = Label(root, text='CALENDAR', font=('MS Sans Serif', 15, 'bold'), bg='#89ABCD').place(x=70, y=10)

button1 = Button(root, text="Show Month", font=('arial', 9, 'bold'), bg='#ABCDEF', command=show_month)
button1.place(x=85, y=50)

button2 = Button(root, text="Show Year", font=('arial', 9, 'bold'), bg='#ABCDEF', command=show_year)
button2.place(x=90, y=83)

root.mainloop()
