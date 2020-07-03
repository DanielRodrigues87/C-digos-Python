altura = float(input('Digite a sua Altura:(m) '))
peso = float(input('Digite o seu peso:(Kg) '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc <= 17:
    print('Abaixo do peso normal')
elif imc >= 18 and imc <= 24.9:
    print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade grau 1.')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau 2.')
else:
   print('Obesidade grau 3 ou obesidade mórbida')