# filename: wk03c0_gui_simple.py
# by Narendra for COMP216 (Aug 2020)

# Creates a simple window with a few widgets
# and uses the grid layout manager

# column − The column to put widget in
#  default 0 (leftmost column).

# columnspan − How many columns widgetoccupies
#  default 1.

# ipadx, ipady − How many pixels to pad widget, 
#  horizontally and vertically, inside widget's borders.

# padx, pady − How many pixels to pad widget, 
#  horizontally and vertically, outside v's borders.

# row − The row to put widget in; 
#  default the first row that is still empty.

# rowspan − How many rows the widget occupies
#  default 1.

# sticky − What to do if the cell is larger than widget. 
#  By default, with sticky='', widget is centered in its cell. 
#  sticky may be the string concatenation of zero or more of 
#  N, E, S, W, NE, NW, SE, and SW, compass directions indicating 
#  the sides and corners of the cell to which widget sticks.



import tkinter as tk           #using an alias for tkinter

root = tk.Tk()
root.geometry('250x250+10+10')
root.title('Grade App')

physicsLabel = tk.Label(root, text='Physics')
physicsEntry = tk.Entry(root, bd=5)
mathsLabel = tk.Label(root, text='Maths')
mathsEntry = tk.Entry(root, bd=5)
addButton = tk.Button(root, text='Add')
totalLabel = tk.Label(root, text='Total')
totalEntry = tk.Entry(root, bd=5)

# physicsEntry.place(x=60,y=10)
# physicsLabel.place(x=10, y=10)
# mathsLabel.place(x=10, y=50)
# mathsEntry.place(x=60,y=50)
# addButton.place(x=100,y=100)
# totalLabel.place(x=10, y=150)
# totalEntry.place(x=60,y=150)

physicsLabel.grid(column=0, row=1)
physicsEntry.grid(column=1, row=1)
mathsLabel.grid(column=0, row=2)
mathsEntry.grid(column=1, row=2)
addButton.grid(column=0, row=3, columnspan=2)
totalLabel.grid(column=0, row=4)
totalEntry.grid(column=1, row=4)

root.mainloop()