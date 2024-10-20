def create_latest_version():
    new_version_code = '''\
import tkinter as tk
from tkinter import messagebox

def click_button(value):
    entry.insert(tk.END, value)

def calcular():
    try:
        expr = entry.get()
        resultado = eval(expr)
        result_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na expressão: {e}")

def limpar():
    entry.delete(0, tk.END)
    result_label.config(text="Resultado: ")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Calculadora - Versão Atualizada")

root.configure(bg='#000033')

entry = tk.Entry(root, width=20, font=('Microsoft Tai Le', 18, 'bold'), bd = 0, bg ='#310947', fg='#FFFFFF')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', 'C', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click_button(x) if x != 'C' else limpar()
    tk.Button(root, text=button, width=5, height=2, font=('Microsoft Tai Le', 14), bg='#310947', fg='#FFFFFF', bd = 0, command=action).grid(row=row_val, column=col_val, padx=1, pady=4)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="=", width=5, height=2, font=('Microsoft Tai Le', 14, 'bold'), bg='#FFFFFF', fg='#310947', bd = 0, command=calcular).grid(row=row_val, column=col_val, padx=2, pady=4)

result_label = tk.Label(root, text="Resultado: ", font=('Microsoft Tai Le', 18, 'bold'), bg='#000033', fg='#FFFFFF', bd = 0,)
result_label.grid(row=row_val + 1, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
'''

    with open('latest_version.py', 'w') as file:
        file.write(new_version_code)
    
    with open('version.txt', 'w') as file:
        file.write('2.0.0')  # Atualiza a versão conforme necessário

if __name__ == '__main__':
    create_latest_version()
