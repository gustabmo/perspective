## guexel@gmail.com 
## https://github.com/gustabmo/perspective
## needs PYGAME https://www.pygame.org/

import math
import random
import perspectivesolids
import perspective
from vectorfunctions import *


edges = perspectivesolids.Edges()

center = (0,0,0)
base1 = (0,1,0)
base2 = (0,0,1)
baseN = crossProduct ( base1, base2 )
edges.parallelogramFromCenter ( center, base1, base2 )

projcenter = pointPlusVector ( center, baseN, -0.5 )
edges.addEdge ( pointPlusVector ( projcenter, base2, -1 ), pointPlusVector ( center, base2, -1 ), (100,100,100) )
edges.addEdge ( pointPlusVector ( projcenter, base2, -1 ), projcenter, (100,100,100) )
edges.cross3D ( projcenter, 0.03 )

colors = ( (255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255) )

for numVanP in range(3):
	r1 = random.random()
	r2 = random.random()
	tr = 5
	t0 = 2+numVanP*tr
	vanishingP = pointPlus2Vectors ( center, base1, base2, r1*2-1, r2*2-1 )
	edges.setDefaultColorAndTime ( colors[numVanP], t0, 99999 )

	edges.cross3D ( vanishingP, 0.03)

	linebase = normalizeVector ( vectorAB ( projcenter, vanishingP ) )
	edges.addEdge ( pointPlusVector(vanishingP,linebase,-2), pointPlusVector(vanishingP,linebase,+3), None, t0+tr*0.3 )

	numD = 3
	for d in range(numD):
		newP = pointPlus2Vectors ( center, base1, base2, random.random()*2-1, random.random()*2-1 )
		td = t0+tr*0.6+0.3*d/numD
		edges.addEdge ( pointPlusVector(newP,linebase,-3), pointPlusVector(newP,linebase,+3), None, td )
		projLineBase = normalizeVector ( vectorAB ( vanishingP, newP ) )
		centerProjLine = pointPlusVector ( vanishingP, vectorAB(vanishingP,newP), 0.5 )
		edges.addEdge ( 
			pointPlusVector(centerProjLine,projLineBase,-2), 
			pointPlusVector(centerProjLine,projLineBase,+2), 
			(colors[numVanP][0]*0.6,colors[numVanP][1]*0.6,colors[numVanP][2]*0.6),
			td+0.01,td+tr*1.2 
		)



perspective.display ( edges )