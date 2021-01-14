import random
cactus_img = [pygame.image.load(link + 'кактусы/Cactus0.png'),pygame.image.load(link + 'кактусы/Cactus1.png'),pygame.image.load(link + 'кактусы/Cactus2.png')]

shot_img = pygame.image.load(link+ 'объекты/shot.png')
shot_img = pygame.transform.scale(shot_img, (22,5))

dino_img = [pygame.image.load(link + 'динозавр/Dino0.png'),pygame.image.load(link + 'динозавр/Dino1.png'),pygame.image.load(link + 'динозавр/Dino2.png')
,pygame.image.load(link + 'динозавр/Dino3.png'),pygame.image.load(link + 'динозавр/Dino4.png')]

dino_img_stop = pygame.image.load(link + 'динозавр/Dino_jump.png')

landShaft= pygame.image.load(link+'ландшафт\\Shop.jpg')

stone_img = [pygame.image.load(link + 'объекты/Stone0.png'),pygame.image.load(link + 'объекты/Stone1.png')]


cloud_img = [pygame.image.load(link + 'объекты/Cloud0.png'),pygame.image.load(link + 'объекты/Cloud1.png')]

if random.randint(1,50) == 1:
	legendary=True
	land = pygame.image.load(link + 'ландшафт/legendary_Land.jpg')
	health_img = pygame.image.load(link + 'объекты/legendary_heart.png')
	
	
	dino_img_stop = pygame.image.load(link + 'динозавр/legendary_Dino_jump.png')
	dino_img = [pygame.image.load(link + 'динозавр/legendary_Dino0.png'),pygame.image.load(link + 'динозавр/legendary_Dino1.png'),pygame.image.load(link + 'динозавр/legendary_Dino2.png')
	,pygame.image.load(link + 'динозавр/legendary_Dino3.png'),pygame.image.load(link + 'динозавр/legendary_Dino4.png')]

else:
	legendary=False
	land = pygame.image.load(link + 'ландшафт/Land.jpg')
	
	health_img = pygame.image.load(link + 'объекты/heart.png')
	
	dino_img_stop = pygame.image.load(link + 'динозавр/Dino_jump.png')
	dino_img = [pygame.image.load(link + 'динозавр/Dino0.png'),pygame.image.load(link + 'динозавр/Dino1.png'),pygame.image.load(link + 'динозавр/Dino2.png')
	,pygame.image.load(link + 'динозавр/Dino3.png'),pygame.image.load(link + 'динозавр/Dino4.png')]
health_img = pygame.transform.scale(health_img,(30,30))

menu_bg = pygame.image.load(link + 'ландшафт/Menu.jpg')