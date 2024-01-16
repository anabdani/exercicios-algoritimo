percorrido = float(input('Quantos km você percorreu?  '))
dias = int(input('Quantos dias você ficou com o carro? '))
valor =  (percorrido * 0.20) + (dias * 90)

print(f'você ficou {dias} dias com o carro, percorreu {percorrido}KM o valor do serviço e de R${valor:.2f}')