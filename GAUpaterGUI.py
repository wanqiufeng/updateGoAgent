__author__ = 'vincentc'
import tkinter
import tkinter.ttk
import tkinter.filedialog
import updateGoAgent
import threading

root = tkinter.Tk()
root.title("GoAgentUpdater")

def update():
    btnUpdate.state(['disabled'])
    print("goagentPaht:{0}".format(vGoagentPath.get()))
    threading.Thread(target = updateGoAgent.main,args=(vGoagentPath.get(),)).start()

def openFileSelector():
    fileSelected = tkinter.filedialog.askopenfilename(filetypes = [('Executable file','.exe')])
    vGoagentPath.set(fileSelected)

content = tkinter.ttk.Frame(root)
btnSelectFile = tkinter.ttk.Button(content, text='Select Path', command=openFileSelector)
vGoagentPath = tkinter.StringVar()
etyGoagentPath = tkinter.ttk.Entry(content, textvariable=vGoagentPath,width=60)
labelAppId = tkinter.ttk.Label(content, text="AppIDs")
vAppId = tkinter.StringVar()
etyAppId = tkinter.ttk.Entry(content, textvariable=vAppId)


separatorLine = tkinter.ttk.Separator(content, orient=tkinter.HORIZONTAL)
btnUpdate = tkinter.ttk.Button(content, text='Update', command=update)

vInfo = tkinter.StringVar()
labelInfo = tkinter.ttk.Label(content, textvariable=vInfo)
vInfo.set("wait update now!")
p = tkinter.ttk.Progressbar(content, orient=tkinter.HORIZONTAL, mode='determinate')
p.step(0)

content.grid(column=0, row=0, sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
btnSelectFile.grid(column=0,row=0,sticky=(tkinter.N, tkinter.W),pady=20,padx=10)
etyGoagentPath.grid(column=1,row=0,columnspan=2,sticky=(tkinter.N, tkinter.W),pady=20,padx=0)
labelAppId.grid(column=0,row=1,sticky=(tkinter.N, tkinter.W),pady=0,padx=10)
etyAppId.grid(column=1,row=1,columnspan=2,sticky=(tkinter.N, tkinter.W),pady=0,padx=0)
separatorLine.grid(column=0,row=2,columnspan=3,sticky=( tkinter.E, tkinter.W),pady=30,padx=15)
btnUpdate.grid(column=0,row=3,columnspan=2,sticky=(tkinter.S, tkinter.E),pady=0,padx=0)
labelInfo.grid(column=0,row=4,columnspan=3,sticky=( tkinter.E, tkinter.W))
p.grid(column=0,row=5,columnspan=3,sticky=( tkinter.E, tkinter.W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)
content.rowconfigure(5, weight=1)

root.mainloop()