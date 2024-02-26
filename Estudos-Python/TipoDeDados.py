from datetime import datetime

String = str('Olá Mundo')
Inteiro = int( 20)
Flutuante = float(19.5)
Complex = complex(2j)
Lista = list[1,2,3]
Tupla = tuple((1,2,3))
Range = range(6)
Dicionario = dict(nome= 'gabriel', age=20)
Set = set(('a', 'b', 'c'))
Fronset = frozenset(('a', 'b', 'c'))
Boleano = bool(5)
Bytes = bytes(5)
Bytesarray = bytearray(5)

Data = datetime.today().date()

print(type(Bytes))
print(type(Flutuante))
print(type(Complex))
print(type(Range))
print(type(Data))