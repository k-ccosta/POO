"""
Polimorfismo de Interface em Python
========================================================================

O polimorfismo de interface é uma variação do polimorfismo (visto em
polimorfismo.py) em que classes diferentes implementam um método com o
mesmo nome e o mesmo propósito, permitindo que sejam tratadas de forma
uniforme pelo código, mesmo sem compartilhar um comportamento padrão em
comum.

A diferença em relação ao polimorfismo por sobrescrita é sutil, mas
importante:
- No polimorfismo "comum", a superclasse já fornece uma implementação
  (ainda que genérica) do método, e as subclasses apenas a substituem.
- No polimorfismo de interface, a superclasse funciona como um
  "contrato": ela apenas declara quais métodos as subclasses são
  obrigadas a implementar, sem definir um comportamento padrão para
  eles. Cada subclasse fica responsável por sua própria implementação.

Muitas linguagens (Java, C#, etc.) possuem uma palavra-chave própria
para isso, chamada "interface". Python não tem esse recurso nativo, mas
o mesmo efeito é obtido com uma classe abstrata, usando o módulo `abc`
da biblioteca padrão:
- ABC (Abstract Base Class) impede que a classe seja instanciada
  diretamente — ela só existe para ser herdada.
- O decorador @abstractmethod marca um método que toda subclasse
  concreta é obrigada a implementar. Se uma subclasse não o fizer,
  o Python levanta um erro ao tentar instanciá-la.

Neste exemplo, Forma é a interface: ela define o método area(), mas não
diz como calculá-lo. Quadrado e Circulo implementam essa interface, cada
uma com sua própria fórmula de área.
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2


quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(f"Área do quadrado é {area_quadrado}")

circulo = Circulo(4)
area_circulo = circulo.area()
print(f"Área do círculo é {area_circulo}")

# O polimorfismo de interface fica mais evidente aqui: percorremos uma
# lista com objetos de classes diferentes (Quadrado e Circulo) e
# chamamos o mesmo método (area) em cada um, sem nos preocupar com o
# tipo exato de cada objeto — basta que todos implementem a interface
# Forma.
formas = [Quadrado(5), Circulo(4)]

for forma in formas:
    print(f"Área: {forma.area()}")

# Resumo rápido:
# - Interface -> classe abstrata que define quais métodos as
#   subclasses devem implementar, sem fornecer um comportamento padrão
#   para eles. Em Python, isso é feito com ABC e @abstractmethod.
# - Polimorfismo de interface -> classes diferentes (Quadrado, Circulo)
#   implementam o mesmo método (area) cada uma à sua maneira,
#   permitindo que sejam tratadas de forma uniforme.
# - Vantagem prática -> conseguimos percorrer uma lista com objetos de
#   classes diferentes e chamar o mesmo método em todos eles, sem usar
#   if/else para verificar o tipo de cada objeto.
