#  Calc with python tkinter
#  William Dos Santos junqueira


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


    #  ---------Basic Operations-------------

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

    #  -----------------Other operations---------------
    def square(self, x):
        return x**2

    def sqrt(self, x):
        return x**(.5)

    def invert(self, x):
        return 1/x




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # 21
        self.title('calc')
        self.geometry('327x470')
        self.resizable(0, 0)

        #  frames
        self.display_frame = ctk.CTkFrame(self.master, fg_color='#20201e', width=321, height=168)
        self.buttons_frame = ctk.CTkFrame(self.master, fg_color='#20201e')

        self.display_frame.grid(row=0, column=0, padx=3, pady=5)
        self.buttons_frame.grid(row=1, column=0, padx=3,)


        self.draw_buttons()

        self.e = ''
        self.expression = ''






    #  Draw the buttons on screen
    def draw_buttons(self):
        for x in range(6):
            for y in range(4):
                btn = ctk.CTkButton(self.buttons_frame, text=buttons[x][y], width=78, height=46, fg_color='#3c3b38', command= lambda x=buttons[x][y]: self.button_callback(x))
                btn.grid(row=x, column=y, padx=1, pady=1)




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


if __name__ == '__main__':
    app = App()
    app.mainloop()
