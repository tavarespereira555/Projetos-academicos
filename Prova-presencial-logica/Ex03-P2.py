lista= list()
print('Digite [0] para sair')
while True:
    num= float(input('Digite o numero: '))
    lista.append(num)
    if num == 0:
        break
print('-' * 40)
print(lista)
print(f'Maior valor da lista: {max(lista)}')
print(f'Media dos valores da lista: {sum(lista) / len(lista)}')
lista[2] = 77
remo= int(input('Digite o valor para poder remover: '))
lista.remove(remo)