import tkinter as tk
from tkinter import scrolledtext

from sentiment import rate

KEYWORD_TRESHHOLD = .3


def process_text():
    text = text_field.get("1.0", tk.END)  # Get the text from the text field

    keyword_list = []
    result, keywords = rate(text)

    for score, key in keywords.items():
        if abs(score) >= KEYWORD_TRESHHOLD:
            keyword_list.append(f"{key} [{score}]")

    print(keyword_list)

    label = "positive"
    if result <= 0:
        label = "negative"

    custom_text_label.config(text=f"{label} [{result}]")
    keyword_label.config(text=f"Keywords: {',    '.join(keyword_list)}")

window = tk.Tk()
window.title("Sentiment analysis (Man kann auch eine Excel Datei einlesen.)")
window.configure(bg="pink")

# Create a multiline text field
text_field = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text_field.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

custom_text_label = tk.Label(window, text="Rating: undefined <----- JS reference", bg="pink")
custom_text_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

process_button = tk.Button(window, text="Process Text", command=process_text)
process_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

keyword_label = tk.Label(window, text="Keywords: undefined <----- JS reference", bg="pink")
keyword_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# Configure grid column weights to make the text field expand
window.columnconfigure(0, weight=1)

# Configure grid row weights to make the text field expand vertically
window.rowconfigure(0, weight=1)

window.mainloop()
