from tkinter import *
import sqlite3
from tkinter import ttk
from PIL import ImageTk,Image
with sqlite3.connect("Hotel.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS customer(id integer PRIMARY KEY AUTOINCREMENT, First_Name text NOT NULL, Last_Name text, Aadhar_no int NOT NULL, Phone_no int, Room_type text, Days int, Time int, AM_PM text, date int, month int, year int); """)
cursor.execute(""" CREATE TABLE IF NOT EXISTS employee(id integer PRIMARY KEY AUTOINCREMENT, emp_id int, emp_name text,dept text, time int, am_pm text); """)
def openn():
    global my_img1
    def show1():
        top2 = Toplevel()
        top2.title('second window')
        top2.geometry("450x300")
        top2.config(bg = 'gray')
        my_label = Label(top2).pack()

        _11 = Label(top2, text = "ID NO.")
        _11.place(x = 0, y = 0)
        _22 = Label(top2, text = "Name")
        _22.place(x = 80, y = 0)
        _33 = Label(top2, text = "DEPT")
        _33.place(x = 160, y = 0)
        _44 = Label(top2, text = "Time")
        _44.place(x = 260, y = 0)
        _55 = Label(top2, text = "Am,PM")
        _55.place(x = 340, y = 0)

        cursor.execute("SELECT * FROM employee")
        display1 = cursor.fetchall()

        num1 = 30

        for i in display1:
            first = Label(top2, text = i[1])
            first.place(x = 0, y = num1)
            last = Label(top2, text = i[2])
            last.place(x = 80, y = num1)
            adh = Label(top2, text = i[3])
            adh.place(x = 160, y = num1)
            phn = Label(top2, text = i[4])
            phn.place(x = 260, y = num1)
            typ = Label(top2, text = i[5])
            typ.place(x = 340, y = num1)

            num1 = num1 + 30
            
            

        
    def second_entry():
        ID = aaa.get()
        T = click9.get()
        A = click10.get()
        if ID=='1':
            name = 'staf 1'
            dept = 'Manager'
        elif ID=='2':
            name = 'staf 2'
            dept = 'Kitchen'
        elif ID=='3':
            name = 'staf 3'
            dept = 'House Keeping'
        elif ID=='4':
            name = 'staf 4'
            dept = 'Security'
        elif ID=='5':
            name = 'staf 5'
            dept = 'Technical'
        else:
            error1["text"] = "Add Proper ID"
        try:
            cursor.execute("INSERT INTO employee(emp_id, emp_name, dept, time, am_pm) VALUES(?,?,?,?,?)",(ID,name,dept,T,A))
            db.commit()
            error1["text"] = "Added"
        except:
            error1["text"] = "Enter Proper choice"
    top = Toplevel()
    top.title('second window')
    top.geometry("250x300")
    top.config(bg = '#89CFF0')
    my_label = Label(top).pack()
    my_img1 = ImageTk.PhotoImage(Image.open("G:\\img1.jpeg"))
    my_label20 = Label(top,image = my_img1)
    my_label20.place(x = 0, y = 0, width = 250, height = 300)
    #ID ENTRY 
    ath = Label(top,text = "Enter Staff id",font =('Times',15,'bold'))
    ath.place(x = 10, y = 30,)
    ath.config(bg="white", padx=0)
    aaa = Entry(top,text = "")
    aaa.place(x = 10, y = 65, width = 200, height = 30)
    #TIME ENTRY
    label15 = Label(top,text = "select Entry Time:",font = ('Times',15,'bold'))
    label15.place(x = 10, y = 100)
    label15.config(bg="white", padx=0)
    option9 = ['1','2','3','4','5','6','7','8','9','10','11','12']
    option10 = ['am','pm']
    click9 = StringVar()
    click9.set(option9[0])
    drop9 = OptionMenu(top, click9, *option9)
    drop9.place(x = 10, y = 140, width = 60, height = 20)
    click10 = StringVar()
    click10.set(option10[0])
    drop10 = OptionMenu(top, click10, *option10)
    drop10.place(x = 75, y = 140, width = 60, height = 20)
    #Entry Button
    button1 = Button(top,text = "Submit", command = second_entry)
    button1.place(x = 60, y = 200, width = 125, height = 50)
    #MSG
    error1 = Message(top,text="", width = 160)
    error1.place(x = 10, y = 260)
    error1.config(bg="white", padx = 0)
    button2 = Button(top,text = "Submit", command = show1)
    button2.place(x = 60, y = 250, width = 100, height = 30)
    
def show():
    top1 = Toplevel()
    top1.title('Third window')
    top1.geometry("1000x300")
    top1.config(bg = 'gray')
    my_label = Label(top1).pack()

    _1 = Label(top1, text = "First Name")
    _1.place(x = 0, y = 0)
    _2 = Label(top1, text = "Last Name")
    _2.place(x = 80, y = 0)
    _3 = Label(top1, text = "Aadhar No.")
    _3.place(x = 160, y = 0)
    _4 = Label(top1, text = "Phone No.")
    _4.place(x = 260, y = 0)
    _5 = Label(top1, text = "Room Type")
    _5.place(x = 340, y = 0)
    _6 = Label(top1, text = "No of Days")
    _6.place(x = 420, y = 0)
    _7 = Label(top1, text = "Time")
    _7.place(x = 500, y = 0)
    _8 = Label(top1, text = "AM,PM")
    _8.place(x = 580, y = 0)
    _9 = Label(top1, text = "Day")
    _9.place(x = 660, y = 0)
    _10 = Label(top1, text = "Month")
    _10.place(x = 740, y = 0)
    _11 = Label(top1, text = "Year")
    _11.place(x = 820, y = 0)

    cursor.execute("SELECT * FROM customer")
    display = cursor.fetchall()

    num = 30
    for i in display:
        first = Label(top1, text = i[1])
        first.place(x = 0, y = num)
        last = Label(top1, text = i[2])
        last.place(x = 80, y = num)
        adh = Label(top1, text = i[3])
        adh.place(x = 160, y = num)
        phn = Label(top1, text = i[4])
        phn.place(x = 260, y = num)
        typ = Label(top1, text = i[5])
        typ.place(x = 340, y = num)
        days = Label(top1, text = i[6])
        days.place(x = 420, y = num)
        t = Label(top1, text = i[7])
        t.place(x = 500, y = num)
        Ap = Label(top1, text = i[8])
        Ap.place(x = 580, y = num)
        D = Label(top1, text = i[9])
        D.place(x = 660, y = num)
        M = Label(top1, text = i[10])
        M.place(x = 740, y = num)
        Y = Label(top1, text = i[11])
        Y.place(x = 820, y = num)

        num = num+30
        

        

    

def add_new_user():
    try:     
        one = str(first.get())
        two = str(last.get())
        three = int(aadhar.get())
        four = int(phone.get())
        five = clicked.get()
        six = int(days.get())
        seven = click.get()
        eight = click2.get()
        nine = click3.get()
        ten = click4.get()
        eleven = click5.get()
    except:
        error["text"] = "Enter proper number"


    try:
        cursor.execute("INSERT INTO customer(First_Name, Last_Name, Aadhar_no, Phone_no, Room_type, Days, Time, AM_PM, date, month, year) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(one,two,three,four,five,six,seven,eight,nine,ten,eleven))
        db.commit()
        error["text"] = "Added New User"
    except:
        error["text"] = "Enter choice"


window = Tk()
window.geometry("580x550")
window.config(bg = '#89CFF0')
my_img = ImageTk.PhotoImage(Image.open("G:\\img1.jpeg"))
my_label = Label(image = my_img)
my_label.place(x = 0, y = 0, width = 580, height = 550)

error = Message(text="", width = 160)
error.place(x = 10, y = 10)
error.config(bg="white", padx = 0)
#Heading label
label0 = Label(text = "Hotel ABC ",font = ('Italic',30,'bold'))
label0.place(x = 30, y = 10, width = 500, height = 50)
label0.config(bg="lightgreen", padx=0)

error = Message(text="", width = 160)
error.place(x = 10, y = 10)
error.config(bg="black", padx = 0)

#First Name
label1 = Label(text = "Enter First Name: ",font = ('Times',15,'bold'))
label1.place(x = 30, y = 80, height = 30)
label1.config(bg="white", padx=0)
first = Entry(text = "")
first.place(x = 250, y = 80, width = 200, height = 30)

#Last Name 
label2 = Label(text = "Enter Last Name: ",font = ('Times',15,'bold'))
label2.place(x = 30, y = 130)
label2.config(bg="white", padx=0)
last = Entry(text = "")
last.place(x = 250, y = 130, width = 200, height = 30)

#Aadhar Number
label3 = Label(text = "Enter Aadhar Number: ",font = ('Times',15,'bold'))
label3.place(x = 30, y = 180)
label3.config(bg="white", padx=0)
aadhar = Entry(text = "")
aadhar.place(x = 250, y = 180, width = 200, height = 30)

#Phone Number
label4 = Label(text = "Enter Phone Number: ",font = ('Times',15,'bold'))
label4.place(x = 30, y = 230)
label4.config(bg="white", padx=0)
phone = Entry(text = "")
phone.place(x = 250, y = 230, width = 200, height = 30)

#Room Type
label5 = Label(text = "Select Room Type:",font = ('Times',15,'bold'))
label5.place(x = 30, y = 280)
label5.config(bg="white", padx=0)
option = ['Non Ac room','Ac Room','Delux Room','Private Suite']
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(window, clicked, *option)
drop.place(x = 250, y = 280, width = 200, height = 30)

#No of Days
label6 = Label(text = "Enter Days of stay: ",font = ('Times',15,'bold'))
label6.place(x = 30, y = 330)
label6.config(bg="white", padx=0)
days = Entry(text = "")
days.place(x = 250, y = 330, width = 200, height = 30)

#Time of checkin
label7 = Label(text = "Select Check in Time:",font = ('Times',15,'bold'))
label7.place(x = 30, y = 380)
label7.config(bg="white", padx=0)
option1 = ['1','2','3','4','5','6','7','8','9','10','11','12']
option2 = ['am','pm']
click = StringVar()
click.set(option1[0])
drop1 = OptionMenu(window, click, *option1)
drop1.place(x = 30, y = 430, width = 60, height = 20)
click2 = StringVar()
click2.set(option2[0])
drop2 = OptionMenu(window, click2, *option2)
drop2.place(x = 100, y = 430, width = 60, height = 20)

#checkin date
label8 = Label(text = "Select check in date: ",font = ('Times',15,'bold'))
label8.place(x = 300, y = 380)
label8.config(bg="white", padx=0)
option3 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
option4 = ['1','2','3','4','5','6','7','8','9','10','11','12']
option5 = ['2022','2023']
click3 = StringVar()
click3.set(option3[0])
drop3 = OptionMenu(window, click3, *option3)
drop3.place(x = 300, y = 430, width = 50, height = 20)
click4 = StringVar()
click4.set(option4[0])
drop4 = OptionMenu(window, click4, *option4)
drop4.place(x = 355, y = 430, width = 60, height = 20)
click5 = StringVar()
click5.set(option5[0])
drop5 = OptionMenu(window, click5, *option5)
drop5.place(x = 420, y = 430, width = 60, height = 20)

#Submit Button
button = Button(text = "Submit", command = add_new_user)
button.place(x = 220, y = 480, width = 125, height = 50)

#Staff Entry Button
button = Button(text = "To make staff entry", command = openn)
button.place(x = 400, y = 480, width = 125, height = 50)

#Show Button
button = Button(text = "Show", command = show)
button.place(x = 40, y = 480, width = 125, height = 50)



window.mainloop()
