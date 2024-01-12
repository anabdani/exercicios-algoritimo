largura = float(input('Digite a largura da parede? '))
altura = float(input('Digite a altura da parede? '))
area = largura * altura
tinta = area /2

print(f'para pintar uma parede de {largura:.2f} x {altura:.2f} com uma área de {area:.2f}m2,você ira gastar {tinta:.2f}l de tinta.')