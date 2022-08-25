numeros=[0,0,0,0,0]
x=0
while x < 5:
    numeros[x]=int(input("numero%d:"%(x+1)))
    x+=1
while True:
    escolhido=int(input("que posição voce quer imprimir(0 para sair):"))
    if escolhido ==0:
        break
print("voce escolheu o numero%d"%(numeros[escolhidos-1]))
