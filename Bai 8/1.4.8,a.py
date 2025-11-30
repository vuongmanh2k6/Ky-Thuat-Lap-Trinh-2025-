import tkinter as tk
from tkinter import messagebox

def show_info():
    hoten = entry_name.get()
    ngaysinh = entry_birth.get()
    mssv = entry_mssv.get()
    nganh = entry_major.get()

    messagebox.showinfo("Thông tin cá nhân",
                        f"Họ tên: {hoten}\n"
                        f"Ngày sinh: {ngaysinh}\n"
                        f"MSSV: {mssv}\n"
                        f"Ngành học: {nganh}")

root = tk.Tk()
root.title("Thông tin cá nhân")

tk.Label(root, text="Họ tên:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Ngày sinh:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="MSSV:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Ngành học:").grid(row=3, column=0, padx=5, pady=5, sticky="w")

entry_name = tk.Entry(root, width=30)
entry_birth = tk.Entry(root, width=30)
entry_mssv = tk.Entry(root, width=30)
entry_major = tk.Entry(root, width=30)

entry_name.grid(row=0, column=1)
entry_birth.grid(row=1, column=1)
entry_mssv.grid(row=2, column=1)
entry_major.grid(row=3, column=1)

tk.Button(root, text="Hiển thị", command=show_info).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
