import csv

from PIL import Image

dicImagenes = {'b':'imagenes/blanco.png',
               'n': 'imagenes/negro.png', 
               'g': 'imagenes/gris.png',
               'd':'imagenes/derecho.png', 
               'r': 'imagenes/reves.png',
               'x': 'imagenes/x.png', 
               'n0': 'imagenes/n0.png',
               'n1': 'imagenes/n1.png',
               'n2': 'imagenes/n2.png',
               'n3': 'imagenes/n3.png'}

for i in dicImagenes:
    dicImagenes[i] = Image.open(dicImagenes[i])
    
columnas = 0
filas = 0
with open('map.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for lineNum, line in enumerate(csv_reader):
        if len(line) > columnas:
            columnas = len(line)
        filas = lineNum

filas += 1        

w = columnas * 50
h = filas * 50
nueva = Image.new('RGB', (w, h))
print('Tamaño imagen: ',w, 'x',h)

y = -50

with open('map.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        x = 0
        y += 50
        for imagen in row:
            try:
                nueva.paste(dicImagenes[imagen],(x,y))
            except:
                nueva.paste(dicImagenes['b'],(x,y))
            x += 50

nombreFic = input('Nombre del fichero:\n')
nueva.save(nombreFic + '.png')