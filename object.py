class object():
    def __init__(self, x, y, width,image,speed):
        self.x = x
        self.y = y
        self.widht = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.widht:
            display.blit(self.image,(self.x,self.y))
            # pygame.draw.rect(display,(224,91,22),(self.x, self.y, self.widht, self.height))
            self.x -= self.speed
            return True
        else:
            return False
    def return_self(self,radius,y,widht,image):
        self.x = radius
        self.y = y
        self.widht = widht
        self.image = image
        display.blit(self.image,(self.x,self.y))