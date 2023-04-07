#Novo modelo de cadastro.
users = [] #nome
age = [] #idade
gender = [] #sexo
marital_status = [] #estado_civil
city = [] #cidade
country = [] #pais


for indice in range(5):
    opcao = int(input("O que você deseja fazer: 1) Cadastro: 2) Sair: "))
    if opcao == 1:
            nome = input('Digite o seu nome: ')
            idade = int(input('Digite a sua idade: '))
            sexo = input('Masculino ou Feminino? ')
            estado_civil = input('Qual o seu estado civil? ')
            cidade = input('Qual a sua cidade? ')
            pais = input('Digite o seu pais: ')
            
            users.append(nome)
            age.append(idade)
            gender.append(sexo)
            marital_status.append(estado_civil)
            city.append(cidade)
            country.append(pais)

    elif opcao == 2:
        print("Programa finalizado!")
        break
    
    print(users)
    print(age)
    print(gender)
    print(marital_status)
    print(city)
    print(country)
