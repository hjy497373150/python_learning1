import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.hi_three = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi)
        self.hi_three.pack()

    def say_hi(self):
        print("hello,world!")


root = tk.Tk()
root.title("hello,world!")
app = APP(root)
root.mainloop()
