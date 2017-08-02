# CurvHor

## ¿Que es?

CurvHor es un paquete que te permite realizar los cálculos de los elementos que contiene una Curva Horizontal a partir de los datos de un archivo CSV, (ésto, hablando de topografía), como lo son la longitud de la curva, la cuerda, las subyacentes, la externa, la ordenada media y el radio de esta misma, ya sea para la obtención de ellos o la comprobación, en dado caso de ya tener una curva trazada, de manera simple solamente con la utilizacion de un archivo delimitado por comas y el ángulo de deflexión de la curva deseada.


## Condiciones

El paquete tendra la funcionalidad de realizar los cálculos sin ninguna dificultad si los datos contenidos en el archivo CSV son de las coordenadas a todo lo largo del trazo de la curva contando con las del PC (Punto Comienzo) y el PT (Punto de Termino), sin importar si no se encuentra ordenado el archivo.


## Instalación Del Paquete
Para la instalación es necesario correr estos comandos en la consola...  
```
1.- conda install git
```
```
2.- pip install git+https://github.com/edyanez11/CurvHor     
```
Y ahora solamente se importa de la misma manera que cualquier módulo.  
Como puede ser:
```
import CurvHor
```
Y queda listo para ser utilizado.

## ¿Cómo utilizarlo?

Una vez instalado e importado el paquete a nuestra consola, es necesario hacer la inserción de 4 variables (que en sí serían solo dos, ya que, 3 de las variables necesarias son para la especificación del ángulo de inflexión), donde en la primera; se pide el nombre del archivo CSV donde se encuentran contenidas las coordenadas de la curva (cabe hacer la mención de que el nombre del archivo tiene que estar escrito sin la extensión de este mismo), la segunda; son los grados correspondientes al ángulo de inflexión (°), en la tercera; se piden los minutos de este mismo ángulo ('), y en la última variable se piden los segundos (").
Una vez ingresados las variables correspondientes de la manera indicada serán generados los resultados de las variables anteriormente mencionandas, solo queda esperar.


## Ejemplo 

Suponiendo que el nombre de nuestro archivo sea "datos_curva"(por decir un nombre), y nuestro ángulo de deflexión sea de 87°42'12" en el programa se introduciría de la siguiente manera: 
```
CurvHor(datos_curva, 87, 42, 12)
```
Y con esto, ya tendrian todos los valores calculados de una curva horizontal.


## Resultados

Como resultado el programa generará los valores correspondientes a la 'longitud de la curva', 'el radio', 'las subtangentes', 'la externa', 'la ordenada media' y 'la cuerda'. Dando como resultado una imagen de una curva con las subtangentes y la cuerda trazadas como se puede observar en la imagen de enseguida:

![](https://user-images.githubusercontent.com/30146147/28871811-ce02d3a0-774b-11e7-9e26-f7af439eb784.png)

Indicando que no tuvo ningún error al momento de realizar el proceso, y después de cerrar la ventana emergente de esa imagen se mostrarán los resultados  expreados en mestros de los elementos de la curva horizontal, mas o menos de la siguiente manera:

![](https://user-images.githubusercontent.com/30146147/28872220-da98589a-774d-11e7-8687-8ee6dbc08418.png)



