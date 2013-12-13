__author__ = 'vincentc'
import tkinter
import tkinter.ttk
root = tkinter.Tk()
root.title("GoAgentUpdater")
content = tkinter.ttk.Frame(root, padding=(3,3,12,12),width=800,height=600)
label = tkinter.ttk.Label(content, text="Update Mode")
separatorLine = tkinter.ttk.Separator(content, orient=tkinter.HORIZONTAL)

content.grid(column=0, row=0, sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))
label.grid(column=1, row=2, columnspan=2, padx=5)
separatorLine.grid(column=1 ,row=3,columnspan=10,sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()