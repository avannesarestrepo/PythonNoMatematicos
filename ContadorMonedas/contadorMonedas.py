from cv2 import cv2
import numpy as np

original = cv2.imread('monedas.jpg')

grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

