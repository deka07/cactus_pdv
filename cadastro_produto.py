from tkinter import *
from tkinter import messagebox
import sqlite3

janela3 = Tk()
janela3.title('Cactus PDV')

class Produto:
# ------------ Banco de dados -----------------#
   def add_produto(self):
      banco = sqlite3.connect('adailto.db')
      cursor = banco.cursor()
      cursor.execute("INSERT INTO tb_produtos (cod_barra, produto, marca, descricao, preco_custo, preco_final) VALUES  ('087368', 'agua', 'ola', 'agua mineral', '80', '120')")
      cursor.commit()
      messagebox.showinfo("Cadastro Concluido", "Produto cadastrado com sucesso!")
      cursor.close()

#-------------- Tela de cadastro ------------#
frame_cadastro = Frame(janela3,  width=200, height=500,)
frame_cadastro.pack(padx=20, side=RIGHT)


lbl_nome_produto = Label(frame_cadastro, text='Cadastro de Produto:', font=('Calibri', 16), justify=LEFT)
lbl_nome_produto.pack()

lbl_codigo = Label(frame_cadastro, text='Código:', font=('Calibri', 14))
lbl_codigo.pack()

ety_codigo = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_codigo.pack()

lbl_produto = Label(frame_cadastro, text='Produto:', font=('Calibri', 14))
lbl_produto.pack()

ety_produto = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_produto.pack()

lbl_marca = Label(frame_cadastro, text='Marca:', font=('Calibri', 14))
lbl_marca.pack()

ety_marca = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_marca.pack()

lbl_descricao = Label(frame_cadastro, text='Descrição:', font=('Calibri', 14))
lbl_descricao.pack()

ety_descricao = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_descricao.pack()

lbl_custo = Label(frame_cadastro, text='Custo:', font=('Calibri', 14))
lbl_custo.pack()

ety_custo = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_custo.pack()

lbl_preco_final = Label(frame_cadastro, text='Preco Final:', font=('Calibri', 14))
lbl_preco_final.pack()

ety_preco_final = Entry(frame_cadastro, width=35, font=('Calibri', 14))
ety_preco_final.pack()

btn_limpar = Button(frame_cadastro, text='Limpar', font=('Calibri', 14))
btn_limpar.pack(side=LEFT, padx= 60, pady= 20)

btn_cadastro = Button(frame_cadastro, text='Cadastrar', font=('Calibri', 14))
btn_cadastro.pack(side=LEFT, padx= 20, pady= 20)




janela3.mainloop()