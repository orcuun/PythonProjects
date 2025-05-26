from tkinter import*
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if ( username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")

    elif (username=="mrorcun6" and password=="mrorcun64"):    
        messagebox.showinfo("","login sucess")

    else:
        messagebox.showinfo("","incorrect username and password")    


root = Tk()
root.title("Login")
root.geometry("500x300")


global entry1
global entry2

Label(root,text="Username").place(x=150,y=25)
Label(root,text="Password").place(x=150,y=100)


entry1 = Entry(root,bd=10)
entry1.place(x=150,y=50)

entry2 = Entry(root,bd=10)
entry2.place(x=150,y=125)

Button(root,text="Login",command=login,height=3,width=13,bd=5).place(x=150,y=200)

mainloop()