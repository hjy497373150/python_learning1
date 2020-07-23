from tkinter import *


def callback():
    var.set("吹吧你，我才不信呢~")


root = Tk()
root.title("使命召唤20")
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您所下载的游戏包含未成年限制内容，\n请已满18周岁再体验游戏！")
textlabel = Label(frame1, textvariable=var, justify=LEFT)
textlabel.pack()

thebutton = Button(frame2, text="我已满18周岁", command=callback)
thebutton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
