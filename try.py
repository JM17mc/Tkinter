import tkinter as tk

root = tk.Tk()

root.title("Widget Ga ni Mac")
root.geometry("800x500")

label = tk.Label(root, text="Welcome, Bwisitor!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbook = tk.Text(root, height=3, font=('Arial',16))
textbook.pack()

myentry = tk.Entry(root)
myentry.pack()

root.mainloop()