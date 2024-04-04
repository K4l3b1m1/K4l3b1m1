import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def cadastrar_restaurante():
    exibir_subtitulos("Cadastro de novos restaurantes")

    nome = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("Digite a categoria do restaurante que deseja cadastrar: ")

    dados_do_restaurante = {"nome": nome, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome} foi cadastrado com sucesso!\n")

    retornar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulos("Listando todos os restaurantes")

    print(f"- {'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | Status\n")
    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    print()

    retornar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulos("Alternando estado de restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante["nome"] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            if restaurante["ativo"]:
                print(f"O restaurante foi ativado com sucesso!")
            else:
                print(f"O restaurante foi desativado com sucesso!")

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    retornar_ao_menu_principal()


def finalizando_app():
    exibir_subtitulos("Finalizando o app")


def exibir_subtitulos(texto):
    os.system("cls")
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(f"* {texto} *")
    print(linha)
    print()


def retornar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal.\n")
    main()


def exibir_nome():
    print("░██████╗░█████╗░██████╗░░█████╗░██████╗░        ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗")
    print("██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗        ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝")
    print("╚█████╗░███████║██████╦╝██║░░██║██████╔╝        █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░")
    print("░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗        ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗")
    print("██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║        ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝")
    print("╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝        ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░")
    print()


def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair")


def escolher_opcao():
    opcao_escolhida = input("Escolha uma opção: ")
    print(f"Você escolheu a opção {opcao_escolhida}")

    if opcao_escolhida.isdigit() and opcao_escolhida in ("1", "2", "3", "4"):
        opcao_escolhida = int(opcao_escolhida)
    else:
        print("Opção inválida, favor digitar uma das quatro opções válidas!\n")
        retornar_ao_menu_principal()

    if opcao_escolhida == 1:
        cadastrar_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizando_app()


def main():
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
