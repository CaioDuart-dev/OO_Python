from package.maths.terms import Circulo
from package.maths.terms import Ponto
def Circle():
    circle = Circulo(raio,x,y) #objeto que recebe a instância de uma classe.
    return circle #retorna o objeto para poder ser manipulado.

def Point():
    point = Ponto(x,y)
    return point

raio = int(input("digite o raio: ")) 
x = int(input("digite a coordenada x: ")) 
y = int(input("digite a coordenada y: ")) 

if __name__ == "__main__":
    circle = Circle() #chama o objeto
    circle.circunferencia() #chama as funções do objeto instanciado
    circle.area()
    circle.diametro()
    circle.coordenada()
    
else:
    point = Point()
    point.distance()

