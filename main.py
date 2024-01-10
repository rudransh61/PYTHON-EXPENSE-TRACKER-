import tkinter
from tkinter import messagebox


# 

expense = {}

ct= 1

def inputError():
    if enterExpenseField.get() == "" :
        messagebox.showerror("Input Error")
         
        return 0
     
    return 1

def show():
    global expense
    TextArea.delete(1.0, tkinter.END)
    total = 0
    for key in expense:
        try :
            total += int(expense[key])
            TextArea.insert('end -1 chars', "[ " + str(key) + " ] " + expense[key] + "\n")
        except :
            expense[key] = 0 
    
    Total.config(text="Total : "+str(total))
        

    
    
def insert():
    global ct
    global expense
    value = inputError()
    
    if value == 0 :
        return
    
    content1 = enterExpenseField.get()
    content2 = enterExpenseNumberField.get()
    
    expense.update({enterExpenseField.get() : enterExpenseNumberField.get()}) 
    # print(content1)
    # print(content2)
    # print(expense)
    
    show()


#

win = tkinter.Tk()
win.configure(background = "light green")
win.title("ToDo App")
win.geometry("300x400")

Submit = tkinter.Button(win, text = "Submit", fg = "Black", bg = "light Blue", command = insert)
Total = tkinter.Label(win, text = "Total : ", bg = "light green")
enterExpense = tkinter.Label(win, text = "Enter Your Task", bg = "light green")
enterExpenseField = tkinter.Entry(win)
enterExpenseNumberField = tkinter.Entry(win)
TextArea = tkinter.Text(win, height = 5, width = 30, font = "lucida 13")

Total.grid(row = 5, column = 5)
enterExpense.grid(row = 0, column = 5)
enterExpenseField.grid(row = 1, column = 5, ipadx = 50)
enterExpenseNumberField.grid(row = 2, column = 5, ipadx = 50)
Submit.grid(row = 3, column = 5)
TextArea.grid(row = 4, column = 5, padx = 10, sticky = tkinter.W)

win.mainloop()
