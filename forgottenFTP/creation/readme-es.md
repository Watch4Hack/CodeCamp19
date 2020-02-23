# **Generación reto "forgottenFTP"**

- **1**. Cambiamos la dirección MAC de nuestro host: *sudo macchanger -m de:ad:be:ef:13:37 wlp62s0*

- **2**. Establecemos un servidor FTP a la escucha: *python -m pyftpdlib -u admin -P Sur3Th47UC4N7gU355M3 -d . -p 65535*

- **3**. Iniciamos WireShark y empezamos a capturar el trafico de la interfaz.

- **4**. Generamos tráfico basura y posteriormente, con otro equipo, accedemos al servicio FTP.

- **5**. Volvemos a generar más tráfico irrelevante y guardamos el archivo .pcap.
