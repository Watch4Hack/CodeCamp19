# **Resolución reto del "Don't Remember"**

Vemos mediante el uso de *file* que es correcta la extensión del archivo, nos encontramos con un archivo python compilado, el cual nos solicita al ejecutarse una contraseña.

      binaryshadow@BinaryLaptop:~/ctf$ file triHash.pyc 
      triHash.pyc: python 2.7 byte-compiled
      binaryshadow@BinaryLaptop:~/ctf$ python triHash.pyc 
      #####  #####  ###    #####  #####  #####  ### ###  #####     ##  #####
      #      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   #
      #      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  #####
      #      #   #  #  #   #      #      #   #  #     #  #          #      #
      #####  #####  ###    #####  #####  #   #  #     #  #          #      #

      Introduzca la clave de desbloqueo del software: 

Ya con esta información procedemos a empezar con la resolución del problema:

- **1**. Descompilamos el archivo "*triHash.pyc*" utilizando el programa "**uncompyle6**" -> *uncompyle6 triHash.pyc > triHash.py*

- **2**. Analizamos el código en el archivo "*triHash.py*" y encontramos la contraseña consiste en una cadena de tres palabras separadas por "\_", que la cadena consta de 14 letras y, además, que contamos con los 3 hash SHA256 de las palabras que conponen dicha clave (se ordenan durante la ejecución).
  - **SHA256 = [
 'B9776D7DDF459C9AD5B0E1D6AC61E27BEFB5E99FD62446677600D7CACEF544D0',
 '5694D08A2E53FFCAE0C3103E5AD6F6076ABD960EB1F8A56577040BC1028F702B',
 '14EBE56A5008E7C251101E9E1FDBE281AB0A82BD6FA00A5CEF746B9EE0DD31D1']**


- **3**. Si analizamos más de cerca el código, encontramos que hay una variable donde se ván ordenando dichos hash, para luegos compararlos con los hash del texto introducido, esta variable es "*correctFlag*". Por lo que podemos modificar el código para imprimir dicha variable antes de la comprobación, obteniendo asi el hash de las palabras ordenado:
        
        ...
        if index != 1:
          answer = answer + '_'
          correctFlag = correctFlag + '_'
        print 'Hashes del password ordenados: ' + correctFlag
        if correctFlag.upper() == answer.upper():
        ...
        
- **4**. Ejecutamos el código modificado, intruducimos un string cualquiera de 14 caracteres y obtenemos los tres hashes ordenados, separados por el caracter '_' -> *python triHash.py*

  1º *14EBE56A5008E7C251101E9E1FDBE281AB0A82BD6FA00A5CEF746B9EE0DD31D1*

  2º *B9776D7DDF459C9AD5B0E1D6AC61E27BEFB5E99FD62446677600D7CACEF544D0*

  3º *5694D08A2E53FFCAE0C3103E5AD6F6076ABD960EB1F8A56577040BC1028F702B*

      #####  #####  ###    #####  #####  #####  ### ###  #####     ##  #####
      #      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   #
      #      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  #####
      #      #   #  #  #   #      #      #   #  #     #  #          #      #
      #####  #####  ###    #####  #####  #   #  #     #  #          #      #

      Introduzca la clave de desbloqueo del software: 11111111111111
      Hashes del password ordenados: 14EBE56A5008E7C251101E9E1FDBE281AB0A82BD6FA00A5CEF746B9EE0DD31D1_B9776D7DDF459C9AD5B0E1D6AC61E27BEFB5E99FD62446677600D7CACEF544D0_5694D08A2E53FFCAE0C3103E5AD6F6076ABD960EB1F8A56577040BC1028F702B

      En algo te has equivocado, sigue intentando

- **5**. Utilizamos cualquier base de datos web de hash SHA256 y buscamos la inversa de los hash que componen la contraseña (Ej: *https://hashtoolkit.com/decrypt-sha512-hash/*). Una vez tengamos los inversos de los hash tenemos que la contraseña es **break_the_code**.

- **6**. Ejecutamos el programa e introducimos la contraseña, obteniendo el Flag de la resolución de la prueba -> *python triHash.py*
      
      #####  #####  ###    #####  #####  #####  ### ###  #####     ##  #####
      #      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   #
      #      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  #####
      #      #   #  #  #   #      #      #   #  #     #  #          #      #
      #####  #####  ###    #####  #####  #   #  #     #  #          #      #

      Introduzca la clave de desbloqueo del software: break_the_code

      La clave es correcta.
      La flag es: CodeCamp19{br3ak_th3_c0d3}

  **Flag -> CodeCamp19{br3ak_th3_c0d3}**


