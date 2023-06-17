#Cadastro de Alunos da Ultima.School.

alunos = [] 
idade = []
sexo = []
cidade = []
estado = []
curso = []

for indice in range(6):
  
  nome = input('Digite o seu nome: ')
  id = int(input('Digite sua idade: ')) # idade
  genero = input('Qual é o seu sexo? ')
  municipio = input('Qual é a sua cidade? ')
  est = input('Digite seu estado: ') # estado
  cur = input('Qual é o seu curso? ') # cur

  
  alunos.append(nome)
  idade.append(id)
  sexo.append(genero)
  cidade.append(municipio)
  estado.append(est)
  curso.append(cur)

print(alunos)
print(idade)
print(sexo)
print(cidade)
print(estado)
print(curso)
