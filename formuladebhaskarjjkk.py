import math
a = float(input('Escreva um numero para "a": '))
b = float(input('Escreva um numero para "b": '))
c = float(input('Escreva um numero para "c": '))

try:
    num = ((b**2)-4*a*c)

    raiz=math.sqrt(num)

    res1 = ((-b + raiz)/(2*a))
    res2 = ((-b - raiz)/(2*a))

    if res1 == res2:
        print(f'R1:{res1}')
    else:
        print(f'R1:{res1} R2:{res2}') 
except:
    print('conta invalida.')