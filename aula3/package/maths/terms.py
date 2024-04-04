class Reta():

    def __init__(self,a,b): #função construtora (a função principal)

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y
    
    # def setA(self,a):

    #     if(a>0)
    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')

import turtle 

class Circulo():
    pass
    def __init__(self,raio, x, y):
        self.raio = raio
        self.x = x
        self.y = y
        t = turtle.Turtle() #cria o curso q fará o desneho na tela

        # Desenha o eixo x
        t.penup()
        t.goto(-400, 0)
        t.pendown()
        t.shape("circle")
        t.shapesize(0.1)
        for i in range(0,80):
            t.forward(10)
            t.stamp()

        # Desenha o eixo y
        t.penup()
        t.goto(0, -400)
        t.pendown()
        t.left(90)
        for i in range(0,80):
            t.forward(10)
            t.stamp()
            
        #reposicionada a tartaruga pra fazer o raio
        t.penup()
        t.left(-90)
        t.goto(x,y)
        t.pendown()
        
        #faz o raio enquanto desenha o circulo
        t.goto(x, y-raio) #origem fica no centro da tela
        t.write(f"\n\n\n r = {raio}")
        t.circle(raio) #desenha o circulo com o raio especificado
        turtle.done() #impede de fechar automaticamente a aba do desenho

    def circunferencia(self):
        C = 2*3.1415*self.raio
        print(f"\na circunferência é: {C}")

    def area(self):
        A = 3.1415*self.raio**2

        print(f"a área é: {A}")

    def diametro(self):
        D = 2*self.raio
        print(f"o diametro é: {D}")
    
    def coordenada(self):
        print(f'as coordenadas são: x: {self.x} e y: {self.y}\n')

class Ponto:
    pass
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self):
        dis = (self.x**2 + self.y**2)**(1/2)
        print(f'a distância até a origem é: {dis}')
