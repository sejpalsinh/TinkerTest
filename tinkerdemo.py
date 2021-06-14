from tkintercomponents import *
tk_Root = Tk()
def cleartable():
    tbl2.clearTable()

def uncheckall():
    tbl2.uncheckAll()

def addalldata():
    tbl2.refreshData(datalst)

btn = Button(tk_Root, text='Clear All', bd='5',command=cleartable)
btn.pack(side='top')
btn = Button(tk_Root, text='Uncheck All', bd='5',command=uncheckall)
btn.pack(side='top')
btn = Button(tk_Root, text='Add all data', bd='5',command=addalldata)
btn.pack(side='right')

# Gui Logic
headers = ["Id","Password","Pin"]
datalst = [("Sejpal",18,"Rajkot"),("bhagi",18,"Rajkot"),("brij",18,"Rajkot"),("srushti",18,"Rajkot"),("harsh",18,"Rajkot"),("umesh",18,"Rajkot"),("hari",18,"Rajkot"),("aaksah",18,"Rajkot"),("shivbha",18,"Rajkot"),("mayur",18,"Rajkot"),("rashesh",18,"Rajkot"),("jayraj",18,"Rajkot"),("vimal",18,"Rajkot"),("vivek",18,"Rajkot"),("nirav",18,"Rajkot")]
uncheckImg = PhotoImage(file='images/uncheck.png')
checkedImg = PhotoImage(file='images/checked.png')
tbl1 = Table(tk_Root,headers)
tbl2 = CheckboxTable(tk_Root,["Id","Password","Pin"],uncheckImg,checkedImg)
tbl2.refreshData(datalst)
tk_Root.mainloop()
