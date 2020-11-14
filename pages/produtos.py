from tkinter import *
from tkinter import ttk # Biblioteca da Tabela.
import sqlite3


def tela_produto():
   janela = Tk()
   janela.title('Cactus PDV')
   janela.configure(bg='white')
   janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))


   def load_produto():
      banco = sqlite3.connect('adailto.db')
      cursor = banco.cursor()
      lista = cursor.execute("SELECT * fROM tb_produtos ORDER BY produto ASC")
      for i in lista:
         tabela.insert('', END, values=i, tags = ('odd','even'))

      
   ##################### Cadastro #######################
    #-------------- Tela de cadastro ------------#
   frame_cadastro = Frame(janela, width=1000, height=220, highlightbackground="#32CD32", highlightthickness=1.5)
   frame_cadastro.pack(padx=5, side=TOP)

   lbl_codigo = Label(frame_cadastro, text='Código:', font=('Calibri', 14))
   lbl_codigo.place(x=10, y=20)

   ety_codigo = Entry(frame_cadastro, font=('Calibri', 14))
   ety_codigo.place(x=100, y=20)

   lbl_produto = Label(frame_cadastro, text='Produto:', font=('Calibri', 14))
   lbl_produto.place(x=350, y=20)

   ety_produto = Entry(frame_cadastro, font=('Calibri', 14))
   ety_produto.place(x=450, y=20)

   lbl_marca = Label(frame_cadastro, text='Marca:', font=('Calibri', 14))
   lbl_marca.place(x=10, y=60)

   ety_marca = Entry(frame_cadastro, font=('Calibri', 14))
   ety_marca.place(x=100, y=60)

   lbl_descricao = Label(frame_cadastro, text='Descrição:', font=('Calibri', 14))
   lbl_descricao.place(x=350, y=60)

   ety_descricao = Entry(frame_cadastro, font=('Calibri', 14))
   ety_descricao.place(x=450, y=60)

   lbl_custo = Label(frame_cadastro, text='Custo:', font=('Calibri', 14))
   lbl_custo.place(x=10, y=100)

   ety_custo = Entry(frame_cadastro, font=('Calibri', 14))
   ety_custo.place(x=100, y=100)

   lbl_preco_final = Label(frame_cadastro, text='Preco Final:', font=('Calibri', 14))
   lbl_preco_final.place(x=350, y=100)

   ety_preco_final = Entry(frame_cadastro, font=('Calibri', 14))
   ety_preco_final.place(x=450, y=100)

    # ------------ Banco de dados -----------------#
   def add_produto():
      codigo = int(ety_codigo.get())
      produto = ety_produto.get()
      marca = ety_marca.get()
      descricao = ety_descricao.get()
      custo = float(ety_custo.get())
      final = float(ety_preco_final.get())

      banco = sqlite3.connect('adailto.db')
      cursor = banco.cursor()
      cursor.execute("INSERT INTO tb_produtos (cod_barra, produto, marca, descricao, preco_custo, preco_final) VALUES (?, ?, ?, ?, ?, ?)", (codigo, produto, marca, descricao, custo, final))
      banco.commit()
      cursor.close()

      ety_codigo.delete(0, 'end')
      ety_produto.delete(0, 'end')
      ety_marca.delete(0, 'end')
      ety_descricao.delete(0, 'end')
      ety_custo.delete(0, 'end')
      ety_preco_final.delete(0, 'end')

   def limpar_campo():
      ety_codigo.delete(0, 'end')
      ety_produto.delete(0, 'end')
      ety_marca.delete(0, 'end')
      ety_descricao.delete(0, 'end')
      ety_custo.delete(0, 'end')
      ety_preco_final.delete(0, 'end')

   btn_limpar = Button(frame_cadastro, text='Limpar', font=('Calibri', 14), bg='#32CD32', command=limpar_campo)
   btn_limpar.place(x=300, y=150)

   btn_cadastro = Button(frame_cadastro, text='Cadastrar', font=('Calibri', 14), bg='#32CD32', command=add_produto)
   btn_cadastro.place(x=400, y=150)


   ##################### Criando a tabela ###############
   frame_tabela = Frame(janela,padx=10, highlightbackground="#32CD32", highlightthickness=1.5)
   frame_tabela.pack(padx=1,pady=1)

   lbl_pod = Label(frame_tabela, text='Lista de Produtos:', font=('Calibri', 18, 'bold'), fg="#32CD32")
   lbl_pod.grid(row=0, column=0)

   style = ttk.Style()
   style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Calibri', 11)) # Modifica a fonte do corpo
   style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modifica s fonte do cabeçalho
   style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove as bordas

   tabela = ttk.Treeview(frame_tabela, style="mystyle.Treeview", selectmode='browse', column=('column1', 'column2', 'column3', 'column4', 'column5', 'column6'), show='headings')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#1', text='Código')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#2', text='Produto')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#3', text='Marca')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#4', text='Descrição')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#5', text='Custo')

   tabela.column('column1', width=200, minwidth=50, stretch=NO)
   tabela.heading('#6', text='Preço')

   tabela.grid(row=1, column=0)

   # Passando dados do banco para a tabela:
   load_produto()



   def voltar():
      from home import tela_principal
      tela_produto.destroy()
      tela_principal()

   btn_voltar = Button(frame_tabela, text='Voltar', command=voltar, font=('Calibri', 12))
   btn_voltar.grid(row=3, column=0)

   janela.mainloop()

tela_produto()