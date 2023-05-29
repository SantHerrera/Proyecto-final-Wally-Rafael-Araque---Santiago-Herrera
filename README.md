# Proyecto-final-Wally-Rafael-Araque---Santiago-Herrera
Explicación Proyecto final Wally Rafael Araque - Santiago Herrera.

Para comprender lo realizado en el proyecto tendremos en cuenta los siguientes pasos:

Configuración del entorno:

Instalar Python en tu sistema.
Instalar las bibliotecas necesarias, como OpenCV para el procesamiento de imágenes y PySerial para la comunicación con el robot.
Conexión con el robot Wally:

Establecer una conexión entre tu programa Python y el robot Wally. Esto puede involucrar la configuración de una conexión serial o utilizar una biblioteca específica proporcionada por el fabricante del robot.
Movimiento del robot:

Implementar funciones para controlar los movimientos del robot, como avanzar, retroceder, girar a la izquierda y girar a la derecha. Estos comandos pueden enviarse al robot a través de la conexión establecida.
Detección y reconocimiento de objetos:

Utilizar la biblioteca OpenCV para capturar imágenes de la cámara del robot y procesarlas.
Implementar algoritmos de visión por computadora para detectar objetos en las imágenes capturadas. Puedes utilizar técnicas como detección de bordes, segmentación de colores o detección de características para identificar objetos en la escena.
Categorización de objetos según su composición:

Una vez que se detecta un objeto, puedes utilizar técnicas de aprendizaje automático o visión por computadora para analizar su composición. Esto podría involucrar la extracción de características de los objetos detectados y la clasificación basada en un modelo preentrenado o entrenado en el momento.
Interacción con objetos:

Implementar funciones para interactuar con los objetos detectados. Por ejemplo, el robot podría tener un brazo mecánico que puede agarrar objetos o utilizar otros sensores para medir propiedades físicas de los objetos, como su peso o temperatura.
Prueba y refinamiento:

Realizar pruebas exhaustivas del proyecto para verificar su funcionamiento correcto.
Realizar ajustes y mejoras en el código según sea necesario para lograr una mayor precisión en la detección de objetos y en la categorización basada en la composición.

Ahora, en cuanto a la interfaz, puedes crear una interfaz de usuario (UI) que muestre la información sobre los objetos reconocidos y permita al usuario interactuar con el robot. Puedes utilizar bibliotecas de Python como Tkinter o PyQt para crear una interfaz gráfica. La interfaz podría mostrar una lista de objetos reconocidos y permitir al usuario seleccionar un objeto para realizar una acción específica, como moverlo a una ubicación diferente.

Además, podrías mostrar información adicional sobre los objetos, como su categoría de composición, mediante etiquetas o íconos visuales en la interfaz. Esto ayudaría al usuario a comprender mejor qué objetos reconoce el robot y cómo están categorizados.
