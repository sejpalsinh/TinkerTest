import tkinter as tk
from tkintercomponents import *

tk_Root = tk.Tk()
tk_Root.title("Tab Widget")
tabControl = ttk.Notebook(tk_Root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")



# Gui Logic
headers = ["Id","Password","Pin"]
datalst = [("Sejpal",18,"Rajkot"),("bhagi",18,"Rajkot"),("brij",18,"Rajkot"),("srushti",18,"Rajkot"),("harsh",18,"Rajkot"),("umesh",18,"Rajkot"),("hari",18,"Rajkot"),("aaksah",18,"Rajkot"),("shivbha",18,"Rajkot"),("mayur",18,"Rajkot"),("rashesh",18,"Rajkot"),("jayraj",18,"Rajkot"),("vimal",18,"Rajkot"),("vivek",18,"Rajkot"),("nirav",18,"Rajkot")]
uncheckImg = PhotoImage(file='images/uncheck.png')
checkedImg = PhotoImage(file='images/checked.png')
tbl1 = Table(tab1,headers,datalst)
tbl2 = CheckboxTable(tab2,["Id","Password","Pin"],uncheckImg,checkedImg,20,30)
tbl2.refreshData(datalst)

tk_Root.mainloop()