salario = float(input("digite o salario para calculo do imposto"))
base = salario 
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35 ))
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20))
print("salario: R$%6.2f Imposto a pagar: R$%6.2f"%(salario,imposto))



# imposto 2


salario = int(input("informe seu salario:"))
if salario>= 1200:
 print("pagara imposto")
else: salario <= 1200
print("nao precisara pagar imposto")
