import math
import perspectivesolids
import perspective
from vectorfunctions import *


def passingPlane ( edges, normal, color, time ):
  count = 0
  initlen = edges.numEdges()
  normnormal = normalizeVector ( normal )
  p0 = vectorTimesFactor ( normnormal, -1*math.sqrt(3) )
  step = vectorTimesFactor ( normnormal, 1/100 )
  goOn = True
  time[0] += 0.5
  while (goOn):
    poly = intersectPlaneCuboid ( p0, normal, (0,0,0), (1,0,0), (0,1,0), (0,0,1) )
    if len(poly)==0:
      if (edges.numEdges() > initlen): 
        goOn=False
    else:
      edges.polygon ( poly, color, time[0], time[0]+0.05 )
      time[0] += 0.05
    p0 = pointPlusVector ( p0, step )
    count += 1
    if (count > 1000000): raise


edges = perspectivesolids.Edges()

edges.cube((0,0,0), (0,0,1), (0,1,0), (100,100,100) )

time = [0]
passingPlane ( edges, (1,9,0), (255,000,255), time )
passingPlane ( edges, (9,9,9), (255,000,000), time )
passingPlane ( edges, (9,7,5), (255,255,000), time )
passingPlane ( edges, (1,4,6), (000,255,255), time )
passingPlane ( edges, (0,1,9), (000,255,000), time )

perspective.display(edges)