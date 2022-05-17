#Detección de colores

#Se importa l  libreria opencv
import cv2

#Se importa la libreria numpy como np
import numpy as np

#Se inical elproceso de captura del Streaming y se guarda en la variable cap
cap = cv2.VideoCapture(0)

# En la línea 17, 18, 20 y 21 se especifica los rangos, para ello se crear un array con numpy,
# allí se especificarán los componentes en H, S y V, seguido de np.uint8 que acepta valores
# entre 0 y 255.Estas arrays se guardaran cada uno en una variable. Estas se declaran antes del el while,
# debido a que solo será necesario declararlas una vez.

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)

redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)

#Se inicia el ciclo while que mientras sea verdadero se ejecutara en bucle.

while True:

#Se declaran dos variable que se inician con la lectura de la variable cap que es la que esta 
#capturando el Streaming.

  ret,frame = cap.read()

#En esa linea si la varaible ret es verdadera se ejecutará el siguente codigo.
  if ret==True:

# Por defecto OpenCV lee a las imágenes o fotogramas en BGR, por esto la transformaremos al espacio de color HSV. 
# Para ello utilizaremos la función cv2.cvtColor, como primer argumento le daremos la imagen a transformar,
# y luego cv2.COLOR_BGR2HSV, para indicar que transformaremos de BGR a HSV. 

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#  En estas líneas se buscar los rangos, para detectar el color rojo,
#  por ello en la línea 51 se usa la función cv2.inRange,
#  el primer argumento es la imagen en la cual se buscará el rango, 
#  en este caso frameHSV, luego el límite inicial y final del primer rango, 
#  el mismo proceso se realizará en la línea 52, para el segundo rango.

#  De aquí se obtendrán las imágenes maskRed1 y maskRed2, que son binarias en donde el color blanco
#  refleja el lugar en donde está presente el primer y segundo rango respectivamente,
#  mientras que el color negro mostrará el lugar donde no están presentes estos rangos.

    maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
    maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)

#  Como deseamos detectar el color rojo, y tenemos 2 rangos establecidos, debemos unirlos,
#  para ello usaremos la línea 58. Aquí estamos sumando ambas imágenes para mostrar en una sola (maskRed),
#  la presencia del color rojo. maskRed por lo tanto también será binaria.

    maskRed = cv2.add(maskRed1, maskRed2)

#  En la linea 67 es donde podremos ver el color rojo detectado,
#  y en las regiones de la imagen donde no se presente este color se visualiza en negro.
#  Para eso se utiliza la funcion de cv2.bitwise_and, 
#  a esta le entregamos como primer y segundo argumento la imagen o fotograma en BGR (frame), luego, mask = maskRed.
#  Esto lo que hace es que la región blanca demaskRed permita visualizar los colores de frame, 
#  mientras que la región en negro se mantenga. 

    maskRedvis = cv2.bitwise_and(frame, frame, mask= maskRed) 

#  En las lineas 73, 74 y 75 se mostraran las capturas del Streaming en ventanas con la funcion imshow,
#  esta ventana recibe dos argumentos el primero seria el titulo de la ventana y el segundo 
#  el objeto que se desea mostrar.
       
    cv2.imshow('frame', frame)
    cv2.imshow('maskRed', maskRed)
    cv2.imshow('maskRedvis', maskRedvis)

#  En la linea 61 se crea una condicion para romper el ciclo del while la cual invoca la funcion waitKey 
#  que esperar para presionar una tecla si la teca presionada es la s se rompera el ciclo con la palabra 
#  reservada break.

    if cv2.waitKey(1) & 0xFF == ord('s'):
      break

#  En la linea 86 al cumplirse el if dejara de capturar el Streaming

cap.release()

#  En la linea 90 destruira todos las ventanas creadas por opencv con la funcion destroyAllWindows.

cv2.destroyAllWindows()