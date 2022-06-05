import perspective
import perspectivesolids


edges = perspectivesolids.Edges()


c=1 ## la moitié des côtés du cube
p=5 ## longeur des pointes
colorLettres = (255,255,255)
colorCube = (90,90,90)
deltaColor = 90


pointe=(c+p,0,0)
colorEtoile=(128+deltaColor,128,128)
edges.addEdge ( pointe, (c,c,c), colorEtoile )
edges.addEdge ( pointe, (c,-c,c), colorEtoile )
edges.addEdge ( pointe, (c,-c,-c), colorEtoile )
edges.addEdge ( pointe, (c,c,-c), colorEtoile )

pointe=(0,c+p,0)
colorEtoile=(128,128+deltaColor,128)
edges.addEdge ( pointe, (c,c,c), colorEtoile )
edges.addEdge ( pointe, (-c,c,c), colorEtoile )
edges.addEdge ( pointe, (-c,c,-c), colorEtoile )
edges.addEdge ( pointe, (c,c,-c), colorEtoile )

pointe=(0,0,c+p)
colorEtoile=(128,128,128+deltaColor)
edges.addEdge ( pointe, (c,c,c), colorEtoile )
edges.addEdge ( pointe, (-c,c,c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,c), colorEtoile )
edges.addEdge ( pointe, (c,-c,c), colorEtoile )

pointe=(-c-p,0,0)
colorEtoile=(128-deltaColor,128,128)
edges.addEdge ( pointe, (-c,c,c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,-c), colorEtoile )
edges.addEdge ( pointe, (-c,c,-c), colorEtoile )

pointe=(0,-c-p,0)
colorEtoile=(128,128-deltaColor,128)
edges.addEdge ( pointe, (c,-c,c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,-c), colorEtoile )
edges.addEdge ( pointe, (c,-c,-c), colorEtoile )

pointe=(0,0,-c-p)
colorEtoile=(128,128,128-deltaColor)
edges.addEdge ( pointe, (c,c,-c), colorEtoile )
edges.addEdge ( pointe, (-c,c,-c), colorEtoile )
edges.addEdge ( pointe, (-c,-c,-c), colorEtoile )
edges.addEdge ( pointe, (c,-c,-c), colorEtoile )

# cube
edges.addEdge ( (c,c,c), (-c,c,c), colorCube )
edges.addEdge ( (c,c,c), (c,-c,c), colorCube )
edges.addEdge ( (c,c,c), (c,c,-c), colorCube )
edges.addEdge ( (-c,-c,-c), (-c,-c,c), colorCube )
edges.addEdge ( (-c,-c,-c), (c,-c,-c), colorCube )
edges.addEdge ( (-c,-c,-c), (-c,c,-c), colorCube )
edges.addEdge ( (-c,c,c), (-c,-c,c), colorCube )
edges.addEdge ( (-c,c,c), (-c,c,-c), colorCube )
edges.addEdge ( (c,-c,c), (-c,-c,c), colorCube )
edges.addEdge ( (c,-c,c), (c,-c,-c), colorCube )
edges.addEdge ( (c,c,-c), (-c,c,-c), colorCube )
edges.addEdge ( (c,c,-c), (c,-c,-c), colorCube )

edges.lettresXYZ ( c+p, c, colorLettres )


perspective.display ( edges )