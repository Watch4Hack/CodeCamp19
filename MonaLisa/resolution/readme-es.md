# **Resolución del reto "METAmorphosis"**

**Pista: "Algunas imágenes contienen información interesante en sus metadatos."**

- **1**. Abrimos la imagen y a simple vista en el margen superior derecho se aprecia algo, ampliamos la imagen y vemos el texto: UltraHidden

![alt text](text.png)

- **2**. Obtenemos mensaje secreto de dentro de la imagen utilizando la contraseña que hemos encontrado: **steghide extract -sf MonaLisa.jpg**. Vemos el contenido del texto y obtenemos la credenciales (la flag).

![alt text](steghide.png)


  **CodeCamp2019{CEO_CodeCamp2019:4ny0n3C4nH4ckM3}**
