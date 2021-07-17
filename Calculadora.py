from tkinter import *


def func_button1():
    screen.insert(END, "1")


def func_button2():
    screen.insert(END, "2")


def func_button3():
    screen.insert(END, "3")


def func_button4():
    screen.insert(END, "4")


def func_button5():
    screen.insert(END, "5")


def func_button6():
    screen.insert(END, "6")


def func_button7():
    screen.insert(END, "7")


def func_button8():
    screen.insert(END, "8")


def func_button9():
    screen.insert(END, "9")


def func_button0():
    screen.insert(END, "0")


def func_button_plus():
    screen.insert(END, "+")


def func_button_minus():
    screen.insert(END, "-")


def func_button_multiply():
    screen.insert(END, "*")


def func_button_divide():
    screen.insert(END, "/")


def func_button_clear():
    screen.delete(0, END)


def func_button_equal():
    expression = screen.get()
    for i in expression:
        if not i.isnumeric():
            operator = i
            operator_index = expression.index(i)
            number1 = int(expression[:operator_index])
            number2 = int(expression[operator_index+1:])
            if operator == "+":
                result = number1 + number2
                screen.delete(0, END)
                screen.insert(0, result)
            elif operator == "-":
                result = number1 - number2
                screen.delete(0, END)
                screen.insert(0, result)
            elif operator == "*":
                result = number1 * number2
                screen.delete(0, END)
                screen.insert(0, result)
            elif operator == "/":
                result = number1 / number2
                screen.delete(0, END)
                screen.insert(0, result)


# Janela principal
root = Tk()
root.title("Calculadora")
root.geometry("235x200")
root.resizable(False, False)

# Visor
screen = Entry(root, width=28)
screen.place(x=4, y=5)

# Botões
button1 = Button(root, text="1", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button1)
button1.place(x=5, y=35)

button2 = Button(root, text="2", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button2)
button2.place(x=62, y=35)

button3 = Button(root, text="3", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button3)
button3.place(x=120, y=35)

button_plus = Button(root, text="+", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_plus)
button_plus.place(x=180, y=35)

button4 = Button(root, text="4", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button4)
button4.place(x=5, y=73)

button5 = Button(root, text="5", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button5)
button5.place(x=62, y=73)

button6 = Button(root, text="6", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button6)
button6.place(x=120, y=73)

button_minus = Button(root, text="-", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_minus)
button_minus.place(x=180, y=73)

button7 = Button(root, text="7", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button7)
button7.place(x=5, y=112)

button8 = Button(root, text="8", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button8)
button8.place(x=62, y=112)

button9 = Button(root, text="9", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button9)
button9.place(x=120, y=112)

button_multiply = Button(root, text="*", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_multiply)
button_multiply.place(x=180, y=112)

button_clear = Button(root, text="Clear", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_clear)
button_clear.place(x=5, y=150)

button0 = Button(root, text="0", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button0)
button0.place(x=62, y=150)

button_equal = Button(root, text="=", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_equal)
button_equal.place(x=120, y=150)

button_divide = Button(root, text="/", width=5, bg="DarkOrchid4", fg="white smoke", command=func_button_divide)
button_divide.place(x=180, y=150)

root.mainloop()
