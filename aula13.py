nome = 'Gustavo Moraes'
altura = 1.78
peso = 69 
imc = peso / (altura * altura) 

#f-string
linha1 = f'{nome} tem {altura:.2f} de altura,'
linha2 = f'pesa {peso} quilos e seu IMC é,'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)