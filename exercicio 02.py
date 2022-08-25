v =int(input("velocidade:"))
if v > 80:
    print('Você será multado em R${}, por estar a {}Km/h acima dos 80Km/h permitidos.'.format((v - 80) * 7,v-80))
else:
    print("velocidade permitida")
