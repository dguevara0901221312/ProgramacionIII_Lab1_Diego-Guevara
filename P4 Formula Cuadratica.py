print('4. Programa operador de formula cuadratica')
a = float(input('Escriba el dato A: '))
b = float(input('Escriba el dato B: '))
c = float(input('Escriba el dato C: '))


resultado1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
resultado2 = (-b - (b**2-4*a*c)**0.5) / (2*a)

print ('El resultado 1 es: ', resultado1)
print ('El resultado 2 es: ', resultado2)