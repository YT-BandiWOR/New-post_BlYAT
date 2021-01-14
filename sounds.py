import random
shot_sound = pygame.mixer.Sound(link+'audio/shot.wav')

if random.randint(1,50) == 1:
	hp_ = pygame.mixer.Sound(link + 'audio/legendary_hp-.wav')

else:
	hp_ = pygame.mixer.Sound(link + 'audio/hp-.wav')

jump_sound = pygame.mixer.Sound(link + 'audio/рык.wav')


fall_sound = pygame.mixer.Sound(link + 'audio/падение.wav')



loss = pygame.mixer.Sound(link + 'audio/loss.wav')
hearts_plus_sound = pygame.mixer.Sound(link + 'audio/hp+.wav')


button_sound = pygame.mixer.Sound(link + 'audio/button.wav')