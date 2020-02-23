# **Generación reto "RSAtwist"**

- **1**. Creamos un par de claves RSA con clave privada de 512 bits: *openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:512*

- **2**. Extraemos clave publica: *openssl rsa -pubout -in private_key.pem -out public_key.pem*

- **3**. Ciframos el archivo con la clave pública: *openssl rsautl -encrypt -inkey public_key.pem -pubin -in flag.txt -out flag.enc*
