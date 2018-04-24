import cv2

imagem = cv2.imread("saitama.jpg")
cv2.imshow("Original", imagem)

print "Altura (height): %d pixels" % (imagem.shape[0])
print "Largura (width): %d pixels" % (imagem.shape[1])
print "Canais (channels): %d" % (imagem.shape[2])

#cv2.waitKey(0)
#cv2.imwrite("nova imagem.jpg",image)
(b, g, r) = imagem[0, 0]
print("Pixel (0, 0) - vermelho: {}, verde: {}, Azul{}".format(b, g, r))
imagem[0, 0] = (0, 0, 225)
(b, g, r) = imagem[0, 0]
print("Pixel (0,0)- vermelho: {}, Verde: {}, Azul: {}".format(b, g, r))
corner = imagem[0:100, 0:100]
cv2.imshow("corner", corner)

imagem[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Update", imagem)
cv2.waitKey(0)

