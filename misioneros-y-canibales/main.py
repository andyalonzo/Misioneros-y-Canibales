#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importacion de los módulos
import pygame
from pygame.locals import *
import sys
from modulocanibal import *
# y cualquier otro modulo usado

 
# -----------
# Constantes
# -----------
 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

PERSONAJES_T = 20

MISIONEROS_L = 70
MISIONEROS_R = 505
MISIONEROS_V = 218

CANIBALES_L = 1
CANIBALES_R = 575
CANIBALES_V = 217

PERSONAJE_BL = 183
PERSONAJE_BR = 413
PERSONAJE_BV = 237

# ----------------------------------------------
# Clases y Funciones utilizadas (lo explicare en la siguiente parte)
# ----------------------------------------------

def main():
	pygame.init()
	running = True
	# creamos la ventana y le indicamos un titulo:
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Misioneros y Canibales")
	
	#Cargar assets
	fondo = pygame.image.load("fondo.jpg").convert()
	fondop = pygame.image.load("perdedor.png").convert()
	fondog = pygame.image.load("ganador.png").convert()
	barco = pygame.image.load("barco.jpg").convert()
	misionero = pygame.image.load("misionero.png").convert_alpha()
	canibal = pygame.image.load("canibal.png").convert_alpha()
	screen.blit(fondo, (0, 0))
	
	
	#Canibales
	screen.blit(canibal, (CANIBALES_L, CANIBALES_V))
	screen.blit(canibal, (CANIBALES_L+PERSONAJES_T, CANIBALES_V))
	screen.blit(canibal, (CANIBALES_L+PERSONAJES_T+PERSONAJES_T, CANIBALES_V))
	
	#Misioneros
	screen.blit(misionero, (MISIONEROS_L, MISIONEROS_V))
	screen.blit(misionero, (MISIONEROS_L+PERSONAJES_T, MISIONEROS_V))
	screen.blit(misionero, (MISIONEROS_L+PERSONAJES_T+PERSONAJES_T, MISIONEROS_V))
	
	#screen.blit(misionero, (PERSONAJE_BL, PERSONAJE_BV))
	#screen.blit(canibal, (PERSONAJE_BL+25, PERSONAJE_BV))
	
	#screen.blit(misionero, (PERSONAJE_BR, PERSONAJE_BV))
	#screen.blit(canibal, (PERSONAJE_BR+25, PERSONAJE_BV))
	
	tmp_pos = 0
	
	# se muestran lo cambios en pantalla
	pygame.display.flip()
	
	# llamar a la clase canibal
	CAN = Canibal()
	# el bucle principal del juego
	while running:
		#  [self.barco_p,self.canib_iz,self.mision_iz,self.mision_de,self.canib_de,self.barco_c,self.barco_m]
		datos = CAN.getValues()
		print(datos)
		if CAN.perdedor == True:
			screen.blit(fondop,(0, 0))
		elif CAN.ganador == True:
			screen.blit(fondog,(0, 0))
		else:
			screen.blit(fondo, (0, 0))
		if datos[0] ==0:
			screen.blit(barco, (160, 260)) # Barco en la izquierda
		else:
			screen.blit(barco, (390, 260)) # Barco en la derecha
		## MOSTRAR PERSONAJES DEL LADO IZQUIERDO
		for i in range(datos[1]):
			screen.blit(canibal, (CANIBALES_L+(PERSONAJES_T)*i, CANIBALES_V))
		for i in range(datos[2]):
			screen.blit(misionero, (MISIONEROS_L+(PERSONAJES_T)*i, MISIONEROS_V))
		## MOSTRAR PERSONAJES DEL LADO DERECHO
		for i in range(datos[3]):
			#Mostrar Canibales en la izquierda
			screen.blit(canibal, (CANIBALES_R+(PERSONAJES_T)*i, CANIBALES_V))
		for i in range(datos[4]):
			screen.blit(misionero, (MISIONEROS_R+(PERSONAJES_T)*i, MISIONEROS_V))
		## MOSTRAR PERSONAJES EN EL BARCO 
		if datos[0] == 0:
			tmp_count = 0
			for i in range(datos[5]):
				#Mostrar Canibales en la izquierda
				screen.blit(canibal, (PERSONAJE_BL+(PERSONAJES_T)*i, PERSONAJE_BV))
				tmp_count = tmp_count +1
			for i in range(datos[6]):
				#Mostrar Canibales en la izquierda
				screen.blit(misionero, (PERSONAJE_BL+(tmp_count)*21+(PERSONAJES_T)*i, PERSONAJE_BV))
		else:
			tmp_count = 0
			for i in range(datos[5]):
				#Mostrar Canibales en la izquierda
				screen.blit(canibal, (PERSONAJE_BR+(PERSONAJES_T)*i, PERSONAJE_BV))
				tmp_count = tmp_count +1
			for i in range(datos[6]):
				#Mostrar Canibales en la izquierda
				screen.blit(misionero, (PERSONAJE_BR+(tmp_count)*21+(PERSONAJES_T)*i, PERSONAJE_BV))
			
		for event in pygame.event.get():
			# se muestran lo cambios en pantalla
			pygame.display.flip()
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if CAN.perdedor == False and CAN.ganador == False:
					print("Capturar teclas")
					if event.key == K_LEFT:
						CAN.setBarcoPosition(0)
					elif event.key == K_RIGHT:
						CAN.setBarcoPosition(1)
					elif event.key == K_c:
						CAN.subirCanibal()
					elif event.key == K_x:
						CAN.bajarCanibal()
					elif event.key == K_m:
						CAN.subirMisionero()
					elif event.key == K_n:
						CAN.bajarMisionero()

if __name__ == "__main__":
	main()
