import os


#como fazer uma lista
usuario_conta = []
senha_conta = []

def limpar(finalizar):
        os.system('cls')
        print(finalizar)
        print()

def fecha_tudo():
        limpar()
        print("obrigado pela sua ajuda e tambem por testar o nosso codigo :) ")

# um exemplo do como pode fazer uma função quando o usuario usar uma caracter errado que não tenha sido pre definido
def opcao_invalida():
    print('opção invalida\n')
    input(' digite uma tecla para voltar ao menu principal')
    main()

def welcome():
        limpar("""O̳̿͟͞l̳̿͟͞a̳̿͟͞ ̳̿͟͞c̳̿͟͞o̳̿͟͞m̳̿͟͞o̳̿͟͞ ̳̿͟͞v̳̿͟͞a̳̿͟͞i̳̿͟͞,̳̿͟͞ ̳̿͟͞p̳̿͟͞a̳̿͟͞r̳̿͟͞a̳̿͟͞ ̳̿͟͞c̳̿͟͞o̳̿͟͞m̳̿͟͞e̳̿͟͞ç̳̳̿̿͟͟͞͞a̳̿͟͞r̳̿͟͞m̳̿͟͞o̳̿͟͞s̳̿͟͞ ̳̿͟͞d̳̿͟͞e̳̿͟͞ ̳̿͟͞a̳̿͟͞l̳̿͟͞g̳̿͟͞u̳̿͟͞m̳̿͟͞a̳̿͟͞s̳̿͟͞ ̳̿͟͞i̳̿͟͞n̳̿͟͞f̳̿͟͞o̳̿͟͞r̳̿͟͞m̳̿͟͞e̳̿͟͞ ̳̿͟͞a̳̿͟͞l̳̿͟͞g̳̿͟͞u̳̿͟͞n̳̿͟͞s̳̿͟͞ ̳̿͟͞p̳̿͟͞a̳̿͟͞r̳̿͟͞a̳̿͟͞ ̳̿͟͞q̳̿͟͞u̳̿͟͞e̳̿͟͞ ̳̿͟͞p̳̿͟͞o̳̿͟͞s̳̿͟͞s̳̿͟͞a̳̿͟͞m̳̿͟͞o̳̿͟͞s̳̿͟͞ ̳̿͟͞c̳̿͟͞o̳̿͟͞n̳̿͟͞t̳̿͟͞i̳̿͟͞n̳̿͟͞u̳̿͟͞a̳̿͟͞r̳̿͟͞\n """)
        Nome = input ('qual seu nome :')
        try:
                Idade = int(input ('qual sua idade:'))
                # condicional para verifcar se um número corresponde ao que se pede
                if 0 < Idade <= 12:
                        print('você é uma criança\n')
                elif 12 < Idade <= 18:
                        print("você é um adolecente\n")
                elif Idade <= 100:
                        print('você é um adulto\n')
                # o 18 pode ser colocado no lugar
                # qualquer valor pois ele define apenas o limite que pode ser colocado
                else:
                        print(Idade,'oooooo você realmente tem muitos anos vividos parabens\n')
        except:
                print('idade não e valida tente novamente\n')
                opcao_invalida()
                
#condicional de verificador de usuario e senha
def criar_senha():
        print('para continuar presisamos que você crie um usuario e senha pra manter seu dado  seguros\n ')

        usuario = input('digite o usuario: ')
        usuario_conta.append(f'{usuario}')

        senha = input('digite a senha: ')
        senha_conta.append(f'{senha}')
        print('ok tudo certo agora suas informaçõe estão seguras')


#como criar um indentificador se o numero e impar ou par
def impar_ou_par():
                print('para comfirmamos que você não e uma robo digite um Número: ')
                try:
                        Numero = int(input("digite um numero: "))
                        if Numero % 2 == 0:
                                print("o número que você colocou é par")

                        else:

                                print('o número que você ccolocou é impar')
                except:
                       opcao_invalida()
                       limpar()


def opnião():   
        print('obridado pra que posamos finalizar diga se você gostou?\n')
        print('1. sim\n')
        print('2. não\n')
        try:
                Opcão = int(input(' escolha uma opção:'))       
                match Opcão:
                        case 1 : 
                                print('que bom que você gostou :) ')
                                opinião_1 = input('qual ponto você gostou?: ')
                        

                        case 2:
                                print('que pena tentaremos melhorar na proxima obrigado\n')
                                
                        case _:
                                print("opção invalida")
                                input('clique em alguma tecla para volta a onde estava')
        except:
                print('que pena que não legal do que foi feito melhoraremos no futuro :.)')
                limpar()

                                
def main():
    os.system('cls')
    welcome()
    criar_senha()
    impar_ou_par()
    opnião()

if __name__ =='__main__':
        main()
                

    