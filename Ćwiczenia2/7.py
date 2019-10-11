lista=list(range(1,11))
print(lista)
podziel=lista[5:10]
del lista[5:10]
print(lista)
print(podziel)


lista3 = lista+podziel
print(lista3)
lista3.insert(0,0)
print(lista3)
lista3.sort(reverse=True)
print(lista3)

