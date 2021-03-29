## guexel@gmail.com 
## https://github.com/gustabmo/perspective
##
## 2020.03.20 a simple 3D perspective viewer
## needs PYGAME https://www.pygame.org/
##

import sys
import math
import time
import pygame
import pygame.freetype
from vectorfunctions import *


winSizeX=1100
winSizeY=700


def lettresXYZ ( e, pos, size, colorLettres ):
	# lettre X
	e.append ( ( (pos+size/2,0,0), (pos+size/2+size,size,0), colorLettres ) )
	e.append ( ( (pos+size/2,size,0), (pos+size/2+size,0,0), colorLettres ) )

	# lettre Y
	e.append ( ( (0,pos+size/2,0), (0,pos+size/2+size/2,0), colorLettres ) )
	e.append ( ( (0,pos+size/2+size/2,0), (size/2,pos+size/2+size,0), colorLettres ) )
	e.append ( ( (0,pos+size/2+size/2,0), (-size/2,pos+size/2+size,0), colorLettres ) )

	# lettre Z
	e.append ( ( (0,0,pos+size/2), (0,0,pos+size/2+size), colorLettres ) )
	e.append ( ( (0,size,pos+size/2), (0,0,pos+size/2+size), colorLettres ) )
	e.append ( ( (0,size,pos+size/2+size), (0,size,pos+size/2), colorLettres ) )


def addVector ( e, coords, color ):
	e.append ( ( coords, (0,0,0), color ) )
	e.append ( ( coords, (coords[0]-math.copysign(0.1,coords[0]),coords[1],coords[2]), color ) )
	e.append ( ( coords, (coords[0],coords[1]-math.copysign(0.1,coords[1]),coords[2]), color ) )
	e.append ( ( coords, (coords[0],coords[1],coords[2]-math.copysign(0.1,coords[2])), color ) )



def createEx20_6c ():
	e=[]

	colorAxes = (100,100,100)
	e.append ( ( (-10,0,0), (10,0,0), colorAxes ) )
	e.append ( ( (0,-10,0), (0,10,0), colorAxes ) )
	e.append ( ( (0,0,-10), (0,0,10), colorAxes ) )

	lettresXYZ ( e, 11, 2, colorAxes )

	addVector ( e, (1,4,-1), (250,200,0) )

	colorTarget = (100,100,250)
	e.append ( ( (3,-10,2), (3,10,2), colorTarget ) )

	colorTry = (10,250,10)
	addVector ( e, (3,(-16+6*math.sqrt(301))/46,2), colorTry )
	addVector ( e, (3,(-16-6*math.sqrt(301))/46,2), colorTry )

	colorTry = (250,10,10)
	addVector ( e, (3,(-4+math.sqrt(2661))/23,2), colorTry )
	addVector ( e, (3,(-4-math.sqrt(2661))/23,2), colorTry )

	return e


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

	lettresXYZ ( e, c+p, c, colorLettres )

	return e




def test_20200205_gp_ex_2():
	colorCube = (180,180,180)
	colorD1 = (10,255,10)
	colorD2 = (255,10,10)
	colorPQ = (10,10,255)
	deltaColor = 90

	e=[]

	e.append ( ( (+5,+5,+5), (+5,+5,-5), colorCube ) )
	e.append ( ( (+5,+5,+5), (+5,-5,+5), colorCube ) )
	e.append ( ( (+5,-5,-5), (+5,+5,-5), colorCube ) )
	e.append ( ( (+5,-5,-5), (+5,-5,+5), colorCube ) )

	e.append ( ( (-5,+5,+5), (+5,+5,+5), colorCube ) )
	e.append ( ( (-5,+5,-5), (+5,+5,-5), colorCube ) )
	e.append ( ( (-5,-5,-5), (+5,-5,-5), colorCube ) )
	e.append ( ( (-5,-5,+5), (+5,-5,+5), colorCube ) )

	e.append ( ( (-5,+5,+5), (-5,+5,-5), colorCube ) )
	e.append ( ( (-5,+5,+5), (-5,-5,+5), colorCube ) )
	e.append ( ( (-5,-5,-5), (-5,+5,-5), colorCube ) )
	e.append ( ( (-5,-5,-5), (-5,-5,+5), colorCube ) )

	e.append ( ( (-3,+5,+5), (-3,+5,+3), colorCube ) )
	e.append ( ( (-5,+5,+3), (-3,+5,+3), colorCube ) )
	e.append ( ( (-3,-5,+5), (-3,-5,+3), colorCube ) )
	e.append ( ( (-5,-5,+3), (-3,-5,+3), colorCube ) )
	e.append ( ( (-3,-5,+3), (-3,+5,+3), colorPQ ) )

	for n in range(-10,+10):
		e.append ( ( (n/2,+5,-5), (n/2,-5,+5), colorD1 ) )
		e.append ( ( (n/2,+5,+5), (n/2,-5,-5), colorD2 ) )

	return e





def addLine ( e, p0, p1, color, t, duration ):
	if ((len(p0)==3) and (len(p1)==3)):
		div = 10
		dt = duration/(div+1)
		v = vectorAB ( p0, p1, 1/div )
		pp = p0
		for n in range(0,div):
			pn = pointPlusVector ( pp, v )
			e.append ( ( pp, pn, (255,255,255), t, t+dt*2 ) )
			e.append ( ( pp, pn, color, t+dt*2 ) )
			pp = pn
			t += dt



def addLineProjection ( e, p0, p1, center, planeP0, planeNormal, color, t, duration ):
	if ((len(p0)==3) and (len(p1)==3)):
		div = 10
		dt = duration/(div+1)
		v = vectorAB ( p0, p1, 1/div )
		pp = p0
		for n in range(0,div):
			pn = pointPlusVector ( pp, v )
			ok = True
			try:
				ppProj = projectionCenterPointPlane ( center, pp, planeP0, planeNormal  )
				pnProj = projectionCenterPointPlane ( center, pn, planeP0, planeNormal  )
			except ValueError:
				ok = False
			if (ok and (distPoints(ppProj,pnProj) < 20)):
				e.append ( ( pp, pn, (255,255,255), t, t+dt*2 ) )
				e.append ( ( pp, pn, color, t+dt*2 ) )
			pp = pn
			t += dt



def projectionCircleHyperbole():
	e = [];
	t = 0.0;

	colorSq1 = ( 100, 200, 20 )
	colorSq2 = ( 200, 100, 20 )
	colorCenter = ( 0, 0, 150 )
	colorConstruction = ( 70, 70, 70 )

	projCenter = ( -6, 0, 6.5 )
	projCenterBase = ( projCenter[0], projCenter[1], 0 )

	projPlaneP0 = ( 0,0,0 )
	projPlaneNormal = ( 0,0,1 )

	e.append ( ( projCenter, projCenterBase, colorCenter ) )
	e.append ( ( projCenterBase, ( 0, 0, 0 ), colorCenter ) ) 
	e.append ( ( (0,20,0), (0,-20,0), colorConstruction ) )
	e.append ( ( (0,-20,0), (30,-20,0), colorConstruction ) )
	e.append ( ( (30,-20,0), (30,20,0), colorConstruction ) )
	e.append ( ( (30,20,0), (0,20,0), colorConstruction ) )

	pA = ( 0, 5, 0 )
	pB = ( 0, 5, 10 )
	pC = ( 0, -5, 10 )
	pD = ( 0, -5, 0 )

	# e.append ( ( pA, pB, colorSq1, t ) )
	t += 0.25
	e.append ( ( pB, pC, colorSq1, t ) )
	t += 0.25
	e.append ( ( pC, pD, colorSq1, t ) )
	t += 0.25
	e.append ( ( pD, pA, colorSq1, t ) )
	t += round(t)

	semiDiagSq = 5*2**0.5
	pE = ( 0,0,5+semiDiagSq )
	pF = ( 0,0+semiDiagSq,5 )
	pG = ( 0,0,5-semiDiagSq )
	pH = ( 0,0-semiDiagSq,5 )
	e.append ( ( pE, pF, colorSq2, t ) )
	t += 0.25
	e.append ( ( pF, pG, colorSq2, t ) )
	t += 0.25
	e.append ( ( pG, pH, colorSq2, t ) )
	t += 0.25
	e.append ( ( pH, pE, colorSq2, t ) )
	t += round(t)

	pAp = projectionCenterPointPlane ( projCenter, pA, projPlaneP0, projPlaneNormal )
	pBp = projectionCenterPointPlane ( projCenter, pB, projPlaneP0, projPlaneNormal )
	pCp = projectionCenterPointPlane ( projCenter, pC, projPlaneP0, projPlaneNormal )
	pDp = projectionCenterPointPlane ( projCenter, pD, projPlaneP0, projPlaneNormal )
	pEp = projectionCenterPointPlane ( projCenter, pE, projPlaneP0, projPlaneNormal )
	pFp = projectionCenterPointPlane ( projCenter, pF, projPlaneP0, projPlaneNormal )
	pGp = projectionCenterPointPlane ( projCenter, pG, projPlaneP0, projPlaneNormal )
	pHp = projectionCenterPointPlane ( projCenter, pH, projPlaneP0, projPlaneNormal )

	addLine ( e, projCenter, pB, colorConstruction, t, 1 )
	addLine ( e, pB, pBp, colorConstruction, t, 1 )

	torig=t
	addLine ( e, pA, pB, colorSq1, t, 1 )
	addLineProjection ( e, pA, pB, projCenter, projPlaneP0, projPlaneNormal, colorSq1, torig, 1 )



	return e





def chessboard():
	e=[];

	colorChessboard = ( 80, 80, 80 )
	colorProjectedChessboard = ( 180, 180, 180 )
	colorBlackSquares = ( 0, 190, 0 )
	colorFrame = ( 150, 150, 0 )
	colorRays = ( 80, 80, 250 )
	squares = 4
	sqSize = 1

	chessboardSize = squares*sqSize

	obs = ( +chessboardSize*0.7, -chessboardSize*0.8, chessboardSize*0.8 )
	baseobs = ( obs[0],obs[1],0 )

	for n in range ( 0, squares+1 ):
		e.append ( ( ( n*sqSize, 0, 0 ), ( n*sqSize, chessboardSize, 0 ), colorChessboard ) )
		e.append ( ( ( 0, n*sqSize, 0 ), ( chessboardSize, n*sqSize, 0 ), colorChessboard ) )

	for px in range ( 0, squares ):
		for py in range ( 0, squares ):
			if (((px+py) % 2)==0):
				x = px*sqSize
				y = py*sqSize
				for n in range ( 1,10 ):
					e.append ( ( ( x+(n/10*sqSize), y, 0 ), ( x+(n/10*sqSize), y+sqSize, 0 ), colorBlackSquares ) )

	e.append ( ( (-chessboardSize*0.1,0,0), (chessboardSize*1.1,0,0), colorFrame ) )
	e.append ( ( (-chessboardSize*0.1,0,chessboardSize), (chessboardSize*1.1,0,chessboardSize), colorFrame ) )
	e.append ( ( (-chessboardSize*0.1,0,0), (-chessboardSize*0.1,0,chessboardSize), colorFrame ) )
	e.append ( ( (chessboardSize*1.1,0,0), (chessboardSize*1.1,0,chessboardSize), colorFrame ) )

	e.append ( ( obs, baseobs, colorFrame ) )
	e.append ( ( baseobs, (obs[0],0,0), colorFrame ) )

	corner = (0,squares*sqSize,0)

	e.append ( ( obs, corner, colorRays ) )
	e.append ( ( baseobs, corner, colorRays ) )

	projCorner = pointPlusVector (
		obs,
		vectorAB ( obs, corner ),
		(0-obs[1])/(corner[1]-obs[1])
	)
	baseprojCorner = ( projCorner[0],projCorner[1],0 )

	e.append ( ( projCorner, baseprojCorner, colorRays ) )

	e.append ( ( projCorner, (0,0,0), colorProjectedChessboard ) )

	for n in range ( 1, squares+1 ):
		e.append ( ( obs, ( 0,n*sqSize,0 ), colorRays ) )
	

	return e



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

	# PinS : le point P projecte' dans l'ecran S (S=Screen)
	vectorSCtoPinS = vectorAB ( SC, pointPlusVector ( eye, vecEyeP, a ) )

	if (abs(dotProduct(vectorSCtoPinS,vecEyeSC)) > 0.0001):
		print ( "ERROR A.3to2 vEyeSC",v2st(vecEyeSC),"vectorSCtoPinS",v2st(vectorSCtoPinS) )

	return (
		winSizeX//2 + int ( dotProduct ( vectorSCtoPinS, horizS ) ),
		winSizeY//2 - int ( dotProduct ( vectorSCtoPinS, vertS ) )
	)


def drawPerspective ( win, textfont, eye, pov, t, obj ):
	distScreen = (winSizeX/2)
	# SC = ScreenCenter
	vecEyeSC = vectorAB ( eye, pov, distScreen*1.5 / distPoints(eye,pov) )
	SC = pointPlusVector ( eye, vecEyeSC )

	# vertS/horizS : les vecteurs vertical et horizontal vers le haut et la droite de l'ecran, avec longueur 1
	if (vecEyeSC[0]==0) and (vecEyeSC[1]==0):
		horizS = ( 1,0,0 )
		if (vecEyeSC[2]==0):
			vertS = ( 0,1,0 )
		else:
			vertS = normalizeVector ( ( 0,-vecEyeSC[2],0 ) )
	elif (vecEyeSC[2]==0):
		horizS = normalizeVector ( (-vecEyeSC[1], vecEyeSC[0], 0 ) )
		vertS = (0,0,1)
	else:
		horizS = normalizeVector ( (-vecEyeSC[1], vecEyeSC[0], 0 ) )
		if (vecEyeSC[2]>=0):
			vertS = normalizeVector ( (-vecEyeSC[0], -vecEyeSC[1], (vecEyeSC[0]**2+vecEyeSC[1]**2)/vecEyeSC[2] ) )
		else:
			vertS = normalizeVector ( (vecEyeSC[0], vecEyeSC[1], -(vecEyeSC[0]**2+vecEyeSC[1]**2)/vecEyeSC[2] ) )

	pygame.Surface.fill ( win, (0,0,0) )
	for line in obj:
		if (
			(len(line) <= 3)
			or
			(
				(t >= line[3]) 
				and 
				((len(line) <= 4) or (t < line[4]))
			)
		):
			pygame.draw.line ( 
				win, 
				line[2], 
				point3Dto2D(line[0],eye,SC,vecEyeSC,horizS,vertS),
				point3Dto2D(line[1],eye,SC,vecEyeSC,horizS,vertS)
			)


	textfont.render_to ( win, (10,10), "{:.2f}".format(t), (130,130,130) )

	pygame.display.flip()

	

def display ( figure ):
	pygame.init()
	win=pygame.display.set_mode((winSizeX,winSizeY))
	clock=pygame.time.Clock()
	textfont = pygame.freetype.Font("c:\\windows\\Fonts\\arial.ttf", 24)

	# figure = createEtoile()
	# figure = createEx20_6c()
	# figure = test_20200205_gp_ex_2()
	# figure = chessboard()
	# igure = projectionCircleHyperbole()

	angle = 0
	radius = 40
	t = 0
	eye = [0,0,0]
	pov = [0,0,0]
	running = True
	timerunning = False
	height = 10


	while (running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		angle += math.pi/200
		drawPerspective ( 
			win, 
			textfont,
			( math.sin(angle)*radius, math.cos(angle)*radius, height ), 
			pov, 
			t, 
			figure 
		)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_DOWN]:
			radius += 1
		if keys[pygame.K_UP]:
			radius -= 1
		if keys[pygame.K_PAGEUP]:
			height += 0.5
		if keys[pygame.K_PAGEDOWN]:
			height -= 0.5
		if keys[pygame.K_RIGHT]:
			timerunning = True
		if keys[pygame.K_LEFT]:
			t -= 1
			if (t < 0):
				t = 0
			timerunning = False
		if keys[pygame.K_ESCAPE]:
			running = False

		clock.tick(30)
		if (timerunning):
			eratime = t
			t += 0.03
			if (math.trunc(eratime) != math.trunc(t)):
				t=t
				#t = math.trunc(t)
				#timerunning = False



	if (1==2):
		for n in range(0,2000,2):
			pygame.event.get()
			rayon = 15*(500/(n+1))
			drawPerspective ( 
				win, 
				textfont,
				(
					math.cos(math.radians(n))*rayon,
					math.sin(math.radians(n))*rayon,
					(-400+n)/80
				),
				(0,0,0), 
				t,
				figure 
			)
			clock.tick(30)

		for n in range(-200,200,2):
			pygame.event.get()
			drawPerspective(
				win,
				textfont,
				(n/10,n/10+15,n/10+15),
				(0,0,0),
				t, 
				figure		
			)
			clock.tick(30)

	time.sleep(1)
	pygame.quit()



