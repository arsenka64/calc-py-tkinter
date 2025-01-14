from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Калькутор")
root.geometry("180x300")
root.resizable(False,False)
root.iconbitmap('icon.ico')

answer = Entry(root,width=27,bd =10)

def step_2():
    cur = answer.get()
    answer.delete(0, END)
    try:
        result1 = float(cur) ** 2
        result = str(result1)
        answer.insert(END, result)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")

def delete_entry():
    answer.delete(0, END)

def null(num):
    cur = answer.get()
    answer.delete(0,END)
    answer.insert(END, cur + num)

def remove_last_character():
    current_text = answer.get()
    answer.delete(len(current_text) - 1)

def calculate():
    try:
        expression = answer.get()
        result = eval(expression)
        answer.delete(0,END)
        answer.insert(0, str(result))
    except Exception:
        messagebox.showerror("Ошибка","Ошибка")


buttonEnt = Button(root, text="=",width=4,height=2,font=30,bg='#B22222',command=calculate)
button0 = Button(root, text="0",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null("0"))
button1 = Button(root, text="1",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null("1"))
button2 = Button(root, text="2",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null("2"))
button3 = Button(root, text="3",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null("3"))
button4 = Button(root, text="4",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null("4"))
button5 = Button(root, text="5",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null('5'))
button6 = Button(root, text="6",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null('6'))
button7 = Button(root, text="7",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null('7'))
button8 = Button(root, text="8",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null('8'))
button9 = Button(root, text="9",width=4,height=2,font=30,bg='#00FF7F',command=lambda: null('9'))

buttonMinus = Button(root, text="-",width=4,height=2,bg='#FF8C00',font=30,command=lambda: null(' - '))
buttonPlus = Button(root, text="+",width=4,height=2,bg='#FF8C00',font=30,command=lambda: null(' + '))
buttonVozved = Button(root, text="^",width=4,height=2,bg='#FF8C00',font=30,command=lambda: null(' ** '))
buttonX2 = Button(root, text="x²",width=4,height=2,bg='#FFFACD',font=30,command=step_2)
buttonDot = Button(root, text=".",width=4,height=2,bg='#FF1493',font=30,command=lambda: null('.'))
buttonNazad = Button(root, text="⏎",width=4,height=2,bg='#8B008B',font=30,command=remove_last_character)
buttonX = Button(root, text="×",width=4,height=2,bg='#FF8C00',font=30,command=lambda: null(' * '))
buttonRazdel = Button(root, text="÷",width=4,height=2,bg='#FF8C00',font=30,command=lambda: null(' / '))
buttonC = Button(root, text="C",width=4,height=2,bg='#FFFAFA',font=30,command=lambda:delete_entry())

answer.place(x=0,y=10)
buttonVozved.place(x=135,y=50)
buttonPlus.place(x=135,y=100)
buttonMinus.place(x=135,y=150)
buttonEnt.place(x=135,y=250)
buttonNazad.place(x=135,y=200)

button3.place(x=90,y=50)
button6.place(x=90,y=100)
button9.place(x=90,y=150)
buttonDot.place(x=90,y=200)
buttonC.place(x=90,y=250)

button2.place(x=45,y=50)
button5.place(x=45,y=100)
button8.place(x=45,y=150)
button0.place(x=45,y=200)
buttonRazdel.place(x=45,y=250)

button1.place(x=0,y=50)
button4.place(x=0,y=100)
button7.place(x=0,y=150)
buttonX2.place(x=0,y=200)
buttonX.place(x=0,y=250)

root.mainloop()