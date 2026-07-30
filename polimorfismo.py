"""
Polimorfismo em Python
========================================================================

Polimorfismo é um dos pilares da Programação Orientada a Objetos (POO),
junto com encapsulamento e herança. A palavra vem do grego e significa
"muitas formas" (poli = muitas, morfismo = formas).

Na prática, polimorfismo é a capacidade de objetos de classes diferentes
responderem de maneiras diferentes ao mesmo método, desde que todos
compartilhem métodos com o mesmo nome. Isso permite tratar objetos
diferentes de um jeito uniforme no código, sem precisar saber, de
antemão, de qual classe exata cada objeto é.

Neste exemplo, usamos uma hierarquia de classes que representam animais
para entender como o polimorfismo acontece por meio da sobrescrita de
método (method overriding):
- Animal: classe base (ou superclasse) que define um comportamento
  genérico para emitir som.
- Cachorro e Gato: subclasses que herdam de Animal e sobrescrevem o
  método emitir_som, cada uma com sua própria implementação.
"""


class Animal:
    def emitir_som(self):
        print("Emitindo som genérico...")


class Cachorro(Animal):
    # Sobrescrita de método (method overriding): Cachorro redefine o
    # método emitir_som, que já existe em Animal, com um comportamento
    # próprio. O nome do método continua o mesmo, mas o resultado muda
    # de acordo com a classe que o executa — essa é a essência do
    # polimorfismo.
    def emitir_som(self):
        print("Au au")


class Gato(Animal):
    def emitir_som(self):
        print("Miau")


# Cada objeto chama a sua própria versão de emitir_som, de acordo com a
# classe a que pertence.
cachorro = Cachorro()
cachorro.emitir_som()  # Au au

gato = Gato()
gato.emitir_som()  # Miau

# O verdadeiro poder do polimorfismo fica mais claro quando tratamos
# objetos de classes diferentes de forma uniforme, sem nos preocupar com
# o tipo exato de cada um — basta que todos tenham o mesmo método.
#
# No laço abaixo, percorremos uma lista com animais de tipos diferentes
# e chamamos o mesmo método (emitir_som) para cada um. O Python decide,
# em tempo de execução, qual versão do método deve ser usada para cada
# objeto. Esse comportamento é conhecido como "ligação tardia" (late
# binding).
animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()  # Au au / Miau

# Resumo rápido:
# - Polimorfismo    -> permite que objetos de classes diferentes
#   respondam de formas diferentes ao mesmo método.
# - Sobrescrita de método -> técnica usada aqui para implementar o
#   polimorfismo: as subclasses (Cachorro, Gato) redefinem um método
#   herdado da superclasse (Animal).
# - Vantagem prática -> conseguimos percorrer uma lista com objetos de
#   classes diferentes e chamar o mesmo método em todos eles, sem usar
#   if/else para verificar o tipo de cada objeto.
