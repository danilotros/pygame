
import sys,pygame
from pygame.locals import *
import logica
import time
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego Serpiente")
lo=logica.juego()


fase=0
seleccion=0
ubicacion=0
comer=(200,200)
puntos=0
while True:
	if fase==0:
		lo.colorf()
		lo.titulo(seleccion)
	elif fase==1:
		lo.colorf()
		comer,puntos=lo.jugar(ubicacion,comer,puntos)
		lo.comida(comer)
		lo.puntaje(puntos)
	elif fase==2:
		lo.colorf()
		lo.credits()


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			pass
		elif event.type==KEYDOWN:
			if fase==0:
				if event.key==pygame.K_DOWN:
					if seleccion<1:
						seleccion+=1
					else:
						seleccion=0
				elif event.key==pygame.K_UP:
					if seleccion >0:
						seleccion-=1
					else:
						seleccion=1
				elif event.key==pygame.K_SPACE:
					if seleccion==0:
						fase=1
					elif seleccion==1:
						fase=2

			elif fase==1:
				if event.key==pygame.K_x:
					fase=0
				if event.key==pygame.K_DOWN and ubicacion !=90 :
					ubicacion=270
				if event.key==pygame.K_UP and ubicacion != 270:
					ubicacion=90
				if event.key==pygame.K_RIGHT and ubicacion !=180:
					ubicacion=0
				if event.key==pygame.K_LEFT and ubicacion !=0:
					ubicacion=180
			elif fase==2:
				if event.key==pygame.K_x:
					fase=0



	pygame.display.update()
	time.sleep(0.1)

	pass
