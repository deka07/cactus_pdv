from tkinter import *
from tkinter import ttk
import datetime

window = Tk()
window.title("Cactus PDV - NFe")
window.geometry('560x360')

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
    total = float()
    valor = float(ent1.get())
    quant = ent2.get()
    if quant == '' or None:
        quant = float(1)
        valor_final = valor * quant
        ent1.delete(0, 'end') # Limpa os Entry
        ent2.delete(0, 'end') # Limpa os Entry
    else:
        valor = float(ent1.get())
        quant = float(ent2.get())
        valor_final = valor * quant
        ent1.delete(0, 'end') # Limpa os Entry
        ent2.delete(0, 'end') # Limpa os Entry

    lb4 = Label(text='Total a pagar: {}' .format(total))
    lb4.grid(row=4,column=1)


btn1 = Button(text='Finalizar', command=soma)
btn1.grid(row=5, column=1)


def relogio():
    tempo = datetime.datetime.now()
    lb_relogio = Label(window,font=('Arial', 30), fg='green')
    lb_relogio.grid(row=7, column=2)
    lb_relogio['text'] = tempo.strftime('%H:%M:%S')
    window.after(1000, relogio)

relogio()
window.mainloop()