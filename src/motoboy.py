
def motoboy(num_pedidos, num_pizzas_roberto, array):

    temp_mochila_motoboy = [[0 for x in range(31)] for x in range(31)]    

    if not num_pedidos == 0:

        for i in range(0, int(num_pedidos)):

            for j in range(0, int(num_pizzas_roberto)):

                if array[i][1] > j:
                    temp_mochila_motoboy[i][j] = temp_mochila_motoboy[i - 1][j]
                else:
                    temp_mochila_motoboy[i][j] = max(temp_mochila_motoboy[i - 1][j - array[i][1]] + array[i][0], temp_mochila_motoboy[i - 1][j])               

    tempoMinutos = temp_mochila_motoboy[num_pedidos - 1][num_pizzas_roberto - 1]

    return tempoMinutos