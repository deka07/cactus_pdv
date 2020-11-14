from tkinter import *
import datetime

def tela_relatorio():
    janela_relatorio = Tk()
    janela_relatorio.configure(bg='white')
    janela_relatorio.geometry("{0}x{1}+0+0".format(janela_relatorio.winfo_screenwidth(), janela_relatorio.winfo_screenheight()))

    def relogio():
        tempo = datetime.datetime.now()
        lb_relogio = Label(janela_relatorio, font=('Arial', 30), fg='green')
        lb_relogio.place(x=50, y=50)
        lb_relogio['text'] = tempo.strftime('%H:%M:%S')
        janela_relatorio.after(1000, relogio)

    def voltar():
        from home import tela_principal
        janela_relatorio.destroy()
        tela_principal()

    btn_voltar = Button(janela_relatorio, text='Consultar', font=('Calibri', 12), command=voltar)
    btn_voltar.pack()


    relogio()
    janela_relatorio.mainloop()

tela_relatorio()