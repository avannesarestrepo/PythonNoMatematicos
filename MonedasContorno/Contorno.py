#Documentación: https://furry-find-e06.notion.site/Leer-imagenes-desde-Python-af0b5b6d00b64ed3817349d3e5508f46'''

from cv2 import THRESH_BINARY, cv2
imagen=cv2.imread('MonedasContorno\contorno.jpg')

#Convertir imagen en blanco y negro
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
umbral = cv2.threshold(grises, 100,255, cv2.THRESH_BINARY)

#Mostrar
cv2.imshow('imagen', grises)
cv2.imshow('imagen original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

