# RECEBE O VALOR A SER MUTIPLICADO
tabuada= int(input("Digite o número a ser multiplicado:"))
# CONTADOR INICIAL EM 1
count=1
# ENQUANTO O CONTADOR FOR MENOR QUE OU IGUAL A 10 ELE IMPRIME MAIS UMA VEZ A FORMULA
while count <=10:
    print (count, "*",tabuada, "=", count*tabuada)
    count += 1