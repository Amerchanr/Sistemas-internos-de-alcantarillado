# Sistemas de Internos de alcantarillado
## Descripción del Problema
Dentro de complejos empresariales y residenciales, los sistemas internos de alcantarillado están diseñados para recolectar las aguas residuales y dirigirlas hacia el sistema principal de la ciudad. Estos sistemas suelen emplear bombas trituradoras para extraer el agua, pero debido a la falta de conciencia social, las personas tienden a desechar residuos de gran tamaño en las alcantarillas, lo que provoca obstrucciones frecuentes. La acumulación de sólidos en las aguas residuales genera graves consecuencias técnicas, económicas y sociales. Las obstrucciones deterioran rápidamente las bombas, aumentan los costos de mantenimiento y reparaciones, y originan reboses que causan contaminación ambiental, malos olores y afectan la calidad de vida de las comunidades cercanas.

En lugares críticos como centros comerciales, estos problemas impactan negativamente la actividad económica al alejar a los clientes. Además, las intervenciones correctivas realizadas por los técnicos deben ejecutarse en entornos peligrosos, húmedos y contaminados, lo que conlleva altos riesgos laborales. Por lo tanto, es necesario implementar un sistema de control que prevenga los daños recurrentes en las bombas y otros componentes del sistema de alcantarillado, asegurando su correcto funcionamiento, prolongando su vida útil y minimizando los riesgos asociados.

<img width="261" alt="Image" src="https://github.com/user-attachments/assets/0066ef38-1b7c-49fb-a67f-d2e0cc35e5a2" />
## Descripción del Prototipo
Para abordar esta problemática, se propone desarrollar un prototipo basado en
sensores y tecnologías IoT, diseñado para monitorear y detectar taponamientos de
manera temprana en tiempo real. Este sistema permitirá identificar condiciones
críticas, como acumulación de sólidos o cambios en la presión, y enviará alertas a
los técnicos encargados antes de que ocurran fallas mayores. Además, el prototipo
facilitará el mantenimiento preventivo, optimizando recursos, minimizando los daños
en las bombas y prolongando su vida útil. Este enfoque también busca garantizar la
seguridad de los técnicos y reducir los impactos negativos en la comunidad,
promoviendo un modelo sostenible y replicable para sistemas de bombeo similares.


## Requerimientos
### Requerimientos funcionales de Hardware

- Se requiere de sensor que me permita obtener información sobre el nivel del agua
- Se requiere un sensor que permita medir el flujo que la bomba está enviando a través de la tubería
- Se requiere de una protección física que evite que la bomba se vea afectada por atascamientos.
- Se requiere de un sistema de respaldo que verifique el correcto funcionamiento de los sensores
### Requerimientos no funcionales de Hardware

- El sistema debe ser capaz de ampliarse para integrar másnsensores o actuadores sin necesidad de rediseñar su arquitectura.
- El sistema debe operar de forma continua y garantizar un tiempo de inactividad no mayor al 1% durante su operación anual.
- Los componentes del sistema deben ser eficientes en términos de energía, reduciendo el impacto ambiental y los costos operativos.


### Requerimientos funcionales de Software
- Se requiereque el sistema permita visualizar variables críticas, como nivel y flujo en tiempo real desde la interfaz HMI. 
- Se requiere que la interfaz de usuario envíe una alerta visual y auditiva al dispositivo del técnico, para notificar cualquier cambio o problema en el estado de las bombas.
- Se requiere un sistema de control sea capaz de almacenar la información proporcionada por los sensores y en función de esos datos, activar o desactivar la bomba.
- Se requiere que el software almacene los datos registrados durante  un rango de 6 meses ,permitiendo la generación de reportes y análisis.
### Requerimientos no funcionales de Software
- El sistema debe contar con protocolos de encriptación y autenticación de usuarios para proteger los datos y prevenir accesos no autorizados.


## Diagrama de Flujo
![Image](https://github.com/user-attachments/assets/03a44c93-02a1-4531-9b3e-51724e1e66f4)

## Diagrama de Caja Negra
<img width="362" alt="Image" src="https://github.com/user-attachments/assets/1fe7b3c2-e333-49cc-823d-9c679954f8bb" />
## Diagrama Tecnologico
