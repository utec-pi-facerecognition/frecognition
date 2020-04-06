# Redes Neuronales Recurrentes 

 Las *Recurrent Neural Networks (RNN)* se diferencia de una red neuronal en el tipo de datos a procesar, estas redes permiten trabajar con una secuencia de datos relacionados entre sí, como una serie de palabras o de imágenes, mientras que las redes neuronales sólo pueden procesar una palabra o imagen.
 
 La manera en la que trabajan las neuronas en este tipo de redes es enviando la salida en un determinado tiempo como parámetro de entrada a la misma neurona.
 
![imagen](images/im1.png)

De esa manera considerando un determinado tiempo podemos tener distintas capas para cada instante de tiempo.

![imagen](images/im2.png)

Entonces tendríamos una secuencias de entradas  $x = (x_{1}, ... x_{t})$ durante un tiempo $t$ con una salida $y=(y_{1},...,y_t)$ donde cada salida también será una entrada en la siguiente capa de tiempo, por lo que en este caso simple de neurona se puede expresar con la función de activación $y_t=f(Wx_t+Uy_{t-1}+b)$.

Se puede decir que este tipo de red neuronal cuenta con memoria, puesto que para calcular el estado en un determinado tiempo debe recordar sus anteriores estados. A pesar de esto el peso que tendrá $y_1$ irá disminuyendo conforme pase el tiempo, es decir será menos importante hasta el punto de ser olvidada, debido a esto existe una extensión de las redes neuronales, las *Long-Short Term Memory*(LSTM).

## Long-Short Term Memory
Esta extensión de RNN permite tener un mejor manejo de la memoria debido a que trabaja con una celda de estados, esta se encarga de añadir o remover datos de la memoria de la red. Para esto las neuronas trabajan con 3 puertas: Input Gate (permite añadir datos la memoria), Output Gate (actualiza el estado oculto de la neurona), Forget Gate (olvidar un dato).

### Arquitecturas de redes recurrentes

 - One to many : recibe como entrada un dato único y retorna una secuencia. Ej: Descripción de una imagen
 - Many to one : recibe como entrada una secuencia y retorna un dato único. Ej: Detección de persona en vídeos.
 - Many to many : tanto la entrada como la salida son secuencias. Ej: Traductores.

## Fuentes

 - Codificandobits. (2019, Junio) Redes Neuronales Recurrentes. Recuperado de: https://www.youtube.com/watch?v=bKkjQx_PS_M&list=PL9E7H1rzXKFKRQA2TiNRJG3bezPDxG6c3
 - Jordi Torres (2019) Redes Neuronales Recurrentes. Recuperado de https://torres.ai/redes-neuronales-recurrentes/

