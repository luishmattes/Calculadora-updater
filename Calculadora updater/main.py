import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, colorchooser

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Função para definir o caminho do version.txt em um diretório acessível
def get_version_file():
    if sys.platform == "win32":
        # Diretório para Windows (AppData)
        return os.path.join(os.getenv('APPDATA'), 'Calculadora', 'version.txt')
    else:
        # Diretório para Unix (Linux/Mac) (pasta do usuário)
        return os.path.join(os.path.expanduser('~'), '.calculadora', 'version.txt')

VERSION_FILE = get_version_file()
LATEST_VERSION_FILE = resource_path('latest_version.py')

# Criação do diretório se ele não existir
os.makedirs(os.path.dirname(VERSION_FILE), exist_ok=True)

def get_local_version():
    if not os.path.exists(VERSION_FILE):
        print("Arquivo version.txt não encontrado.")
        return None
    with open(VERSION_FILE, 'r') as file:
        version = file.read().strip()
        print(f"Versão local encontrada: {version}")
        return version

def get_latest_version():
    if not os.path.exists(LATEST_VERSION_FILE):
        print("Arquivo latest_version.py não encontrado.")
        return None
    with open(LATEST_VERSION_FILE, 'r') as file:
        code = file.read().strip()
        if not code:
            print("Arquivo latest_version.py está vazio.")
            return None
    print("Arquivo latest_version.py encontrado e não está vazio.")
    return '2.0.0'

def update_program():
    latest_version = get_latest_version()
    if latest_version is None:
        print("Não há uma versão mais recente disponível ou o arquivo está vazio.")
        return
    with open(LATEST_VERSION_FILE, 'r') as src, open(resource_path('calculadora.py'), 'w') as dst:
        dst.write(src.read())
    with open(VERSION_FILE, 'w') as file:
        file.write(latest_version)


def check_for_update():
    local_version = get_local_version()
    latest_version = get_latest_version()
    
    if latest_version is None:
        print("Não foi possível obter a versão mais recente.")
        return
    
    if local_version != latest_version:
        resposta = messagebox.askyesno("Atualização disponível", f"Uma nova versão ({latest_version}) está disponível. Deseja atualizar agora?")
        if resposta:
            print(f"Atualizando da versão {local_version} para a {latest_version}...")
            update_program()
            print('Atualização concluída. Reiniciando...')
            subprocess.Popen([sys.executable, resource_path('calculadora.py')])
            sys.exit()
        else:
            print("Atualização cancelada pelo usuário.")
    else:
        print(f"Você já está usando a versão mais recente: {local_version}.")


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

def escolher_cor():
    cor = colorchooser.askcolor(title="Escolher Cor do Background")[1]
    if cor:
        root.configure(bg=cor)
        result_label.configure(bg=cor)
        entry.configure(bg=cor)

check_for_update()

root = tk.Tk()
root.title("Calculadora")

cor_default = '#260339'
root.configure(bg=cor_default)

entry = tk.Entry(root, width=20, font=('Microsoft Tai Le', 18, 'bold'), bd=0, bg='#310947', fg='#BD5CF3')
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
    tk.Button(root, text=button, width=5, height=2, font=('Microsoft Tai Le', 14), bg='#310947', fg='#9775AA', bd=0, command=action).grid(row=row_val, column=col_val, padx=1, pady=4)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="=", width=5, height=2, font=('Microsoft Tai Le', 14, 'bold'), bg='#9775AA', fg='#310947', bd=0, command=calcular).grid(row=row_val, column=col_val, padx=2, pady=4)

result_label = tk.Label(root, text="Resultado: ", font=('Microsoft Tai Le', 18, 'bold'), bg=cor_default, fg='#BD5CF3', bd=0)
result_label.grid(row=row_val + 1, column=0, columnspan=4, padx=10, pady=10)

tk.Button(root, text="Escolher Cor", width=10, height=2, font=('Microsoft Tai Le', 12, 'bold'), bg='#9775AA', fg='#310947', bd=0, command=escolher_cor).grid(row=row_val + 2, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
