num_1 =int(input("num_1"))
num_2 =int(input("num_2"))
operacao = input("adicao = +\ndivisao = /\nsubtracao = -\nmultiplicacao = *\ndigite a operação:")
if operacao == "+":
     print(num_1 + num_2)
elif operacao =="-":
     print(num_1 - num_2)
elif operacao =="*":
     print(num_1 * num_2)
elif operacao =="/":
     print(num_1 / num_2)
else:
     print('operação invalida.')
