


#media.py
#autor: Alexsey Batista Da Silva
# data
# le uma quantidade de notas e calcula a media


qtde_notas = int(input("Digite a quantidade de notas a serem digitadas: "))
x =0 
acumula_nota =0 
while x <= qtde_notas:
    nota =float(input("Digite uma nota: 1"))
    acumula_nota = acumula_nota + nota
    x = x + 1
    
media = acumula_nota/qtde_notas
print("AMEDIA E {:.1F}".format(media))