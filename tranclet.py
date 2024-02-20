import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp:
    def __init__(self):
        self.translator = Translator()
        self.history = []

    def translate_text(self):
        text = text_entry.get("1.0", tk.END).strip()

        if text:
            translated_text = self.translator.translate(text, dest="ru").text
            translated_entry.delete("1.0", tk.END)
            translated_entry.insert(tk.END, translated_text)

            self.history.append((text, translated_text))
            self.update_history()
    
    def update_history(self):
        history_text.delete("1.0", tk.END)

        for entry in self.history:
            original_text = entry[0]
            translated_text = entry[1]

            history_text.insert(tk.END, f"Original: {original_text}\n")
            history_text.insert(tk.END, f"Translated: {translated_text}\n\n")

root = tk.Tk()
root.title("Online Translator")

translator_app = TranslatorApp()

# Создание вкладок
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Translate')
tab_control.add(tab2, text='History')
tab_control.pack(expand=1, fill="both")

# Вкладка 1 - Перевод текста
text_entry = tk.Text(tab1, height=10, width=50)
text_entry.pack()

translate_button = tk.Button(tab1, text="Translate", command=translator_app.translate_text)
translate_button.pack()

translated_entry = tk.Text(tab1, height=10, width=50)
translated_entry.pack()

# Вкладка 2 - История запросов и результатов
history_text = tk.Text(tab2, height=20, width=50)
history_text.pack()

root.mainloop()