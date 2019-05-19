from PIL import Image
import bitarray
import sys, getopt
import os
import os.path

def recuperarArchivo(img1, img2, salida):
	if os.path.isfile(img1) and os.path.isfile(img2):
		im_original = Image.open(img1) # Imagen original
		pix_original = im_original.load()
		im_intercepted = Image.open(img2) # Imagen modificada
		pix_intercepted = im_intercepted.load()
		width, height = im_original.size
		ba = bitarray.bitarray() # Creamos un array de bits
		aux = 0;
		for y in range(0, height): # Por cada fila
		    for x in range(0, width): # Por cada columna
		        if pix_original[x,y] != pix_intercepted[x,y]: # Si el pixel es distinto
		        	ba.append(True) # Es un 1 en el array
		        else:
		        	ba.append(False) # 0 en caso contrario
		        aux = aux + 1
		with open(salida, 'wb') as fh:
		    ba.tofile(fh) # Guardamos los bits obtenidos en un archivo
		    exit(0)
	else:
            print("Error: Las imagenes especificadas no existen. Compruebe que su ubicacion")
	exit(1)

if __name__ == "__main__":
	if len(sys.argv) == 4:
		recuperarArchivo(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		print ("Este script permite recuperar un archivo ocultado en los pixeles de dos imagenes aparentemente identicas. \
            Como son las generadas mediante el script \"generar_imagen_con_dato\"")
		print ("Requisitos: \
		\n\tTener las dos imagenes que ocultan un archivo en las diferencias de sus pixeles. Siendo los pixeles iguales un 0 y los diferentes un 1.\n")
		print ("Uso: recuperar_archivo_pixeles.py <imagen1> <imagen2> <archivoSalida>\n")
	exit(0)
