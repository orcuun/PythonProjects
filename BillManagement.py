from tkinter import*

root = Tk()
root.geometry("1000x500")
root.title("Bizim Gave")
root.resizable(False,False)


def Reset():
    entry_tost.delete(0,END)
    entry_çay.delete(0,END)
    entry_gazoz.delete(0,END)
    entry_limonata.delete(0,END)
    entry_çikolata.delete(0,END)
    entry_su.delete(0,END)
    entry_oralet.delete(0,END)
    entry_soda.delete(0,END)

def Total():
    try: a1 = int(tost.get())
    except: a1 = 0

    try: a2 = int(çay.get())
    except: a2 = 0

    try: a3 = int(gazoz.get())
    except: a3 = 0

    try: a4 = int(limonata.get())
    except: a4 = 0

    try: a5 = int(çikolata.get())
    except: a5 = 0

    try: a6 = int(su.get())
    except: a6 = 0

    try: a7 = int(oralet.get())
    except: a7 = 0

    try: a8 = int(soda.get())
    except: a8 = 0

#Define Cost of Each İtem Per Quantity

    c1 = 50*a1
    c2 = 8*a2
    c3 = 20*a3
    c4 = 30*a4
    c5 = 12*a5
    c6 = 5*a6
    c7 = 15*a7
    c8 = 10*a8


    lbl_total = Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total = Entry(f2,font=("aria",20,"bold"),textvariable=hesap,bd=6,width=15,bg="red")
    entry_total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7+c8
    string_bill = "TL",str("%.2f" %totalcost)
    hesap.set(string_bill)


Label(text="BIZIM GAVE",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menü Card

f=Frame(root,bg="red",highlightbackground="black",highlightthickness=2,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menü",font=("Gabriola",40,"bold"),fg="white",bg="red").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tost ..........................50TL",fg="white",bg="red").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Çay ...........................8TL",fg="white",bg="red").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Gazoz .........................20TL",fg="white",bg="red").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Limonata ......................30TL",fg="white",bg="red").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Çikolata ......................12TL",fg="white",bg="red").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Su ............................5TL",fg="white",bg="red").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Oralet ........................15TL",fg="white",bg="red").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Soda ..........................10TL",fg="white",bg="red").place(x=10,y=290)

#Bıll

f2 = Frame(root,bg="yellow",highlightbackground="black",highlightthickness=2,width=300,height=370)
f2.place(x=690,y=118)

Bill = Label(f2,text="Fiş",font=("calibri",20),bg="yellow")
Bill.place(x=120,y=10)



#Entry Work

f1 = Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

tost = StringVar()
çay = StringVar()
gazoz = StringVar()
limonata = StringVar()
çikolata = StringVar()
su = StringVar()
oralet = StringVar()
soda = StringVar()
hesap = StringVar()

#Label

lbl_tost = Label(f1,font=("aria",16,"bold"),text="Tost",width=12,fg="black")
lbl_çay = Label(f1,font=("aria",16,"bold"),text="Çay",width=12,fg="black")
lbl_gazoz = Label(f1,font=("aria",16,"bold"),text="Gazoz",width=12,fg="black")
lbl_limonata = Label(f1,font=("aria",16,"bold"),text="Limonata",width=12,fg="black")
lbl_çikolata = Label(f1,font=("aria",16,"bold"),text="Çikolata",width=12,fg="black")
lbl_su = Label(f1,font=("aria",16,"bold"),text="Su",width=12,fg="black")
lbl_oralet = Label(f1,font=("aria",16,"bold"),text="Oralet",width=12,fg="black")
lbl_soda = Label(f1,font=("aria",16,"bold"),text="Soda",width=12,fg="black")
lbl_tost.grid(row=1,column=0)
lbl_çay.grid(row=2,column=0)
lbl_gazoz.grid(row=3,column=0)
lbl_limonata.grid(row=4,column=0)
lbl_çikolata.grid(row=5,column=0)
lbl_su.grid(row=6,column=0)
lbl_oralet.grid(row=7,column=0)
lbl_soda.grid(row=8,column=0)

#Entry

entry_tost = Entry(f1,font=("aria",16,"bold"),textvariable=tost,bd=6,width=8,bg="lightyellow")
entry_çay = Entry(f1,font=("aria",16,"bold"),textvariable=çay,bd=6,width=8,bg="lightyellow")
entry_gazoz = Entry(f1,font=("aria",16,"bold"),textvariable=gazoz,bd=6,width=8,bg="lightyellow")
entry_limonata = Entry(f1,font=("aria",16,"bold"),textvariable=limonata,bd=6,width=8,bg="lightyellow")
entry_çikolata = Entry(f1,font=("aria",16,"bold"),textvariable=çikolata,bd=6,width=8,bg="lightyellow")
entry_su = Entry(f1,font=("aria",16,"bold"),textvariable=su,bd=6,width=8,bg="lightyellow")
entry_oralet = Entry(f1,font=("aria",16,"bold"),textvariable=oralet,bd=6,width=8,bg="lightyellow")
entry_soda = Entry(f1,font=("aria",16,"bold"),textvariable=soda,bd=6,width=8,bg="lightyellow")
entry_tost.grid(row=1,column=1)
entry_çay.grid(row=2,column=1)
entry_gazoz.grid(row=3,column=1)
entry_limonata.grid(row=4,column=1)
entry_çikolata.grid(row=5,column=1)
entry_su.grid(row=6,column=1)
entry_oralet.grid(row=7,column=1)
entry_soda.grid(row=8,column=1)

#Buttons

btn_reset = Button(f1,bd=5,fg="black",bg="lightyellow",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=9,column=0)

btn_total = Button(f1,bd=5,fg="black",bg="lightyellow",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=9,column=1)

root.mainloop()