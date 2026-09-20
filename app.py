import tkinter as tk
import random
from tkinter import messagebox

# ฟังก์ชันเมื่อแฟนกดปุ่ม "ตกลง"
def clicked_yes():
    # ซ่อนหน้าต่างหลัก
    root.withdraw()
    # เด้งกล่องข้อความบอกรัก
    messagebox.showinfo("เค้ารักเบบี๋มากเลยนะอยู่ด้วยกันไปนานๆนะ", "รักนะจุ๊ปมั้วฟฟฟฟฟ")
    root.destroy()

# ฟังก์ชันทำให้ปุ่ม "ไม่" วาร์ปหนีเมื่อเมาส์เลื่อนมาโดน
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

# สร้างหน้าต่างโปรแกรม
root = tk.Tk()
root.title("มีอะไรจะถามหน่อยยย 💖")
root.geometry("400x300")
root.configure(bg="#ffe6e6")
root.resizable(False, False)

# ข้อความคำถาม
label_title = tk.Label(
    root,
    text="เป็นแฟนกันแล้ว\nห้ามทิ้งกันไปไหนนะ ตกลงไหม? 🥺",
    font=("Arial", 16, "bold"),
    bg="#ffe6e6",
    fg="#cc0000"
)
label_title.pack(pady=40)

# ปุ่มตกลง (Yes)
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

# ปุ่มไม่ตกลง (No)
button_no = tk.Button(
    root,
    text="ไม่ตกลง 😜",
    font=("Arial", 12, "bold"),
    bg="#b3b3b3",
    fg="white"
)
button_no.place(x=210, y=160, width=110, height=40)

# เมื่อเมาส์เลื่อนมาโดนปุ่ม No ให้วาร์ปหนี
button_no.bind("<Enter>", move_no_button)

# เริ่มทำงานโปรแกรม
root.mainloop()
