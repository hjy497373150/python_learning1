import tkinter as tk
app = tk.Tk()
app.title('hjy demo')  # 设置窗口标题
thelabel = tk.Label(app, text="这是我第一个窗口!")  # 设置label
thelabel.pack()  # 自动调整位置
app.mainloop()
