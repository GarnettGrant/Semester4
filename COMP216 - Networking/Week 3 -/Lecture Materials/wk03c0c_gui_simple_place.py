# filename: wk03c0_gui_simple.py
# by Narendra for COMP216 (Aug 2020)

# Creates a simple window with a few widgets
# and uses the place layout manager

# anchor − The exact spot of widget other options refer to: 
#  may be N, E, S, W, NE, NW, SE, or SW, compass directions 
#  indicating the corners and sides of widget; 
#  default is NW (the upper left corner of widget).

# bordermode − INSIDE (the default) to indicate that other 
#  options refer to the parent's inside (ignoring the parent's border); 
#  OUTSIDE otherwise.

# height, width − Height and width in pixels.

# relheight, relwidth − Height and width as a float 
#  between 0.0 and 1.0, as a fraction of the height 
#  and width of the parent widget.

# relx, rely − Horizontal and vertical offset as a float 
#  between 0.0 and 1.0, as a fraction of the height 
#  and width of the parent widget.

# x, y − Horizontal and vertical offset in pixels.


import tkinter as tk           #using an alias for tkinter

root = tk.Tk()
root.geometry('250x250+10+10')
root.title('Grade App')

physicsLabel = tk.Label(root, text='Physics')
physicsEntry = tk.Entry(root, bd=5)
mathsLabel = tk.Label(root, text='Maths')
mathsEntry = tk.Entry(root, bd=5)
totalLabel = tk.Label(root, text='Total')
totalEntry = tk.Entry(root, bd=5)
addButton = tk.Button(root, text='Add')

# physicsEntry.place(x=60,y=10)
# physicsLabel.place(x=10, y=10)
# mathsLabel.place(x=10, y=50)
# mathsEntry.place(x=60,y=50)
# totalLabel.place(x=10, y=150)
# totalEntry.place(x=60,y=150)
# addButton.place(x=100,y=100)

physicsLabel.place(relx=0.04, rely=0.04)
physicsEntry.place(relx=0.24, rely=0.04)
mathsLabel.place(relx=0.04, rely=0.20)
mathsEntry.place(relx=0.24, rely=0.20)
totalLabel.place(relx=0.04, rely=0.60)
totalEntry.place(relx=0.24, rely=0.60)
addButton.place(relx=0.40, rely=0.40)


root.mainloop()