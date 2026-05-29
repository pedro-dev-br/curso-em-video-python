from random import choices
nums = choices(range(0, 15), k=5)
print(nums)
maior = max(nums)
menor = min(nums)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')