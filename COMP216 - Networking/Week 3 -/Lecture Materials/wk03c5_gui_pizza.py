from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class PizzaGUI(Tk):

    def __init__( self, title : str) -> None:
        Tk.__init__( self )
        self.title( title )
        self.create_styles()
        Canvas(self, width=560, height=300).pack()
        containter = Frame(self)
        # containter['borderwidth'] = 3
        containter['relief'] = 'ridge'
        containter.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.create_variables()
        self.create_ui(containter)
        self.init_ui()

    def create_styles(self):
        style = Style()
        # style.theme_use('classic')
        style.configure('.', background='aquamarine', foreground='green')#, padding=(20, 10, 10, 10))

    def create_variables(self):
        self.crust = StringVar()
        self.name = StringVar()
        self.address = StringVar()  
        self.size = StringVar()

        self.cheese = StringVar()  
        self.olive = StringVar()  
        self.pepper = StringVar()
        self.mushroom = StringVar()
        self.pineapple = StringVar()
        self.mushroom = StringVar()
        self.spinach = StringVar()
   
        self.toppings = [self.cheese, self.olive, self.pepper, self.mushroom, self.pineapple, self.spinach]

    def init_ui(self):
        self.crust.set('Regular')
        self.name.set('Narendra')
        self.address.set('Progress Ave.')
        self.size.set('Medium')
        for var in self.toppings:
            var.set('')
        self.cheese.set('cheese')

    def ok_handler(self):
        toppings = str.join(', ', list(filter(None, [string_var.get() for string_var in self.toppings])))
        output = f'''
Name    : {self.name.get()}
Address : {self.address.get()}
Size    : {self.size.get()}
Crust   : {self.crust.get()}
Toppings: {toppings}

'''
        messagebox.showinfo('Order Information', output)

    def create_ui(self, parent):
        #row 1
        label = Label(parent, text='Pizza Order')
        label.place(relx=0.25, rely=0.008, relwidth=0.5, relheight=0.2)
       
        #row 2
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.215, relwidth=0.94, relheight=0.1)
        label = Label(frame, text='Name')
        label.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.98)
        entry = Entry(frame, textvariable=self.name)
        entry.place(relx=0.35, rely=0.01, relwidth=0.50, relheight=0.98)

        #row 2
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.325, relwidth=0.94, relheight=0.1)
        label = Label(frame, text='Address')
        label.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.98)
        entry = Entry(frame, textvariable=self.address)
        entry.place(relx=0.35, rely=0.01, relwidth=0.50, relheight=0.98)

        #row 4
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.435, relwidth=0.94, relheight=0.1)
        label = Label(frame, text='Size')
        label.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.98)
        cbox = Combobox(frame, textvariable=self.size)
        cbox['values'] = ('Small', 'Medium', 'Large', 'x-Large')
        cbox.place(relx=0.35, rely=0.01, relwidth=0.50, relheight=0.98)
       
        #row 5
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.545, relwidth=0.94, relheight=0.1)
        label = Label(frame, text='Crust')
        label.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.98)
        cbox = Combobox(frame, textvariable=self.crust)
        cbox['values'] = ('Regular', 'Whole Wheat', 'Glutten Free')
        cbox.place(relx=0.35, rely=0.01, relwidth=0.50, relheight=0.98)

        #row 6
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.655, relwidth=0.94, relheight=0.2)
        label = Label(frame, text='Toppings')
        label.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.45)
        chkbtn = Checkbutton(frame, text='Cheese', variable=self.cheese, onvalue='cheese', offvalue='')
        chkbtn.place(relx=0.35, rely=0.01, relwidth=0.30, relheight=0.45)
        chkbtn = Checkbutton(frame, text='Olive', variable=self.olive, onvalue='olive', offvalue='')
        chkbtn.place(relx=0.504, rely=0.01, relwidth=0.30, relheight=0.45)
        chkbtn = Checkbutton(frame, text='Pepper', variable=self.pepper, onvalue='pepper', offvalue='')
        chkbtn.place(relx=0.743, rely=0.01, relwidth=0.30, relheight=0.45)

        chkbtn = Checkbutton(frame, text='Mushroom', variable=self.mushroom, onvalue='mushroom', offvalue='')
        chkbtn.place(relx=0.35, rely=0.51, relwidth=0.30, relheight=0.45)
        chkbtn = Checkbutton(frame, text='Pineapple', variable=self.pineapple, onvalue='pineapple', offvalue='')
        chkbtn.place(relx=0.504, rely=0.51, relwidth=0.30, relheight=0.45)
        chkbtn = Checkbutton(frame, text='Spinach', variable=self.spinach, onvalue='spinach', offvalue='')
        chkbtn.place(relx=0.743, rely=0.51, relwidth=0.30, relheight=0.45)

        #row 7
        frame = Frame(parent)
        frame.place(relx=0.03, rely=0.865, relwidth=0.94, relheight=0.1)
        ok = Button(frame, text='Ok', command=self.ok_handler)
        ok.place(relx=0.0167, rely=0.01, relwidth=0.30, relheight=0.98)
        reset = Button(frame, text='Reset', command=self.init_ui)
        reset.place(relx=0.35, rely=0.01, relwidth=0.30, relheight=0.98)
        exit = Button(frame, text='Exit', command=self.quit)
        exit.place(relx=0.683, rely=0.01, relwidth=0.30, relheight=0.98)

app = PizzaGUI('My Awesome GUI')
app.mainloop()


