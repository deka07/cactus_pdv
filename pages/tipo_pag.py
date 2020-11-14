from tkinter import *

def tipo_pagamento():
    window = Tk()
    window.title("Forma de Pagamento")
    window.geometry('460x360')
    window.configure(bg='#F0FFF0')
    window.resizable(width=0, height=0) # A função para restringir a largura e o tamanho da altura.

    def dinhero():
        tela_d = Tk()
        tela_d.title("Pagamento em Dinheiro")
        tela_d.geometry('650x350')
        tela_d.configure(bg='#F0FFF0')
        tela_d.resizable(width=0, height=0) # A função para restringir a largura e o tamanho da altura.

        lbl = Label(tela_d, text='Valor Total: ', font=('Calibri', 16, 'bold'), fg='white', bg='green')
        lbl.grid(row=0, column=0)
        lbl2 = Label(tela_d, text='Valor Recebido ', font=('Calibri', 16, 'bold'), fg='white', bg='green')
        lbl2.grid(row=1, column=0)
        lbl3 = Label(tela_d, text='Troco: ', font=('Calibri', 16, 'bold'), fg='white', bg='green')
        lbl3.grid(row=3, column=0)

        lbl = Label(tela_d, text='0,00', font=('Calibri', 16, 'bold'), fg='white', bg='green')
        lbl.grid(row=0, column=1)
        lbl2 = Entry(tela_d, font=('Calibri', 16, 'bold'))
        lbl2.grid(row=1, column=1)
        btn = Button(tela_d, text='Pagar', font=('Calibri', 16), fg='green', width=10,)
        btn.grid(row=2, column=1)
        lbl3 = Label(tela_d, text='Troco: ', font=('Calibri', 16, 'bold'), fg='white', bg='green')
        lbl3.grid(row=3, column=1)

        tela_d.mainloop()

    def cartão():
        pass

    def vale():
        pass


    lbl = Label(window, text='Tipo de Pagamento:', font=('Calibri', 24), fg='white', bg='green', width=29)
    lbl.pack(pady=10)

    btn = Button(window, text='À Vista', font=('Calibri', 20), fg='green', width=30, command=dinhero)
    btn.pack(pady=10)

    btn1 = Button(window, text='Cartão', font=('Calibri', 20), fg='green', width=30, command=cartão)
    btn1.pack(pady=10)

    btn2 = Button(window, text='Vale RF/AL', font=('Calibri', 20), fg='green', width=30, command=vale)
    btn2.pack(pady=10)

    window.mainloop()

tipo_pagamento()
