#  Calc with python tkinter
#  William Dos Santos junqueira

from tkinter import *
import customtkinter as ctk


buttons = [['%', 'CE', 'C', '←'],
  ['⅟ₓ', 'x²', ' ²√x', '÷'],
  ['7', '8', '9', 'x'],
  ['4', '5', '6', '-'],
  ['1', '2', '3', '+'],
  ['', '0', ',', '=']]



class Calc:
    def __init__(self):
        pass


    def doAritimatic(self, expression):
        e = expression.split(' ')


        numbers = e[::2]
        operators = e[1::2]


        n = 1
        x = numbers[0]
        for i, operator in enumerate(operators):
            y = numbers[n]
            x = self.identify_operation(operator, float(x), float(y))
            n += 1

        return x



    # identify the operation and start the desired function
    def identify_operation(self, operator, x, y=0):
        if operator == '+':
             operation = self.sum(x, y)

        elif operator == '-':
            operation = self.subtraction(x, y)

        elif operator == '÷':
            operation = self.division(x, y)

        elif operator == 'x':
            operation = self.multiplication(x, y)

        elif operator == '%':
            operation = self.percentage(x, y)
        return operation


    #  --Basic Operations

    def sum(self, x, y):
        return x+y

    def subtraction(self, x, y):
        return x-y

    def division(self, x, y):
        return x/y

    def multiplication(self, x, y):
        return x*y

    def percentage(self, x, y):
        return (x/100) * y

    #  Other operations
    def square(self, x):
        return x**2

    def sqrt(self, x):
        return x**(.5)

    def invert(self, x):
        return 1/x


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('calc')

        #  frames
        # self.display_frame = Frame(self.master, bg='blue')
        self.buttons_frame = ctk.CTkFrame(self.master)

        # self.display_frame.pack(fill='both', expand='true')
        self.buttons_frame.pack()

        self.draw_buttons()

        self.e = ''
        self.expression = ''


    def draw_buttons(self):
        for x in range(6):
            for y in range(4):
                btn = ctk.CTkButton(self.buttons_frame, text=buttons[x][y], command= lambda x=buttons[x][y]: self.button_callback(x))
                btn.grid(row=x, column=y, padx=4, pady=4)


    def button_callback(self, x):

        show = True


        if x == '=':

            self.expression = self.e
            print('-'*10)
            print('expression -->', self.expression)
            self.result =  Calc().doAritimatic(self.expression.replace(',', '.'))
            print('Result -->', self.result)
            self.e = str(self.result)


        elif x in '+-x÷%':
            if self.e[-2:]  in ' + - x ÷ % ':
                pass

            else:
                self.e += ' '+x+' '
                self.expression = self.e

        elif x == '←':
            self.e = self.e[:-1]


        elif x == 'CE':
            self.expression = ''
            self.e = str(self.result)

        elif x == 'C':
            self.expression = ''
            self.e = '0'

        elif x == ' ²√x':

            try:
                self.e.replace(',', '.')
                e = float(self.e)
                self.result = Calc().sqrt((e))
                print('Result -->', self.result)
                self.e = str(self.result)


            except:
                show = False

        elif x == 'x²':
            try:
                self.e.replace(',', '.')
                e = float(self.e)
                self.result = Calc().square((e))
                print('Result -->', self.result)
                self.e = str(self.result)

            except:
                show = False

        elif x == '⅟ₓ':
            try:
                self.e.replace(',', '.')
                e = float(self.e)
                self.result = Calc().invert((e))
                print('Result -->', self.result)
                self.e = str(self.result)

            except:
                show = False




        else:
            if self.e == '0':
                self.e = x
            else:
                self.e += x


        if show: print(self.e)




app = App()
app.mainloop()
