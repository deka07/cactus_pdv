from tkinter import *

janela2 = Tk()
janela2.title('Cactus PDV')

def onclick_add_item():
    lista_itens = [ety_codigo.get(), ety_quantidade.get(), ety_preco.get()]
    for item in lista_itens:
        listbox.insert(END, item)
def soma():
    vl_produto = int(float(ety_preco.get()))
    qt_protudo = int(float(ety_quantidade.get()))
    
    lbl_valor_total["text"] =str(vl_produto)

#### --------------- Vendas -------------- ####
frame_vendas = Frame(janela2,  width=200, height=500,)
frame_vendas.pack(padx=20, side=RIGHT)


lbl_nome_produto = Label(frame_vendas, text='Nome do Produto:', font=('Calibri', 16), justify=LEFT)
lbl_nome_produto.pack()

lbl_codigo = Label(frame_vendas, text='Código:', font=('Calibri', 14))
lbl_codigo.pack()

ety_codigo = Entry(frame_vendas, width=35, font=('Calibri', 14))
ety_codigo.pack()

lbl_quantidade = Label(frame_vendas, text='Produto:', font=('Calibri', 14))
lbl_quantidade.pack()

ety_quantidade = Entry(frame_vendas, width=35, font=('Calibri', 14))
ety_quantidade.pack()

lbl_unidade = Label(frame_vendas, text='Unidades:', font=('Calibri', 14))
lbl_unidade.pack()

ety_unidade = Entry(frame_vendas, width=35, font=('Calibri', 14))
ety_unidade.pack()

lbl_preco = Label(frame_vendas, text='Preço:', font=('Calibri', 14))
lbl_preco.pack()

ety_preco = Entry(frame_vendas, width=35, font=('Calibri', 14))
ety_preco.pack()

lbl_valor_total = Label(frame_vendas, text='R$: 100,00', font=('Calibri', 14))
lbl_valor_total.pack()

btn_consulta = Button(frame_vendas, text='Consultar', font=('Calibri', 14), command=soma)
btn_consulta.pack()

btn_add_item = Button(frame_vendas, text='Add Item', font=('Calibri', 14), command=onclick_add_item)
btn_add_item.pack()

btn_finalizar_compra = Button(frame_vendas, text='Finalizar Compra', font=('Calibri', 14), width=30)
btn_finalizar_compra.pack()



#-----------------------------------------------------------#
### --------------- TextView ----------------------------####
frame_vendas_2 = Frame(janela2)
frame_vendas_2.pack(padx=1,pady=1)

lbl_itens = Label(frame_vendas_2, text='Itens da venda:', font=('Calibri', 14))
lbl_itens.pack()

listbox = Listbox(frame_vendas_2, bg = "light yellow", width=150, height=20, font=('Calibri', 12))
listbox.pack(pady=8)
listbox.insert(END, "### ------- Itens da Compra ------ ###")

btn_remover_item = Button(frame_vendas_2, text='Remover Item', font=('Calibri', 14), width=30, command=lambda listbox=listbox: listbox.delete(ANCHOR))
btn_remover_item.pack()


janela2.mainloop()