palindromo= lambda string :string ==string[::-1]
print(palindromo('xavier'))
print(palindromo('ana'))

"""
el palindrome es ver si un nombre se lee
igual de izquierda a derecha o se viseversa
el resutado va ser siempre un dato de tipo booleano es decir False o True.
"""
def palindromo(string):
    return string == string[::-1]
print(palindromo('ana'))
#