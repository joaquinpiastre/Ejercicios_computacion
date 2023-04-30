import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", help="Operador de la operación ", type=str)
parser.add_argument("-n", help="Primer número", type=int)
parser.add_argument("-m", help="Segundo número", type=int)

arguments = parser.parse_args()

if arguments.o and arguments.n and arguments.m:
    if arguments.o in ["+", "-", "*", "/"]:
        if arguments.o == "/" and arguments.m == 0:
            print("toda deivision por cero no tiene un numero bien definido")
        else:
            if arguments.o == "+":
                res = arguments.n + arguments.m
            elif arguments.o == "-":
                res = arguments.n - arguments.m
            elif arguments.o == "*":
                res = arguments.n * arguments.m
            elif arguments.o == "/":
                res = arguments.n / arguments.m
            print(f"{arguments.n} {arguments.o} {arguments.m} = {res}")
    else:
        print("No se puede realizar")
else:
    print("Falta argumento")