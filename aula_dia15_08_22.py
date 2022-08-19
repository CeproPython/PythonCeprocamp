#1) Assuma os seguintes valores: X=5, A=2, B=3, C=1 e D=2. Utilizando as
#tabelas-verdade de .e., .ou. e .não., responda se o resultado das expressões
#seguintes é verdadeiro ou falso:

X=5 
A=2 
B=3
C=1 
D=2

! (A > 3) || (2 < 7)

! (X < 5)

(x < 6) && (B >= D)

(A > B) && !(C < B)

(X < 2) || ! (A < D)

! (X = 2) || ( C &lt; 2)


! (D < 0) && (B > 7)

(C > 5) || (D > 0)

(A > B) || (C < B)


(B > C) && (X > D)


# 2) Para que construir um diagrama de bloco?



#3) Explique em poucas palavras a diferença entre algoritmo e programa. Todo
#algoritmo pode se tornar um programa? O que precisa ser feito par que isso
#aconteça?



#4) Na instrução leia numRG, numRG é considerado um dado de entrada? Se
#sim, que tipo você o classificaria? Se não é, por quê?
    Sim, Imput = recebimento


#5) Assinale onde todos os nomes são válidos para variáveis:
#(v) ResultadoFinal; SOS_MataAtlantica; Salario_Base
#( x) 7seçoes; CPF_Titular; Valortotal
#( v) media_fnal; ValorTotal; contador
#( x) %porcentagem;@e-mail; &amp;agro_negocio
#( v) cep_cliente; cep_fornecedor; e_mail


#6) Faça um Algoritmo para apresentar o produto dos dez primeiros números
#inteiros (1, 2, 3, ...10).
numeros = int(input())
i = 1
par = 0
impar = 0
if (numeros % 2 == 0):
par = 1
else:
impar = 1
while i < 10:
proximo_numero = int(input())
i = i + 1
if (proximo_numero % 2 == 0):
par = par + 1
else:
impar = impar + 1

print("Quantidade de números pares: ", par)
print("Quantidade de números ímpares é: ", impar)


#7) Faça um programa que exiba seu nome na tela.
name = "Alexsey Batista da Silva"
print(name)

#8) A tabela abaixo apresenta os operadores relacionais utilizados na
#programação de computadores. Preencha a coluna Descrição para cada um
#deles:
# = atribui 
# > Maior paa menor
# < Menor para maior
# >= Maior ou igual
# <= Menor ou igual
# <> Igual  
#
#
#
#

#9) Para ser aprovado o aluno precisa ter média >=7 (Condição 1) e
#faltas <=10 (Condição 2). Conforme o resultado Verdadeiro ou Falso na
#coluna (Condição 1 .e. Condição 2), responda se ele está aprovado ou
#reprovado. Você deve preencher as colunas em branco.

#   Media   faltas  condição 1  e   condição 2  Situação(A/R)
#   8,0     30       verdadeiro e falso = falso Reprovado   
#   6,5     6
#   10      11
#   6,5     0 
#   10      0
#   1       1
#   10      1
#   7,5     9
#   3       25
#   10      13
#   0       0
#
#
#


#Desafio (para os sobreviventes)
#10) Faça um Algoritmo para determinar o maior entre dois números fornecidos
#pelo usuário.
# receba o primeiro numero
# receba o segundo numero  
# compare os numeros
#   
#
#
#
#
#
#
#
