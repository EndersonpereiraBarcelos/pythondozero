import os


restaurantes = [
    {"Nome": "Praca", "Categoria": "Japonesa", "ativo": False},
    {"Nome": "Pizzaria", "Categoria": "Pizza", "ativo": True},
    {"Nome": "Lanchonete", "Categoria": "Lanche", "ativo": False},
]


def exibir_name():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
"""
    )


def exibir_opcoes():
    print("1. Cadastro restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def voltando_menu():
    input("\nDigite 0 para voltar menu inicial ")
    main()


def finalizar_app():
    exibir_texto("Finalizando sistema")


def opcao_invalida():
    print("Opção invalida!\n")
    voltando_menu()


def exibir_texto(texto):
    os.system("clear")
    print(texto)


def cadastrar_novo_restaurante():
    exibir_texto("Cadastro novos restaurantes\n")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(
        f"Digite nome da categoria do restaurante {nome_do_restaurante}: "
    )
    dados_restaurante = {
        "Nome": nome_do_restaurante,
        "Categoria": categoria,
        "ativo": False,
    }
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    restaurantes.append(dados_restaurante)

    voltando_menu()


def listar_restaurante():
    exibir_texto("Listando restaurantes\n")

    for restaurante in restaurantes:
        nome_do_restaurante = restaurante["Nome"]
        Categoria = restaurante["Categoria"]
        ativo = restaurante["ativo"]
        print(f"{nome_do_restaurante} - {Categoria} - {ativo}")

    voltando_menu()


def alternar_estado():
    exibir_texto('Alterando estado restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alterar ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['ativo']  = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante["ativo"] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')


    voltando_menu()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurante()

        elif opcao_escolhida == 3:
            alternar_estado()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("clear")
    exibir_name()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
