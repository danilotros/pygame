import pygame
from pygame.locals import *
import random
pygame.init
marco=pygame.display.set_mode((800,600))
fondo=(21,9,59)
fondoti=(18, 40, 220)
fondos= (18, 40, 80)
pygame.font.init()
fuente=pygame.font.Font("oberon3d.ttf",50)
fuenteJ=pygame.font.Font("oberon3d.ttf",25)

titulo= fuente.render("SNAKE",True,fondoti)
unoJ=fuenteJ.render("Jugar",True,fondoti)
juegar=fuente.render("SNAKE",True,fondoti)
creditos=fuenteJ.render("Creditos",True,fondoti)
creditoT=fuente.render("CREDITOS",True,fondoti)
creditoC=fuenteJ.render(" HECHO POR Daniel GARCIA PEREA",True,fondoti)
volver=fuenteJ.render("volver x",True,fondoti)
opcion=fuenteJ.render("oprima espacio",True,fondoti)
puntacion=fuenteJ.render("Puntaje",True,fondoti)

serpiente=[(100,100),(80,100),(80,120),(80,140),(80,160),(100,160)]



class juego(object):
    def __init_(self):
        print("graficas ")
        pass
    def colorf(self):
        marco.fill(fondo)
    def titulo(self,seleccion):

        if seleccion==0:
            pygame.draw.rect(marco,fondos,(270,100,200,30))
        elif seleccion==1:
            pygame.draw.rect(marco,fondos,(270,140,200,30))
        marco.blit(titulo,(260,10))
        marco.blit(unoJ,(280,100))
        marco.blit(creditos,(280,140))
        marco.blit(opcion,(260,70))
        pass
    def credits(self):
        marco.blit(creditoT,(240,100))
        marco.blit(creditoC,(100,170))
        marco.blit(volver,(100,210))

        pass
    def jugar(self,ubicacion,comer,puntos):
        contar=0
        for i in serpiente:
            contar+=1
            pygame.draw.rect(marco,fondos,(i[0]+1,i[1]+1,18,18))
            if serpiente.index(i)==len(serpiente)-1:
                if ubicacion==0:
                    serpiente.append((i[0]+20,i[1]))
                elif ubicacion==90:
                    serpiente.append((i[0],i[1]-20))
                elif ubicacion==180:
                    serpiente.append((i[0]-20,i[1]))
                elif ubicacion==270:
                    serpiente.append((i[0],i[1]+20))
                if i !=comer:
                    del serpiente[0]
                    return (comer,puntos)
                else:
                    puntos+=1
                    return ((random.randint(0,40)*20,random.randint(0,29)*20),puntos)
                break

    def comida(self,comer):
        pygame.draw.rect(marco,fondos,(comer[0],comer[1],18,18))
    def puntaje(self,puntaje):
        marco.blit(puntacion,(10,10))
        Puntuar=fuenteJ.render(str(puntaje),True,fondoti)
        marco.blit(Puntuar,(190,10))
        return puntacion
