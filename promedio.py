def promedio():
    n = 0
    c = 0
    suma = 0

    while n >= 0:
        n = int (input('Ingresa numeros para obtener el promedio:'))
        
        if n > 0:
            c = c+1
            suma = suma + n
        
        if n == -1:
            print('El promedio es: ',suma/c)
