from tkintercomponents import *
tk_Root = Tk()
uncheckedImg = PhotoImage(file='images/uncheck.png')
checkedImg = PhotoImage(file='images/checked.png')
def addUser():
    userTable.adduser(userIdEntry.getData(),userPassword.getData(),userPin.getData())
    userIdEntry.clearInput()
    userPassword.clearInput()
    userPin.clearInput()

userIdEntry = InputEntry(tk_Root,"User Id")
userIdEntry.setGride(0,0,0)
userPassword = InputEntry(tk_Root,"Pasword")
userPassword.setGride(0,1,0)
userPin = InputEntry(tk_Root,"Pin")
userPin.setGride(0,2,0)
adduserBtn = Button(tk_Root, text = "Add User", command = addUser,bd=6)
adduserBtn.grid(row=0,column=3, pady=0)

userTable = CheckboxTable(tk_Root,["Id","Password","Pin"],uncheckedImg,checkedImg,1,0,0,4)

tk_Root.mainloop()