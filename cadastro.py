# Sistema simples de cadastro de participantes

participantes = []

def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    participantes.append({"nome": nome, "idade": idade})
    print("Participante cadastrado com sucesso!")

def listar():
    print("\nLista de Participantes:")
    for p in participantes:
        print(f"Nome: {p['nome']} | Idade: {p['idade']}")

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        break
