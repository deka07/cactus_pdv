from tkinter import *
import sqlite3

def tela_vendas():

    janela2 = Tk()
    janela2.title('Cactus PDV')
    janela2.configure(bg='#F0FFF0')
    janela2.geometry("{0}x{1}+0+0".format(janela2.winfo_screenwidth(), janela2.winfo_screenheight()))
    
    lista = []

    def onclick_add_item(event=None):
        cod_bar = ety_codigo.get()
        banco = sqlite3.connect('adailto.db')
        cursor = banco.cursor()
        cursor.execute("SELECT cod_barra, produto, preco_final fROM tb_produtos WHERE cod_barra = ?", (cod_bar,))
        lista_itens = cursor.fetchall()
        soma=0
        for item in lista_itens:
            listbox.insert(END, item)
            lista.append(item[2])    
            for i in lista:
                soma = soma + float(i)

        lbl_soma = Label(frame_vendas_2, text='{:.2f}'.format(soma), font=('Calibri', 30, 'bold'), fg='white', bg='green')
        lbl_soma.place(x=620, y=365)

        codi = Label(frame_topo, text=item[0], font=('Calibri', 28, 'bold'), fg='green', width=20)
        codi.grid(row=1, column=0)
        prod = Label(frame_topo, text=item[1], font=('Calibri', 28, 'bold'),  fg='green', width=20)
        prod.grid(row=1, column=1)
        preco = Label(frame_topo, text=item[2], font=('Calibri', 28, 'bold'),  fg='green', width=20)
        preco.grid(row=1, column=2)

    def consulta(event=None):
        vl_produto = int(float(ety_preco.get()))
        qt_protudo = int(float(ety_quantidade.get()))
        
        lbl_valor_total["text"] =str(vl_produto)
    
    def finalizar():
        from tipo_pag import tipo_pagamento
        tipo_pagamento()

    def voltar():
        from home import tela_principal
        tela_vendas.destroy()
        tela_principal()

    #### --------------- Cabeçalho -------------- ####
    frame_topo = Frame(janela2, width=900, height=100,)
    frame_topo.pack(pady=10)
    lbl_codi = Label(frame_topo, text='Código:', font=('Calibri', 20, 'bold'),  fg='green', width=20)
    lbl_codi.grid(row=0, column=0)
    lbl_nome_produto = Label(frame_topo, text='Nome do Produto:', font=('Calibri', 20, 'bold'),  fg='green', width=20)
    lbl_nome_produto.grid(row=0, column=1)
    lbl_preco = Label(frame_topo, text='Preço', font=('Calibri', 20, 'bold'),  fg='green', width=20)
    lbl_preco.grid(row=0, column=2)
    

    #### ------------------------------------- ####
    #### --------------- Vendas -------------- ####
    frame_vendas = Frame(janela2, bg='#F0FFF0')
    frame_vendas.pack(padx=5, side=RIGHT)

    lbl_codigo = Label(frame_vendas, text='Código:',  bg='#F0FFF0', font=('Calibri', 14))
    lbl_codigo.pack()
    ety_codigo = Entry(frame_vendas, width=35, font=('Calibri', 14))
    ety_codigo.pack()
    lbl_quantidade = Label(frame_vendas, text='Produto:',  bg='#F0FFF0', font=('Calibri', 14))
    lbl_quantidade.pack()
    ety_quantidade = Entry(frame_vendas, width=35, font=('Calibri', 14))
    ety_quantidade.pack()
    lbl_unidade = Label(frame_vendas, text='Unidades:',  bg='#F0FFF0', font=('Calibri', 14))
    lbl_unidade.pack()
    ety_unidade = Entry(frame_vendas, width=35, font=('Calibri', 14))
    ety_unidade.pack()
    lbl_preco = Label(frame_vendas, text='Preço:',  bg='#F0FFF0', font=('Calibri', 14))
    lbl_preco.pack()
    lbl_valor_total = Label(frame_vendas, text='Deka',  bg='#F0FFF0', font=('Calibri', 24, 'bold'))
    lbl_valor_total.pack()

    btn_add_item = Button(frame_vendas, text='Add Item', font=('Calibri', 14), command=onclick_add_item)
    btn_add_item.pack()
    janela2.bind('<Return>', onclick_add_item)

    btn_finalizar_compra = Button(frame_vendas, text='Finalizar Compra', font=('Calibri', 14), bg='#98FB98', width=30, command=finalizar)
    btn_finalizar_compra.pack(pady=10)

#----------------------------------------------------------------#
#----------------------------------------------------------------#
    frame_consulta = Frame(frame_vendas,  width=50, height=50,)
    frame_consulta.pack(pady=30)
    lbl_cod = Label(frame_consulta, text='Consultar Preço:', font=('Calibri', 14))
    lbl_cod.pack()
    ent_cod = Entry(frame_consulta, width=30, font=('Calibri', 14))
    ent_cod.pack(pady=5)
    btn_consulta = Button(frame_consulta, text='Consultar', width=20, bg='#ADFF2F', font=('Calibri', 14), command=consulta)
    btn_consulta.pack(pady=5)
    frame_consulta.bind('<Return>', consulta)

#----------------------------------------------------------------#
### -------------------- TextView ----------------------------####
    frame_vendas_2 = Frame(janela2, height=100,  bg='#F0FFF0')
    frame_vendas_2.pack(padx=5, side=RIGHT)

    listbox = Listbox(frame_vendas_2, width=100, height=10, bg='#FFFFF0', font=('Calibri', 20))
    listbox.pack(pady=10, padx=20)
    listbox.insert(END, "### ------------------ Itens da Compra ------------------- ###")
    listbox.insert(END, "Código          Produto                Quant.              Preço")

    

    total_compra = Label(frame_vendas_2, text='Total a pagar: ', font=('Calibri', 30, 'bold'), fg='white', bg='green')
    total_compra.pack()

    btn_remover_item = Button(frame_vendas_2, text='Remover Item', bg='#F4A460', font=('Calibri', 14), width=30, command=lambda listbox=listbox: listbox.delete(ANCHOR))
    btn_remover_item.pack(pady=5)

    btn_voltar = Button(frame_vendas_2, text='Voltar', bg='#66CDAA', font=('Calibri', 14), width=30, command=voltar)
    btn_voltar.pack(pady=5)

    janela2.mainloop()
