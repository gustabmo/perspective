## guexel@gmail.com 
## https://github.com/gustabmo/perspective

from vectorfunctions import *


def parallelepiped ( edges, center, base0, base1, base2, color, time0=-1, time1=1e10 ) :
	A = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, +1 )
	B = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, -1 )
	C = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, -1 )
	D = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, +1 )
	E = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, +1 )
	F = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, -1 )
	G = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, -1 )
	H = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, +1 )

	edges.append ( ( A, B, color, time0, time1 ) ) 
	edges.append ( ( B, C, color, time0, time1 ) ) 
	edges.append ( ( C, D, color, time0, time1 ) ) 
	edges.append ( ( D, A, color, time0, time1 ) ) 
	edges.append ( ( A, E, color, time0, time1 ) ) 
	edges.append ( ( B, F, color, time0, time1 ) ) 
	edges.append ( ( C, G, color, time0, time1 ) ) 
	edges.append ( ( D, H, color, time0, time1 ) ) 
	edges.append ( ( E, F, color, time0, time1 ) ) 
	edges.append ( ( F, G, color, time0, time1 ) ) 
	edges.append ( ( G, H, color, time0, time1 ) ) 
	edges.append ( ( H, E, color, time0, time1 ) ) 



def cube ( edges, center, up, right, color, time0=-1, time1=1e10 ) :
	base = orthogonalBase ( up, right )
	parallelepiped ( edges, center, base[0], base[1], base[2], color, time0, time1 )


def octahedron ( edges, center, base0, base1, base2, color, time0=-1, time1=1e10 ) :
	A = pointPlusVector ( center, base0 )	
	B = pointPlusVector ( center, base0, -1 )	
	C = pointPlusVector ( center, base1 )	
	D = pointPlusVector ( center, base2 )	
	E = pointPlusVector ( center, base1, -1 )	
	F = pointPlusVector ( center, base2, -1 )	

	edges.append ( ( A, C, color, time0, time1 ) )
	edges.append ( ( A, D, color, time0, time1 ) )
	edges.append ( ( A, E, color, time0, time1 ) )
	edges.append ( ( A, F, color, time0, time1 ) )
	edges.append ( ( C, D, color, time0, time1 ) )
	edges.append ( ( D, E, color, time0, time1 ) )
	edges.append ( ( E, F, color, time0, time1 ) )
	edges.append ( ( F, C, color, time0, time1 ) )
	edges.append ( ( B, C, color, time0, time1 ) )
	edges.append ( ( B, D, color, time0, time1 ) )
	edges.append ( ( B, E, color, time0, time1 ) )
	edges.append ( ( B, F, color, time0, time1 ) )


def regularoctahedron ( edges, center, up, right, color, time0=-1, time1=1e10 ) :
	base = orthogonalBase ( up, right )
	octahedron ( edges, center, base[0], base[1], base[2], color, time0, time1 )



def cubeoctahedron ( edges, center, up, right, color, time0=-1, time1=1e10 ) :
	base2 = orthogonalBase ( up, right )
	base1 = []
	base1.append ( vectorTimesFactor ( base2[0], 0.5 ) )
	base1.append ( vectorTimesFactor ( base2[1], 0.5 ) )
	base1.append ( vectorTimesFactor ( base2[2], 0.5 ) )
	parallelepiped ( edges, center, base1[0], base1[1], base1[2], color, time0, time1 )
	octahedron ( edges, center, base2[0], base2[1], base2[2], color, time0, time1 )

	colordim = [ color[0]*0.7, color[1]*0.7, color[2]*0.7 ]

	def losangeInFace ( ndx, factor ):
		ndxA = 0
		if ndxA==ndx:
			ndxA+=1
		ndxB = ndxA+1
		if ndxB==ndx:
			ndxB+=1
		P = pointPlusVector ( pointPlusVector ( center, base1[ndx], factor ), base1[ndxA], -1 )
		Q = pointPlusVector ( pointPlusVector ( center, base1[ndx], factor ), base1[ndxB], -1 )
		R = pointPlusVector ( pointPlusVector ( center, base1[ndx], factor ), base1[ndxA], +1 )
		S = pointPlusVector ( pointPlusVector ( center, base1[ndx], factor ), base1[ndxB], +1 )

		edges.append ( ( P, Q, colordim, time0, time1 ) )
		edges.append ( ( Q, R, colordim, time0, time1 ) )
		edges.append ( ( R, S, colordim, time0, time1 ) )
		edges.append ( ( S, P, colordim, time0, time1 ) )

	losangeInFace ( 0, +1 )
	losangeInFace ( 0, -1 )
	losangeInFace ( 1, +1 )
	losangeInFace ( 1, -1 )
	losangeInFace ( 2, +1 )
	losangeInFace ( 2, -1 )



def cross3D ( edges, P, len, color, time0=-1, time1=1e10 ):
	edges.append ( ( pointPlusVector ( P, (-len,0,0) ), pointPlusVector ( P, (+len,0,0) ), color, time0, time1 ) )
	edges.append ( ( pointPlusVector ( P, (0,-len,0) ), pointPlusVector ( P, (0,+len,0) ), color, time0, time1 ) )
	edges.append ( ( pointPlusVector ( P, (0,0,-len) ), pointPlusVector ( P, (0,0,+len) ), color, time0, time1 ) )


def drawPlan ( edges, P0, PN, radius, color, time0=-1, time1=1e10 ):
	V1 = vecProduct ( PN, P0 )
	if lengthVector(V1)==0: V1 = vecProduct ( PN, (0,0,1) )
	if lengthVector(V1)==0: V1 = vecProduct ( PN, (0,1,0) )
	if lengthVector(V1)==0: V1 = vecProduct ( PN, (1,0,0) )
	V1 = normalizeVector(V1)
	V2 = normalizeVector(vecProduct(PN,V1))
	for n in range(-10,+10):
		D1 = pointPlusVector ( P0, V1, n/10.5*radius )
		w = (1-(n/10.5)**2)**0.5
		edges.append ( ( pointPlusVector(D1,V2,+w*radius), pointPlusVector(D1,V2,-w*radius), color, time0, time1 ) )























