class Carro:
    numero_rodas: 4
    quantiade_passageiros = 5

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def buzinar(self):
        print("Buzinando...")

carro = Carro()

carro.acelerar()
carro.buzinar()

# Exemplo de desperdício
# class Uno:
#     modelo = "Uno"
#     marca = "Fiat"
#     ano = 1992
#     numero_rodas: 4
#     quantiade_passageiros = 5
    
#     def acelerar(self):
#         print("Acelerando...")

#     def frear(self):
#         print("Freando...")
    
#     def buzinar(self):
#         print("Buzinando...")

# Utilizando o conceito de herança
class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992

uno = Uno()

uno.buzinar()