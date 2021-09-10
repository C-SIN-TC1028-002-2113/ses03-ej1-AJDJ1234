def main():
    #escribe tu código abajo de esta línea
    a = 4
    b = 5
    oper1 = 2 * (3/4) + 4 * (2/3) - 3 * (1/5) + 5 * (1/2)

    oper2 = 2 * (pow(((35)**2),0.5)) + 4 * (pow(((36)**3),0.5)) - 6 * (pow(((49)**2),0.5))

    oper3 = (a**3 + 2*b**2) / (4*a)

    oper4 = ((2*(a+b)**2) + (4*(a-b)**2)) / (a*(b)**2)

    oper5 = pow(((a+b)**2 + 2**(a+b)),0.5) / (2*a + 2*b)**2

    print(round(oper1,4))
    print(round(oper2,4))
    print(round(oper3,4))
    print(round(oper4,4))
    print(round(oper5,4))

if __name__ == '__main__':
    main()
