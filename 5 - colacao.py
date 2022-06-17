print('Me voy a la cocina')
print('Abro la nevera')

hay_leche = input('Hay leche? (S/N) > ')

if hay_leche == 's':
    hay_colacao = input('Hay colacao? (S/N) > ')
    if hay_colacao == 's':
        print('Sacamos la leche de la nevera')
        print('Buscamos el Colacao')
        print('Mezclamos en un vaso')
    else:
        print('Añadir Colacao a la lista de compras')
else:
    print('Añadir leche a la lista de compras')