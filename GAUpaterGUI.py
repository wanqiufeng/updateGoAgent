__author__ = 'vincentc'
import tkinter
import tkinter.ttk
import tkinter.filedialog
import updateGoAgent
root = tkinter.Tk()
root.title("GoAgentUpdater")

def update():
    print("fdd")

def openFileSelector():
    fileSelected = tkinter.filedialog.askopenfilename(filetypes = [('Executable file','.exe')])
    goagentPath.set(fileSelected)

content = tkinter.ttk.Frame(root, padding=(3,3,12,12),width=800,height=600)
modeLabel = tkinter.ttk.Label(content, text="Update Mode")
modeLine = tkinter.ttk.Separator(content, orient=tkinter.HORIZONTAL)
updateMode = tkinter.StringVar()
manualMode = tkinter.ttk.Radiobutton(content, text='Manual Mode', variable=updateMode, value='manual',command=openFileSelector)
goagentPath = tkinter.StringVar()
goagentPathEntry = tkinter.ttk.Entry(content, textvariable=goagentPath)
autoMode = tkinter.ttk.Radiobutton(content, text='Auto Mode', variable=updateMode, value='auto')

buttonLabel = tkinter.ttk.Label(content, text="Handle Buttons")
buttonLine = tkinter.ttk.Separator(content, orient=tkinter.HORIZONTAL)
btnUpdate = tkinter.ttk.Button(content, text='Update', command=update)
btnEnforceUpdate = tkinter.ttk.Button(content, text='Enforce Update', command=update)

content.grid(column=0, row=0, sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
modeLabel.grid(column=1, row=2, columnspan=2, padx=5)
modeLine.grid(column=1 ,row=3,columnspan=10,sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
manualMode.grid(column=2,row=4)
goagentPathEntry.grid(column=3,row=4)
#fileSelector.grid(column=3,row=4)
autoMode.grid(column=2,row=5)
buttonLabel.grid(column=1,row=9, columnspan=2, padx=5)
buttonLine.grid(column=2,row=10,columnspan=10,sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
btnUpdate.grid(column=2,row=12)
btnEnforceUpdate.grid(column=3,row=12)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()