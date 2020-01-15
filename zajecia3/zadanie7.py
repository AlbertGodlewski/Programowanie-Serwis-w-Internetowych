def reverse(word):
    #return word[len(word)::-1]
    return word[::-1]


a = "sprawdz czy kod dziala"
print(a + " -> " + reverse(a))
