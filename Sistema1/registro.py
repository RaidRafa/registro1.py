import time

def lin():
    print("-"*30)


nomes =list()

lin()
print("      Seja Bem Vindo!")
lin()

while True:

    time.sleep(2)

    print("  Escolha uma das opções:")
    print(f"""
    1- Adicionar um nome
    2- Consultar um nome
    3- Deletar nome
    4- Sair do sistema\n""")

    opcao=int(input(f"OPÇÃO: "))
    time.sleep(2)

    if opcao == 1:
        quantNome=int(input("Quantos nomes deseja Adicionar: "))
        for name in range(0, quantNome):
            nome=input("Digite seu nome: ")
            nomes.insert(0, nome)
            print("Nome adicionado!!")
            time.sleep(2)




    elif opcao == 2:
        print(nomes)
        time.sleep(5)

    elif opcao == 3:
        deletNome=input("Digite o nome que deseja deletar: ")
        for nome in nomes:
            if nome == deletNome:
                print(f"Nome encontrado!\n")
                print("Deletando...")
                time.sleep(2)

                nomes.remove(deletNome)

            else:
                print(f"Nome não encontrado!!\n")


    elif opcao == 4:
        print("Saindo do sistema...")
        exit()

    else:
        print("Opção invalida!!")
        time.sleep(2)