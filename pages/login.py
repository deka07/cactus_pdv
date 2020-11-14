from tkinter import *
import sqlite3
from tkinter import messagebox
from home import tela_principal

janela_login = Tk ()
janela_login.title("Cactus PDV")
janela_login.geometry('500x225') # Define o tamanho da janela
janela_login.configure(bg='white')
janela_login.resizable(width=0, height=0) # A função para restringir a largura e o tamanho da altura.

def validar_acesso(event=None):
    usuario_login = ed1.get()
    senha_login = ed2.get()
    banco = sqlite3.connect('adailto.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * fROM tb_usuarios WHERE usuario = ? AND senha = ?", (usuario_login, senha_login))
    if cursor.fetchall():
        janela_login.destroy()
        tela_principal()       
    else:
        messagebox.showinfo( 'Erro!', 'Acesso negado: Usurio ou senha invalida!')

img_logo = PhotoImage(file='img/cactus.png')
logo = Label(image=img_logo, bg='white')
cb = Label(text='Cactus Bits', font=("Helvetica", 16), fg="Green", bg='white')

lb1 = Label (text = "Usuario: ", font=("Helvetica", 14), bg='white')
lb2 = Label (text = "Senha: ", font=("Helvetica", 14), bg='white')

ed1 = Entry (font=("Helvetica", 14), bg='white')
ed2 = Entry (show="*", font=("Helvetica", 14), bg='white')

bt1 = Button (text = "Entrar", bg='#32CD32', font=("Helvetica", 14), command=validar_acesso)
janela_login.bind('<Return>', validar_acesso)

logo.place(x=25, y=20)
cb.place(x=35, y=150)
lb1.place(x=170, y=65)
lb2.place(x=170, y=100)
ed1.place(x=250, y=65)
ed2.place(x=250, y=100)
bt1.place(x=390, y=135)

janela_login.mainloop()