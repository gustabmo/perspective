def addVector ( e, coords, color ):
	e.append ( ( coords, (0,0,0), color ) )
	e.append ( ( coords, (coords[0]-math.copysign(0.1,coords[0]),coords[1],coords[2]), color ) )
	e.append ( ( coords, (coords[0],coords[1]-math.copysign(0.1,coords[1]),coords[2]), color ) )
	e.append ( ( coords, (coords[0],coords[1],coords[2]-math.copysign(0.1,coords[2])), color ) )



def createEx20_6c ():
	e = perspectivesolides.Edges()

	colorAxes = (100,100,100)
	e.edges.append ( ( (-10,0,0), (10,0,0), colorAxes ) )
	e.edges.append ( ( (0,-10,0), (0,10,0), colorAxes ) )
	e.edges.append ( ( (0,0,-10), (0,0,10), colorAxes ) )

	e.lettresXYZ ( 11, 2, colorAxes )

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

	for n in range(-10,+10+1):
		e.append ( ( (n/2,+5,-5), (n/2,-5,+5), colorD1 ) )
		e.append ( ( (n/2,+5,+5), (n/2,-5,-5), colorD2 ) )

	return e





def addLine ( e, p0, p1, color, t, duration ):
	if ((len(p0)==3) and (len(p1)==3)):
		div = 10
		dt = duration/(div+1)
		v = vectorAB ( p0, p1, 1/div )
		pp = p0
		for n in range(div):
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
		for n in range(div):
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

	for n in range ( squares+1 ):
		e.append ( ( ( n*sqSize, 0, 0 ), ( n*sqSize, chessboardSize, 0 ), colorChessboard ) )
		e.append ( ( ( 0, n*sqSize, 0 ), ( chessboardSize, n*sqSize, 0 ), colorChessboard ) )

	for px in range ( squares ):
		for py in range ( squares ):
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






	# figure = createEtoile()
	# figure = createEx20_6c()
	# figure = test_20200205_gp_ex_2()
	# figure = chessboard()
	# figure = projectionCircleHyperbole()
