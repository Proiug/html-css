print('Olá, Mundo!')
#comentarios de uma unica linha usa apenas jogo da velha
'''enquanto comentarios de varias linhas
usam aspas tres vezes'''

#uso de ; em python.

'''python nao requer ponto e virgulha no final de cada tag, mas,
é possivel usar para se parar documentos, veja abaxio'''
instrucao1; instrucao2; instrucao3 #nao precisa usar ; mas pode ser util.

#pra que serve os parenteses?

'''Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções. Por exemplo'''
resultado = ('a + b') *'c'

#numeros inteiros e decimais!!!

'''numeros inteiros (int) sao aqueles que nao tem parte decimal'''
#Exemplo de numero inteiro (int)
idade = 25
quantidade = 100
#os numeros acima sao numeros inteiros, para marcar valores inteiros como idade e quantidade

'''Numeros Flutuantes (Float) os numeros flutuantes sao usados para demarcar preços altura etc, veja um exemplo abaixo'''
preço = 9.99
altura = 1.75
#tudo que for realicionado a quantidade, idade a variavel (int) e necessaria.
#tudo que for relacionado a preço e altura a  variavel (float) e necessaria.

#O que são as cadeias de textos? (strings)
'''as Cadeias de textos sao usadas para demarcar nome, mensagem etc. Veja um exemplo abaixo!!'''
nome = "juan"
mensagem = 'Ola, Mundo!'

#ou seja quando for necessario usar uma variavel para se especificar nome ou mensagem usar a variavel (strings)

'''Booleanos? os valores booleanos representam os valores de verdade, True e False, veja exemplos abaixo!!!'''
é_maior_de_idade = True#Verdadeiro
tem_desconto = False#Falso
#entao true para verdadeiro e False para falso se empre começar com letra MAIUSCULA

#aonde vai a variavel e o valor para atribuir?

nome = "Juan"
idade = 25
altura = 1.75
é_estudade = True

'''Nesta linha de codigo, Podemos ver que as variaveis ficam a Esquerda do codico, e o valor de atribuição fica sempre a direita.
o Sinal de igual (=) e o operador de atribuição do codico
as variaveis vao sempre a esquedar do operador, e o valor desejavel para atribuir vai a direita!!!'''

# O que sao os Aritimeticos??

'''Aritméticos
Os operadores aritméticos são utilizados para realizar operações matemáticas básicas. Os principais operadores aritméticos em Python são:

Soma (+): soma dois valores.
Subtração (-): subtrai o segundo valor do primeiro.
Multiplicação (*): multiplica dois valores.
Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
Exponenciação (**): eleva o primeiro valor à potência do segundo.'''

a = 10
b = 3

soma = a + b #13 

subtracao = a -b #7

multiplicacao = a * b # 30

divisao = a / b #3.333333

divisao_inteira = a // b #3

modulo = a % b #1

exponenciacao = a ** b #1000

'''De comparação
Os operadores de comparação são utilizados para comparar dois valores e devolvem um valor booleano (True ou False) segundo o resultado da comparação. Os operadores de comparação em Python são:

Igual a (==): devolve True se ambos os valores são iguais.
Diferente de (!=): devolve True se os valores são diferentes.
Maior que (>): devolve True se o primeiro valor é maior que o segundo.
Menor que (<): devolve True se o primeiro valor é menor que o segundo.
Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.
Exemplos:'''

a = 10
b = 3

igual = a == b #False
diferente = a != b #True
maior_que = a > b #True
menor_que = a < b #False
maior_ou_igual = a >= b #True
menor_ou_igual = a <= b #False