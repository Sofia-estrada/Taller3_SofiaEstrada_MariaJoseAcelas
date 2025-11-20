# Taller3_SofiaEstrada_MariaJoseAcelas
Integrantes: María José Acelas León Sofia Estrada

  1. Descripción del proyecto:

Este proyecto se basa en el desarrollo de una aplicación en Python capaz de cargar, leer y procesar archivos DICOM, extrayendo metadatos relevantes y realizando un análisis básico de   las imágenes. El objetivo es simular el funcionamiento inicial de un sistema PACS, aplicando conceptos fundamentales de informática médica e interoperabilidad, utilizando librerías como pydicom, numpy y pandas.   Finalmente, el programa implementa Programación Orientada a Objetos mediante una clase principal ProcesadorDICOM, encargada de organizar las funciones de carga, extracción y análisis de las imágenes.

  2. ¿Por qué DICOM y HL7 son cruciales para la interoperabilidad en salud? ¿En qué se diferencian?

DICOM Y HL7 Son cruciales para la interoperabilidad en salud, ya que la estandarización permite que todos hablen el mismo idioma, por lo que el intercambio de datos es más sencillo y menos propenso a errores. Sus principales diferencias son: 
  DICOM: 
    -Es el estándar internacional para almacenar y transmitir imágenes médicas e información relacionada. 
    -Permite la integración de escáneres, servidores, estaciones de trabajo, impresoras y hardware de red de múltiples fabricantes en un sistema de archivo y comunicación de imágenes (PACS). 
    -Admite diversos formatos de imagen, entre ellos, rayos X, ultrasonido, tomografía computarizada (TC) y resonancia magnética (RM). 
  HL7: 
    -Se refiere a un conjunto de estándares internacionales para la transferencia de datos clínicos y administrativos entre aplicaciones de software. 
    -Se centra en el lenguaje y la estructura de dichos datos para garantizar la interoperabilidad entre sistemas. 
    -No se limita a datos de imagen, sino que abarca un amplio espectro de datos de servicios hospitalarios y ambulatorios.

  3. ¿Qué relevancia clínica o de pre-procesamiento podría tener el análisis de la distribución de intensidades de una imagen médica?

La distribución de intensidades en una imagen médica es clave tanto para la interpretación clínica como para el procesamiento computacional, ya que estos métodos buscan mejorar la calidad de la imagen, reducir el ruido y optimizar la interpretabilidad general. En la relevancia clínica, ayuda a diferenciar tejidos (grasa, músculo, hueso, aire), tamnbién permite identificar lesiones con intensidades anómalas, contribuye a evaluar la calidad de la imagen y detectar artefactos, y en el pre-procesamiento, permite normalizar imágenes antes de usarlas en modelos computacionales, facilitando las técnicas de segmentación basadas en umbrales, detectando imágenes fuera del rango esperado (errores de calibración), ayudando a definir parámetros para algoritmos de filtrado o mejora de contraste y calculando la intensidad promedio es un primer paso para comprender la estructura básica de la imagen y su uniformidad.

  4. Dificultades encontradas y la importancia de las herramientas de Python para el análisis de datos médicos.

Dificultades:
  - Algunos archivos pueden estar no identificado, por lo que no todos los tags DICOM están disponibles, debido a que la estructura interna de un archivo DICOM varía según el equipo fabricante.
  - Errores comunes al leer directorios que incluyen archivos que no son DICOM.
  - Manejar las dimensiones y formatos del atributo pixel_array y además encontrar la ruta correcta de los archivos al momento de ejecutar el código.

Importancia de Python: Python ofrece herramientas poderosas para la ingeniería biomédica: 
      -Pydicom permite leer y manipular archivos DICOM de manera simple. 
      -Numpy facilita cálculos sobre matrices de píxeles. 
      -Pandas permite organizar los datos extraídos en tablas fáciles de analizar.

De esta manera, se facilita el análisis múltiple de imágenes y el procesamiento de los datos para convertirlos en información comprensible y fiable para los pacientes y el personal médico.
