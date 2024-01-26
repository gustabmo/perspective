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


	def addEdge ( self, P0, P1, color=None, T0=None, T1=None, width=None ):
		if (color==None): color = self.defaultColor
		if (width==None): width = self.defaultWidth
		if (T0==None): T0 = self.defaultT0
		if (T1==None): T1 = self.defaultT1
		self.edges.append ( ( P0, P1, color, T0, T1, width ) )


	def parallelogram ( self, center, base0, base1, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		A = pointPlus2Vectors ( center, base0, base1, -1, -1 )
		B = pointPlus2Vectors ( center, base0, base1, -1, +1 )
		C = pointPlus2Vectors ( center, base0, base1, +1, +1 )
		D = pointPlus2Vectors ( center, base0, base1, +1, -1 )

		self.addEdge ( A, B )
		self.addEdge ( B, C )
		self.addEdge ( C, D )
		self.addEdge ( D, A )


	def cuboid ( self, 
		center, base0, base1, base2, 
		color=None, T0=None, T1=None, width=None,
		drawCuboid=True,
		drawProjection=False,drawCenterToPoint=False,
		projectionCenter=None,projectionPlane=None,
		drawProjectionSupportLines=False,supportProjectionPlane=None
	) :
		self.setDefaultColorAndTime(color, T0, T1, width)

		A = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, +1 )
		B = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, +1 ), base2, -1 )
		C = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, -1 )
		D = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, +1 ), base1, -1 ), base2, +1 )
		E = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, +1 )
		F = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, +1 ), base2, -1 )
		G = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, -1 )
		H = pointPlusVector ( pointPlusVector ( pointPlusVector ( center, base0, -1 ), base1, -1 ), base2, +1 )

		if drawCuboid:
			self.addEdge ( A, B ) 
			self.addEdge ( B, C )
			self.addEdge ( C, D )
			self.addEdge ( D, A )
			self.addEdge ( A, E )
			self.addEdge ( B, F )
			self.addEdge ( C, G )
			self.addEdge ( D, H )
			self.addEdge ( E, F )
			self.addEdge ( F, G )
			self.addEdge ( G, H )
			self.addEdge ( H, E )

		if drawProjection or drawProjectionSupportLines:
			Ap = projectPointOnPlane ( A, projectionCenter, projectionPlane )
			Bp = projectPointOnPlane ( B, projectionCenter, projectionPlane )
			Cp = projectPointOnPlane ( C, projectionCenter, projectionPlane )
			Dp = projectPointOnPlane ( D, projectionCenter, projectionPlane )
			Ep = projectPointOnPlane ( E, projectionCenter, projectionPlane )
			Fp = projectPointOnPlane ( F, projectionCenter, projectionPlane )
			Gp = projectPointOnPlane ( G, projectionCenter, projectionPlane )
			Hp = projectPointOnPlane ( H, projectionCenter, projectionPlane )

		if drawProjection:
			self.addEdge ( Ap, Bp ) 
			self.addEdge ( Bp, Cp )
			self.addEdge ( Cp, Dp )
			self.addEdge ( Dp, Ap )
			self.addEdge ( Ap, Ep )
			self.addEdge ( Bp, Fp )
			self.addEdge ( Cp, Gp )
			self.addEdge ( Dp, Hp )
			self.addEdge ( Ep, Fp )
			self.addEdge ( Fp, Gp )
			self.addEdge ( Gp, Hp )
			self.addEdge ( Hp, Ep )

		if drawCenterToPoint:
			self.addEdge ( projectionCenter, A )
			self.addEdge ( projectionCenter, B )
			self.addEdge ( projectionCenter, C )
			self.addEdge ( projectionCenter, D )
			self.addEdge ( projectionCenter, E )
			self.addEdge ( projectionCenter, F )
			self.addEdge ( projectionCenter, G )
			self.addEdge ( projectionCenter, H )

		if drawProjectionSupportLines:
			pass

	# end cuboid



	def cube ( self, center, up, right, color=None, T0=None, T1=None ):
		base = orthogonalBase ( up, right )
		self.cuboid ( center, base[0], base[1], base[2], color, T0, T1 )


	def octahedron ( self, center, base0, base1, base2, color=None, T0=None, T1=None, width=None ) :
		self.setDefaultColorAndTime(color, T0, T1, widt)

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


	def regularOctahedron ( self, center, up, right, color=None, T0=None, T1=None ) :
		base = orthogonalBase ( up, right )
		self.octahedron ( edges, center, base[0], base[1], base[2], color, T0, T1 )


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


