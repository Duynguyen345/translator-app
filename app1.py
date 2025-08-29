from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

root = Tk()
root.title('Translator of Duy Dev')
root.geometry("400x500")

# Nếu icon.ico có thật thì giữ lại, nếu không có thì comment dòng dưới
try:
    root.iconbitmap(r"C:\Users\LENOVO\Pictures\logo.ico")
except:
    print("Không tìm thấy logo.ico")

# Load background nếu có
try:
    load = Image.open(r"C:\Users\LENOVO\Pictures\background.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.place(x=0, y=0)
except:
    print("Không tìm thấy background.png")

# Tiêu đề
name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#011327")
name.config(font=("Arial", 24, "bold"))
name.pack(pady=10)

# Ô nhập văn bản
box = Text(root, width=28, height=8, font=("Roboto", 16))
box.pack(pady=20)

# Khung chứa nút
Button_frame = Frame(root, width=400, height=50, bg="#011327")
Button_frame.pack(side=BOTTOM, fill=X)
# Ô kết quả
box1 = Text(root, width=28, height=8, font=("Roboto", 16))
box1.pack(pady=20)

# Chức năng
translator = Translator()

def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)

def translate():
    text = box.get(1.0, END).strip()
    if text:
        result = translator.translate(text, src="en", dest="vi")  # dịch Anh -> Việt
        box1.delete(1.0, END)
        INPUT = box.get(1.0,END)
        print(INPUT)
        t = Translator()
        a= t.translate(INPUT,src="en",dest="vi")
        b = a.text
        box1.insert(END,b)

# Nút
clear_button = Button(Button_frame, text="Clear Text", font=("Arial", 10, 'bold'),
                      bg='#303030', fg="#FFFFFF", command=clear)
clear_button.place(x=50, y=10)

translate_button = Button(Button_frame, text="Translate", font=("Arial", 10, 'bold'),
                          bg='#303030', fg="#FFFFFF", command=translate)
translate_button.place(x=250, y=10)

root.mainloop()
