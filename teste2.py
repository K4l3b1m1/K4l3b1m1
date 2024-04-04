lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

for i in range(10, 0, -1):
    print(i)

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")

frase = "Era uma vez, em uma pequena vila esquecida pelo tempo, um jovem chamado Tiago. Ele vivia com sua mãe em uma casinha humilde na beira do rio. A vida era difícil, e a tristeza parecia ser a única companheira constante de Tiago, pois seu pai havia desaparecido no mar anos atrás e eles mal tinham o que comer. Certo dia, enquanto caminhava pela floresta em busca de lenha, Tiago encontrou um filhote de pássaro caído do ninho. Com o coração apertado pela situação do pequeno ser, ele decidiu cuidar dele. O pássaro, que ele chamou de Esperança, cresceu forte e saudável sob os cuidados de Tiago Os anos passaram, e a amizade entre Tiago e Esperança se tornou a luz que faltava na vida do jovem. A presença do pássaro trouxe alegria e cor à casa e logo a sorte de Tiago começou a mudar. Sua bondade e amor pelos animais correram pela vila, e as pessoas começaram a procurá-lo para que cuidasse de seus bichos também. Com o tempo Tiago se tornou um veterinário respeitado e amado por todos Sua mãe que antes vivia preocupada, agora sorria todos os dias ao ver o filho tão realizado E embora o passado ainda doesse, Tiago aprendeu que a tristeza pode dar lugar à felicidade, e que cada fim pode ser um novo começo. E assim em uma tarde ensolarada enquanto Tiago cuidava de seus animais, uma figura familiar apareceu na estrada que levava à vila Era seu pai, que contra todas as probabilidades, havia sobrevivido e finalmente encontrado o caminho de volta para casa. A família se reuniu em um abraço apertado, e as lágrimas que corriam eram de pura felicidade. E eles viveram felizes para sempre com a certeza de que mesmo nos momentos mais sombrios sempre há esperança para um final feliz."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

#como criar um dicionario
pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}
 
# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")