def area(a, h):
    '''
    Возвращает площадь треугольника

        Параметры:
            a(int): основание треугольника
            h(int): высота треугольника

        Возвращаемое значение:
            a * h / 2: площадь треугольника
    '''
    if (type(a) is not int or type(h) is not int):
        raise TypeError("Аргумент должен быть типа int")
    
    if (a <= 0 or h <= 0):
        raise ValueError("Аргумент должен быть больше нуля")
    
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника

        Параметры:
            a(int): 1 сторона треугольника
            b(int): 2 сторона треугольника
            c(int): 3 сторона треугольника

        Возвращаемое значение:
            a + b + c: периметр треугольника
    '''
    if (type(a) is not int or type(b) is not int or type(c) is not int):
        raise TypeError("Аргумент должен быть типа int")
    
    if (a <= 0 or b <= 0 or c <= 0):
        raise ValueError("Аргумент должен быть больше нуля")
    
    return a + b + c
