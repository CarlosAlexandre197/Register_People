#Cadastro de alunos da Ultima.School.

alunos = [] 
idade = []
sexo = []
cidade = []
estado = []

for indice in range(5):
  
  nome = input('Digite o seu nome: ')
  id = int(input('Digite sua idade: ')) # idade
  genero = input('Qual é o seu sexo? ')
  municipio = input('Qual a sua cidade? ')
  est = input('Digite seu Estado: ') # estado

  
  alunos.append(nome)
  idade.append(id)
  sexo.append(genero)
  cidade.append(municipio)

print(alunos)
print(idade)
print(sexo)
print(cidade)