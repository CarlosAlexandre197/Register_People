usuarios = []

for indice in range(5):
    opcao = int(input("O que você deseja fazer: 1) Cadastrar nome: 2) Sair: "))
    if opcao == 1:
            nome = input("Digite o seu nome: ")
            usuarios.append(nome)
    elif opcao == 2:
        print("Programa finalizado!")
        break
    print(usuarios)