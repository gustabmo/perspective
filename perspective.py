## guexel@gmail.com 
## 2020.03.20 a simple 3D perspective viewer, uses PYGAME for rendering https://www.pygame.org/

import sys
import math
import time
import pygame


winSize=600


def createEtoile():
	c=1 ## la moitié des côtés du cube
	p=5 ## longeur des pointes
	colorLettres = (255,255,255)
	colorCube = (10,10,10)
	deltaColor = 90

	e=[]

	pointe=(c+p,0,0)
	colorEtoile=(128+deltaColor,128,128)
	e.append ( ( pointe, (c,c,c), colorEtoile ) )
	e.append ( ( pointe, (c,-c,c), colorEtoile ) )
	e.append ( ( pointe, (c,-c,-c), colorEtoile ) )
	e.append ( ( pointe, (c,c,-c), colorEtoile ) )

	pointe=(0,c+p,0)
	colorEtoile=(128,128+deltaColor,128)
	e.append ( ( pointe, (c,c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,c,-c), colorEtoile ) )
	e.append ( ( pointe, (c,c,-c), colorEtoile ) )

	pointe=(0,0,c+p)
	colorEtoile=(128,128,128+deltaColor)
	e.append ( ( pointe, (c,c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,c), colorEtoile ) )
	e.append ( ( pointe, (c,-c,c), colorEtoile ) )

	pointe=(-c-p,0,0)
	colorEtoile=(128-deltaColor,128,128)
	e.append ( ( pointe, (-c,c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,-c), colorEtoile ) )
	e.append ( ( pointe, (-c,c,-c), colorEtoile ) )

	pointe=(0,-c-p,0)
	colorEtoile=(128,128-deltaColor,128)
	e.append ( ( pointe, (c,-c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,-c), colorEtoile ) )
	e.append ( ( pointe, (c,-c,-c), colorEtoile ) )

	pointe=(0,0,-c-p)
	colorEtoile=(128,128,128-deltaColor)
	e.append ( ( pointe, (c,c,-c), colorEtoile ) )
	e.append ( ( pointe, (-c,c,-c), colorEtoile ) )
	e.append ( ( pointe, (-c,-c,-c), colorEtoile ) )
	e.append ( ( pointe, (c,-c,-c), colorEtoile ) )

	# cube
	e.append ( ( (c,c,c), (-c,c,c), colorCube ) )
	e.append ( ( (c,c,c), (c,-c,c), colorCube ) )
	e.append ( ( (c,c,c), (c,c,-c), colorCube ) )
	e.append ( ( (-c,-c,-c), (-c,-c,c), colorCube ) )
	e.append ( ( (-c,-c,-c), (c,-c,-c), colorCube ) )
	e.append ( ( (-c,-c,-c), (-c,c,-c), colorCube ) )
	e.append ( ( (-c,c,c), (-c,-c,c), colorCube ) )
	e.append ( ( (-c,c,c), (-c,c,-c), colorCube ) )
	e.append ( ( (c,-c,c), (-c,-c,c), colorCube ) )
	e.append ( ( (c,-c,c), (c,-c,-c), colorCube ) )
	e.append ( ( (c,c,-c), (-c,c,-c), colorCube ) )
	e.append ( ( (c,c,-c), (c,-c,-c), colorCube ) )

	# lettre X
	e.append ( ( (c+p+c/2,0,0), (c+p+c/2+c,c,0), colorLettres ) )
	e.append ( ( (c+p+c/2,c,0), (c+p+c/2+c,0,0), colorLettres ) )

	# lettre Y
	e.append ( ( (0,c+p+c/2,0), (0,c+p+c/2+c/2,0), colorLettres ) )
	e.append ( ( (0,c+p+c/2+c/2,0), (c/2,c+p+c/2+c,0), colorLettres ) )
	e.append ( ( (0,c+p+c/2+c/2,0), (-c/2,c+p+c/2+c,0), colorLettres ) )

	# lettre Z
	e.append ( ( (0,0,c+p+c/2), (0,0,c+p+c/2+c), colorLettres ) )
	e.append ( ( (0,c,c+p+c/2), (0,0,c+p+c/2+c), colorLettres ) )
	e.append ( ( (0,c,c+p+c/2+c), (0,c,c+p+c/2), colorLettres ) )

	return e


def vectorAB ( A,B,factor=1 ):
	return (
		(B[0]-A[0])*factor,
		(B[1]-A[1])*factor,
		(B[2]-A[2])*factor
	)


def pointPlusVector ( A,V, factor=1 ):
	return (
		A[0]+V[0]*factor,
		A[1]+V[1]*factor,
		A[2]+V[2]*factor
	)


def vectorTimesFactor ( V,F ):
	return ( V[0]*F, V[1]*F, V[2]*F )


def lengthVector ( V ):
	return (V[0]**2 + V[1]**2 + V[2]**2) ** 0.5


def normalizeVector ( V ):
	return vectorTimesFactor ( V, 1/lengthVector(V) )


def distPoints ( A,B ):
	return ((B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2) ** 0.5


def dotProduct ( V1,V2 ):
	return (V1[0]*V2[0] + V1[1]*V2[1] + V1[2]*V2[2])


def v2st ( V ):
	return "(%.2f,%.2f,%.2f)" % V


def point3Dto2D ( P,eye,SC,vecEyeSC,horizS,vertS ):
	# droite eye -> P sont les points: eye+a*(P-eye) pour tout "a"
	# plan de l'ecran sont les points Q dont: (Q-SC) dot-product vecEyeSC = 0 
	# => (eye+a*(P-eye)-SC) dot-product vecEyeSC = 0
	# => ((eye-SC) + a*(P-eye)) dot-product vecEyeSC = 0
	# => a = -((eye-SC) d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	# => a = ((SC-eye) d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	# => a = (vecEyeSC d-p vecEyeSC) / ((P-eye) d-p vecEyeSC)
	vecEyeP = vectorAB(eye,P)
	a = dotProduct(vecEyeSC,vecEyeSC)/dotProduct(vecEyeP,vecEyeSC)

	# PinS : le point P projecte' dans l'ecran S (S=Screen)
	vectorSCtoPinS = vectorAB ( SC, pointPlusVector ( eye, vecEyeP, a ) )

	if (abs(dotProduct(vectorSCtoPinS,vecEyeSC)) > 0.0001):
		print ( "ERROR A.3to2 vEyeSC",v2st(vecEyeSC),"vectorSCtoPinS",v2st(vectorSCtoPinS) )

	return (
		winSize//2 + int ( dotProduct ( vectorSCtoPinS, horizS ) ),
		winSize//2 - int ( dotProduct ( vectorSCtoPinS, vertS ) )
	)


def drawPerspective ( win, eye, pov, obj ):
	distScreen = (winSize/2)
	# SC = ScreenCenter
	vecEyeSC = vectorAB ( eye, pov, distScreen*1.5 / distPoints(eye,pov) )
	SC = pointPlusVector ( eye, vecEyeSC )

	# vertS/horizS : les vecteurs vertical et horizontal vers le haut et droit de l'ecran, avec longueur 1
	if (vecEyeSC[0]==0) and (vecEyeSC[2]==0):
		horizS = ( 1,0,0 )
		if (vecEyeSC[1]==0):
			vertS = ( 0,0,1 )
		else:
			vertS = normalizeVector ( ( 0,0,-vecEyeSC[1] ) )
	elif (vecEyeSC[1]==0):
		horizS = normalizeVector ( (-vecEyeSC[2], 0, vecEyeSC[0] ) )
		vertS = (0,1,0)
	else:
		horizS = normalizeVector ( (-vecEyeSC[2], 0, vecEyeSC[0] ) )
		if (vecEyeSC[1]>=0):
			vertS = normalizeVector ( (-vecEyeSC[0], (vecEyeSC[0]**2+vecEyeSC[2]**2)/vecEyeSC[1], -vecEyeSC[2] ) )
		else:
			vertS = normalizeVector ( (vecEyeSC[0], -(vecEyeSC[0]**2+vecEyeSC[2]**2)/vecEyeSC[1], vecEyeSC[2] ) )

	pygame.Surface.fill ( win, (0,0,0) )
	for line in obj:
		pygame.draw.line ( 
			win, 
			line[2], 
			point3Dto2D(line[0],eye,SC,vecEyeSC,horizS,vertS),
			point3Dto2D(line[1],eye,SC,vecEyeSC,horizS,vertS)
		)
	pygame.display.flip()

	

def main():
	pygame.init()
	win=pygame.display.set_mode((winSize,winSize))
	clock=pygame.time.Clock()

	etoile = createEtoile()

	for n in range(0,2000,2):
		rayon = 12*(500/(n+1))
		drawPerspective ( 
			win, 
			( math.cos(math.radians(n))*rayon, (-800+n)/40, math.sin(math.radians(n))*rayon ),
			(0,0,0), 
			etoile 
		)
		clock.tick(30)

	for n in range(-200,200,2):
		drawPerspective(
			win,
			(n/10+1.5,n/10+1.5,n/10),
			(0,0,0),
			etoile
		)
		clock.tick(30)

	time.sleep(1)
	pygame.quit()


main()
