# from bookings import possiveisHorarios, quartosNecessarios
from tkinter import *
import re
import random
import numpy as np
import functions


janela = Tk()

janela.title("Entregas")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)
janela.geometry("450x440+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Melhor Ordem",fg="black",font=('Arial',15))
lbl.place(x=100,y=15)
lbl1 = Label(janela, text="Digite a sequência.",fg="black",font=('Arial',13))
lbl1.place(x=65,y=47)

lbl3 = Label(janela, text="Ex: 2 5 3 45 67", font=('Arial',11))
lbl3.place(x=10,y=100)


inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=122)
resultadoLabel = Label(janela, text="Resultado",fg="black",font=('Arial',14))
resultadoLabel.place(x=10,y=185)

caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))


caixaTexto.place(x=10, y=210)


def regras():

    textRegras =    ('O colégio de Nlognônia descobriu que você irá participar de uma\n'
                    'maratona de programação então pediram a sua ajuda na nova brincadeira\n'
                    'que eles inventaram.\n Será dado a você uma lista com N números inteiros'
                    'e distintos, você terá que escolher NI valores e inserir em uma nova lista.\n'
                    ' Há algumas restrições, você terá que percorrer da esquerda para a direita'
                    'e cada vez que você desejar inserir um novo elemento na lista o elemento'
                    'que você está inserindo tem que ser maior do que todos elementos que você'
                    'já inseriu até o momento.\n O tamanho dessa lista deve ser maximizado.\n'
                    'É permitido percorrer está lista uma vez e ela deve ficar em ordem crescente.\n\n'
                    
                    'Entrada deve ser uma lista de inteiros:\n'
                    'Exemplo: 5 7 6 4 12 8 9 10\n\n'

                    'Saída: tamanho da maior subsequencia encontrada\n'
                    'Exemplo: 5\n'
                    )
    
    caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))
    caixaTexto.insert(END,textRegras)
    caixaTexto.place(x=10, y=210)

def clicked():
    
    


    erro =  '   Entrada inválida "{}", formato válido compõe \n' + '   numeros de 1 a 9 que preservem a sequencia, \n' + '   espaços são permitidos \n\n   Por favor, tente novamente.'
    alerta = 0
    valorEntrada = inputEntrada.get()

    try:
        # valorEntrada = valorEntrada.split(',')
        entrada = []
        # entrada = ""
        for i in valorEntrada:

            if not re.match("[0-9, \[ \]]", i):
                erro = erro.format(i)
                alerta=1
                break

            if re.match("[0-9]",i):
                entrada.append(int(i))
        print(entrada)
                

    except:
        erro=erro
        alerta = 1
    
    texto = ""
    
    if(alerta!=0):
        texto = erro

    else:


        result = functions.subsequence(len(entrada),entrada)
        print(result)

        if result:
            texto = "A maior subsequencia encontrada é de " + str(result) + " números."
        else:
            texto = "A entrada informada está errada, o numero de pedidos deveria ser \n" 

    caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=10, y=210)

btn = Button(janela, text="Buscar", command=clicked)
btn.place(x=278,y=150)

btn = Button(janela, text="Regras", command=regras)
btn.place(x=342,y=150)

regras()

janela.mainloop()