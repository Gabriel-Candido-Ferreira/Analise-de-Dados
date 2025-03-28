class Fruta:
    def __init__(self, nome: str, preco_por_kg: float, quantidade: float):
        self.nome=nome
        self.preco_por_kg= preco_por_kg
        self.quantidade=quantidade

maca = Fruta("Maçã", 2.5, 10)
banana = Fruta("Banana", 1.8, 15)

print(f"Nome da Fruta: {maca.nome}")

print(f"Preço por Kg: R${maca.preco_por_kg:.2f}")

print(f"Quantidade em Estoque: {maca.quantidade}kg")

print("----------------------------------------------")

print(f"Nome da Fruta: {banana.nome}")

print(f"Preço por Kg: R${banana.preco_por_kg:.2f}")

print(f"Quantidade em Estoque: {banana.quantidade}kg")