notas=[6,7,5,8,9]
soma=0
x=0
while x<5:
    soma=soma+notas[x]
    x+=1
print("media{:.0f}".format(soma/x))
