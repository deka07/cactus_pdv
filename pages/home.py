from tkinter import *
import datetime

def tela_principal():
    janela_home = Tk()
    janela_home.geometry("{0}x{1}+0+0".format(janela_home.winfo_screenwidth(), janela_home.winfo_screenheight())) # Abre em tela cheia
    janela_home.title("Cactus PDV")
    janela_home.configure(bg='white')
    #janela_home.attributes('-fullscreen',True) # Abre em fullscreen o programa
    
    #-------------------- MENU --------------------------#
    menubar = Menu(janela_home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Usuario")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=janela_home.quit)
    menubar.add_cascade(label="Arquivos", menu=filemenu)

    configmenu = Menu(menubar, tearoff=0)
    configmenu.add_command(label="Certificado", )
    configmenu.add_command(label="Nota", )
    menubar.add_cascade(label="Configuração", menu=configmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Sobre o Softwares")
    helpmenu.add_command(label="Sobre a Cactus")
    menubar.add_cascade(label="Ajuda", menu=helpmenu)

 #-----------------------------------------------------#
    def abri_vendas():
        from vendas import tela_vendas
        janela_home.destroy()
        tela_vendas()
    
    def abrir_estoque():
        from produtos import tela_produto
        janela_home.destroy()
        tela_produto()

    def abrir_relatorio():
        from relatorios import tela_relatorio
        janela_home.destroy()
        tela_relatorio()

    def abrir_nota():
        from Nota import nota
        janela_home.destroy()
        nota()

    def relogio():
        tempo = datetime.datetime.now()
        lb_relogio = Label(janela_home, font=('Arial', 26, 'bold'), fg='green', bg='white')
        lb_relogio.place(x=1150, y=20)
        lb_relogio['text'] = tempo.strftime('%H:%M:%S')
        janela_home.after(1000, relogio)    

    logotipo = PhotoImage(file='img/cactus_logo.png')
    logo1 = Label(image=logotipo, bg='white')
    logo1.place(x=100, y=100)

    cb_pdv = Label(text='CACTUS PDV', font=('Helvetica' , 42, 'bold'), fg="Green", bg='white')
    cb_pdv.place(x=100, y=460)

    icn1 = PhotoImage(file='img/despesas.png')
    icn2 = PhotoImage(file='img/venda.png')
    icn3 = PhotoImage(file='img/estoque.png')
    icn4 = PhotoImage(file='img/relatorio.png')
    icn5 = PhotoImage(file='img/nota.png')

    bt1 = Button (janela_home, image=icn1, text = "Financeiro", bg='white', borderwidth=2, relief="ridge", height = 138, width = 148).place(x=650, y=145)
    bt2 = Button (janela_home, command=abri_vendas, image=icn2, text = "Vendas", bg='white', borderwidth=2, relief="ridge", height = 138, width = 148).place(x=850, y=145)
    bt3 = Button (janela_home, command=abrir_estoque, image=icn3, text = "Estoque", bg='white', borderwidth=2, relief="ridge", height = 138, width = 148).place(x=650, y=345)
    bt4 = Button (janela_home, command=abrir_relatorio, image=icn4, text = "Relatórios", bg='white', borderwidth=2, relief="ridge", height = 138, width = 148).place(x=850, y=340)
    bt4 = Button (janela_home, command=abrir_nota, image=icn5, text = "Nf-e", bg='white', borderwidth=2, relief="ridge", height = 138, width = 148).place(x=1050, y=145)

    relogio()

    lbl_codigo = Label(janela_home, text='© COPYRIGHT 2020 - Cactus Bits LTDA. Todos os direitos reservados', font=('Calibri', 14, 'italic'), bg='white', fg='green')
    lbl_codigo.place(x=500, y=660)
    

    janela_home.config(menu=menubar)
    janela_home.mainloop()
