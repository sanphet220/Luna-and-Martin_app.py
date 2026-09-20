import tkinter as tk
import random
from tkinter import messagebox

def clicked_yes():
    root.withdraw()
    messagebox.showinfo("เค้ารักเบบี๋มากเลยนะอยู่ด้วยกันไปนานๆนะ", "รักนะจุ๊ปมั้วฟฟฟฟฟ")
    root.destroy()

def move_no_button(event):
    while True:
        new_x = random.randint(20, 290)
        new_y = random.randint(120, 250)
        # ไม่ให้ไปทับปุ่มตกลง (x 70-180, y 160-200)
        overlap = (new_x < 180 and new_x + 110 > 70 and
                   new_y < 200 and new_y + 40 > 160)
        if not overlap:
            break
    button_no.place(x=new_x, y=new_y)

root = tk.Tk()
root.title("มีอะไรจะถามหน่อยยย 💖")
root.geometry("400x300")
root.configure(bg="#ffe6e6")
root.resizable(False, False)

label_title = tk.Label(
    root,
    text="เป็นแฟนกันแล้ว\nห้ามทิ้งกันไปไหนนะ ตกลงไหม? 🥺",
    font=("Arial", 16, "bold"),
    bg="#ffe6e6",
    fg="#cc0000"
)
label_title.pack(pady=40)

button_yes = tk.Button(
    root,
    text="ตกลงอยู่แล้ว ❤️",
    font=("Arial", 12, "bold"),
    bg="#ff4d4d",
    fg="white",
    command=clicked_yes,
    cursor="hand2"
)
button_yes.place(x=70, y=160, width=110, height=40)

button_no = tk.Button(
    root,
    text="ไม่ตกลง 😜",
    font=("Arial", 12, "bold"),
    bg="#b3b3b3",
    fg="white"
)
button_no.place(x=210, y=160, width=110, height=40)

button_no.bind("<Enter>", move_no_button)

root.mainloop()
