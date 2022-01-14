from tkinter import *

root = Tk()

def myclick(): 
    mylabel3 = Label(root, text=e.get())
    #mylabel3.grid(row=4, column=0)
    mylabel3.pack()


e = Entry(root, width=50)
#e.grid(row=3, column=0)
e.pack()
e.insert(0, "Updated Target Values") ##how to do this in Grey

#define / create object
mylabel = Label(root, text="Netstar Ucount Commission - Manual Upload App")
mylabel2 = Label(root, text="Please Enter all new target values below and then click submit")
mybutton = Button(root, text="Submit", command=myclick, background="Light Grey", foreground="Black")

#Display and use object
#Different methods to display items

#mylabel.pack()

#mylabel.grid(row=0, column=0)
#mylabel2.grid(row=1, column=0)
#mybutton.grid(row=5, column=0, padx=100, pady=50)


mylabel.pack()
mylabel2.pack()
mybutton.pack()

user_input = [] 
user_input.append(e.get())


root.mainloop()
