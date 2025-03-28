class Pessoa:

  # Metodo Construtor
  def __init__(self, Nome:str, Idade:int):
    self.Nome = Nome
    self.Idade = Idade
    self.acordado=False
    self.comendo=False
    self.dirigindo=False

  def Boas_Vindas(self):
    print('Olá sem benvindo: ', self.Nome)

  def Recusado(self):
    print('Seu acesso foi recusado!')

  # Função
  def Maior_Idade(self):
    if self.Idade >= 18:
      print('Usuário é maior de idade')
      self.Boas_Vindas()
      return True
    else:
      print('Usuário é menor de Idade')
      self.Recusado()
      return False

  def acordar(self):
    if self.acordado:
      print(f"{self.Nome} já está acordado.")
        
    else:
      self.acordado = True
      print(f"{self.Nome} acordou.")
  
  def comer(self):
    if self.comendo:
      print(f"{self.Nome}, já está comendo")
    elif self.dirigindo:
      print(f"{self.Nome}, está dirigindo")
    elif not self.acordado:
      print(f"{self.Nome}, está dormindo")
    else:
      self.comendo = True
      print(f"{self.Nome}, começou a comer")

  def parar_de_comer(self):
    if self.comendo:
      self.comendo = False
      print(f"{self.Nome}, parou de comer")
    else:
      print(f"{self.Nome}, não está comendo")
    
  def dirigir(self):
    if self.Maior_Idade():
      if self.comendo or not self.acordado:
        print(f"{self.Nome}, não pode dirigir pq está ocupado")
      elif self.dirigindo:
        print(f"{self.Nome}, já está dirigindo")
      else:
        self.dirigindo = True
        print(f"{self.Nome}, começou a dirigir")
    else:
      print(f"{self.Nome}, não pode dirigir")
  
  def parar_de_dirigir(self):
    if self.dirigindo:
      self.dirigindo=False
    else:
      print(f"{self.Nome}, não está dirigindo")
  
  def dormir(self):
    if self.comendo or self.dirigindo:
      print(f"{self.Nome}, não pode comer pq está ocupado")
    elif not self.acordado:
      print(f"{self.Nome}, já está dormindo")
    else:
      self.acordado = False
      print(f"{self.Nome}, começou a dormir")      
  
pessoa1 = Pessoa('CANDIM', 12)

pessoa1.acordar()
pessoa1.dirigir()