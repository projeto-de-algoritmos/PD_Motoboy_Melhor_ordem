import sys
import functions


def menu():
    arquivo = open("input.txt","r+")
    linhas = arquivo.readlines()
    cont = 0;
    for i in linhas:
        cont= cont+1
    # print(cont)

    for i in range(1,cont,2):
        lista = [int(x) for x in linhas[i].split()]
        # print(lista)
        resultado = functions.subsequence(len(lista),lista)

        print(resultado)
menu();

# https://stackoverflow.com/questions/11354544/read-lines-containing-integers-from-a-file-in-python
# https://www.tutorialspoint.com/python3/file_readlines.htm