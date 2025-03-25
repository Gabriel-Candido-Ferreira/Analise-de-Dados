import math

Lista_nr = [ 0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
Lista_str = ['gabriel', 'maria', 'wagner']
Lista_variada = [1, 'gabriel', True, [0.5, 3, 5]]

Lista_de_carros = ['VW', 'GOL', 'TESLA']
marca01, marca02,marca03 = Lista_de_carros

print(Lista_nr)
print("\n")
print(Lista_str)
print("\n")
print(Lista_variada)
print("\n")
print(marca01, marca02,marca03)
print("\n")
print(len(Lista_nr))

print("---------------------------------------------------------------------")
#tuplas são imutaveis 
tuplas = (1, 2, 3,)
tuplas_variadas = (1, 'gabriel', True, (0.5, 3, 5))

print(tuplas)
print("\n")
print(tuplas_variadas)
print("\n")
print(len(tuplas_variadas))
print("\n")
print(min(tuplas))
print("\n")
print(max(tuplas))
print("\n")
print(pow(3,4))
print("\n")
print(math.sqrt(81))
print("\n")
print(math.ceil(3.4))
print("\n")
print(math.floor(3.4))

print("---------------------------------------------------------------------")
dicionario = {
    'Index' : 'valor', 
    'ID' : 1,
    'nome': 'gabriel',
    'lista': Lista_nr,
    'tupla': tuplas,
}
print(dicionario)

print(len(dicionario))

