#Documentación: https://furry-find-e06.notion.site/Leer-imagenes-desde-Python-af0b5b6d00b64ed3817349d3e5508f46'''

from cv2 import THRESH_BINARY, cv2
imagen=cv2.imread('placas-amarilla.png')

#Convertir imagen en blanco y negro
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#generando el umbral 
# _ se utiliza para ignorar un valor si un función retorna mas de un resultado
_,umbral = cv2.threshold(grises, 100,255, cv2.THRESH_BINARY)

#findcontours
contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#drawcontours
cv2.drawContours(imagen, contornos, -1, (164, 53, 240), 3)
#Mostrar
cv2.imshow('imagen original', imagen)
#cv2.imshow('imagen grises', grises)
#cv2.imshow('imagen umbral', umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()

