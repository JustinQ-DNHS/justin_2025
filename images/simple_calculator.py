import tkinter as tk
from tkmacosx import Button as button
from tkinter import ttk

class calculator:
    def __init__(self):
        # Styling for window
        self.colors = {
            'body': {'bg': 'black'},
            'num_btn': {'bg': '#262624', 'fg': '#FFFFFF', 'font': ('Arial', 18)},
            'operator_btn': {'bg': 'blue', 'fg': '#FFFFFF', 'font': ('Arial', 18)},
            'entry': {'bg': '#262624', 'fg': '#ffffff', 'font': ('Arial', 26)},
            'text': {'bg': 'black', 'fg': '#ffffff', 'font': ('Arial', 30)},
            'frame': {'bg': 'black'}
        }

        # Sets the inital parameters for the window
        self.root = tk.Tk()
        self.root.config(**self.colors['body'])
        self.root.geometry('400x400')
        self.root.title("Simple Calculator")

        self.label = tk.Label(self.root, text="Calculator!", **self.colors['text'])
        self.label.pack(pady=10)

        # Creates a entry box at the top of window to display output
        self.entry_value = tk.StringVar()
        self.output = tk.Entry(self.root,
                                font=self.colors['entry']['font'],
                                bg=self.colors['entry']['bg'],
                                fg=self.colors['entry']['fg'],
                                readonlybackground=self.colors['entry']['bg'],
                                justify='right',
                                textvariable=self.entry_value,
                                state='readonly')
        self.output.pack(padx=25, fill='x')
        # Creates a frame to organize buttons in
        self.btn_frame = tk.Frame(self.root, width=400, **self.colors['frame'])
        # Sets the weight of the buttons with numbers higher
        for i in range(3):
            self.btn_frame.columnconfigure(i, weight=2)
        # Sets the weight of the operators to be less
        self.btn_frame.columnconfigure(3, weight=1)
        # Inserts the frame into the window
        self.btn_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=25)
        # Calls the build_btn function to create hte buttons
        self.build_btn()
        # Loops the code to create the window
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.mainloop()
    
    # Function that puts all the buttons inside the btn_frame
    def build_btn(self):
        row = 1
        column = 0
        # Creates the buttons from 1-9 in the frame
        for i in range(9):
            btn = button(self.btn_frame, text=str(i+1), **self.colors['num_btn'], command=lambda value=i+1: self.update_output(value))
            btn.grid(row=row, column=column, sticky=tk.E+tk.W)
            column += 1
            if column == 3:
                column = 0
                row += 1
        # Adds the remaining buttons
        operators = ['C', '+', '-', '*', '/', '0', '.', '=', '(', ')', '%'] # the order this is done in is extremely important
        # Adds the operators
        for i in range(5):
            btn = button(self.btn_frame, text=operators[i], **self.colors['operator_btn'], command=lambda value=operators[i]: self.update_output(value))
            btn.grid(row=i, column=3, sticky=tk.E+tk.W)
        # Addes the bottom 3 buttons
        for i in range (3):
            btn = button(self.btn_frame, text=operators[i+5], **self.colors['num_btn'], command=lambda value=operators[i+5]: self.update_output(value))
            btn.grid(row=4, column=i, sticky=tk.E+tk.W)
            btn1 = button(self.btn_frame, text=operators[i+8], **self.colors['num_btn'], command=lambda value=operators[i+8]: self.update_output(value))
            btn1.grid(row=0, column=i, sticky=tk.E+tk.W)
        # Must use lambda due to the way command works, since it only calls a function on press when you don't include the ()
    
    # Entry Value Updater
    def update_output(self, value):
        current_value = self.output.get()
        if current_value == "Error" or current_value == '0':
            self.entry_value.set('')
            current_value = ''
        #elif [value != '*' and current_value == '0']:
        #    self.entry_value.set('')
        #    current_value = ''
        if value == '=':
            self.calculate_output()
        elif value == 'C':
            self.entry_value.set('')
        elif value == 'delete':
            self.entry_value.set(self.output.get()[:-1])
        else:
            if current_value:
                if current_value[-1] == '%':
                    self.entry_value.set(f'{current_value}*{str(value)}')
                else:
                    self.entry_value.set(current_value + str(value))
            else:
                self.entry_value.set(value)

    # When '=' is pressed evaluates current string
    def calculate_output(self):
        current_value = self.output.get()
        current_value = current_value.replace('(', '*(')
        try:
            output = round(eval(current_value.replace('%', '*0.01')), 4)
            self.entry_value.set(output)
        except Exception as e:
            self.entry_value.set("Error")

    # Adds keyboard compatibility
    def on_key_press(self, event):
        if event.keysym in [str(i) for i in range(10)]:
            self.update_output(event.char)
        elif event.keysym in ['asterisk', 'parenleft', 'parenright', 'plus', 'minus', 'percent', 'slash', 'period']:
            self.update_output(event.char)
        elif event.keysym == 'Return':
            self.calculate_output()
        elif event.keysym == 'BackSpace':
            if event.state == 1:
                self.update_output('C')
            else:
                self.update_output('delete')

calculator()