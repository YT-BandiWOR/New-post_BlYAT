from main import *
class Bullet(object):
	def __init__(self, x,y, speed=8 ):
		self.x=x
		self.y=y
		self.speed=speed

	def move(self):
		self.x+= self.speed
		if self.x <= display_width:
			display.blit(shot_img, (self.x,self.y))
			return True
		else:
			return False