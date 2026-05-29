print('-' * 38)
print(f'{'LISTAGEM DE PREÇOS':^38}')
print('-' * 38)

lista = ('Pão', 1.90,
         'Leite', 5,
         'Carne', 30,
         'Suco', 0.50,
         'Refrigerante', 7,
         'Arroz', 25,
         'Feijão', 6.50,
         'Macarrão', 4)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>.2f}')
print('-' * 38)