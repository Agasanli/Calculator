import tkinter as tk
import turtle

def sum():
    if num1.get().isdigit() and num2.get().isdigit():
        n1 = float(num1.get())
        n2 = float(num2.get())
        result.configure(text=str(n1 + n2))
    
def output():
    if num1.get().isdigit() and num2.get().isdigit():
        n1 = float(num1.get())
        n2 = float(num2.get())
        result.configure(text=str(n1 - n2))
    
def multiply():
    if num1.get().isdigit() and num2.get().isdigit():
        n1 = float(num1.get())
        n2 = float(num2.get())
        result.configure(text=str(n1 * n2))
    
def divide():
    if num1.get().isdigit() and num2.get().isdigit():
        n1 = float(num1.get())
        n2 = float(num2.get())
        result.configure(text=str(n1 / n2))

screen = tk.Tk()
screen.title("Calculator")
screen.geometry("420x400")
screen.config(bg='#5F9EA0')

result = tk.Label(screen, text= "Result", fg="red", font="Arial 16 bold", width=35, justify="center")
result.place(x=-20, y=30)

num1 = tk.Entry(screen, font="Courier 16 bold", fg="green",width=20, justify="right")
num1.place(x=70,y=80)
num2 = tk.Entry(screen, font="Courier 16 bold", fg="green",width=20, justify="right")
num2.place(x=70,y=120)

key1 = tk.Button(screen,text= "+", font="Courier 16 bold",width=10, command=sum)
key1.place(x=130, y= 160)
key2 = tk.Button(screen,text= "-", font="Courier 16 bold",width=10, command=output)
key2.place(x=130, y= 200)
key3 = tk.Button(screen,text= "*", font="Courier 16 bold",width=10, command=multiply)
key3.place(x=130, y= 240)
key4 = tk.Button(screen,text= "/", font="Courier 16 bold",width=10, command=divide)
key4.place(x=130, y= 280)

num1.focus

screen.mainloop()