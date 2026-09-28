import cv2
## Leer la imagen con cv2 = coputer vision
img = cv2.imread('perrobeisbol.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrar imagen en ventana
cv2.imshow('perrobeisbol0068', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las vetanas
cv2.destroyAllWindows()




