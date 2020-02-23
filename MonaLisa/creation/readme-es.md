# **Generación reto "MonaLisa"**

- **1**. Descargamos una imagen jpg de la Mona Lisa (un clásico de la esteganografía)

- **2**. Abrimos la imagen con un editor, y añadimos el texto con transparencia al margen superior derecho (UltraHidden).

- **3**. Con steghide escondemos el archivo con el mensaje dentro de la imagen, asignando como contraseña *UltraHidden*: **steghide embed -cf MonaLisa.jpg -ef message.txt**
