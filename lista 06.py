messes = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
print(maior_valor)
print(menor_valor)
print(vendas_1sem,"\n       ",messes )
