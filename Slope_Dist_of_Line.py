# Slope and Distance of an co-ordinates using class function on python

import math

class Coordinate:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def slope(self):
		#y2 - y1 / x2 -x1
		x1 = self.coor1[0]
		y1 = self.coor1[1]
		x2 = self.coor2[0]
		y2 = self.coor2[1]
		out = (y2 - y1) / (x2 - x1)
		print(out)



	def distance(self):
		print(math.dist(self.coor1,self.coor2))



coordinate1 = (3,2)
coordinate2 = (8,10)

my_core = Coordinate(coordinate1,coordinate2)
my_core.slope()
my_core.distance()
