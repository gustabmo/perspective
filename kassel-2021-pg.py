## guexel@gmail.com 
## https://github.com/gustabmo/perspective
## needs PYGAME https://www.pygame.org/

import perspectivesolids
import perspective
from vectorfunctions import *


edges = perspectivesolids.Edges()

center = (0,0,0)
base = orthogonalBase((0,0,2),(0,2,0))
edges.cubeOctahedron ( center, base[2], base[1], (120,190,70) )

A = pointPlusVector ( center, base[1] )
B = pointPlusVector ( center, base[2] )
vecAB = vectorAB ( A, B )
P0 = midPoint ( A, B )

AtoBsteps=50
AtoBtime=15

for i in range(0,AtoBsteps*5):
	MP = pointPlusVector ( A, vecAB, i/AtoBsteps )
	edges.cross3D ( MP, 0.05, (255,255,255), 1+i/AtoBsteps*AtoBtime, 1+(i+1)/AtoBsteps*AtoBtime )
	PN = vectorAB ( MP, center )
	edges.plane ( P0, PN, 3, (0,100,180), 1+i/AtoBsteps*AtoBtime, 1+(i+1)/AtoBsteps*AtoBtime )


perspective.display ( edges )