import math

def main():
    #escribe tu código abajo de esta línea
    area_pintura = float(input("Area a pintar en metros: "))
    rend = float(input("Rendimiento (m2/l): "))

    ltrs = math.ceil(area_pintura / rend)

    print("Litros a comprar:",ltrs)


if __name__ == '__main__':
    main()
