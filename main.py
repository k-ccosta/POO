"""
Introdução à Programação Orientada a Objetos (POO) em Python
==============================================================

Neste exemplo, usamos uma classe que representa um celular para entender
os conceitos mais básicos da POO.

Conceitos abordados aqui:
- Classe: um "molde" que define quais atributos e comportamentos os
  objetos criados a partir dela terão.
- Objeto (ou instância): um elemento concreto, criado a partir de uma
  classe, que segue o molde definido por ela.
- Atributos: características que descrevem o objeto (ex: marca, modelo,
  cor).
- Métodos: ações/comportamentos que o objeto pode realizar (ex: fazer uma
  ligação, tirar uma foto).
- self: parâmetro que representa a própria instância dentro dos métodos.
  É sempre o primeiro parâmetro de um método e é passado automaticamente
  pelo Python — não precisamos informá-lo na hora de chamar o método.
"""


class Celular:
    # Atributos da classe.
    #
    # Observação importante: como foram definidos diretamente dentro da
    # classe (e não dentro de um método), esses são "atributos de classe" —
    # ou seja, o valor inicial é o mesmo para todo objeto criado a partir
    # de Celular, a menos que seja alterado individualmente em cada
    # instância depois.
    #
    # Cuidado com vírgulas no final de um valor: escrever
    # marca = "Samsung",  (com vírgula sobrando)
    # faz o Python interpretar o valor como uma tupla ("Samsung",) e não
    # como uma simples string "Samsung". É um erro comum e sutil para quem
    # está começando, então fique atento à pontuação.
    marca = "Samsung"
    modelo = "S23"
    cor = "Preto"

    # Métodos são funções definidas dentro de uma classe.
    # O primeiro parâmetro de todo método é sempre "self", que representa
    # o próprio objeto que está chamando o método. É por meio dele que o
    # método consegue acessar os atributos e os demais métodos da
    # instância.
    def fazer_ligacao(self):
        print("Ligando")

    def tirar_foto(self):
        print("Xis")

    def despertar(self):
        print("Trim")

    # Além do self, um método pode receber outros parâmetros normalmente,
    # como qualquer função. Aqui, "calcular" recebe dois valores e
    # devolve a soma deles — por exemplo, para simular a calculadora
    # do aparelho.
    def calcular(self, v1, v2):
        return v1 + v2


# Criando um objeto (instância) da classe Celular.
# É como usar o molde da classe para produzir um celular "de verdade",
# com seus próprios atributos e métodos prontos para uso.
#
# Dica de boas práticas: por convenção (PEP 8), nomes de variáveis em
# Python são escritos em snake_case (letras minúsculas separadas por
# underscore), por isso usamos celular_kelvin e não celular_Kelvin.
celular_kelvin = Celular()

# Acessando um atributo do objeto com a notação ponto (objeto.atributo).
print(celular_kelvin.marca)  # Samsung

# Chamando um método do objeto (objeto.metodo()).
# Note que não passamos o "self" na chamada — o Python cuida disso
# automaticamente, passando o próprio objeto (celular_kelvin) por trás
# dos panos.
celular_kelvin.fazer_ligacao()

# Chamando um método que recebe parâmetros e guardando o valor retornado
# em uma variável.
resultado = celular_kelvin.calcular(2, 3)
print(resultado)  # 5

# Resumo rápido:
# - Classe  -> Celular
# - Objeto  -> celular_kelvin
# - Atributos -> marca, modelo, cor
# - Métodos   -> fazer_ligacao, tirar_foto, despertar, calcular
