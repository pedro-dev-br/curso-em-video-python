tabela = ('Pal', 'Fla', 'Flu', 'Ath', 'Bra', 'Cor', 'São', 'Bah', 'Cru',
          'Bot', 'Vit', 'Atl', 'Int', 'Grê', 'Cori', 'Vas', 'San', 'Mir', 'Rem', 'Cha')
print('-=' * 30)
print(f'Tabela completa: {tabela}')
print('-=' * 30)
print(f'5 primeiros colocados: {tabela[0:5]}')
print('-=' * 30)
print(f'4 últimos colocados {tabela[16:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 30)
for i in range(0, len(tabela)):
    if tabela [i] == 'Cha':
        print(f'A Chapecoense está na posição {i + 1}')
print('-=' * 30)
print(f'A Chapecoense está na posição {tabela.index('Cha')+1}')