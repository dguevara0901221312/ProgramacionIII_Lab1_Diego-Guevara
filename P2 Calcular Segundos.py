print('2. Programa conversor de hora a segundos')
hora = input("Escriba la hora en formato Hr:Mn ")

hr, min = map(int, hora.split(':'))
resultado = hr * 3600 + min * 60 

print('Los segundos transcurridos son: ', resultado)