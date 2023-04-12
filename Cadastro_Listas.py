'''Desenvolva um programa que recebe dados de clientes e armazene-os em uma lista. 
A saída do seu programa será os dados formatados dos 5 clientes cadastrados.'''

clientes = [] 

for cliente in range(5):
  nome  = input('Digite o seu Nome: ')
  cpf   = input('Digite o ceu CPF: ')
  idade = int(input('Digite a sua idade: '))
  
  pessoa = {'nome': nome, 'cpf': cpf, 'idade': idade}
  clientes.append(pessoa)

for indice in range(5):
    print('Cliente:', clientes[indice]['nome'], 'CPF:', clientes[indice]['cpf'], 'Idade:', clientes[indice]['idade'])
