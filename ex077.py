palavras = ('lua', 'sol', 'arte', 'artista',
            'futebol', 'pintura', 'creditiva',
            'programa', 'cadeconsig', 'programa')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')