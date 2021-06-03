from calculo import Calculo

class Entrada():
    def entradas():
        Matriz = []
        #print("Entre com os Coeficientes do Sistema Linear:")
        dados = [[4,3,3,1],[2,-3,5,-1],[1,-1,1,-1],[-2,-1,1,4]]#input().split(' ')
        #print("Entre com os Termos Independentes do Sistema Linear:")
        Termos = [3,2,0,-2]#input().split(' ')

        for i in dados:
            Matriz.append(i)
        Calculo.funcao(Matriz,Termos)