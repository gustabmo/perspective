## guexel@gmail.com 
## https://github.com/gustabmo/perspective


# vector from point A to point B
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


## distance between points
def distPoints ( A,B ):
	return ((B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2) ** 0.5


def midPoint ( A,B ):
	return pointPlusVector ( A, vectorAB ( A, B, 0.5 ) )


def dotProduct ( V1,V2 ):
	return (V1[0]*V2[0] + V1[1]*V2[1] + V1[2]*V2[2])


## vectorial product, or cross product
def vecProduct ( V1,V2 ):
	return (
		V1[1]*V2[2] - V1[2]*V2[1],
		V1[2]*V2[0] - V1[0]*V2[2],
		V1[0]*V2[1] - V1[1]*V2[0],
	)


def v2st ( V ):
	return "(%.2f,%.2f,%.2f)" % V


def intersectLinePlane ( lineP0, lineVect, planeP0, planeNormal ):
	d = dotProduct ( vectorAB ( lineP0, planeP0 ), planeNormal ) / dotProduct ( lineVect, planeNormal )
	return pointPlusVector ( lineP0, lineVect, d )


def projectionCenterPointPlane ( center, point, planeP0, planeNormal ):
	return intersectLinePlane ( center, vectorAB ( center, point ), planeP0, planeNormal )


# returns the usual X,Y,Z (X towrds us = front, Y right, Z up)
def orthogonalBase ( up, right ):
	# takes the length of the up vector as half the side of the cube, ignores the length of the parameter right
	result = []
	lengthUp = lengthVector ( up )
	front = vecProduct ( right, up )
	if (lengthVector(front) > 0):
		rightPerp = vecProduct ( up, front ) # recalculates, just in case right was not perpendicular to up...
		rightWithUpLen = vectorTimesFactor ( rightPerp, lengthUp/lengthVector(rightPerp) )
		frontWithUpLen = vectorTimesFactor ( front, lengthUp/lengthVector(front) )
		result.append ( frontWithUpLen )
		result.append ( rightWithUpLen )
		result.append ( up )
	else:
		# returns a default orthogonal base
		result.append ( (1,0,0) )
		result.append ( (0,1,0) )
		result.append ( (0,0,1) )
	return result
