import tkinter as tk

name = "Wagner"

def greet(name: str) -> str:
    return f"Olá, {name}!"

def show_window(message: str) -> None:
    root = tk.Tk()
    root.title("Hello World")
    tk.Label(root, text=message, padx=20, pady=20).pack()
    tk.Button(root, text="OK", command=root.destroy).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    show_window(greet(name))
