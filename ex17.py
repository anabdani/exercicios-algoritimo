velocidade = int(input('Qual a velocidade do carro? '))
velocidade_maxima = 80
if velocidade > velocidade_maxima:
    multa = (velocidade - velocidade_maxima)*5
    print(f'você foi multado! velocidade: {velocidade} km/h. multa: R${multa:.2f}')
else: 
    print('velocidade dentro do limite permitido!')