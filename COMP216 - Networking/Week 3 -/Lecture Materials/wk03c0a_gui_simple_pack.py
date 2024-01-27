# filename: wk03c0_gui_simple.py
# by Narendra for COMP216 (Aug 2020)

# Creates a simple window with a few widgets
# and uses the pack layout manager

# expand − When set to true, widget expands to fill any 
#  space not otherwise used in widget's parent.

# fill − Determines whether widget fills any extra space 
#  allocated to it by the packer, or keeps its own minimal dimensions: 
#    NONE (default), 
#    X (fill only horizontally), 
#    Y (fill only vertically), 
#    or BOTH (fill both horizontally and vertically).

# side − Determines which side of the parent widget packs against: 
#    TOP (default), 
#    BOTTOM, 
#    LEFT, 
#    or RIGHT.

import tkinter as tk           #using an alias for tkinter

HEIGHT = 250
WIDTH = 250
H_OFFSET = 600
V_OFFSET = 400

root = tk.Tk()
root.geometry(f'{WIDTH}x{HEIGHT}+{H_OFFSET}+{V_OFFSET}')
# root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Grade App')

physicsLabel = tk.Label(root, text='Physics')
physicsEntry = tk.Entry(root, bd=5)

mathsLabel = tk.Label(root, text='Maths')
mathsEntry = tk.Entry(root, bd=5)

addButton = tk.Button(root, text='Add')

totalLabel = tk.Label(root, text='Total')
totalEntry = tk.Entry(root, bd=5)

physicsLabel.pack()
physicsEntry.pack()
mathsLabel.pack()
mathsEntry.pack()
totalLabel.pack()
totalEntry.pack()
addButton.pack()

# physicsLabel.pack()
# physicsEntry.pack(fill='x')
# mathsLabel.pack()
# mathsEntry.pack(fill='x')
# totalLabel.pack()
# totalEntry.pack(fill='x')
# addButton.pack()

root.mainloop()