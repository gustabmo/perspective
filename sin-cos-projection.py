import math
import perspectivesolids
import perspective
from vectorfunctions import *


radius=10
center=14
rodsW=0.05
rodsL=2
anglestep=1.5
timestep=0.03

def Wheel(edges):
	prev=None
	angle = 0
	while (angle <= 360):
		p = ( 0, center+math.cos(angle/180*math.pi)*radius, center+math.sin(angle/180*math.pi)*radius )
		#spoke
		if (angle%15==0):
			edges.addEdge ( (0,center,center), p, (70,70,70) )
		#wheel
		if (prev!=None):
			edges.addEdge ( prev, p, (120,120,120) )
		prev=p
		angle+=anglestep



def Rotation(edges,time,spoke=False,projY=False,projZ=False,factorTime=1):
	angle = 0
	while (angle <= 360):
		t1 = time[0]+timestep*factorTime
		p = ( rodsL/2, center+math.cos(angle/180*math.pi)*radius, center+math.sin(angle/180*math.pi)*radius )
		if spoke:
			edges.addEdge ( (0,center,center), (0,p[1],p[2]), (210,210,0), time[0], t1)
		edges.cuboid (
			p,
			(rodsL/2,0,0), (0,rodsW,0), (0,0,rodsW), 
			(210,210,0),
			time[0], t1
		)
		if projY:
			edges.addEdge ( p, (p[0],0,p[2]), (120,120,0), time[0], t1 )
			edges.addEdge ( (0,0,p[2]), (rodsL,0,p[2]), (120,120,0), time[0], t1 )
		if projZ:
			edges.addEdge ( p, (p[0],p[1],0), (120,120,0), time[0], t1 )
			edges.addEdge ( (0,p[1],0), (rodsL,p[1],0), (120,120,0), time[0], t1 )
		time[0] = t1
		angle+=anglestep
	

def RulerMarks(edges,time):
	time[0] = time[0]+2

	edges.addEdge ( (0,0,center), (0,center*2,center), (0,90,210), time[0], 1e10 )
	edges.addEdge ( (0,center,0), (0,center,center*2), (0,90,210), time[0], 1e10 )

	time[0] = time[0]+3

	edges.addEdge ( (0,center*2,center), (0,center*2-rodsL,center+rodsL*0.3), (0,90,210), time[0], 1e10 )
	edges.addEdge ( (0,center*2,center), (0,center*2-rodsL,center-rodsL*0.3), (0,90,210), time[0], 1e10 )

	time[0] = time[0]+1
	
	edges.addEdge ( (0,center,center*2), (0,center+rodsL*0.3,center*2-rodsL), (0,90,210), time[0], 1e10 )
	edges.addEdge ( (0,center,center*2), (0,center-rodsL*0.3,center*2-rodsL), (0,90,210), time[0], 1e10 )

	time[0] = time[0]+3


	edges.addEdge ( (rodsL/2,0,center+radius), (rodsL/2,0,center-radius), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,0,center+radius), (rodsL*0.8,0,center+radius), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,0,center       ), (rodsL*0.8,0,center       ), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,0,center-radius), (rodsL*0.8,0,center-radius), (0,130,120), time[0], 1e10 )

	time[0] = time[0]+2

	edges.addEdge ( (rodsL/2,center+radius,0), (rodsL/2,center-radius,0), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,center+radius,0), (rodsL*0.8,center+radius,0), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,center       ,0), (rodsL*0.8,center       ,0), (0,130,120), time[0], 1e10 )
	edges.addEdge ( (rodsL*0.2,center-radius,0), (rodsL*0.8,center-radius,0), (0,130,120), time[0], 1e10 )

	time[0] = time[0]+2

	# edges.addEdge ( (rodsL*1.5))


def RulerScale(edges,time):
	time[0]=time[0]+3

	edges.write ( (rodsL*2,center-rodsL*0.2,0), (-rodsL*0.8,0,0), (0,rodsL*0.4,0), "0", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2
	edges.write ( (rodsL*2,center-radius-rodsL/2,0), (-rodsL*0.8,0,0), (0,rodsL*0.4,0), "-1", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2
	edges.write ( (rodsL*2,center+radius-rodsL/2,0), (-rodsL*0.8,0,0), (0,rodsL*0.4,0), "+1", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2

	edges.write ( (rodsL*2,0,center-rodsL/2), (0,0,rodsL*0.8), (-rodsL*0.4,0,0), "0", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2
	edges.write ( (rodsL*2,0,center-radius-rodsL/2), (0,0,rodsL*0.8), (-rodsL*0.4,0,0), "-1", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2
	edges.write ( (rodsL*2,0,center+radius-rodsL/2), (0,0,rodsL*0.8), (-rodsL*0.4,0,0), "+1", (0,130,120), time[0], 1e10 )
	time[0]=time[0]+2




edges = perspectivesolids.Edges()

edges.cuboid ( (center,center,center), (center,0,0), (0,center,0), (0,0,center), (80,80,80) )
Wheel(edges)


time = [5]
Rotation(edges,time,False)
Rotation(edges,time,True)
Rotation(edges,time,True,True,False,2)
Rotation(edges,time,True,False,True,1.5)
Rotation(edges,time,True,True,True,3)
RulerMarks(edges,time)
Rotation(edges,time,True,True,True,3)
RulerScale(edges,time)
Rotation(edges,time,True,True,True,5)
Rotation(edges,time,True,True,True,5)
Rotation(edges,time,True,True,True,2)


perspective.display ( edges, pov=[rodsL/2,center,center] )