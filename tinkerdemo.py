from tkinter import *
from tkintercomponents import Table
tk_Root = Tk()

# Gui Logic
tk_Root.minsize(1000, 600)
tk_Root.maxsize(1000, 600)
headers = ["Name","Age","City"]
datalst = [("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot")]
tbl = Table(tk_Root,datalst,headers)
tk_Root.mainloop()
