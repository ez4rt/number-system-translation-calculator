import tkinter as tk


def convert():
    try:
        number = entry.get()
        ss_number = int(number, base_ss)

        if ss_number < 0:
            result = "Число должно быть положительным"
        else:
            if convert_ss == 2:
                result = bin(ss_number)[2:]
            elif convert_ss == 8:
                result = oct(ss_number)[2:]
            elif convert_ss == 10:
                result = str(ss_number)
            elif convert_ss == 16:
                result = hex(ss_number)[2:]
            else:
                result = "Ошибка"

        result_var.set(result)
    except ValueError:
        result_var.set("Неверный ввод")


def set_value(value: int, mode: str):
    global base_ss, convert_ss
    if mode == 'base':
        base_ss = value
    elif mode == 'convert':
        convert_ss = value


base_ss = 10
convert_ss = 2

root = tk.Tk()
root.title("Калькулятор перевода систем счисления")

frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=0, pady=0)

tk.Label(frame1, text="Перевести число:").pack(side=tk.LEFT, expand=True)
entry = tk.Entry(frame1)
entry.pack(side=tk.LEFT, expand=True)

tk.Label(frame1, text="из").pack(side=tk.LEFT, expand=True)
base_var = tk.StringVar(value="Десятичной")
base_menu = tk.OptionMenu(frame1, base_var, "Двоичной", "Восьмеричной", "Десятичной", "Шестнадцатеричной",
                          command=lambda value: set_value({"Двоичной": 2, "Восьмеричной": 8, "Десятичной": 10,
                                                          "Шестнадцатеричной": 16}[value], 'base'))
base_menu.pack(side=tk.LEFT, expand=True)

tk.Label(frame1, text="в").pack(side=tk.LEFT, expand=True)
convert_var = tk.StringVar(value="Двоичную")
convert_menu = tk.OptionMenu(frame1, convert_var, "Двоичную", "Восьмеричную", "Десятичную", "Шестнадцатеричную",
                             command=lambda value: set_value({"Двоичную": 2, "Восьмеричную": 8, "Десятичную": 10,
                                                              "Шестнадцатеричную": 16}[value], 'convert'))
convert_menu.pack(side=tk.LEFT, expand=True)

convert_button = tk.Button(frame1, text="Перевести", command=convert)
convert_button.pack(expand=True)

frame2 = tk.Frame(root)
frame2.grid(row=1, column=0, padx=0, pady=0)

result_var = tk.StringVar()
tk.Label(frame2, text="Результат:").pack(side=tk.LEFT)
tk.Label(frame2, textvariable=result_var).pack(side=tk.LEFT)

root.mainloop()
