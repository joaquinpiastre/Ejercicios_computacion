import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", help= "archivo de entrada")
parser.add_argument("-o", help= "archivo de salida")

arguments = parser.parse_args()

if arguments.i:
    try:
        with open(arguments.i, "r") as f_in:
            contenido = f_in.read()
            if arguments.o:
                try:
                    with open(arguments.o, "w") as f_out:
                        f_out.write(contenido)
                        print(f"Se copió el contenido de {arguments.i} a {arguments.o}")
                except IOError as e:
                    print(f"Error al abrir el archivo {arguments.o}: {e}")
            else:
                print("Falta colocar el nombre al archivo de salida")
    except IOError as e:
        print(f"Error al abrir el archivo {arguments.i}: .. {e}")
else:
    print("Faltaria el nombre de archivo de entrada")