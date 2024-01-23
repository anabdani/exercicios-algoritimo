nome = input('Qual e seu nome? ')
nota_1 = float(input('Qual foi a primeira nota? '))
nota_2 = float(input('Qual foi a outra nota? '))
media = (nota_1 + nota_2)/2
if media >= 7.0:
    print(f'{nome} você foi aprovado!!,suas notas foram:  {nota_1} pontos e {nota_2} pontos ,dando uma media de {media}')
else:
    print(f'{nome} você foi reprovado sua media é de {media} pontos')
