from calculo import Calculo

class Entrada():
    def entradas():
        Matriz = []
        Termos = []
        dados = []
        n = int(input("Número de variáveis do Sistema: "))
        for i in range(n):
            print("Entre com todos os índeces da",i+1,"ª variável:")
            linha = []
            for j in range(n):
                print("X",i+1,"= ",end="")
                t = float(input())
                linha.append(t)
            dados.append(linha)
        print("Entre com os",n,"Termos Independentes:")
        for i in range(n):
            t = float(input())
            Termos.append(t)

        for i in dados:
            Matriz.append(i)
        Calculo.funcao(Matriz,Termos)