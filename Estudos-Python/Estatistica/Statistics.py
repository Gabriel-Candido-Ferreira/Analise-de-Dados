import statistics

lista = [ 12,45,25,29,18,20,29]
lista2 = [ 15,45,20,29,30,18,20]

print(sum(lista)/ len(lista))

print(statistics.mean(lista))
print(statistics.median(lista))
print(statistics.median(lista2))
print(statistics.mode(lista))
print(statistics.mode(lista2))