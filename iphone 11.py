produtos = ['apple tv','mac','iphone x','IPad','apple watch','mach book','airpods']
print(produtos)

produtos.append('iphone 11')
print(produtos)

produto_remover = 'iphone x'
if produto_remover in produtos:
    produtos.remove('iphone x')
else: 
    print('{ } não existe na lista de produtos'.format(produto_remover))
    
