import math
import perspective
import perspectivesolids
from vectorfunctions import *



def addVector ( e, coords, color ):
	e.addEdge ( coords, (0,0,0), color )
	e.addEdge ( coords, (coords[0]-math.copysign(0.1,coords[0]),coords[1],coords[2]), color )
	e.addEdge ( coords, (coords[0],coords[1]-math.copysign(0.1,coords[1]),coords[2]), color )
	e.addEdge ( coords, (coords[0],coords[1],coords[2]-math.copysign(0.1,coords[2])), color )



def createEx20_6c (e):

	colorAxes = (100,100,100)
	e.addEdge ( (-10,0,0), (10,0,0), colorAxes )
	e.addEdge ( (0,-10,0), (0,10,0), colorAxes )
	e.addEdge ( (0,0,-10), (0,0,10), colorAxes )

	e.lettresXYZ ( 11, 2, colorAxes )

	addVector ( e, (1,4,-1), (250,200,0) )

	colorTarget = (100,100,250)
	e.addEdge ( (3,-10,2), (3,10,2), colorTarget )

	colorTry = (10,250,10)
	addVector ( e, (3,(-16+6*math.sqrt(301))/46,2), colorTry )
	addVector ( e, (3,(-16-6*math.sqrt(301))/46,2), colorTry )

	colorTry = (250,10,10)
	addVector ( e, (3,(-4+math.sqrt(2661))/23,2), colorTry )
	addVector ( e, (3,(-4-math.sqrt(2661))/23,2), colorTry )






def test_20200205_gp_ex_2(e):
	colorCube = (180,180,180)
	colorD1 = (10,255,10)
	colorD2 = (255,10,10)
	colorPQ = (10,10,255)
	deltaColor = 90

	e.addEdge ( (+5,+5,+5), (+5,+5,-5), colorCube )
	e.addEdge ( (+5,+5,+5), (+5,-5,+5), colorCube )
	e.addEdge ( (+5,-5,-5), (+5,+5,-5), colorCube )
	e.addEdge ( (+5,-5,-5), (+5,-5,+5), colorCube )

	e.addEdge ( (-5,+5,+5), (+5,+5,+5), colorCube )
	e.addEdge ( (-5,+5,-5), (+5,+5,-5), colorCube )
	e.addEdge ( (-5,-5,-5), (+5,-5,-5), colorCube )
	e.addEdge ( (-5,-5,+5), (+5,-5,+5), colorCube )

	e.addEdge ( (-5,+5,+5), (-5,+5,-5), colorCube )
	e.addEdge ( (-5,+5,+5), (-5,-5,+5), colorCube )
	e.addEdge ( (-5,-5,-5), (-5,+5,-5), colorCube )
	e.addEdge ( (-5,-5,-5), (-5,-5,+5), colorCube )

	e.addEdge ( (-3,+5,+5), (-3,+5,+3), colorCube )
	e.addEdge ( (-5,+5,+3), (-3,+5,+3), colorCube )
	e.addEdge ( (-3,-5,+5), (-3,-5,+3), colorCube )
	e.addEdge ( (-5,-5,+3), (-3,-5,+3), colorCube )
	e.addEdge ( (-3,-5,+3), (-3,+5,+3), colorPQ )

	for n in range(-10,+10+1):
		e.addEdge ( (n/2,+5,-5), (n/2,-5,+5), colorD1 )
		e.addEdge ( (n/2,+5,+5), (n/2,-5,-5), colorD2 )






def addLine ( edges, p0, p1, color, t, duration ):
	if ((len(p0)==3) and (len(p1)==3)):
		div = 10
		dt = duration/(div+1)
		v = vectorAB ( p0, p1, 1/div )
		pp = p0
		for n in range(div):
			pn = pointPlusVector ( pp, v )
			edges.addEdge ( pp, pn, (255,255,255), t, t+dt*2 )
			edges.addEdge ( pp, pn, color, t+dt*2 )
			pp = pn
			t += dt



def addLineProjection ( edges, p0, p1, center, planeP0, planeNormal, color, t, duration ):
	if ((len(p0)==3) and (len(p1)==3)):
		div = 10
		dt = duration/(div+1)
		v = vectorAB ( p0, p1, 1/div )
		pp = p0
		for n in range(div):
			pn = pointPlusVector ( pp, v )
			ok = True
			try:
				ppProj = projectionCenterPointPlane ( center, pp, planeP0, planeNormal  )
				pnProj = projectionCenterPointPlane ( center, pn, planeP0, planeNormal  )
			except ValueError:
				ok = False
			if (ok and (distPoints(ppProj,pnProj) < 20)):
				edges.addEdge ( pp, pn, (255,255,255), t, t+dt*2 )
				edges.addEdge ( pp, pn, color, t+dt*2 )
			pp = pn
			t += dt



def projectionCircleHyperbole(edges):
	t = 0.0;

	colorSq1 = ( 100, 200, 20 )
	colorSq2 = ( 200, 100, 20 )
	colorCenter = ( 0, 0, 150 )
	colorConstruction = ( 70, 70, 70 )

	projCenter = ( -6, 0, 6.5 )
	projCenterBase = ( projCenter[0], projCenter[1], 0 )

	projPlaneP0 = ( 0,0,0 )
	projPlaneNormal = ( 0,0,1 )

	edges.addEdge ( projCenter, projCenterBase, colorCenter )
	edges.addEdge ( projCenterBase, ( 0, 0, 0 ), colorCenter ) 
	edges.addEdge ( (0,20,0), (0,-20,0), colorConstruction )
	edges.addEdge ( (0,-20,0), (30,-20,0), colorConstruction )
	edges.addEdge ( (30,-20,0), (30,20,0), colorConstruction )
	edges.addEdge ( (30,20,0), (0,20,0), colorConstruction )

	pA = ( 0, 5, 0 )
	pB = ( 0, 5, 10 )
	pC = ( 0, -5, 10 )
	pD = ( 0, -5, 0 )

	# edges.addEdge ( pA, pB, colorSq1, t )
	t += 0.25
	edges.addEdge ( pB, pC, colorSq1, t )
	t += 0.25
	edges.addEdge ( pC, pD, colorSq1, t )
	t += 0.25
	edges.addEdge ( pD, pA, colorSq1, t )
	t += round(t)

	semiDiagSq = 5*2**0.5
	pE = ( 0,0,5+semiDiagSq )
	pF = ( 0,0+semiDiagSq,5 )
	pG = ( 0,0,5-semiDiagSq )
	pH = ( 0,0-semiDiagSq,5 )
	edges.addEdge ( pE, pF, colorSq2, t )
	t += 0.25
	edges.addEdge ( pF, pG, colorSq2, t )
	t += 0.25
	edges.addEdge ( pG, pH, colorSq2, t )
	t += 0.25
	edges.addEdge ( pH, pE, colorSq2, t )
	t += round(t)

	pAp = projectionCenterPointPlane ( projCenter, pA, projPlaneP0, projPlaneNormal )
	pBp = projectionCenterPointPlane ( projCenter, pB, projPlaneP0, projPlaneNormal )
	pCp = projectionCenterPointPlane ( projCenter, pC, projPlaneP0, projPlaneNormal )
	pDp = projectionCenterPointPlane ( projCenter, pD, projPlaneP0, projPlaneNormal )
	pEp = projectionCenterPointPlane ( projCenter, pE, projPlaneP0, projPlaneNormal )
	pFp = projectionCenterPointPlane ( projCenter, pF, projPlaneP0, projPlaneNormal )
	pGp = projectionCenterPointPlane ( projCenter, pG, projPlaneP0, projPlaneNormal )
	pHp = projectionCenterPointPlane ( projCenter, pH, projPlaneP0, projPlaneNormal )

	addLine ( edges, projCenter, pB, colorConstruction, t, 1 )
	addLine ( edges, pB, pBp, colorConstruction, t, 1 )

	torig=t
	addLine ( edges, pA, pB, colorSq1, t, 1 )
	addLineProjection ( edges, pA, pB, projCenter, projPlaneP0, projPlaneNormal, colorSq1, torig, 1 )







def chessboard(edges):
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

	for n in range ( squares+1 ):
		edges.addEdge ( ( n*sqSize, 0, 0 ), ( n*sqSize, chessboardSize, 0 ), colorChessboard )
		edges.addEdge ( ( 0, n*sqSize, 0 ), ( chessboardSize, n*sqSize, 0 ), colorChessboard )

	for px in range ( squares ):
		for py in range ( squares ):
			if (((px+py) % 2)==0):
				x = px*sqSize
				y = py*sqSize
				for n in range ( 1,10 ):
					edges.addEdge ( ( x+(n/10*sqSize), y, 0 ), ( x+(n/10*sqSize), y+sqSize, 0 ), colorBlackSquares )

	edges.addEdge ( (-chessboardSize*0.1,0,0), (chessboardSize*1.1,0,0), colorFrame )
	edges.addEdge ( (-chessboardSize*0.1,0,chessboardSize), (chessboardSize*1.1,0,chessboardSize), colorFrame )
	edges.addEdge ( (-chessboardSize*0.1,0,0), (-chessboardSize*0.1,0,chessboardSize), colorFrame )
	edges.addEdge ( (chessboardSize*1.1,0,0), (chessboardSize*1.1,0,chessboardSize), colorFrame )

	edges.addEdge ( obs, baseobs, colorFrame )
	edges.addEdge ( baseobs, (obs[0],0,0), colorFrame )

	corner = (0,squares*sqSize,0)

	edges.addEdge ( obs, corner, colorRays )
	edges.addEdge ( baseobs, corner, colorRays )

	projCorner = pointPlusVector (
		obs,
		vectorAB ( obs, corner ),
		(0-obs[1])/(corner[1]-obs[1])
	)
	baseprojCorner = ( projCorner[0],projCorner[1],0 )

	edges.addEdge ( projCorner, baseprojCorner, colorRays )

	edges.addEdge ( projCorner, (0,0,0), colorProjectedChessboard )

	for n in range ( 1, squares+1 ):
		edges.addEdge ( obs, ( 0,n*sqSize,0 ), colorRays )



print ( "" )
print ( "1 chessboard" )
print ( "2 projectionCircleHyperbole" )
print ( "3 Ex20_6c" )
print ( "4 test_20200205_gp_ex_2" )
print ( "" )
choice = input ( "choice? " )

edges = perspectivesolids.Edges()

if (choice=="1"): chessboard(edges)
elif (choice=="2"): projectionCircleHyperbole(edges)
elif (choice=="3"): createEx20_6c(edges)
elif (choice=="4"): test_20200205_gp_ex_2(edges)
else:
	print ( "" )
	print ( "wrong choice..." )
	exit()

perspective.display ( edges )

edge = Edges()

