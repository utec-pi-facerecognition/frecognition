# Matrices dispersa (Sparse Matrix)

## ¿Qué es?

Una matriz que consiste mayormente de 0s

## Cuantificación

disperso = numero de 0s / total de elementos

## Representación

Requerimos de estructuras de datos para poder representar la data dispersa sin
los 0s y solamente guardar la data relevante. En consecuencia, nos ayuda a
mejorar la velocidad de las operaciones que hagan uso de esta matriz.

### Ejemplos

* Dictionary of Keys
* List of Lists
* Coordinate List
* Compressed Sparse Row (usuado frecuentemente)
* Compressed Sparse Column

## Compressed Sparse Column

```python
from scipy.sparse import csr_matrix

A = csr_matrix([[1, 2, 0], [0, 0, 3]])

print(A)
```


[A Gentle Introduction to Sparse Matrices for Machine Learning](https://machinelearningmastery.com/sparse-matrices-for-machine-learning/)

[Sparse Matrices For Efficient Machine Learning](https://dziganto.github.io/Sparse-Matrices-For-Efficient-Machine-Learning/)
