import tkinter as tk
root = tk.Tk()
root.title("我的第一个 Python 动画")
canvas = tk.Canvas(root, width=600, height=360, bg="#172033")
canvas.pack()
dot = canvas.create_oval(20, 160, 40, 180, fill="#42d9c8", outline="")
dx, dy = 4, 3
def move():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(dot)
    if x1 <= 0 or x2 >= 600:
        dx = -dx
    if y1 <= 0 or y2 >= 360:
        dy = -dy
    canvas.move(dot, dx, dy)
    root.after(20, move)
root.bind("<Escape>", lambda event: root.destroy())
root.after(20, move)
root.resizable(False, False)
root.mainloop()
