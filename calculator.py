import tkinter as tk
class Calculator:
    pass  

def press(key):
    entry_var.set(entry_var.get() + str(key))


def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")


def clear():
    entry_var.set("")


root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)

entry_var = tk.StringVar()


entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief="sunken", justify="right")
entry.pack(fill="x", padx=10, pady=10)


frame = tk.Frame(root)
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for btn in buttons:
    action = lambda x=btn: calculate() if x == '=' else press(x)
    tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1


tk.Button(root, text="Clear", font=("Arial", 14), width=20, command=clear).pack(pady=10)

root.mainloop()