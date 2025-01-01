## guexel@gmail.com 
## https://github.com/gustabmo/perspective

if __name__ == '__main__':
    print ( "this is a library used by other modules" )


from vectorfunctions import *


class Edges:

	def __init__(self):
		self.edges = []
		self.setDefaultTimeEternal()
		self.setDefaultColor ( (255,255,255), 1 );


	def setDefaultTime ( self, newT0, newT1 ):
		if newT0!=None:
			self.defaultT0 = newT0
		if newT1!=None:
			self.defaultT1 = newT1


	def setDefaultTimeEternal ( self ):
		self.setDefaultTime ( -1, 1e10 )


	def setDefaultColor ( self, color, width=None ):
		if (color!=None):
			self.defaultColor = color
		if (width!=None):
			self.defaultWidth = width


	def setDefaultWidth ( self, width ):
		if (width!=None):
			self.defaultWidth = width


	def setDefaultColorAndTime ( self, color, newT0, newT1, width=None ):
		self.setDefaultColor(color,width)
		self.setDefaultTime(newT0, newT1)


	def numEdges ( self ):
		return len ( self.edges )
		

	def maxDistance ( self, center, atLeast=0 ):
		maxD = atLeast
		for e in self.edges:
			maxD = max ( maxD, pointsDistance(center,e[0]), pointsDistance(center,e[1]) )
		return maxD


	def edge ( self, P0, P1, color=None, T0=None, T1=None, width=None ):
		self.addEdge ( P0, P1, color, T0, T1, width )


	def addEdge ( self, P0, P1, color=None, T0=None, T1=None, width=None ):
		if (color==None): color = self.defaultColor
		if (width==None): width = self.defaultWidth
		if (T0==None): T0 = self.defaultT0
		if (T1==None): T1 = self.defaultT1
		self.edges.append ( ( P0, P1, color, T0, T1, width ) )


	def parallelogramFromCenter ( self, center, base0, base1, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		A = pointPlus2Vectors ( center, base0, base1, -1, -1 )
		B = pointPlus2Vectors ( center, base0, base1, -1, +1 )
		C = pointPlus2Vectors ( center, base0, base1, +1, +1 )
		D = pointPlus2Vectors ( center, base0, base1, +1, -1 )

		self.addEdge ( A, B )
		self.addEdge ( B, C )
		self.addEdge ( C, D )
		self.addEdge ( D, A )


	def parallelogramFromCorner ( self, corner, base0, base1, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		A = corner
		B = pointPlusVector ( corner, base0 )
		C = pointPlus2Vectors ( corner, base0, base1 )
		D = pointPlusVector ( corner, base1 )

		self.addEdge ( A, B )
		self.addEdge ( B, C )
		self.addEdge ( C, D )
		self.addEdge ( D, A )


	def cuboidFromCorner ( self, 
		corner, base0, base1, base2, 
		color=None, T0=None, T1=None, width=None,
		drawCuboid=True,
		drawProjection=False,drawCenterToPoint=False,
		projectionCenterAndPlane=None,
		drawProjectionSupportLines=False,supportProjectionPlane=None,
		colorDrawBase0=None,
		colorDrawBase1=None,
		colorDrawBase2=None,
		colorDrawExtensionBase0=None,
		colorDrawExtensionBase1=None,
		colorDrawExtensionBase2=None,
	) :
		halfBase0 = vectorTimesFactor ( base0, 0.5 )
		halfBase1 = vectorTimesFactor ( base1, 0.5 )
		halfBase2 = vectorTimesFactor ( base2, 0.5 )
		center = pointPlusVector ( pointPlusVector ( pointPlusVector ( corner, halfBase0, 1), halfBase1, 1), halfBase2, 1 )
		self.cuboid ( 
			center, halfBase0, halfBase1, halfBase2,
			color, T0, T1, width,
			drawCuboid, 
			drawProjection,drawCenterToPoint, 
			projectionCenterAndPlane,
			drawProjectionSupportLines,supportProjectionPlane,
			colorDrawBase0,
			colorDrawBase1,
			colorDrawBase2,
			colorDrawExtensionBase0,
			colorDrawExtensionBase1,
			colorDrawExtensionBase2
		)


	def cuboid ( self, 
		center, base0, base1, base2, 
		color=None, T0=None, T1=None, width=None,
		drawCuboid=True,
		drawProjection=False,drawCenterToPoint=False,
		projectionCenterAndPlane=None,
		drawProjectionSupportLines=False,supportProjectionPlane=None,
		colorDrawBase0=None,
		colorDrawBase1=None,
		colorDrawBase2=None,
		colorDrawExtensionBase0=None,
		colorDrawExtensionBase1=None,
		colorDrawExtensionBase2=None,
		lengthExtension=3
	) :

		def addEdgeExtended ( A, B, color ):
			self.addEdge ( 
				pointPlusVector ( A, normalizeVector(vectorAB(A,B)), -lengthExtension ), 
				pointPlusVector ( B, normalizeVector(vectorAB(A,B)), +lengthExtension ), 
				color 
			)

		self.setDefaultColorAndTime(color, T0, T1, width)

		A = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, +1 )
		B = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, -1 )
		C = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, -1 )
		D = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, +1 )
		E = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, +1 )
		F = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, -1 )
		G = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, -1 )
		H = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, +1 )

		if drawProjection or drawProjectionSupportLines or drawCenterToPoint:
			Ap = projectionCenterPointPlane ( projectionCenterAndPlane[0], A, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Bp = projectionCenterPointPlane ( projectionCenterAndPlane[0], B, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Cp = projectionCenterPointPlane ( projectionCenterAndPlane[0], C, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Dp = projectionCenterPointPlane ( projectionCenterAndPlane[0], D, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Ep = projectionCenterPointPlane ( projectionCenterAndPlane[0], E, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Fp = projectionCenterPointPlane ( projectionCenterAndPlane[0], F, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Gp = projectionCenterPointPlane ( projectionCenterAndPlane[0], G, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )
			Hp = projectionCenterPointPlane ( projectionCenterAndPlane[0], H, projectionCenterAndPlane[1], projectionCenterAndPlane[2] )

		if drawCenterToPoint:
			longest = getLongestEdge ( projectionCenterAndPlane[0], A, Ap )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], B, Bp )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], C, Cp )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], D, Dp )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], E, Ep )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], F, Fp )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], G, Gp )
			self.addEdge ( longest[0], longest[1] )
			longest = getLongestEdge ( projectionCenterAndPlane[0], H, Hp )
			self.addEdge ( longest[0], longest[1] )

		if (colorDrawExtensionBase0 != None):
			addEdgeExtended ( Ap, Ep, colorDrawExtensionBase0 )
			addEdgeExtended ( Bp, Fp, colorDrawExtensionBase0 )
			addEdgeExtended ( Cp, Gp, colorDrawExtensionBase0 )
			addEdgeExtended ( Dp, Hp, colorDrawExtensionBase0 )

		if (colorDrawExtensionBase1 != None):
			addEdgeExtended ( Bp, Cp, colorDrawExtensionBase1 )
			addEdgeExtended ( Dp, Ap, colorDrawExtensionBase1 )
			addEdgeExtended ( Fp, Gp, colorDrawExtensionBase1 )
			addEdgeExtended ( Hp, Ep, colorDrawExtensionBase1 )

		if (colorDrawExtensionBase2 != None):
			addEdgeExtended ( Ap, Bp, colorDrawExtensionBase2 )
			addEdgeExtended ( Cp, Dp, colorDrawExtensionBase2 )
			addEdgeExtended ( Ep, Fp, colorDrawExtensionBase2 )
			addEdgeExtended ( Gp, Hp, colorDrawExtensionBase2 )

		if drawProjection:
			self.addEdge ( Ap, Bp, colorDrawBase2 )
			self.addEdge ( Bp, Cp, colorDrawBase1 )
			self.addEdge ( Cp, Dp, colorDrawBase2 )
			self.addEdge ( Dp, Ap, colorDrawBase1 )
			self.addEdge ( Ap, Ep, colorDrawBase0 )
			self.addEdge ( Bp, Fp, colorDrawBase0 )
			self.addEdge ( Cp, Gp, colorDrawBase0 )
			self.addEdge ( Dp, Hp, colorDrawBase0 )
			self.addEdge ( Ep, Fp, colorDrawBase2 )
			self.addEdge ( Fp, Gp, colorDrawBase1 )
			self.addEdge ( Gp, Hp, colorDrawBase2 )
			self.addEdge ( Hp, Ep, colorDrawBase1 )

		if drawCuboid:
			self.addEdge ( A, B, colorDrawBase2 )
			self.addEdge ( B, C, colorDrawBase1 )
			self.addEdge ( C, D, colorDrawBase2 )
			self.addEdge ( D, A, colorDrawBase1 )
			self.addEdge ( A, E, colorDrawBase0 )
			self.addEdge ( B, F, colorDrawBase0 )
			self.addEdge ( C, G, colorDrawBase0 )
			self.addEdge ( D, H, colorDrawBase0 )
			self.addEdge ( E, F, colorDrawBase2 )
			self.addEdge ( F, G, colorDrawBase1 )
			self.addEdge ( G, H, colorDrawBase2 )
			self.addEdge ( H, E, colorDrawBase1 )

		if drawProjectionSupportLines:
			pass

	# end cuboid



	def cube ( self, center, up, right, color=None, T0=None, T1=None, width=None ):
		base = orthogonalBase ( up, right )
		self.cuboid ( center, base[0], base[1], base[2], color, T0, T1, width )


	def octahedron ( self, center, base0, base1, base2, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		A = pointPlusVector ( center, base0 )	
		B = pointPlusVector ( center, base0, -1 )	
		C = pointPlusVector ( center, base1 )	
		D = pointPlusVector ( center, base2 )	
		E = pointPlusVector ( center, base1, -1 )	
		F = pointPlusVector ( center, base2, -1 )	

		self.addEdge ( A, C )
		self.addEdge ( A, D )
		self.addEdge ( A, E )
		self.addEdge ( A, F )
		self.addEdge ( C, D )
		self.addEdge ( D, E )
		self.addEdge ( E, F )
		self.addEdge ( F, C )
		self.addEdge ( B, C )
		self.addEdge ( B, D )
		self.addEdge ( B, E )
		self.addEdge ( B, F )


	def regularOctahedron ( self, center, up, right, color=None, T0=None, T1=None, width=None ) :
		base = orthogonalBase ( up, right )
		self.octahedron ( edges, center, base[0], base[1], base[2], color, T0, T1, width )


	def cubeOctahedron ( self, center, up, right, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)
		base2 = orthogonalBase ( up, right )
		base1 = [
			vectorTimesFactor ( base2[0], 0.5 ),
			vectorTimesFactor ( base2[1], 0.5 ),
			vectorTimesFactor ( base2[2], 0.5 )
		]
		self.cuboid ( center, base1[0], base1[1], base1[2] )
		self.octahedron ( center, base2[0], base2[1], base2[2] )

		colordim = [ self.defaultColor[0]*0.7, self.defaultColor[1]*0.7, self.defaultColor[2]*0.7 ]

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

			self.addEdge ( P, Q, colordim )
			self.addEdge ( Q, R, colordim )
			self.addEdge ( R, S, colordim )
			self.addEdge ( S, P, colordim )

		losangeInFace ( 0, +1 )
		losangeInFace ( 0, -1 )
		losangeInFace ( 1, +1 )
		losangeInFace ( 1, -1 )
		losangeInFace ( 2, +1 )
		losangeInFace ( 2, -1 )


	def cross3D ( self, P, len, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)
		self.addEdge ( pointPlusVector ( P, (-len,0,0) ), pointPlusVector ( P, (+len,0,0) ) )
		self.addEdge ( pointPlusVector ( P, (0,-len,0) ), pointPlusVector ( P, (0,+len,0) ) )
		self.addEdge ( pointPlusVector ( P, (0,0,-len) ), pointPlusVector ( P, (0,0,+len) ) )


	def plane ( self, P0, PN, radius, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		V1 = crossProduct ( PN, P0 )
		if lengthVector(V1)==0: V1 = crossProduct ( PN, (0,0,1) )
		if lengthVector(V1)==0: V1 = crossProduct ( PN, (0,1,0) )
		if lengthVector(V1)==0: V1 = crossProduct ( PN, (1,0,0) )
		V1 = normalizeVector(V1)
		V2 = normalizeVector(crossProduct(PN,V1))
		for n in range(-10,+10):
			D1 = pointPlusVector ( P0, V1, n/10.5*radius )
			w = (1-(n/10.5)**2)**0.5
			self.addEdge ( pointPlusVector(D1,V2,+w*radius), pointPlusVector(D1,V2,-w*radius) )


	def lettresXYZ ( self, pos, size, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		# lettre X
		self.addEdge ( (pos+size/2,0,0), (pos+size/2+size,size,0) )
		self.addEdge ( (pos+size/2,size,0), (pos+size/2+size,0,0) )

		# lettre Y
		self.addEdge ( (0,pos+size/2,0), (0,pos+size/2+size/2,0) )
		self.addEdge ( (0,pos+size/2+size/2,0), (size/2,pos+size/2+size,0) )
		self.addEdge ( (0,pos+size/2+size/2,0), (-size/2,pos+size/2+size,0) )

		# lettre Z
		self.addEdge ( (0,0,pos+size/2), (0,0,pos+size/2+size) )
		self.addEdge ( (0,size,pos+size/2), (0,0,pos+size/2+size) )
		self.addEdge ( (0,size,pos+size/2+size), (0,size,pos+size/2) )


	def polygon ( self, poly, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)
		first = None
		last = None
		for p in poly:
			if (first==None): 
				first = p
			if (last!=None):
				self.addEdge ( last, p )
			last = p
		if (last != None):
			self.addEdge ( last, first )

	def write ( self, p0, up, right, text, color=None, T0=None, T1=None, width=None ):
		self.setDefaultColorAndTime(color, T0, T1, width)
		for c in text:
			if (c=="0"):
				self.polygon (
					(
						pointPlus2Vectors(p0,up,right,0,0.2),
						pointPlus2Vectors(p0,up,right,0,0.8),
						pointPlus2Vectors(p0,up,right,0.2,1),
						pointPlus2Vectors(p0,up,right,0.8,1),
						pointPlus2Vectors(p0,up,right,1,0.8),
						pointPlus2Vectors(p0,up,right,1,0.2),
						pointPlus2Vectors(p0,up,right,0.8,0),
						pointPlus2Vectors(p0,up,right,0.2,0),
						pointPlus2Vectors(p0,up,right,0,0.2)
					),
					color,T0,T1 
				)
				p0 = pointPlusVector ( p0, right, 1.1 )
			elif (c=="-"):
				self.addEdge ( pointPlusVector(p0,up,0.5), pointPlus2Vectors(p0,up,right,0.5,0.8), color,T0,T1 )
				p0 = pointPlusVector ( p0, right, 1 )
			elif (c=="+"):
				self.addEdge ( pointPlusVector(p0,up,0.5), pointPlus2Vectors(p0,up,right,0.5,0.8), color,T0,T1 )
				self.addEdge ( pointPlus2Vectors(p0,up,right,0.1,0.3), pointPlus2Vectors(p0,up,right,0.9,0.3), color,T0,T1 )
				p0 = pointPlusVector ( p0, right, 1 )
			elif (c=="1"):
				self.addEdge ( pointPlusVector(p0,up,0), pointPlus2Vectors(p0,up,right,0,0.8), color,T0,T1 )
				self.addEdge ( pointPlus2Vectors(p0,up,right,0,0.4), pointPlus2Vectors(p0,up,right,1,0.4), color,T0,T1 )
				self.addEdge ( pointPlus2Vectors(p0,up,right,1,0.4), pointPlus2Vectors(p0,up,right,0.4,0.15), color,T0,T1 )
				p0 = pointPlusVector ( p0, right, 1 )


