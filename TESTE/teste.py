from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Cactus PDV - NFe")
window.geometry('560x360')

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", )
filemenu.add_command(label="Open", )
filemenu.add_command(label="Save", )
filemenu.add_command(label="Save as...", )
filemenu.add_command(label="Close", )

lista = []
lb1 = Label(text='Produto:').grid(row=1,column=1)
lb2 = Label(text='Valor:').grid(row=2,column=1)
lb3 = Label(text='Quantidade:').grid(row=3,column=1)

ent1 = Entry()
ent1.grid(row=2,column=2)
ent2 = Entry()
ent2.grid(row=3,column=2)

def soma():
    valor = float()
    quant = float()
    valor = float(ent1.get())
    quant = ent2.get()
    if quant == '' or None:
        quant = float(1)
        valor_final = valor * quant
        lista.append(valor_final)
        soma = 0
        for i in lista:
            soma = soma + int(i)
        print
        ent1.delete(0, 'end') # Limpa os Entry
        ent2.delete(0, 'end') # Limpa os Entry
        
    else:
        valor = float(ent1.get())
        quant = float(ent2.get())
        valor_final = valor * quant
        lista.append(valor_final)
        soma = 0
        for i in lista:
            soma = soma + int(i)
        ent1.delete(0, 'end') # Limpa os Entry
        ent2.delete(0, 'end') # Limpa os Entry
    

    lb4 = Label(text='Total a pagar: {}' .format(soma))
    lb4.grid(row=4,column=1)

btn1 = Button(text='Finalizar')
btn1.grid(row=5, column=1)

window.config(menu=menubar)
window.mainloop()