original = float(input('Digite o preço do produto: '))
desconto = (5 * original /100)
promocional = original - desconto
print(f'o preço do produto é de R${original:.2f},com o desconto de 5% ele saí a R${promocional:.2f}.')