from tkinter import *
def convert():                                                              #função par ou ímpar
    print('Par ou Ímpar?')
    if(str(ent_num.get()).isnumeric()):
        num = int(ent_num.get())
        soma = num % 2
        if soma == 0:
            lb['text'] = 'É Par'
        else:
            lb['text'] = 'É Ímpar'
    else:
        lb['text'] = 'Valor inválido'

def primo():                                                                #função primos
    print('Primo')
    if(str(ent_num.get()).isnumeric()):
        num = int(ent_num.get())
        if num == 2:
            lb['text'] = '2 é primo, pois o 2 é o único\n número par que é primo!'
        elif num % 2 == 0:
            lb['text'] = 'Não é primo'
        else:
            x = 3
            while x < num:
                if num % x == 0:
                    break
                x = x + 2
            if x == num:
                lb['text'] = 'É primo'
            else:
                lb['text'] = f'Não é primo, pois é divisível por {x}'
    else:
        lb['text'] = 'Valor inválido'

janela = Tk()
janela.title('Par ou Ímpar')
text_orient = Label(janela, text = 'Digite um número:')
text_orient.grid(column = 0, row = 0)
ent_num = Entry(janela, width = 10)
ent_num.grid(column = 0, row = 1)
bt_rt = Button(janela, text = 'Par ou Ímpar?', command = convert)
bt_rt.grid(column = 0, row = 3)
bt_primo = Button(janela, text = 'Primo?', command = primo)
bt_primo.grid(column = 0, row = 4)
lb = Label(janela, text = '?')
lb.grid(column = 0, row = 2)
janela.mainloop()