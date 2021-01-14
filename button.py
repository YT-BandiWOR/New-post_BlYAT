from main import *
class Button:
	def __init__(self,width, heigth,i_c=(13,162, 58),a_c=(23,204,58)):
		self.width = width
		self.heigth = heigth
		self.inactive_clr = i_c
		self.active_clr = a_c

	def draw(self, x , y , message, action=None , font_size=30):
		self.x=x
		self.y=y
		mouse= pygame.mouse.get_pos()
		click= pygame.mouse.get_pressed()


		if x< mouse[0] < x + self.width and y< mouse[1] < y + self.heigth:
			pygame.draw.rect(display,self.active_clr , (x,y,self.width, self.heigth))
                
			if click[0] == 1:
				pygame.mixer.Sound.play(button_sound)
				pygame.time.delay(300)
				if action is not None:
					action()

		else:
			pygame.draw.rect(display, self.inactive_clr , (x,y,self.width, self.heigth))

		print_text(message=message,x=x+10,y=y+10,font_size= font_size)

	def check(self):
		mouse= pygame.mouse.get_pos()
		click= pygame.mouse.get_pressed()


		if self.x< mouse[0] < self.x + self.width and self.y< mouse[1] < self.y + self.heigth:        
			if click[0] == 1:
				return True
		else:
			return False