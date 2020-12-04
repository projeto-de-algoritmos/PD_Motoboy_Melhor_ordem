def main():
    
    print("Bem vindo PD_Motoboy_e_melhor_ordem")
    print("Escolha o Algoritmo")
    print("1 para Motoboy(knapsack)")
    print("2 para Melhor ordem(subsequência)")
    print("3 para Sair")
    opcao = int(input('Digite aqui: '))

    if(opcao == 1):
        from interface import janela

    elif(opcao == 2):
        from interface2 import janela
    elif(opcao == 3):
        print("Obrigado e até mais!")
    else:
        print()
        print("Opção inválida!")
        print()

        main()


main()
