from package.maths.terms import Reta
# de 'pacote' importar 'classe' - recebe o programa
# de 'pacote' importar 'arquivo' - recebe o módulo 
def workspace():
    segmento_1 = Reta(2,3)
    segmento_1.model()
    print(f'Interpolando o valor 4: y = {segmento_1.interpolar(4)}')
# variavel de ambiente: __name__
if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')
