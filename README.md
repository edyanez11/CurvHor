# CurvHor

## ¿Que es?

CurvHor es un paquete que te permite realizar los calculos de los elementos que contiene una Curva Horizontal a partir de los datos de un archivo CSV, (ésto, hablando de topografía), como lo son la longitud de la curva, las subyacentes, la externa, la ordenada media y el radio de esta misma, ya sea para la obtención de ellos o la comprobación, en dado caso de ya tener una curva trazada.

## Restricciones

El paquete tendra la funcionalidad de realizar los cálculos sin ninguna dificultad si los datos contenidos en el archivo CSV son de las coordenadas a todo lo largo del trazo de la curva contando con las del PC (Punto Comienzo) y el PT (Punto de Termino), sin importar si no se encuentra ordenado el archivo.

## Instalacion Del Paquete
Para la instalacion es necesario correr estos comandos en la consola...  
```
1.- conda install git
```
```
2.- pip install git+https://github.com/edyanez11/CurvHor     
```
Y ahora solamente se importa de la misma manera que cualquier modulo.  
Como puede ser:
```
import CurvHor
```
## ¿Como utilizarlo?

Una vez instalado e importado el paquete a nuestra consola, es necesario hacer la inserción de 4 variables (que en sí serían solo dos, ya que, 3 de las variables necesarias son para la especificación del ángulo de inflexión), donde en la primera; se pide el nombre del archivo CSV donde se encuentran contenidas las coordenadas de la curva (cabe hacer la mención de que el nombre del archivo tiene que estar escrito sin la extensión de este mismo), la segunda; son los grados correspondientes al ángulo de inflexión (°), en la tercera; se piden los minutos de este mismo ángulo ('), y en la última variable se piden los segundos (").
Una vez ingresados las variables correspondientes de la manera indicada serán generados los datos, solo queda esperar.
