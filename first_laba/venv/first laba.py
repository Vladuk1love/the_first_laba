from PIL import Image
image1 = Image.open("picc.png")
image2 = Image.open("picc2.png")










def quadratic_equation(a:float, b:float, c:float):
    D = b**2 - 4*a*c
    if a == 0 and b != 0:
        return float((-c)/b)
    elif a == 0 and b == 0:
        image1.show()
    else:
        if D < 0:
            image2.show()
        else:
            x1 = (-b + D**0.5)/(2*a)
            x2 = (-b - D**0.5)/(2*a)
            return set([x1, x2])


a = float(input('Введите коэффицент а'))
b = float(input('Введите коэффицент b'))
c = float(input('Введите коэффицент c'))
print(quadratic_equation(a, b, c))
