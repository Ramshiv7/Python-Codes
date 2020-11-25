# Python code to find the Volume and Surface area of an cylinder

class Cylinder:

	pi = 3.14

	def __init__(self,r,h):
		self.r = r
		self.h = h

	def vol(self):

		v = self.h * (self.r)**2 * Cylinder.pi
		print(v)

	def sa(self):

		a = 2 * Cylinder.pi * self.r * self.h + 2 * Cylinder.pi* self.r**2 
		print(a)

cyl = Cylinder(3,2)

cyl.vol()
cyl.sa()
