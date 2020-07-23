from tkinter import *

root = Tk()
group = LabelFrame(root, text='最好的脚本语言是？', padx=5, pady=5)
group.pack(padx=10, pady=10)

changes = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lua", 4)]

v = IntVar()
for lan, num in changes:
    b = Radiobutton(group, text=lan, variable=v, value=num)
    b.pack(anchor=W)

mainloop()
