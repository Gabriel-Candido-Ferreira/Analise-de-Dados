class Carro:

    def __init__(self, marca, modelo, cor):
        
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        return self.velocidade
    
    def info_carro(self):
        print(f'O carro é um {self.marca} { self.modelo}, da cor {self.cor}')
    
    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0
        
        return self.velocidade

lista_carros = []

while True:

    print("\n--- Menu ---")
    print("1. Adicionar novo carro")
    print("2. Exibir informações dos carros")
    print("3. Exibir informações do carro")
    print("4. Acelerar um carro")
    print("5. Frear um carro")
    print("6. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")

        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)
    
    elif opcao == 2:
        if lista_carros:
            for carro in lista_carros:
                carro.info_carro()
                break
        else:
            print("Nenhum carro adicionado ainda.")
    
    elif opcao == 3:
        if lista_carros:
            for carro in lista_carros:
                print(f"Carro: {carro.modelo}")
            opcao_carro = input('Qual carro vc quer verificar?')

            for carro in lista_carros:
                if carro.modelo == opcao_carro:
                    carro.info_carro()
                    break
            else:
                print("Modelo não encontrado.")
        else:
            print("Nenhum carro adicionado ainda.")
    
    elif opcao == 4:
        modelo = input("Digite o modelo do carro que você deseja acelerar: ")

        for carro in lista_carros:
            if carro.modelo == opcao_carro:
                print(f"A velocidade Atual do {carro.modelo} é {carro.acelerar()} Km/h")
                break
        else:
            print("Modelo não encontrado.")
    
    elif opcao == 5:
        modelo = input("Digite o modelo do carro que você deseja frear: ")

        for carro in lista_carros:
            if carro.modelo == opcao_carro:
                print(f"A velocidade Atual do {carro.modelo} é {carro.frear()} Km/h")
                break
        else:
            print("Modelo não encontrado.")
    
    elif opcao == 6:
        print("Saindo do programa.")
        
        break

    else:
        print("Opção inválida. Tente novamente.")    

    