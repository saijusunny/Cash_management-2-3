# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x300")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Company")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('1',))
tree.insert('', 'end', text="1", values=('','jk'))
tree.insert('', 'end', text="2", values=('2', 'Hyundai'))
tree.insert('', 'end', text="3", values=('3', 'Tesla'))
tree.insert('', 'end', text="4", values=('4', 'Wolkswagon'))
tree.insert('', 'end', text="5", values=('5', 'Tata Motors'))
tree.insert('', 'end', text="6", values=('6', 'Renault'))

tree.pack()

win.mainloop()