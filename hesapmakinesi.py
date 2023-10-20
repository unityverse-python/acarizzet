import tkinter as tk

def open_HesapMakinesi():
    hesapMakinesi = tk.Tk()
    hesapMakinesi.title("Hesap Makinesi")

    def button_click(button_text):
        current_value = entry.get()

        if button_text == '=':
            try:
                result = str(eval(current_value))
                entry.delete(0, tk.END)
                entry.insert(tk.END, result)

                with open("sonuc.txt", "a") as file:
                    file.write(result + "\n")

                if '+' in current_value:
                    with open("toplama.txt", "a") as toplama_file:
                        toplama_file.write(result + "\n")

                if '-' in current_value:
                    with open("cikarma.txt", "a") as cikarma_file:
                        cikarma_file.write(result + "\n")

                if '*' in current_value:
                    with open("carpma.txt", "a") as carpma_file:
                        carpma_file.write(result + "\n")
            
            except:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Hata")
        elif button_text == 'C':
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)

    entry = tk.Entry(hesapMakinesi, width=20)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    row, col = 1, 0
    for button in buttons:
        if button == '=':
            tk.Button(hesapMakinesi, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row, column=col)
        else:
            tk.Button(hesapMakinesi, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    hesapMakinesi.mainloop()

def welcome_page():
    root = tk.Tk()
    root.title("Hoş Geldin")
    label = tk.Label(root, text="Merhaba İzzettin'in Hesap makinesi dünyasına hoşgeldinizzz", padx=10, pady=20)
    label.pack()
    button = tk.Button(root, text="Hesap Makinesi'ne Git", command=open_HesapMakinesi)
    button.pack()
    root.mainloop()

welcome_page()
