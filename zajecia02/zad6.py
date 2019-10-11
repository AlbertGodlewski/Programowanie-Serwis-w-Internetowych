import os
import sys

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
for i in range(5,10):
    lista2.append(lista[i])
for i in range(5,10):
    lista.pop()
print (lista)
print (lista2)
