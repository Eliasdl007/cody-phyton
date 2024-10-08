import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de Dados.
@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNO =2

# Lista de alunos.
lista_de_alunos = []

print("\n=== Solicitando dados dos alunos ===")
for i in range(QUANTIDADE_ALUNO):
   
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_de_alunos.append(aluno)

print("\n=== Exibindo dados dos aluno ===")
for aluno in lista_de_alunos:
    print(f"Nome:  {aluno.nome}")
    print(f"Idade: {aluno.idade}")
nome_do_arquivo = "Lista_de_aluno_Senai.txt"

with open(nome_do_arquivo, "a") as arquivo_alunos:
    for aluno in lista_de_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")
print("\n=== Dados dos alunos salvo com sucesso! ===")  

lista_de_alunos = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_alunos:
    for linha in arquivo_alunos:
        nome, idade = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade= int(idade)))

arquivo_alunos.close()

print("\n=== Exibindo dados dos alunos do arquivo ===")
for aluno in lista_de_alunos:
     print(f"Nome:  {aluno.nome}")
     print(f"Idade: {aluno.idade}")
    