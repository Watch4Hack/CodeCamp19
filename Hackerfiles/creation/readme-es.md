# **Generación reto "hackerfiles"**
- **1**. Descargamos la imagen ![alt text](hacker.jpg)

- **2**. Convertimos el texto a binario y elimanos dos bits para hacerlo un poco más complicado. Después pasamos el binario a base64.

- **3**. Añadimos el texto al final del fichero con el siguiente comando:
      echo <texto en base64> >> hacker.jpg

- **4**. Cogemos una palabra dentro del diccionario rockyou.txt que viene por defecto en Kali Linux relacionada con el reto. Comprimimos la imagen en un zip con la contraseña elegida.

      zip --encrypt hackerfiles.zip hacker.jpg


**Tras esto tendremos el archivo hackerfiles.zip**
