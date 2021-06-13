from tkinter import *
from tkintercomponents import *
tk_Root = Tk()


# Gui Logic
headers = ["Name","Age","City"]
datalst = [("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot"),("Sejpal",18,"Rajkot")]
def checkboxtable():
    coldDataId = []
    total_columns = len(datalst[0])
    for colId in range(1, total_columns + 1):
        coldDataId.append("#" + str(colId))
    s = ttk.Treeview(columns=tuple(coldDataId), selectmode='browse')
    s.heading('#0', text='Select')
    headerCounter = 0
    for header in coldDataId:
        print(header)
        s.heading(header, text=headers[headerCounter])
        headerCounter = headerCounter + 1
    s.pack(side="left")
    v = PhotoImage(file='images/uncheck.png')
    for data in datalst:
        s.insert('', 'end', values=tuple(data), image=v)
checkboxtable()
tk_Root.mainloop()
