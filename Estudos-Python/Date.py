import datetime 
import time

Dia_hoje = datetime.datetime.today().date()
print(Dia_hoje)

Data = datetime.datetime.today().date()

Dia = Data.day
Ano = Data.year
Mes = Data.month
print(Ano, Mes, Dia)

Data_antiga = datetime.date(2022,1,1)
print(Data_antiga)

print(Data - Data_antiga)

print("comecei ...")
time.sleep(3)
print("... terminei")