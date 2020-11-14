from tkinter import *
from tkinter import ttk
def nota():
    window = Tk()
    window.title("Cactus PDV - NFe")
    window.geometry('560x360')
    window.configure(bg='white')

    tab_control = ttk.Notebook(window)#1 
    aba1 = ttk.Frame(tab_control)#2
    tab_control.add(aba1, text='Certificado')#3
    tab_control.pack(expand=1, fill='both')

    aba2 = ttk.Frame(tab_control)#2
    tab_control.add(aba2, text='Emitente')#3
    tab_control.pack(expand=1, fill='both')

    lb1 = Label(aba2, text="Razão Social:").grid(row=1,column=1,padx= 5, pady=5)
    ent1 = Entry(aba2).grid(row=1,column=2,padx= 5, pady=5)

    lb2 = Label(aba2, text="Nome Fantasia:").grid(row=1,column=3,padx= 5, pady=5)
    ent2 = Entry(aba2).grid(row=1,column=4,padx= 5, pady=5)

    lb3 = Label(aba2, text="Código Tributário:").grid(row=3,column=1,padx= 5, pady=5)
    ent3 = Entry(aba2).grid(row=3,column=2,padx= 5, pady=5)

    lb4 = Label(aba2, text="Inscrição Municipal:").grid(row=2,column=1,padx= 5, pady=5)
    ent4 = Entry(aba2).grid(row=2,column=2,padx= 5, pady=5)

    lb5 = Label(aba2, text="Inscrição Estadual:").grid(row=2,column=3,padx= 5, pady=5)
    ent5 = Entry(aba2).grid(row=2,column=4,padx= 5, pady=5)

    lb6 = Label(aba2, text="CNAE Fiscal:").grid(row=3,column=3,padx= 5, pady=5)
    ent6 = Entry(aba2).grid(row=3,column=4,padx= 5, pady=5)

    lb7 = Label(aba2, text="Endereço:").grid(row=4,column=1,padx= 5, pady=5)
    ent7 = Entry(aba2).grid(row=4,column=2,padx= 5, pady=5)

    lb8 = Label(aba2, text="Numero:").grid(row=4,column=3,padx= 5, pady=5)
    ent8 = Entry(aba2).grid(row=4,column=4,padx= 5, pady=5)

    aba3 = ttk.Frame(tab_control)#2
    tab_control.add(aba3, text='Cliente')#3
    tab_control.pack(expand=1, fill='both')

    window.mainloop()
