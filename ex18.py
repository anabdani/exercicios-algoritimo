ano_nascimento = int(input('Que ano você nasceu?'))
ano_atual = 2024
idade = ano_atual - ano_nascimento
if idade >= 16:
    print(f'Você tem {idade} anos e pode votar')
else:
    print('Você ainda não tem 18 anos e não pode votar')