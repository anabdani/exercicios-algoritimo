cigarro = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('A quantos anos você fuma? '))
total_cigarros = cigarro * 365 * anos
tempo_perdido_minuto = total_cigarros * 10
tempo_perdido_dias = tempo_perdido_minuto / (24 * 60)

print(f'um fumante perderra aproximadamente{tempo_perdido_dias} dias de vida')