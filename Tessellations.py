##Most of this code for outputting different tessellations was taken from https://github.com/cduck/hyperbolic/blob/master/examples/tiles.ipynb
# and was NOT created by me, Jason Bohne, However did comment so one can change paramters to create different tesssellations



import math
import numpy as np
import drawSvg as draw
from drawSvg import Drawing
from hyperbolic import euclid, util
from hyperbolic.poincare.shapes import *
from hyperbolic.poincare import Transform
from hyperbolic.poincare.util import radialEuclidToPoincare, radialPoincareToEuclid, \
                                     poincareToEuclidFactor, triangleSideForAngles
import hyperbolic.tiles as htiles
#imports essential packages such as DrawSvg to draw vector images and Hyperbolic to create the tiling of the Poincare Disk

def drawTiles(drawing, tiles):
    for tile in tiles:
        d.draw(tile, hwidth=0.075, fill='white') #can change width and fill of tiles
    for tile in tiles:
        d.draw(tile, drawVerts=True, hradius=0.25, hwidth=0.075,
                     fill='red', opacity=0.6) # change color of tile borders, radius, width etc.
        #Function draws the tiles over each level up to depth
p1 = 4
p2 = 6
q = 3
theta1, theta2 = math.pi*2/p1, math.pi*2/p2
phiSum = math.pi*2/q
# above values of p1, p2, q will set angles of each triangle in the tessellation by dividing pi/2 over each
# specified value


r1 = triangleSideForAngles(theta1/2, phiSum/2, theta2/2)
r2 = triangleSideForAngles(theta2/2, phiSum/2, theta1/2)
#solves for the last side of each triange given input parameters of such

tGen1 = htiles.TileGen.makeRegular(p1, hr=r1, skip=1)
tGen2 = htiles.TileGen.makeRegular(p2, hr=r2, skip=1)
tLayout = htiles.TileLayout()
tLayout.addGenerator(tGen1, (1,)*p1)
tLayout.addGenerator(tGen2, (0,)*p2)
#Generates the iterations of tiles

startTile = tLayout.defaultStartTile(rotateDeg=10)
#draws tiles with 360/rotateDeg sides

tiles = tLayout.tilePlane(startTile, depth=4)
#depth specifies how many iterations tessellation will repeat

d = Drawing(2, 2, origin='center')
d.draw(euclid.shapes.Circle(0, 0, 1), fill='silver')
drawTiles(d, tiles)
#draws disk where tessllation will be contained within

d.setRenderSize(w=400)
d.saveSvg('Tess01.svg')
#will save in an image file called Tess01 in same project file
