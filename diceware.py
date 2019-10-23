import sys
import argparse
import random
import time

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre de la lista [DW-Espanol.txt] [DW-Englis.txt] [DW-French.txt] [DW-German.txt]")
parser.add_argument("-n",  "--num", help="Numero de palabras ")
args = parser.parse_args()

if (len(sys.argv) == 5):
    if (args.file and args.num):  
        password = ''
        numWords = int(args.num)
        for x in range(numWords):
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            r3 = random.randint(1,6)
            r4 = random.randint(1,6)
            r5 = random.randint(1,6)

            codigo = str(r1) + str(r2) + str(r3) + str(r4)+ str(r5)

            with open(str(args.file), 'r' ) as lista:
                for linea in lista:
                    palabra = linea.find(codigo)
                    if (palabra >= 0):
                        print(linea.rstrip('\n'))
                        password += linea.split(' ')[1].rstrip('\n')           
        print('\nSu contrasena es: ' + password)
        print('\nTiempo de Ejecución:' + str(time.time()-start_time) + 'seg.\n')
        
else:
    print('Uso: -f [archivo Lista] -n  [Numero de palabras]')