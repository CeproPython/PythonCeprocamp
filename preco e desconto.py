preco=float(input("preço:"))
desconto=float(input("porcentagem do desconto:"))
d=(preco*desconto)/100
pd=preco-d
print(" desconto:",d,"\n","preço a pagar",pd)
