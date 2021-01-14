import random
import pygame
from pygame.locals import *
from time import sleep as s
import os
from images import *
from sounds import *
from button import Button
from object import object
from bullet import Bullet
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()
link = f'{os.getcwd()}\\DATA\\'

#-utf-8-
#   ДИсплей
display_width = 800#800
display_height = 600
#        КАРТИНКИ    КатусОВ



#         ОПЦИИ КАКТУСА
cactus_options = [69,445,37,410,40,420]
#    

img_counter = 0
health = 2



#         ИГРОК
user_width = 60
user_height = 100
user_x = display_width // 3
user_y = display_height - user_height - 100 
#        Кактус
cactus_widht = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100
#         НаЗВАНИЕ ИГРЫ
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dyno")
#          ИКОНКА ИГРЫ
icon = pygame.image.load(link+"иконка/icon.png")
pygame.display.set_icon(icon)
#           КЛОКИ
clock = pygame.time.Clock()
#            РАЗРЕШЕНИЕ ПРЫЖКА
make_jump = bool(False)
#          КОЛИЧЕСТВО ПРЫЖКОВ
jump_counter = 30
#       СТАРТ ИГРЫ
img_counter = 5
#
scores = int(0)


def game_cycle():
    cactus_arr = []


    global make_jump, button, scores


    stone, cloud = open_random_objects()

    create_cactus_arr(cactus_arr)
    game = bool(True)
    
    heart = object(display_width,280,30,health_img,4)

    button = Button(150,50)

    all_btn_bullets= []


    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        

        if keys[pygame.K_x]:
        	all_btn_bullets.append(Bullet(user_x+user_width,user_y))
        	print(all_btn_bullets)
        	print(1)

        display.blit(shot_img, (user_x,user_y-50))

        for bullet in all_btn_bullets:
        	if not bullet.move():
        		all_btn_bullets.remove(bullet)

        move_objects(stone,cloud)
        hearts_plus(heart)
        
        if keys[pygame.K_SPACE]:
            make_jump = True
        
        if make_jump:
            jump()      

        if legendary:
        	scores+= 1
        
        display.blit(land,(0,0))
        count_scores(cactus_arr)
        print_text(f'Очки: {str(scores)}',600,10)
        


        heart.move()
        drow_array(cactus_arr)
        
        draw_dino()
        if check_collision(cactus_arr):
            game= False
        
        chow_health()    
        pygame.display.update()
        clock.tick(70)
    return game_over()

def create_cactus_arr(array):
    choice1 = random.randrange(0,3)
    img = cactus_img[choice1]
    widht = cactus_options[choice1 * 2]
    height = cactus_options[choice1 * 2 + 1]
    array.append(object(display_width + 20, height, widht, img, 4))
    

    choice1 = random.randrange(0,3)
    img = cactus_img[choice1]
    widht = cactus_options[choice1 * 2]
    height = cactus_options[choice1 * 2 + 1]
    array.append(object(display_width + 300, height, widht, img, 4))

    choice = random.randrange(0,3)
    img = cactus_img[choice1]
    widht = cactus_options[choice1 * 2]
    height = cactus_options[choice1 * 2 + 1]
    array.append(object(display_width + 600, height, widht, img, 4))



def drow_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array,cactus)

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum
    choice = random.randrange(0,5)
    if choice == 0:
        radius += random.randrange(10,20)
    else:
        radius += random.randrange(200,350)
    return radius

def jump():
    global user_y, make_jump, jump_counter
    if jump_counter >= -30:
        user_y -= jump_counter / 2.5
        jump_counter -= 1
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        if jump_counter == -30:
            pygame.mixer.Sound.play(fall_sound)
    else:
        jump_counter = 30
        make_jump = False   
def open_random_objects():
    choice = random.randrange(0,2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0,2)
    img_of_cloud = cloud_img[choice]

    stone = object(display_width, display_height-80, 10, img_of_stone, 4)
    cloud = object(display_width, 80, 70, img_of_cloud, 1)

    return stone, cloud

def move_objects(stone,cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500 + random.randrange(10,80), stone.widht, img_of_stone )
    check = cloud.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10,200), cloud.widht, img_of_cloud )
def draw_dino():
    global img_counter

    if not make_jump:
        if img_counter == 25:
            img_counter = 0

        display.blit(dino_img[img_counter//5], (user_x,user_y))

        img_counter += 1
    else:
        display.blit(dino_img_stop,(user_x,user_y))
def print_text(message,x,y,font_color=(0,0,0),font_type=link + 'шрифты/font.ttf',font_size=30):
    font_type = pygame.font.Font(font_type,font_size)
    text= font_type.render(message, True, font_color)
    display.blit(text, (x,y))


def object_return(objects,obj):
    radius = find_radius(objects)

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 +1]

    obj.return_self(radius,height,width,img)


def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449: # Маленький кактус
            if not make_jump:
                if barrier.x <= user_x + user_width -35 <= barrier.x + barrier.widht:   
                    if check_health():
                        object_return(barriers,barrier)
                        return False
                    else:
                        return True
            elif jump_counter >= 0:
                if user_y + user_height -5 >= barrier.y:
                    if barrier.x  <= user_x + user_width - 27 <= barrier.x + barrier.widht:
                        if check_health():    
                            object_return(barriers,barrier)
                            return False
                        else:
                            return True
            else:
                if user_y + user_height -10 >= barrier.y:
                    if barrier.x  <= user_x  <= barrier.x + barrier.widht:
                        if check_health():    
                            object_return(barriers,barrier)
                            return False
                        else:
                            return True
        else:
            if not make_jump:
                if barrier.x <= user_x + user_width -5 <= barrier.x + barrier.widht:
                    if check_health():    
                        object_return(barriers,barrier)
                        return False
                    else:
                        return True
            elif jump_counter == 10:
                if user_y + user_height - 5 >= barrier.y:
                    if barrier.x  <= user_x + user_width - 5 <= barrier.x + barrier.widht:
                        if check_health():    
                            object_return(barriers,barrier)
                            return False
                        else:
                            return True
            elif jump_counter >= -1:
                if user_y + user_height - 5 >= barrier.y:
                    if barrier.x  <= user_x + user_width - 35 <= barrier.x + barrier.widht:
                        if check_health():    
                            object_return(barriers,barrier)
                            return False
                        else:
                            return True
                else:
                    if user_y + user_height -10 >= barrier.y:
                        if barrier.x  <= user_x + 5  <= barrier.x + barrier.widht:
                            if check_health():    
                                object_return(barriers,barrier)
                                return False
                            else:
                                return True
    return False
def pause():
    
    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        print_text('Пауза. Нажмите на Enter, чтобы продолжить...', 160,300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()
 
def game_over():
    global scores, max_scores
    esc_b=Button(110,60,(235, 64, 52),(173, 11, 0))
    ret_b=Button(155,60,(192, 201, 58),(132, 140, 6))
    pygame.mixer.music.stop()
    if int(scores) > int(max_scores):
        max_scores = scores
        f = open(link + '/bin/max_score.txt','w')
        f.write(str(max_scores))

    stopped = True 
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        print_text('Game over!', 200,200,font_size=60,font_color=(247,27,27))
        esc_b.draw(400,300,'Выйти')
        ret_b.draw(180,300,'Переиграть!')
        print_text(f'Макс: {max_scores}',600,35)
        keys = pygame.key.get_pressed()
        if ret_b.check():
            return True
        if esc_b.check():
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)
def count_scores(barriers):
    global scores, max_above
    if not(legendary):
        above_cactus = 0
        if -20 <= jump_counter < 25:
            for barrier in barriers:
                if user_y + user_height - 5 <= barrier.y:
                    if barrier.x <= user_x  <= barrier.x + barrier.widht: 
                        above_cactus += 1 
                    elif barrier.x <= user_x + user_width <= barrier.x + barrier.widht:
                        above_cactus += 1
            max_above = max(max_above,above_cactus)
        else:
            if jump_counter == -30:
                scores += max_above
                max_above = 0
def chow_health():
    global health
    x= 20
    show = 0
    while show != health:
        display.blit(health_img, (x,20) )
        x = x + 40
        show += 1
    
def check_health():
    global health
    health -= 1
    if health < 1:
        pygame.mixer.Sound.play(loss)
        return False
    else:
        pygame.mixer.Sound.play(hp_)
        return True

def hearts_plus(heart):
    global health, user_x, user_y, user_width, user_height
        
    if heart.x <= -heart.widht:
        pribavka = random.randrange(-40,40)
        radius = display_width + random.randrange(500,3000)
        heart.return_self(radius, heart.y + pribavka , heart.widht, heart.image) 

    if user_x <= heart.x <= user_x + user_width:
        if user_y <= heart.y <= user_y + user_height:
            pygame.mixer.Sound.play(hearts_plus_sound)
            if health < 5:
                health += 1
            ch = random.randrange(-1,1)
            if ch < 0:
                pribavka = random.randrange(0,20)

            else:
                pribavka = random.randrange(-20,0)
            radius = display_width + random.randrange(500,3000)
            heart.return_self(radius, heart.y + pribavka , heart.widht, heart.image)

def show_menu():
	pygame.mixer.music.load(link+ 'audio\\bg_menu.mp3')
	pygame.mixer.music.set_volume(10)
	pygame.mixer.music.play(-1)
	show=True
	start_btn= Button(288,70)
	quit_btn= Button(288,70)
	shop_btn= Button(288,70)
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg,(0,0))
		start_btn.draw(270,200,'Начать игру',start_game,50)
		shop_btn.draw(270,300,' Магазин',shop,50)
		quit_btn.draw(270,400,'   Выйти',quit,50)
		pygame.display.update()
		clock.tick(60)




def shop():
	pygame.mixer.music.load(link+'audio\\shop.mp3')
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)
	shop=True
	quit_btn= Button(288,70,(235, 64, 52),(173, 11, 0))
	while shop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if quit_btn.check:
				pygame.quit()
				quit()


        
		display.blit(landShaft,(0,0))
		quit_btn.draw(400,200,'Выйти')
		pygame.display.update()
		clock.tick(60)

def start_game():
	global scores,make_jump,jump_counter,user_y, health
	if legendary:
		pygame.mixer.music.load(link + 'audio/легендарный_фон.mp3')
	else:
		pygame.mixer.music.load(link + 'audio/фон.mp3')
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)
	while game_cycle():
	    scores = 0
	    make_jump = False
	    jump_counter = 30
	    user_y = display_height - user_height - 100 
	    health = 2
	    x= 20

try:
    max_scores = (open(link + 'bin/max_score.txt','r').read())
except:
    a = open(link + 'bin/max_score.txt','w')
    a.write('0')
    a.close()
    try:
        max_scores = int(open(link + 'bin/max_scores.txt','r').read())
    except:
        pass

max_above = 0

show_menu()
pygame.quit()
quit()