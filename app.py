import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'pizza', 'ativo':True}, 
                {'nome':'cantina', 'categoria':'italiana', 'ativo':False}]


def exibir_nome_do_progama():
    '''essa função e responsavel por mostra a logo ou o titulo do app'''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcões():
    '''essa função e responsavel por mostra quais opções estão disponiveis para o usuario escolher'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''esse função e responvel por afirmar  que o codigo foi encerrado
        output:
        -finalizar o app'''

    exibir_subtitulo('finalizando o app\n')

def voltar_ao_menu_principal():
        '''essa função e responsavel por utilizada para voltar para o menu principal
        inputs: digite uma tecla para voltar ao menu principal
        OUTPUT: 
        -voltar ao menuprincipalv'''

        input(' digite uma tecla para voltar ao menu principal: ')
        main()

def opcao_invalida():
    '''esse função e responsavel por informar que o dado fornecido não consta nas opções
     OUTPUT: 
    -voltar ao menu principal '''

    print('opção invalida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''esse função e responsavel por da uma aparencia mais destacada para  opção selecionada com "***" pelo usuario
     input: texto str subistituido '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante ():
    '''essa função e responsavel por cadastrar novo resturante
    inputS:
    -NOME_DO_RESTURANTE
    -CATEGORIA
    
    OUTPUT:
    -dados_do_resturante
    -adicionar a dados_do_resturante
    -voltar ao menu principal'''

    exibir_subtitulo('cadastrar de novos restaurantes')
    nome_do_restaurante = input('digite o nome do resturante que desaja cadastrar: ')
    categoria = input(f'digite o nem da categoria do restuarante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o resturante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''essa função e responsavel por mostrar list de resturante
    OUTPUT: 
    -voltar ao menuprincipal'''

    exibir_subtitulo('Listando Restaurantes\n')
    print(f'{'nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | status')
    for restaurante in restaurantes:
        nome_resturante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo ='ativado' if restaurante ['ativo'] else 'desativado'
        print(f'- {nome_resturante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''essa função e responsavel por alternar o estado do resturante para ativo ou desativado
    OUTPUT:     voltar ao menuprincipal'''

    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()
 


def escolher_opcoes():
    '''essa função que e responsavel por desiguinar ou usuario a opção que o usuario escolheu '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante ()

        elif opcao_escolhida == 2 :
            listar_restaurantes()
            
        elif opcao_escolhida ==  3 :
          alternar_estado_restaurante()

        elif opcao_escolhida == 4 :
            finalizar_app()
            
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''essa função e responsavel por dar inicio ao codigo'''

    os.system('cls')
    exibir_nome_do_progama()
    exibir_opcões()
    escolher_opcoes()

if __name__ =='__main__': 
    main()