import math

import perspectivesolids
import perspective
from vectorfunctions import *


centreDeProjection = (-0.3,-1.7,0.2)
centreDeProjection = (1.3,-0.7,1.6)

edges = perspectivesolids.Edges()
t0 = 0
maxAngle = 14

# les plans vertical et horizontal
edges.parallelogramFromCorner ( (-0.4,0,0), (2.2,0,0), (0,0,2), (0,80,0) )
edges.parallelogramFromCorner ( (-0.4,0,0), (2.2,0,0), (0,2.5,0), (0,80,0) )
edges.edge ( (0,0,0), (0,3,0), (0,80,0) )
edges.edge ( (1.5,0,0), (1.5,3,0), (0,80,0) )

# la position du centre de projection
edges.edge ( centreDeProjection, (centreDeProjection[0],centreDeProjection[1],0), (0,80,0) )
edges.edge ( (centreDeProjection[0],centreDeProjection[1],0), (centreDeProjection[0],0,0), (0,80,0) )
edges.cross3D ( centreDeProjection, 0.02, (40,120,40))



def Desenha ( angle, t0, t1, comLinhaAoCentro, comExtensao, cuboFraquinho ):
	angleRad = angle/180*math.pi

	cornerCubo = (0,1.2,0)
	baseCubo0 = (1.5,0,0)
	baseCubo1 = (0,math.cos(angleRad),math.sin(angleRad))
	baseCubo2 = (0,1.1*math.cos(angleRad+math.pi/2),1.1*math.sin(angleRad+math.pi/2))

	extc0 = None
	extc1 = None
	extc2 = None
	if comExtensao:
		extc0=(2,80,90)
		extc1=(4,90,24)
		extc2=(76,87,3)

	corCubo0 = (5,238,250)
	corCubo1 = (9,247,62)
	corCubo2 = (218,248,7)
	if cuboFraquinho:
		corCubo0 = (1,45,49)
		corCubo1 = (2,49,10)
		corCubo2 = (40,49,2)

	edges.cuboidFromCorner ( 
		cornerCubo, baseCubo0, baseCubo1, baseCubo2,
		(255,255,0), t0,t1, 3,
		True,
		False,False,None,False,None,
		corCubo0,corCubo1,corCubo2
	)
	edges.cuboidFromCorner ( 
		cornerCubo, baseCubo0, baseCubo1, baseCubo2,
		(255,120,50), t0,t1, 2,
		False,
		True, False,
		( centreDeProjection, (0,0,0), (0,1,0) ),
		False,None,
		(4,166,175),(7,173,43),(152,173,5),
		extc0,extc1,extc2
	)
	if comLinhaAoCentro:
		edges.cuboidFromCorner ( 
			cornerCubo, baseCubo0, baseCubo1, baseCubo2,
			(80,80,50), t0,t1, 1,
			False,
			False, True, 
			( centreDeProjection, (0,0,0), (0,1,0) ),
		)



t1=t0+3
Desenha ( maxAngle, t0, t1, True, False, False )
t0=t1

t1=t0+2
Desenha ( maxAngle, t0, t1, False, False, True )
t0=t1

for angleVezes3 in range(maxAngle*3,-80,-1):
	angle = angleVezes3/3

	if (angle==0):
		t1 = t0+3
	elif (angle==maxAngle):
		t1 = t0+3
	else:
		t1 = t0+0.1

	Desenha ( angle, t0, t1, False, True, True )

	t0 = t1


perspective.display ( edges, pov=[1,1,1] )
