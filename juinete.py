import os


#como fazer uma lista
usuario_conta = []
senha_conta = []

def limpar(finalizar):
        """essa função e responsavel por limpar a tela  de codigo anterior
        
        output:
        - print(finalizar)
        - prent()"""
        os.system('cls')
        print(finalizar)
        print()

def fecha_tudo():
        """essa função e responsavel por encerrar o codigo
        
        outpus:
        -limpar()
        - print("obrigado pela [...])"""
        limpar()
        print("obrigado pela sua ajuda e tambem por testar o nosso codigo :) ")

# um exemplo do como pode fazer uma função quando o usuario usar uma caracter errado que não tenha sido pre definido
def opcao_invalida():
    """essa função e redponsavel por ciltar para o menu principal se o usuario usar uma opção não valida
    
    inputs:
    - digite qualquer tecla para voltar ao menu principal
    
    outpus:
    -print (opcão invalida)
    -main()"""
    
    print('opção invalida\n')
    input(' digite uma tecla para voltar ao menu principal')
    main()

def welcome():
        """essa função e responsavel  por obter informação do usuario NOME e IDADE

        INPUTS:
        -qual seu nome
        -qual sua idade
        
        OUTPUS: 
        -você é uma criança
        -você é um adolecente
        -você é um adulto
        - oooo você ralmente tem muitos anos de vividos parabens
        - idade"""

        limpar("""Ola como vai, para começarmos de algumas informe alguns para que possamos continuar\n """)
        Nome = input ('qual seu nome: ')
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

        except: opcao_invalida()
                
#condicional de verificador de usuario e senha
def criar_senha():
        """essa função e responsavel por criar um usuario e senha para o usuario
         inputs:
          -digite um usuario 
          -digite uma senha
          
          outous:
          - os tudo certo agora suas informações estão seguras"""
        
        print('para continuar presisamos que você crie um usuario e senha pra manter seu dado  seguros\n ')

        usuario = input('digite um usuario: ')
        usuario_conta.append(f'{usuario}')

        senha = input('digite a senha: ')
        senha_conta.append(f'{senha}')
        print('ok tudo certo agora suas informaçõe estão seguras')


#como criar um indentificador se o numero e impar ou par
def impar_ou_par():
                """essa função e responsavel por desiguinar se o numero inputado pelo usuario e impar ou par
                input:
                -digite um numero
                
                outputs:
                -o numero e impar
                -o numero e par"""

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
        """essa função e responsavel por obter a opnião do usuario sobre o codigo que ele testou
        inputs:
        -escolha uma opção
        -qual ponto você gostou?
        
        outpus:
        -que bom que você gostou
        -que pena tentaremos melhorar na proxima obrigado
        -opção invalida"""

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

        except: print('que pena que não foi legal do que foi feito melhoraremos no futuro :.)')
        

                                
def main():
    """essa função ersponsavel por da inicio no progama"""
    
    os.system('cls')
    welcome()
    criar_senha()
    impar_ou_par()
    opnião()

if __name__ =='__main__':
        main()
                

    