from package.maths.terms import Ponto


def workspace():
    n = int(input("qtd de pontos: "))
    objPonto = Ponto(n)
    cor = objPonto.cor()
    print(cor)
    coo = objPonto.coordenada()
    print(coo)
    
    objPonto.getPonto(coo,cor)