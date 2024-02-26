string = str('gabriel lindo')
frase= ' ola mundo o dia esta lindo '
CPF = 'CPF: 87634746656'

print(string[0]) #string são listas
print(string[-1])
print(string[-3:])
print(string[0:5]) #pega os valores da posição 0 até a paosição 5
print(len(string))


print(string.replace('lindo', 'lindão'))

print(int(CPF.replace('CPF:','')))

#verifica o começo
print(string.startswith('gabriel'))
#verifica o final
print(string.endswith('lindo'))
#contar palavras/letras
print(string.count('l'))
#transformação 
print(string.capitalize())
#verifica se o valor da string e totalmente numerico
print(string.isdigit())

print(string.upper())
print(string.lower())

#verifica em qual posição começa a palavra 
print(frase.find('lindo'))

#retira os espaços no inicio e no final de uma frase 
print(frase.strip())


#transforma a string em uma lista aparti do parametro que passar 
print(string.split(' '))


endereco = input("digite o seun endereço:")

end = endereco.split(' ')

print(end)
