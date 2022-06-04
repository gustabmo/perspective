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


## cross product, or vectorial product
def crossProduct ( V1,V2 ):
	return (
		V1[1]*V2[2] - V1[2]*V2[1],
		V1[2]*V2[0] - V1[0]*V2[2],
		V1[0]*V2[1] - V1[1]*V2[0],
	)


def v2st ( V ):
	return "(%.2f,%.2f,%.2f)" % V


def intersectLinePlane ( lineP0, lineVect, planeP0, planeNormal ):
	dplvpn = dotProduct ( lineVect, planeNormal )
	if dplvpn==0:
		return None
	else:
		lamb = dotProduct ( vectorAB ( lineP0, planeP0 ), planeNormal ) / dplvpn
		return pointPlusVector ( lineP0, lineVect, lamb )


def intersectSegmentPlane ( lineP0, lineVect, planeP0, planeNormal ):
	dplvpn = dotProduct ( lineVect, planeNormal )
	if dplvpn==0:
		return None
	else:
		lamb = dotProduct ( vectorAB ( lineP0, planeP0 ), planeNormal ) / dplvpn
		if (lamb < 0) or (lamb > 1):
			return None
		else:
			return pointPlusVector ( lineP0, lineVect, lamb )



def projectionCenterPointPlane ( center, point, planeP0, planeNormal ):
	return intersectLinePlane ( center, vectorAB ( center, point ), planeP0, planeNormal )



# returns the usual X,Y,Z (X towrds us = front, Y right, Z up)
def orthogonalBase ( up, right ):
	# takes the length of the up vector as half the side of the cube, ignores the length of the parameter right
	result = []
	lengthUp = lengthVector ( up )
	front = crossProduct ( right, up )
	if (lengthVector(front) > 0):
		rightPerp = crossProduct ( up, front ) # recalculates right, just in case it was not perpendicular to up...
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


class _intersectPlaneCuboid:
	# HE = half edge, a vector that represents one half of one edge, 0,1,2 for each of the 3 axes
	def __init__( self, planeP0, planeNormal, cubeC, cubeHE0, cubeHE1, cubeHE2 ):
		self.planeP0 = planeP0
		self.planeNormal = planeNormal
		self.cubeC = cubeC
		self.arrCubeHE = ( cubeHE0, cubeHE1, cubeHE2 )
		self.iedgesB0 = [[[None for x in range(3)] for y in range(3)] for z in range(3)] # array 3*3*3
		self.searchIntersectionsWithEdges()
		self.buildPolygon()

	def setiEdge ( self, x,y,z,what,rotateAxis=0 ):
		if rotateAxis==0:
			self.iedgesB0[x+1,y+1,z+1] = what
		elif rotateAxis==1:
			self.iedgesB0[z+1,x+1,y+1] = what
		elif rotateAxis==2:
			self.iedgesB0[y+1,z+1,x+1] = what
		else:
			raise

	def getiEdge ( self, x,y,z,rotateAxis=0 ):
		if rotateAxis==0:
			return self.iedgesB0[x+1,y+1,z+1]
		elif rotateAxis==1:
			return self.iedgesB0[z+1,x+1,y+1]
		elif rotateAxis==2:
			return self.iedgesB0[y+1,z+1,x+1]
		else:
			raise

	def cubeHE ( self, axis, rotateAxis=0 ):
		return self.arrCubeHE[(axis+rotateAxis) % 3]

	def findOneEdgeIntersection(self):
		for x in range(-1,2):
			for y in range(-1,2):
				for z in range(-1,2):
					if (getiEdge(x,y,z) != None):
						return (x,y,z)
		return (None,None,None)

	def populatePolygon ( self, vertex ):
		thisintersection = self.getiEdge ( vertex[0],vertex[1],vertex[2] )
		if (self.polygon==[] or (thisintersection != self.polygon[self.polygon.length-1])):
			self.polygon += thisintersection
		self.used[vertex[0],vertex[1],vertex[2]] = True
		# search another edge intersection in the same face as this one
		for x in range(-1,2,2):
			for y in range(-1,2,2):
				for z in range(-1,2,2):
					if (
						(
							(x!=0 and x==vertex[0]) 
							or 
							(y!=0 and y==vertex[1]) 
							or 
							(z!=0 and z==vertex[2]) 
						)
						and 
						(not used[x,y,z])
						and
						(self.getiEdge(x, y, z) != None)
					):
						self.populatePolygon((x,y,z))
						return

	def buildPolygon ( self ):
		self.polygon = []
		self.used = [[[False for x in range(3)] for y in range(3)] for z in range(3)] # array 3*3*3
		(x,y,z) = findOneEdgeIntersection()
		if (x!=None):
			populatePolygon ( (x,y,z) )

	def searchIntersectionsWithEdges ( self ):
		for rotateAxis in range(3):
			for y in range(-1,2,2):
				for z in range(-1,2,2):
					self.setiEdge ( 
						0,y,z, 
						intersectSegmentPlane (
							pointPlusVector (
								pointPlusVector (
									pointPlusVector ( self.cubeC, self.cubeHE(0,rotateAxis), -1 ),
									self.cubeHE(1,rotateAxis), y
								),
								self.cubeHE(2,rotateAxis), z
							),
							vectorTimesFactor ( self.cubeHE(0,rotateAxis), 2 ), # HE*2 = edge,
							self.planeP0,
							self.planeNormal
						),
						rotateAxis
					)



def intersectPlaneCuboid ( planeP0, planeNormal, cubeC, cubeHE1, cubeHE2, cubeHE3 ):
	return _intersectPlaneCuboid ( planeP0, planeNormal, cubeC, cubeHE1, cubeHE2, cubeHE3 ).polygon





