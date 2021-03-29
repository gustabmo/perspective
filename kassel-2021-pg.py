## guexel@gmail.com 
## https://github.com/gustabmo/perspective
## needs PYGAME https://www.pygame.org/

import solids
import perspective
from vectorfunctions import *


edgelist = []

center = (0,0,0)
base=orthogonalBase((0,0,2),(0,2,0))
solids.cubeoctahedron ( edgelist, center, base[2], base[1], (120,190,70) )

A = pointPlusVector ( center, base[1] )
B = pointPlusVector ( center, base[2] )
vecAB = vectorAB ( A, B )
P0 = midPoint ( A, B )

AtoBsteps=50
AtoBtime=15

for i in range(0,AtoBsteps):
	MP = pointPlusVector ( A, vecAB, i/AtoBsteps )
	solids.cross3D ( edgelist, MP, 0.05, (255,255,255), 1+i/AtoBsteps*AtoBtime, 1+(i+1)/AtoBsteps*AtoBtime )
	PN = vectorAB ( MP, center )
	solids.drawPlan ( edgelist, P0, PN, 3, (0,100,180), 1+i/AtoBsteps*AtoBtime, 1+(i+1)/AtoBsteps*AtoBtime )


perspective.display ( edgelist )