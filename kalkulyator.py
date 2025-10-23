# calculator.py
import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def init(self):
        super().init()
        self.title("Kalkulyator")
        self.resizable(False, False)
        self.attributes("-topmost", True)  # oynani doimo yuqorida saqlaydi (vidjet kabi)
        self.configure(padx=6, pady=6)

        # Shrift
        self.display_font = font.Font(size=20, weight="bold")
        self.button_font = font.Font(size=14)

        # Hamma hisobotlar
        self.expression = ""

        # Display (entry tarzida)
        self.display_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.display_var, font=self.display_font,
                         justify="right", bd=4, relief="ridge", width=16)
        entry.grid(row=0, column=0, columnspan=4, pady=(0,8))
        entry.bind("<Return>", lambda e: self.calculate())
        entry.bind("<BackSpace>", lambda e: self.backspace())
        entry.focus_set()

        # Tugmalar ro'yxati (qator-bo'yicha)
        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                action = lambda ch=char: self.on_button(ch)
                b = tk.Button(self, text=char, width=4, height=2, font=self.button_font,
                              command=action)
                b.grid(row=r, column=c, padx=4, pady=4)

        # Klaviatura bindings (raqamlar va amallar)
        for key in "0123456789.+-*/()%":
            self.bind(key, lambda e, k=key: self.insert_char(k))
        self.bind("<Return>", lambda e: self.calculate())
        self.bind("<BackSpace>", lambda e: self.backspace())
        self.bind("<Escape>", lambda e: self.clear())

    def on_button(self, ch):
        if ch == "C":
            self.clear()
        elif ch == "←":
            self.backspace()
        elif ch == "=":
            self.calculate()
        elif ch == "±":
            self.toggle_sign()
        elif ch == "%":
            self.percent()
        else:
            self.insert_char(ch)

    def insert_char(self, ch):
        # oddiy tekshiruv: ikki operatorni ketma-ket qo'yishni cheklash
        if self.expression and self.expression[-1] in "+-*/" and ch in "+-*/":
            # operatorni almashtir
            self.expression = self.expression[:-1] + ch
        else:
            self.expression += ch
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def percent(self):
        # agar hozir raqam bo'lsa, foizga o'tkazish: (x)% -> (x/100)
        try:
            if self.expression:
                # baholashdan oldin oxirgi ifodani olish qiyin; oddiyroq: whole expression sifatida ko'rish
                value = eval(self.expression)
                value = value / 100.0
                # butun bo'lsa intga o'tkazish
                self.expression = str(value)
                self.display_var.set(self.expression)
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def toggle_sign(self):
        # oxirgi raqam yoki butun ifodani manfiy/ musbatga aylantiradi
        try:
            if not self.expression:
                return
            # sinab ko'ramiz: agar butun ifoda raqam bo'lsa
            val = eval(self.expression)
            val = -val
            self.expression = str(val)
            self.display_var.set(self.expression)
        except Exception:
            # agar murakkab ifoda bo'lsa, oddiy backspace-variant: yacheykani o'zgartirmaymiz
            pass


def calculate(self):
        try:
            # xavfsizlik uchun oddiy sanitizatsiya: faqat ruxsat etilgan belgilar
            allowed = "0123456789+-*/().% "
            if all(ch in allowed for ch in self.expression):
                # eval ishlatamiz (oddiy kalkulyator uchun qulay)
                result = eval(self.expression)
                # natijani chiroyli qilib ko'rsatish
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.expression = str(result)
                self.display_var.set(self.expression)
            else:
                raise ValueError("Invalid characters")
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if name == "main":
    app = Calculator()
    app.mainloop()