import tkinter as tk
from tkinter import messagebox

def show_choice():
    choice = v.get()
    messagebox.showinfo("Kết quả", f"Bạn đã chọn: {choice}")

root = tk.Tk()
root.title("Welcome")

v = tk.IntVar()
v.set(1)  # mặc định chọn First

tk.Radiobutton(root, text="First", variable=v, value=1).pack(side="left", padx=5)
tk.Radiobutton(root, text="Second", variable=v, value=2).pack(side="left", padx=5)
tk.Radiobutton(root, text="Third", variable=v, value=3).pack(side="left", padx=5)

tk.Button(root, text="Click Me", command=show_choice).pack(side="left", padx=10)

root.mainloop()
