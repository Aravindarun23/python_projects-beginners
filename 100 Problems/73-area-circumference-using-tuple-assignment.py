radius = float(input("Enter radius: "))

def AreaCir(radius):
    area = 3.14 * radius * radius
    cir = 2 * 3.14 * radius
    return area,cir

area,cir=AreaCir(radius)

print("\nArea of the circle is =",area)
print("Circumference of the circle =",cir)
