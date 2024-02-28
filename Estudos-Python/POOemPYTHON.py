class Pessoa:

  # Metodo Construtor
  def __init__(self, Nome, Idade):
    self.Nome = Nome
    self.Idade = Idade

  def Boas_Vindas(self):
    print('Olá sem benvindo: ', self.Nome)

  def Recusado(self):
    print('Seu acesso foi recusado!')

  # Função
  def Maior_Idade(self):
    if self.Idade >= 18:
      print('Usuário é maior de idade')
      self.Boas_Vindas()
    else:
      print('Usuário é menor de Idade')
      self.Recusado()

Dados = Pessoa('Odemir', 12)

Dados.Maior_Idade()