# Pega o primeiro numero
a = float(input("Primeiro número :"))
#pega o segundo numero
b = float(input("Segundo número :"))
#pergunta qual a operção o usuario quer fazer
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a+b
elif operação == "-":
    resultado = a-b
elif operação == "*":
    resultado = a*b
elif operação == "/":
    resultado = a/b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)


# Pega o primeiro numero
var =int(input('Digite um inteiro :'))
#pega o segundo numero
varr =int(input('Digite outro inteiro :'))
#soma
soma =var + varr
#sub
sub =var-varr
#mult
mult =var*varr
#divi
div =var/varr
#expo
expo =var**varr
#rest
rest_div =var%varr
print('\nSoma: ', soma,'\nSubtração: ', sub,'\nMultiplicação: ', mult,'\nDivisão: ', div,'\nExponenciação: ', expo,'\nResto da divisão: ', rest_div)