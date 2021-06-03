from calculo import Calculo

class Entrada():
    def entradas():
        Matriz = []
        Termos = []
        dados = []
        n = int(input("Número de variáveis do Sistema: "))
        for i in range(n):
            print("Entre com todos os índeces da ",i+1,"ª variável:")
            linha = []
            for j in range(n):
                t = float(input())
                linha.append(t)
            dados.append(linha)
        print("Entre com os ",n,"Termos do Sistema:")
        for i in range(n):
            t = float(input())
            Termos.append(t)
        #print("Entre com os Coeficientes do Sistema Linear:")
#        dados = [[4,3,3,1],[2,-3,5,-1],[1,-1,1,-1],[-2,-1,1,4]]#input().split(' ')
        #print("Entre com os Termos Independentes do Sistema Linear:")
        #Termos = [3,2,0,-2]#input().split(' ')

        for i in dados:
            Matriz.append(i)
        Calculo.funcao(Matriz,Termos)