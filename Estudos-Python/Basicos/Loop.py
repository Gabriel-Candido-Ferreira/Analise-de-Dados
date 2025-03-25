import random
for x in range(10):
    print(x)
print("-----------------------------------------------")
for x in range(1,10): #x vai ate 10, mas começa no 1
    print(x)
print("-----------------------------------------------")

for x in range(1,100,5):#x vai ate 100, mas começa no 1 e pula de 5 em 5 
    print(x)
print("-----------------------------------------------")

lista = ["gabriel", "lindo", "dms"]
for x in lista:
    print(x.upper())
print("-----------------------------------------------")

for index, lista in enumerate(lista):
    print(index, lista)


print("-----------------------------------------------")
p = 1 
while p < 10:
    print(p)
    p += 1

print("------------------------------------------------")

while True:
    eu = random.randint(0,10)
    vc = random.randint(0,10)

    print("eu tirei: ", eu)
    print("vc tirei: ", vc)

    if eu > vc:
        print("eu ganhei")
    elif vc > eu:
        print("vc ganhou")
    else:
        print("empate")
    break

print("\n")

print("------------------------------------------------")

Paises = ["brasil", "Alemanha", "Chile", "Portugal"]

for g in Paises:
    print(g.upper())

    if g == "Chile":
        break
