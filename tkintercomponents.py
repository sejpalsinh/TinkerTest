from tkinter import *
from tkinter import ttk
import tkinter as tk

class Table:
    def __init__(self, root,headinglst,datalst=[], tableside='right', tableheading = "headings", colWidth=90):
        total_rows = len(datalst)
        total_columns = len(headinglst)
        self.treetable = ttk.Treeview(root, selectmode='browse')
        self.treetable.pack(side=tableside)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.treetable.yview)
        verscrlbar.pack(side=tableside, fill='x')
        self.treetable.configure(xscrollcommand=verscrlbar.set)
        self.treetable["columns"] = list(range(total_columns))
        self.treetable['show'] = tableheading
        for col in range(total_columns):
            self.treetable.column(col, width=colWidth, anchor='c')
            self.treetable.heading(col, text=headinglst[col])
        for row in range(total_rows):
            self.treetable.insert("", 'end', values=datalst[row])

class CheckboxTable:
    def __init__(self,root,headers,uncheckImg,checkImg,xPos,yPos,datalst=[],colWidth=90):
        self.checkedImg = checkImg
        self.selectedUsers = []
        self.uncheckedImg = uncheckImg
        coldDataId = []
        total_columns = len(headers)
        for colId in range(1, total_columns + 1):
            coldDataId.append("#" + str(colId))
        self.treetable = ttk.Treeview(columns=tuple(coldDataId),selectmode='browse')
        self.treetable.bind("<<TreeviewSelect>>", self.OnClick)
        self.treetable.heading('#0', text='Select')
        self.treetable.column('#0', width=colWidth, anchor='c')
        headerCounter = 0
        for header in coldDataId:
            self.treetable.heading(header, text=headers[headerCounter])
            self.treetable.column(header, width=colWidth, anchor='c')
            headerCounter = headerCounter + 1
        self.treetable.place(x=xPos,y=yPos)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.treetable.yview)
        verscrlbar.place(x=xPos+80+(colWidth*total_columns),y=yPos,height=225)
        self.treetable.configure(yscrollcommand=verscrlbar.set)
        for data in datalst:
            self.treetable.insert('', 'end', values=tuple(data), image=self.uncheckedImg,tag="unchecked")

    def OnClick(self,event):
        selecteditem = self.treetable.selection()[0]
        if(self.treetable.item(selecteditem,'tags')[0]=='unchecked'):
            self.treetable.item(selecteditem,image=self.checkedImg)
            self.treetable.item(selecteditem, tag="checked")
            self.selectedUsers.append(self.treetable.item(selecteditem,"values")[0])
        elif (self.treetable.item(selecteditem, 'tags')[0] == "checked"):
            self.treetable.item(selecteditem, image=self.uncheckedImg)
            self.treetable.item(selecteditem, tag="unchecked")
            self.selectedUsers.remove(self.treetable.item(selecteditem, "values")[0])
        self.prinSelectedUser()

    def addData(self,userdata):
        self.treetable.insert('', 'end', values=userdata, image=self.uncheckedImg,tag="unchecked")

    def clearTable(self):
        for item in self.treetable.get_children():
            self.treetable.delete(item)

    def refreshData(self,datalst):
        self.clearTable()
        for data in datalst:
            self.treetable.insert('', 'end', values=tuple(data), image=self.uncheckedImg,tag="unchecked")

    def uncheckAll(self):
        for item in self.treetable.get_children():
            self.treetable.item(item, image=self.uncheckedImg)
            self.treetable.item(item, tag="unchecked")
            if(self.treetable.item(item, "values")[0] in self.selectedUsers):
                self.selectedUsers.remove(self.treetable.item(item, "values")[0])
        self.prinSelectedUser()

    def prinSelectedUser(self):
        print(self.selectedUsers)

class InputEntry:
    def __init__(self,tk_Root,placeholder,bdval=7):
        self.entryVar = Entry(tk_Root,bd=bdval)
        self.placeholder = placeholder
        self.entryVar.bind("<FocusIn>", self.foc_in)
        self.entryVar.bind("<FocusOut>", self.foc_out)
        self.entryVar.insert(0, self.placeholder)

    def foc_in(self, *args):
        if(self.entryVar.get()==self.placeholder):
            self.entryVar.delete('0', 'end')

    def foc_out(self, *args):
        if (len(self.entryVar.get())==0):
            self.entryVar.insert(0, self.placeholder)

    def clearInput(self):
        self.entryVar.delete('0', 'end')
        self.entryVar.insert(0, self.placeholder)

    def setGride(self,rowNum,colNum, pdNum = 1,columnspanNum=1):
        self.entryVar.grid(row=rowNum,column=colNum, pady=pdNum,columnspan = columnspanNum)

    def setPlace(self,xPos,yPos):
        self.entryVar.place(x=xPos,y=yPos)

    def getData(self):
        return self.entryVar.get()

class CutomTable:
    def __init__(self,root,headerslst):
        self.thisFrame = PanedWindow(bg="red",height=100,width=100)
        self.thisFrame.pack(fill=BOTH, expand=1)
        for headCount in range(len(headerslst)):
            tk.Label(self.thisFrame, text=headerslst[headCount], anchor="w").grid(row=0, column=headCount, sticky="ew")
        self.numberOfRecords = 0

    def addRecord(self,recordData):
        self.numberOfRecords += 1
        recordData.setLocation(self.numberOfRecords)

    def getRecordCount(self):
        return self.numberOfRecords

    def getFrame(self):
        return self.thisFrame

class CustomData:
    def __init__(self,root,isChecked,userId,userPass,userPin):
        self.checkBox = tk.Checkbutton(root, onvalue=True, offvalue=False)
        if isChecked:
            self.checkBox.selct()
        else:
            self.checkBox.deselect()
        self.idLabel = tk.Label(root, text=userId, anchor="w")
        self.passLabel = tk.Label(root, text=userPass, anchor="w")
        self.pinLabel = tk.Label(root, text=userPin, anchor="w")

    def setLocation(self,xPos):
        self.checkBox.grid(row=xPos, column=0, sticky="ew")
        self.idLabel.grid(row=xPos, column=1, sticky="ew")
        self.passLabel.grid(row=xPos, column=2, sticky="ew")
        self.pinLabel.grid(row=xPos, column=3, sticky="ew")


