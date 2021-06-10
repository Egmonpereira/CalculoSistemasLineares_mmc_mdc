from entrada import Entrada
from mmc_mdc import MMC_MDC
import os
import numpy

if __name__ == "__main__":
    os.system('clear')
    s = input("Resolver Sistema Linear? [S/N]: ")
    m = input("Calcular MMC e MDC? [S/N]: ")
    if s == 's' or s == 'S':
        Entrada.entradas()
    if m == 's' or m == 'S':
        n = input("Digite 2 números inteiros: ").split(" ")
        print("MMC",n,'=',MMC_MDC.mmc(n))
        print("MDC",n,'=',MMC_MDC.mdc(n))
