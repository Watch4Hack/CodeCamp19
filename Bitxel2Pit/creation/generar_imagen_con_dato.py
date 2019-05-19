from PIL import Image
import bitarray
import sys, getopt
import os
import os.path

def generar_reto(imagenOriginal, archivo):
	if os.path.isfile(imagenOriginal) and os.path.isfile(archivo):
		imagen = Image.open(imagenOriginal) # Imagen original
		aux1, aux2 = imagen.size
		if os.path.getsize(archivo)*8 > aux1*aux2:
			print ("El archivo tiene mas bits que pixeles la imagen.")
			print "Pixeles en la imagen:", aux1*aux2
			print "Tam. archivo:", os.path.getsize(archivo)*8
			exit(1)
		imagen.load()
		imagen.save("imagen1.png") # Guardamos en PNG que es el formato que utiliza PIL
		imagen2 = Image.open('imagen1.png')
		tamX, tamY = imagen2.size
		pixeles = imagen2.load() # Leemos la imagen
		y = 0;
		x = 0;
		# Cargamos el ejecutable
		with open(archivo, "rb") as binaryfile :
			data = binaryfile.read(1) # Leemos 1 byte
			while data !="": # Mientra haya datos
				ba = bitarray.bitarray()
				ba.frombytes(data) # Llemanos el array de bits con los del byte cargado
				for z in range(0,8): # Recorremos la lista de bits
					if ba[z] == True:	# Si el bit tiene valor 1
						pixel = imagen2.getpixel((x,y)) # Cargamos los valores RGB
						if pixel[0] > 0: # Restamos 1 al valor RED siempre que sea mayor de 0
							pixeles[x,y] = (pixel[0]-1,pixel[1],pixel[2])
						else: # En caso contrario sumamos 1
							pixeles[x,y] = (pixel[0]+1,pixel[1],pixel[2])
					x = x + 1
					if x == tamX: # Si estamos al final de la columna
						x = 0
						y = y + 1 # Cambiamos de fila
				data = binaryfile.read(1) # Cargamos el siguiente byte
		imagen2.save("imagen2.png"); # Guardamos la imagen con los pixeles alterados que representan el binario del archivo
	else:
		print ("Error: No existen los archivos especificados. Compruebe que ambos archivos existan")
		exit(1)

if __name__ == "__main__":
	if len(sys.argv) == 3:
		generar_reto(sys.argv[1],sys.argv[2])
	else:
		print ("Este script permite ocultar un archivo cualquiera en una pareja de imagenes.\n")
		print ("Requisitos: \
		\n\t1.La imagen de origen ha de ser un PNG o JPG.\
		\n\t2.El archivo no puede tener un numero de bits mayor al numero de pixeles de la imagen.\n")
		print ("Resultado: Se generaran dos imagenes, cuyos pixeles ocultaran el archivo seleccionado, estas imagenes \
			tendran por nombre \"imagen1.png e imagen2.png\"\n")
		print ("Para volver a obtener el dato oculto utilizar el script \"recuperar_archivo_pixeles.py\"\n")
		print ("Uso: ocultar_archivo_pixeles.py <imagen_original> <dato_a_ocultar>\n")
	exit(0)
