#Librería
#importa la libreria de opencv, que es una biblioteca de vision artificial.
import cv2 

# importa la libreria numpy que es muy utilizada en manejo de matrices 
# y se le pone el alias de np para utilizarla.
import numpy as np 

# en esta parte se construye la imagen, con la funcion de numpy llamada zeros,
# que crea una matriz de ceros, de 300 filas, 300 columnas y de 3 canales, 
# que sería BGR. Se especifica el tipo de dato con uint8 que tomara valores entre 0 y 255.
bgr = np.zeros((300,300,3),dtype=np.uint8)

# Se toma todos los elementos de la matriz creada y se asignan nuevos valores para representar 
# un nuevo color, en BGR que seria el amarillo en este caso.
bgr[:,:,:]=(0,255,255)

# se invoca la funcion imshow para mostrar la imagen, esta funcion recibe dos paramatros
# el primer es el titulo de la imagen y el segundo es el objeto que se va a mostrar.
cv2.imshow('BGR',bgr) 

# invoca la funcion waitKey que espera un tiempo determinado, al ponerle cero se dice
# que esperara para siempre, pero esperara que se presione alguna tecla.
cv2.waitKey(0) 

#despues de presionar una tecla el programa invocara la funcion destroyAllWindows que destruira 
#todas las ventanas que se hayan creado con opencv. 
cv2.destroyAllWindows() 