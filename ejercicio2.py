#Librería

#se importa la libreria de opencv 
import cv2

# de la libreria opencv se importa el metodo para visualizar la imagen.
from cv2 import imshow

# se declara una variable como string y se inicializa con el texto flor.
imgText="flor"

#Lectura de las 3 imagenes

# Se lee la imagen  RGB con el metodo imread, entre parentesis se pone el nombre del archivo,
# que se hace con una concardenación con la variable imgText y el teto .jpg
img= cv2.imread(imgText + '.jpg')


#Para visualizar la primer imagen se utiliza el methodo imshow que entre parentesis recibe
# dos parametros el primero es el nombre de la ventana y el segundo el objeto que se va a visualizar.
imshow('Imagen Original ' + imgText ,img)


#Para cambiar el color de la imagen se utiliza la conversion de espacios.
#img_gris  variable usada para almacenar la conversión de espacio de color de img.
#cvtColor es una función de openCV que convierte imágenes de un espacio de color a otro.
#Esta funcion recibe dos parametros el primero es la imagen que se convertira, y el segundo
# es el código de la conversión del espacio de color en este caso la conversión es de RGB a Gris
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Para visualizar la segunda imagen se utiliza el methodo imshow que entre parentesis recibe
# dos parametros el primero parametro es el nombre de la ventana y el segundo parametro es 
# el objeto que se va a visualizar.
cv2.imshow('Gris', img_gris)

#Para cambiar el color de la imagen se utiliza la conversion de espacios.
#imgen  variable usada para almacenar la conversión de espacio de color de img.
#cvtColor es una función de openCV que convierte imágenes de un espacio de color a otro.
#Esta funcion recibe dos parametros el primero es la imagen que se convertira, y el segundo
# es el código de la conversión del espacio de color en este caso la conversión es de RGB a HSV(Hue, Saturation, Value )
image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

#Para visualizar la tercera imagen se utiliza el methodo imshow que entre parentesis recibe
# dos parametros el primero parametro es el nombre de la ventana y el segundo parametro
# el objeto que se va a visualizar.
cv2.imshow('prueba', image)



# invoca la funcion waitKey que espera un tiempo determinado, al ponerle cero se dice
# que esperara para siempre, pero esperara que se presione alguna tecla.
cv2.waitKey(0)

#despues de presionar una tecla el programa invocara la funcion destroyAllWindows que destruira 
#todas las ventanas que se hayan creado con opencv. 
cv2.destroyAllWindows()