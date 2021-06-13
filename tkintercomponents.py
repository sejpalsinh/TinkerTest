from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image


class Table:
    def __init__(self, root, datalst, headinglst, tableside='right', tableheading = "headings", colWidth=90):
        total_rows = len(datalst)
        total_columns = len(datalst[0])
        treev = ttk.Treeview(root, selectmode='browse')
        treev.pack(side=tableside)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=treev.yview)
        verscrlbar.pack(side=tableside, fill='x')
        treev.configure(xscrollcommand=verscrlbar.set)
        treev["columns"] = list(range(total_columns))
        print(treev["columns"])
        treev['show'] = tableheading
        for col in range(total_columns):
            treev.column(col, width=colWidth, anchor='c')
            treev.heading(col, text=headinglst[col])
        for row in range(total_rows):
            treev.insert("", 'end', values=datalst[row])


class CheckboxTable:
    def checkboxtable(datalst,headers):
        coldDataId = []
        total_columns = len(datalst[0])
        for colId in range(1, total_columns + 1):
            coldDataId.append("#" + str(colId))
        s = ttk.Treeview(columns=tuple(coldDataId),selectmode='browse')
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
