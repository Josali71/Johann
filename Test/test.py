

print('Entrez une expression -> ', end='')
expression = input()
print(f'Entrée utilisateur : ({expression}) ')

try:
    result = eval(expression)
except:
    result = 'une erreur s\'est produite'

print(result)