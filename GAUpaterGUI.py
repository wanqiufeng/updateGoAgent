__author__ = 'vincentc'
import tkinter
import tkinter.ttk
import tkinter.filedialog
import updateGoAgent
import threading
import tkinter.messagebox

root = tkinter.Tk()
root.title("GoAgentUpdater")
root.option_add('*tearOff', False)

menubar = tkinter.Menu(root)
root['menu'] = menubar


def guideInfo():
    tkinter.messagebox.showinfo(message='Have a good day')


def aboutInfo():
    tkinter.messagebox.showinfo(message='Have a bad day')


menu_help = tkinter.Menu(menubar)
menubar.add_cascade(menu=menu_help, label='Help')
menu_help.add_command(label='Guide', command=guideInfo)
menu_help.add_command(label='About', command=aboutInfo)


def update():
    btnUpdate.state(['disabled'])
    etyAppId.state(['disabled'])
    print("goagentPaht:{0}".format(vGoagentPath.get()))
    proccessBar.grid(column=0, row=5, columnspan=3, sticky=( tkinter.E, tkinter.W))
    threading.Thread(target=updateGoAgent.main, args=(vGoagentPath.get(),vInfo,proccessBar,vAppId,btnUpdate,etyAppId)).start()


def openFileSelector():
    fileSelected = tkinter.filedialog.askopenfilename(filetypes=[('Executable file', '.exe')])
    vGoagentPath.set(fileSelected)
    vAppId.set(updateGoAgent.getAppId(fileSelected))


content = tkinter.ttk.Frame(root)
btnSelectFile = tkinter.ttk.Button(content, text='Select Path', command=openFileSelector)
vGoagentPath = tkinter.StringVar()
etyGoagentPath = tkinter.ttk.Entry(content, textvariable=vGoagentPath, width=60)
etyGoagentPath.state(['disabled'])
labelAppId = tkinter.ttk.Label(content, text="AppIDs")
vAppId = tkinter.StringVar()
etyAppId = tkinter.ttk.Entry(content, textvariable=vAppId, width=60)

separatorLine = tkinter.ttk.Separator(content, orient=tkinter.HORIZONTAL)
btnUpdate = tkinter.ttk.Button(content, text='Update', command=update)

vInfo = tkinter.StringVar()
labelInfo = tkinter.ttk.Label(content, textvariable=vInfo)
#vInfo.set("wait update now!")
proccessBar = tkinter.ttk.Progressbar(content, orient=tkinter.HORIZONTAL, mode='determinate',length=100)


content.grid(column=0, row=0, sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
btnSelectFile.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W), pady=20, padx=10)
etyGoagentPath.grid(column=1, row=0, columnspan=2, sticky=(tkinter.N, tkinter.W), pady=20, padx=0)
labelAppId.grid(column=0, row=1, sticky=(tkinter.N, tkinter.W), pady=0, padx=10)
etyAppId.grid(column=1, row=1, columnspan=2, sticky=(tkinter.N, tkinter.W), pady=0, padx=0)
separatorLine.grid(column=0, row=2, columnspan=3, sticky=( tkinter.E, tkinter.W), pady=30, padx=15)
btnUpdate.grid(column=0, row=3, columnspan=2, sticky=(tkinter.S, tkinter.E), pady=0, padx=0)
labelInfo.grid(column=0, row=4, columnspan=3, sticky=( tkinter.E, tkinter.W))

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