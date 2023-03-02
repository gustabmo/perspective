## guexel@gmail.com 
## https://github.com/gustabmo/perspective
##
## 2020.03.20 a simple 3D perspective viewer
## needs PYGAME https://www.pygame.org/
## pip install pygame
##

import sys
import math
import time as time_lib
import pygame
import pygame.freetype
from vectorfunctions import *
import perspectivesolids


winSizeX=1100
winSizeY=700


def point3Dto2D ( P,eye,SC,vecEyeSC,horizS,vertS ):
	# droite eye -> P sont les points: eye+a*(P-eye) pour tout "a"
	# plan de l'ecran sont les points Q dont: (Q-SC) dot-product vecEyeSC = 0 
	# => (eye+a*(P-eye)-SC) dot-product vecEyeSC = 0
	# => ((eye-SC) + a*(P-eye)) dot-product vecEyeSC = 0
	# => a = -((eye-SC) d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	# => a = ((SC-eye) d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	# => a = (vecEyeSC d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	vecEyeP = vectorAB(eye,P)
	dPEPESC = dotProduct(vecEyeP,vecEyeSC)
	if (dPEPESC==0):
		a = 1
	else:
		a = dotProduct(vecEyeSC,vecEyeSC)/dPEPESC

	# PinS : le point P projecte' sur l'ecran S (S=Screen)
	vectorSCtoPinS = vectorAB ( SC, pointPlusVector ( eye, vecEyeP, a ) )

	if (abs(dotProduct(vectorSCtoPinS,vecEyeSC)) > 0.0001):
		print ( "ERROR A.3to2 vEyeSC",v2st(vecEyeSC),"vectorSCtoPinS",v2st(vectorSCtoPinS) )

	return (
		winSizeX//2 + int ( dotProduct ( vectorSCtoPinS, horizS ) ),
		winSizeY//2 - int ( dotProduct ( vectorSCtoPinS, vertS ) )
	)


def drawPerspective ( win, textfont, eye, pov, time, edges ):
	distScreen = (winSizeX/2)
	# SC = ScreenCenter
	vecEyeSC = vectorAB ( eye, pov, distScreen*1.5 / distPoints(eye,pov) )
	SC = pointPlusVector ( eye, vecEyeSC )

	# vertS/horizS : les vecteurs vertical et horizontal vers le haut et vers la droite de l'ecran, avec longueur 1
	if (vecEyeSC[0]==0) and (vecEyeSC[1]==0):
		horizS = ( -1,0,0 )
		if (vecEyeSC[2]==0):
			vertS = ( 0,1,0 )
		else:
			vertS = normalizeVector ( ( 0,-vecEyeSC[2],0 ) )
	elif (vecEyeSC[2]==0):
		horizS = normalizeVector ( (vecEyeSC[1], -vecEyeSC[0], 0 ) )
		vertS = (0,0,1)
	else:
		horizS = normalizeVector ( (vecEyeSC[1], -vecEyeSC[0], 0 ) )
		if (vecEyeSC[2]>=0):
			vertS = normalizeVector ( (-vecEyeSC[0], -vecEyeSC[1], (vecEyeSC[0]**2+vecEyeSC[1]**2)/vecEyeSC[2] ) )
		else:
			vertS = normalizeVector ( (vecEyeSC[0], vecEyeSC[1], -(vecEyeSC[0]**2+vecEyeSC[1]**2)/vecEyeSC[2] ) )

	pygame.Surface.fill ( win, (0,0,0) )
	for line in edges.edges:
		if (
			(len(line) <= 3) # no time information
			or
			(
				(time >= line[3]) 
				and 
				((len(line) <= 4) or (time < line[4]))
			)
		):
			pygame.draw.line ( 
				win, 
				line[2], # color
				point3Dto2D(line[0],eye,SC,vecEyeSC,horizS,vertS),
				point3Dto2D(line[1],eye,SC,vecEyeSC,horizS,vertS)
			)

	textfont.render_to ( win, (3,3), "time:{:.2f}s".format(time), (130,130,130) )

	pygame.display.flip()

	

def display ( edges, pov=[0,0,0] ):
	pygame.init()
	win=pygame.display.set_mode((winSizeX,winSizeY))
	clock=pygame.time.Clock()
	textfont = pygame.freetype.Font("c:\\windows\\Fonts\\arial.ttf", 24)

	dim = edges.maxDimension()
	angle = 0
	rotspeed = +0.1
	radius = dim*2
	time = 0
	running = True
	timerunning = True
	height = dim*0.6


	while (running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		angle += rotspeed/180*math.pi
		drawPerspective ( 
			win, 
			textfont,
			( pov[0]+math.sin(angle)*radius, pov[1]+math.cos(angle)*radius, height ), 
			pov, 
			time, 
			edges 
		)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_DOWN]:
			radius += dim/10
		if keys[pygame.K_UP]:
			radius -= dim/10
		if keys[pygame.K_PAGEUP]:
			height += dim/20
		if keys[pygame.K_PAGEDOWN]:
			height -= dim/20
		if keys[pygame.K_INSERT]:
			rotspeed -= 0.05
		if keys[pygame.K_DELETE]:
			rotspeed += 0.05
		if keys[pygame.K_HOME]:
			angle -= 1/180*math.pi
		if keys[pygame.K_END]:
			angle += 1/180*math.pi
		if keys[pygame.K_SPACE]:
			timerunning = not timerunning
		if keys[pygame.K_LEFT]:
			time -= 0.1
			timerunning = False
		if keys[pygame.K_RIGHT]:
			time += 0.1
			timerunning = False
		if keys[pygame.K_ESCAPE]:
			running = False

		clock.tick(30)
		if (timerunning):
			time += 0.03

	time_lib.sleep(1)
	pygame.quit()



if __name__ == '__main__':
    print ( "this is a library used by other modules" )
    