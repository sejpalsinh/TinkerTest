import tkinter as tk
from tkintercomponents import *

tk_Root = tk.Tk()

cusTable = CutomTable(tk_Root,["Select","Id","Password","Pin"])
recorddata = CustomData(cusTable.getFrame(),False,"TS3547","Zerodha","122301")
for i in range(7):
    cusTable.addRecord(CustomData(cusTable.getFrame(),False,"TS3547","Zerodha","122301"))

tk_Root.mainloop()