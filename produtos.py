from tkinter import *
from tkinter import ttk # Biblioteca da Tabela.
from conexao_banco import Banco_db # Importando a classe do banco

janela = Tk()
janela.title('Cactus PDV')


def load_produto():  
   conectar
   lista = cursor.execute("SELECT * fROM tb_produtos ORDER BY produto ASC")
   for i in lista:
      tabela.insert('', END, values=i, tags = ('odd','even'))

   
##################### Cadastro #######################
frame_consulta = Frame(janela)
frame_consulta.pack(padx=1,pady=1)

lbl_pesqusa = Label(frame_consulta, text='Pesquisa', justify=LEFT)
lbl_pesqusa.pack(side=LEFT)

ety_codigo = Entry(frame_consulta)
ety_codigo.pack()

lbl_produto = Label(frame_consulta, text='Produto: ')
lbl_produto.pack()

ety_produto = Entry(frame_consulta)
ety_produto.pack()

btn_novo = Button(frame_consulta, text='Adcionar Produto', font=('Calibri', 14))
btn_novo.pack(side=LEFT, padx= 20, pady= 20)

##################### Criando a tabela ###############
frame_tabela = Frame(janela)
frame_tabela.pack(padx=1,pady=1)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modifica a fonte do corpo
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

tabela.grid(row=0, column=0)

# Passando dados do banco para a tabela:
load_produto()





janela.mainloop()