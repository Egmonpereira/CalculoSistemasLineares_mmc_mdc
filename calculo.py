import numpy

class Calculo():
    def funcao(Matriz,Termos):
        Deter = []
        aux = []

        Deter.append(numpy.linalg.det(Matriz))
        if Deter[0] != 0:
            #Calcula o Determinante das Colunas x1, ... xn
            print("Coeficientes =",Matriz)
            print("Termos independentes =", Termos)
            t = 0
            for i in range(len(Matriz)):
                for j in range(len(Matriz[0])):
                    if t == j:
                        aux.append(Termos)
                    else:
                        aux.append(Matriz[j])
                        
                Deter.append(numpy.linalg.det(aux))
                t = t + 1
                aux.clear()

            print("Valores Reais:")
            for i in range(len(Matriz)):
                print("X",i+1,"=", round(Deter[i+1]/Deter[0],2))
        else:
            print('Sistema Indeterminado ou Impossível')