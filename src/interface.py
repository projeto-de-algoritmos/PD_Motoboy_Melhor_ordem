# from bookings import possiveisHorarios, quartosNecessarios
from tkinter import *
import re
import random
import numpy as np
# import utils
import motoboy

janela = Tk()

janela.title("Entregas")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)
janela.geometry("450x440+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Tele entregas pizza",fg="black",font=('Arial',15))
lbl.place(x=100,y=15)
lbl1 = Label(janela, text="Digite quais as entregas a serem feitas.",fg="black",font=('Arial',13))
lbl1.place(x=65,y=47)
# lbl2 = Label(janela, text="Não é necessario indicar a quantidade de entradas.", font=('Arial',11))
# lbl2.place(x=10,y=80)
lbl3 = Label(janela, text="Ex: 6 10 15 5 23 4 21 2 16 4 19 5 18 2", font=('Arial',11))
lbl3.place(x=10,y=100)


inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=122)
resultadoLabel = Label(janela, text="Resultado",fg="black",font=('Arial',14))
resultadoLabel.place(x=10,y=185)

caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))
# caixaTextoJogador1 = Text(janela, height=1,width=61, font=('Arial',10))
# caixaTextoJogador2 = Text(janela, height=1,width=61, font=('Arial',10))
# caixaTextoJogador1.place(x=10, y=210)
# caixaTextoJogador2.place(x=10, y=245)

caixaTexto.place(x=10, y=210)

nomeJogador1 = "Jogador numero 1"
nomeJogador2 = "Jogador numero 2"

def regras():

    textRegras =    ('  Joseph é um motociclista que trabalha fazendo entregas para uma \n' 
                        'pizzaria. Seu salário é baseado no número de pizzas entregues. Como \n'
                        'esta pizzaria está crescendo ele pediu ao amigo Roberto para ajudá-lo \n' 
                        'nas entregas. Como Roberto não está trabalhando no momento, ele \n'
                        'concordou em receber os piores pedidos (cujas entregas serão mais \ndemoradas).\n'

                        '   Assim, sempre que eles vêm à pizzaria antes de partirem para novas \n' 
                        'entregas, Joseph determina a quantidade de pizzas que Roberto deve \n' 
                        'entregar e seleciona que as que vão consumir mais tempo. Por exemplo, se \n' 
                        'houver 22 pizzas a serem entregues e Joseph determinar que no máximo\n'
                        '10 dessas pizzas (pode ser menos) seriam entregues por Roberto, estas\n'
                        'devem necessariamente estar entre os pedidos que demoram mais para \n'
                        'serem entregues. Isso é ilustrado no primeiro caso de teste, onde \n'
                        'Roberto entregará o segundo, terceiro e sexto pedido, totalizando \n' 
                        '8 pizzas e 62 minutos (23 + 21 + 18). Se o Roberto realmente \n'
                        'entregasse 10 pizzas, ele teria que entregar o segundo, terceiro e\n' 
                        'quarto pedido e demoraria 59 minutos (23 + 21 + 16), o que não é o \n'
                        'objetivo do José porque neste caso seria entregue mais pizzas em\n' 
                        'menos tempo.\n'
    
    
    
                        '   O primeiro digito é um numero inteiro que indica o número de pedidos,\n'
                        'a segunda entrada indica o numero maximo de pizzas que Roberto pode \n'
                        'entregar. As proximas entradas se dizem respeito aos pedidos, dessa \n'
                        'forma se alternam entre o tempo necessario e a quantidade de pizzas \n'
                        'do pedido.')
    
    caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))
    caixaTexto.insert(END,textRegras)
    caixaTexto.place(x=10, y=210)

def clicked():
    
    global nomeJogador1
    global nomeJogador2

    erro =  '   Entrada inválida "{}", formato válido compõe \n' + '   numeros de 1 a 9 que preservem a sequencia, \n' + '   espaços são permitidos \n\n   Por favor, tente novamente.'
    alerta = 0
    valorEntrada = inputEntrada.get()

    try:
        # valorEntrada = valorEntrada.split(',')
        # entrada = []
        entrada = ""
        for i in valorEntrada:

            if not re.match("[0-9, \[ \]]", i):
                erro = erro.format(i)
                alerta=1
                break

            if re.match("[0-9 ]",i):
                # entrada.append(i)
                entrada = entrada + i

    except:
        erro=erro
        alerta = 1
    
    texto = ""
    
    if(alerta!=0):
        texto = erro

    else:

        array = []

        # entrada = "6 10 15 5 23 4 21 2 16 4 19 5 18 2"

        aux = entrada.split(' ')

        # 6 10 15 5 23 4 21 2 16 4 19 5 18 2
        # 7 8 10 4 12 4 20 3 22 3 21 2 15 5 38 2




        array.append([int(aux[0]), int(aux[1])])

        num_pedidos = int(aux[0])
        num_pizzas_roberto = int(aux[1])
        aux.remove(aux[0])
        aux.remove(aux[0])

        inputInteiros = []
        cont = 0

        for i in aux:
        
            if cont == 0:
                aux_vector = int(i)
                cont = cont + 1
            else:
                inputInteiros.append([aux_vector, int(i)])
                cont = 0

        if len(inputInteiros) == num_pedidos:
            minutosRoberto = motoboy.motoboy(num_pedidos, num_pizzas_roberto, inputInteiros)
            texto = "Roberto gastará " + str(minutosRoberto) + " minutos para entregar as pizzas."
        else:
            texto = "A entrada informada está errada, o numero de pedidos deveria ser \n" + str(num_pedidos) + " pedidos porém na entrada tem-se " + str(len(inputInteiros)) + ' pedidos.'

    caixaTexto = Text(janela, height=12,width=61, font=('Arial',10))
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=10, y=210)

btn = Button(janela, text="Jogar", command=clicked)
btn.place(x=278,y=150)

btn = Button(janela, text="Regras", command=regras)
btn.place(x=342,y=150)

regras()

janela.mainloop()