from tkinter import ttk

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
            print(col)
            treev.column(col, width=colWidth, anchor='c')
            treev.heading(col, text=headinglst[col])
        for row in range(total_rows):
            treev.insert("", 'end', values=datalst[row])



