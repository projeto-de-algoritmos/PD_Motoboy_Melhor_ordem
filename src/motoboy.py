
# Exemplo de resolução em C: https://maratonapcauece.wordpress.com/2014/10/08/solucao-uri-1286-motoboy/

def motoboy(num_pedidos, num_pizzas_roberto, array):

    # valor inteiro N (1 ≤ N ≤ 20) que indica o número de pedidos 
    # num_pedidos = 6
    # num_pedidos = 2

    # valor inteiro P (1 ≤ P ≤ 30) indicando o número máximo de pizzas que podem ser entregues por Roberto
    # num_pizzas_roberto = 10
    # num_pizzas_roberto = 15

    # array = [[15, 5],[23, 4],[21, 2],[16, 4],[19, 5],[18, 2]]
    # array = [[47, 12],[39, 4]]


    # while(1):


    # array = []
    matriz = [[0 for x in range(31)] for x in range(31)]    
    # num_pedidos = int(input())
    
    # if num_pedidos == 0:
    #     break

    # num_pizzas_roberto = int(input())

    # for item in range(0, int(num_pedidos)):
    #     entrada_text = input()
    #     # quantidade = input()
    #     aux = entrada_text.split(' ')
    #     array.append([int(aux[0]), int(aux[1])])

    # print("Entrada: ", array)

    # matriz = [[0,0]]

    if not num_pedidos == 0:

        for i in range(0, int(num_pedidos)):

            for j in range(0, int(num_pizzas_roberto)):

                if array[i][1] > j:
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    matriz[i][j] = max(matriz[i - 1][j - array[i][1]] + array[i][0], matriz[i - 1][j])               

    tempoMinutos = matriz[num_pedidos - 1][num_pizzas_roberto - 1]
    print(tempoMinutos, "min.\n")

    return tempoMinutos
    # print("min.\n", matriz)


# motoboy()