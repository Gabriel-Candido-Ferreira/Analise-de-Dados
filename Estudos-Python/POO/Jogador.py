class Jogador:
    def __init__(self, nome, posicao, n_camisa, gols=0):
        self.nome= nome
        self.posicao=posicao
        self.n_camisa= n_camisa
        self.gols= gols

jogador1 = Jogador("Candim", "volante", 29, 500)

print(f"o jogador {jogador1.nome}, que joga na posição {jogador1.posicao}, com a camisa {jogador1.n_camisa}, completou esse mes {jogador1.gols} gols")