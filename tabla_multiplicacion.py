numero=int(input('ingresa un numero menor a 10'))
if numero >= 10:
    print('te pasaste')
else:
    print(f'tabla de multiplicaccion del {numero}')
    for i in range(1, 11):
        print(f'{numero}x{i}={numero * i}')
