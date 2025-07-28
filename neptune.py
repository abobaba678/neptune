import customtkinter as CTk
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog

class App(CTk.CTk):
    def __init__(self):
        self.file = 0

        super().__init__()
        def rotate():
            self.img = self.img.rotate(90, expand=True)
            update()
        def update():
            self.photo1 = ImageTk.PhotoImage(self.img)
            self.image1 = CTk.CTkLabel(app, image=self.photo1, text="")
            self.image1.place(x=0, y=140)

        def inputdio():
            file_path = filedialog.askopenfilename(
              filetypes=[("All files", "*.*")]
            )
            if file_path:
                self.file = file_path
                try:
                    
                    self.img = Image.open(self.file)
                    self.img = self.img.resize((int(self.entryX2.get()), int(self.entryY2.get())), Image.Resampling.LANCZOS)
                    update()
                except Exception as e:
                    print(f"Ошибка при открытии файла: {str(e)}")
        def filter():
            op1 = self.optionmenu_var.get()
            op2 = getattr(ImageFilter, op1)()
            self.img = self.img.filter(op2)
            update()
        def paste():
            file_path = filedialog.askopenfilename(
              filetypes=[("All files", "*.*")]
            )
            file = file_path
            self.img2 = Image.open(file)
            self.img2 = self.img2.resize((int(self.entryX2.get()), int(self.entryY2.get())), Image.Resampling.LANCZOS)
            position = (int(self.entryX.get()), int(self.entryY.get()))  # Пример: 100px от левого края, 50px от верхнего
            self.img.paste(self.img2, position)
            update()
        def save():
            self.img.save(self.entrySave.get())
        
        #пустая строчкаg




        self.title("neptunee")
        self.geometry("700x400")
        self.resizable(True, True)
        try:
            self.after(201, lambda: self.iconbitmap('logo04.ico'))
        except Exception as e:
            pass






        self.optionmenu_var = CTk.StringVar(value="BLUR")
        self.button1 = CTk.CTkButton(self, text="openimage", command=inputdio)
        self.button1.grid(row=0, column=0, sticky="s", padx=5, pady=5)
        self.button2 = CTk.CTkButton(self, text="rotate", command=rotate)
        self.button2.grid(row=0, column=1, sticky="s", padx=5, pady=5)
        self.entryX = CTk.CTkEntry(self, placeholder_text="X")
        self.entryX.grid(row=1, column=1, sticky="s", padx=5, pady=5)
        self.entryY = CTk.CTkEntry(self, placeholder_text="Y")
        self.entryY.grid(row=2, column=1, sticky="s", padx=5, pady=5)
        self.button3 = CTk.CTkButton(self, text="применить фильтр", command=filter)
        self.button3.grid(row=1, column=0, sticky="s", padx=5, pady=5)
        self.entryX2 = CTk.CTkEntry(self, placeholder_text="X открытой картнки")
        self.entryX2.grid(row=0, column=2, sticky="s", padx=5, pady=5)
        self.entryY2 = CTk.CTkEntry(self, placeholder_text="Y открытой картинки")
        self.entryY2.grid(row=1, column=2, sticky="s", padx=5, pady=5)
        self.opitonb1 = CTk.CTkOptionMenu(master=self, values=["BLUR",
"CONTOUR",
"DETAIL",
"EDGE_ENHANCE",
"EDGE_ENHANCE_MORE",
"EMBOSS",
"FIND_EDGES",
"SHARPEN",
"SMOOTH",
"SMOOTH_MORE"], variable=self.optionmenu_var)
        self.opitonb1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.button4 = CTk.CTkButton(self, text="вставить", command=paste)
        self.button4.grid(row=2, column=2, sticky="s", padx=5, pady=5)

        self.button5 = CTk.CTkButton(self, text="save", command=save)
        self.button5.grid(row=0, column=3, sticky="s", padx=5, pady=5)

        self.entrySave = CTk.CTkEntry(self, placeholder_text="имя дял сохранённой картинки")
        self.entrySave.grid(row=1, column=3, sticky="s", padx=5, pady=5)
if __name__ == "__main__":
    app = App()
    app.mainloop()