import pygame
import random

pygame.init()


class NONE_obj(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))


class Pers(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(self.x, y))
        self.left = False
        self.right = False
        self.jump = False
        self.back = False
        self.enter = None
        self.anim_count = 0

    def remover(self, jump_force, right_list):
        keys = pygame.key.get_pressed()
        self.right = True
        self.anim_count += 1
        if self.anim_count >= 30:
            self.anim_count = 0

        if keys[pygame.K_SPACE]:
            jump_sound.play()
            self.jump = True

        if self.jump:
            if not (self.back):
                if self.rect.y > 250:
                    self.rect.y -= jump_force
                else:
                    self.jump = False
                    self.back = True

        if self.back:
            self.rect.y += jump_force
            self.jump = False
            if self.rect.y >= 354:
                self.back = False

        if self.right:
            self.image = right_list[self.anim_count // 10]

    def move(self, speed, jump_force, right_list, left_list, stay):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += speed
            self.right = True
            self.anim_count += 1
            if self.anim_count >= 30:
                self.anim_count = 0
        else:
            self.right = False

        if keys[pygame.K_SPACE]:
            jump_sound.play()
            self.jump = True

        if self.jump:
            if not (self.back):
                if self.rect.y > 250:
                    self.rect.y -= jump_force
                else:
                    self.jump = False
                    self.back = True

        if self.back:
            self.rect.y += jump_force
            self.jump = False
            if self.rect.y >= 354:
                self.back = False

        if self.rect.x > 0:
            if keys[pygame.K_a]:
                self.rect.x -= speed
                self.left = True
                self.anim_count += 1
                if self.anim_count >= 30:
                    self.anim_count = 0
            else:
                self.left = False

        if self.left:
            self.image = left_list[self.anim_count // 10]

        if self.right:
            self.image = right_list[self.anim_count // 10]

        elif self.left == False and self.right == False:
            self.image = stay


class HEAD(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.do = False
        self.nnn = True
        self.counter = 0
        self.enter = None

    def pump(self, hero, back_pict, ground_pict):
        if self.counter <= 1:
            chunga_ch.play()
            self.counter += 1
        if self.nnn:
            if hero.rect.x == 772:
                chunga_ch.stop()
                self.do = True
                self.nnn = False

        if self.do:
            hero.rect.x = 100
            self.rect.y += 1000
            back_pict.image = pygame.image.load("D:\SPRITES PHOTO\kosmos-zvezdy-sozvezdiya-3465.jpg")
            ground_pict.image = pygame.image.load("D:\SPRITES PHOTO\Dollars.png")
            astro_thunder.play()
            self.do = False
            hero.enter = True
            self.nnn = False


class COUNTER(pygame.sprite.Sprite):
    def __init__(self, x, y, all_pict):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        self.image = pygame.image.load(all_pict[self.counter])
        self.rect = self.image.get_rect(center=(x, y))
        self.all_pic = all_pict

    def clear(self):
        self.counter = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.counter = 0

    def moving(self, hero, counter, win_sound, speed):
        self.rect.x -= speed
        if self.y == 400:
            if (
                    hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (
                    hero.rect.y in range(300, 355)):
                if self.counter < 1:
                    counter.counter += 1
                    counter.image = pygame.image.load(counter.all_pic[counter.counter])
                    win_sound.play()
                    self.rect.y += 1000
                    self.counter += 1

        elif self.y == 300:
            if (
                    hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (
                    hero.rect.y in range(200, 326)):
                if self.counter < 1:
                    counter.counter += 1
                    counter.image = pygame.image.load(counter.all_pic[counter.counter])
                    win_sound.play()
                    self.rect.y += 1000
                    self.counter += 1


class Hiters(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.lost = False
        self.x = x
        self.y = y

    def moving(self, hero, speed):
        self.rect.x -= speed
        if self.y == 400:
            if (
                    hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (
                    hero.rect.y in range(300, 355)):
                self.rect.y += 1000
                self.lost = True

        elif self.y == 300:
            if (
                    hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (
                    hero.rect.y in range(200, 326)):
                self.rect.y += 1000
                self.lost = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.ready = False
        self.hit = False

    def moving(self, force, enemy, enemy_health):
        self.rect.x += force
        if enemy.hp == 0:
            enemy.is_alive = False
        if self.rect.x > 1000:
            self.ready = True
        if enemy.is_alive:
            if (self.rect.x == enemy.rect.x + 2) and self.rect.y in range(enemy.hitbox[0], enemy.hitbox[1]):
                hit_sound.play()
                self.hit = True
                enemy_health.change(marsik_enemy)
                enemy.hp -= 1
        if self.hit:
            self.rect.y += 1000
            self.hit = False


class Enemy_health(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename[0])
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 1
        self.picts = filename

    def move(self, enemy):
        self.rect.y = enemy.rect.y - 150

    def change(self, enemy):
        if enemy.is_alive:
            try:
                self.image = pygame.image.load(self.picts[self.counter])
                self.counter += 1
            except:
                enemy.rect.y += 10000
                self.rect.y += 10000


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.ready = False
        self.is_alive = True
        self.up = True
        self.down = False
        self.hp = 3
        self.hitbox = [self.rect.y + 2, self.rect.y + 103]

    def moving(self):
        if self.rect.x >= 800:
            self.rect.x -= 3
        else:
            self.ready = True
            self.image = pygame.image.load("D:\SPRITES PHOTO\marsik_with_gun.png")
        """
        if self.ready:
            if self.up:
                self.rect.y -= 2
                if self.rect.y <= 30:
                    self.up = False
                    self.down = True
            if self.down:
                self.rect.y += 2
                if self.rect.y >= 370:
                    self.up = True
                    self.down = False
        """


class MILITARYCAR(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.back = False

    def come(self):
        if self.rect.x <= 50:
            self.rect.x += 3
        else:
            self.back = True

    def moving(self, y):
        keys = pygame.key.get_pressed()
        if self.rect.y > -40:
            if keys[pygame.K_w]:
                self.rect.y -= y
        if self.rect.y < 400:
            if keys[pygame.K_s]:
                self.rect.y += y


class Eater(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.fall = False
        self.winer = False
        self.hero = hero
        self.pick_up = False
        self.anim_count = 0

    def winnig(self, out):
        if hero.rect.x > self.rect.x - 60:
            if check.counter >= 1:
                hero.rect.y += 3000
                self.image = pygame.image.load(out)
                self.pick_up = True
        if self.rect.x >= 1050 and self.pick_up == True:
            self.winer = True

    def moving(self):
        if not self.pick_up:
            self.rect.x -= 3

        else:
            self.rect.x += 4

    def lose(self, list_fall):
        if hero.rect.x <= -50:
            self.fall = True
        if hero.rect.x > self.rect.x - 60:
            if check.counter < 1:
                hero.rect.x -= 3
                hero.rect.y -= 3
                self.win = True
                self.anim_count += 1
                if self.anim_count >= 30:
                    self.anim_count = 0

                if self.win:
                    hero.image = list_fall[self.anim_count // 10]


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.estart = False
        self.next_level = False

    def restart(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            music_counter = 0
            if (x in range(16, 84)) and (y in range(11, 80)):
                self.estart = True
                if music_counter < 1:
                    klick_sound.play()
                    music_counter += 1

    def next_lev(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            music_counter = 0
            if (x in range(164, 235)) and (y in range(215, 286)):
                self.next_level = True
                if music_counter < 1:
                    klick_sound.play()
                    music_counter += 1


girl_walk_right = [pygame.image.load("D:\SPRITES PHOTO\sight_girl_1.png"),
                   pygame.image.load("D:\SPRITES PHOTO\sight_girl_2.png"),
                   pygame.image.load("D:\SPRITES PHOTO\sight_girl_3.png")]

girl_walk_left = [pygame.image.load("D:\SPRITES PHOTO\left_girl_3.png"),
                  pygame.image.load("D:\SPRITES PHOTO\left_girl_1.png"),
                  pygame.image.load("D:\SPRITES PHOTO\left_girl_2.png")]

girl_fall_to_win = [pygame.image.load("D:\SPRITES PHOTO\sight_girl_1.png"),
                    pygame.image.load("D:\SPRITES PHOTO\Faller1.png"),
                    pygame.image.load("D:\SPRITES PHOTO\Faller2.png"),
                    pygame.image.load("D:\SPRITES PHOTO\Faller3.png"),
                    pygame.image.load("D:\SPRITES PHOTO\Faller4.png")]

out = pygame.image.load("D:\SPRITES PHOTO\sight_girl_1.png")

pict_of_check = ["D:\SPRITES PHOTO\q0.png",
                 "D:\SPRITES PHOTO\q1.png",
                 "D:\SPRITES PHOTO\q2.png",
                 "D:\SPRITES PHOTO\q3.png",
                 "D:\SPRITES PHOTO\q4.png",
                 "D:\SPRITES PHOTO\q5.png",
                 "D:\SPRITES PHOTO\q6.png",
                 "D:\SPRITES PHOTO\q7.png",
                 "D:\SPRITES PHOTO\q8.png",
                 "D:\SPRITES PHOTO\q9.png",
                 "D:\SPRITES PHOTO\q10.png",
                 "D:\SPRITES PHOTO\q11.png",
                 "D:\SPRITES PHOTO\q12.png"]

pict_of_trash = ["D:\SPRITES PHOTO\qTrash.png",
                 "D:\SPRITES PHOTO\qTrash2.png"]

random_pict = random.randint(0, 1)
jump_sound = pygame.mixer.Sound("D:\sounds\gate_kick.mp3")
stay_girl = pygame.image.load("D:\SPRITES PHOTO\GIRL.png")
astro_thunder = pygame.mixer.Sound("D:\sounds\pravis scott - astrothunder ﾉ slowed   reverb ﾉ_.mp3")
astro_thunder.set_volume(0.5)
chunga_ch = pygame.mixer.Sound("D:\sounds\passin.mp3")
chunga_ch.set_volume(0.3)
nn = "D:\SPRITES PHOTO\GIRL.png"
klick_sound = pygame.mixer.Sound("D:\sounds\klick.mp3")

earth_pict = pygame.image.load("D:\SPRITES PHOTO\Planet1.png")
NONE_obj(500, 430, "D:\SPRITES PHOTO\блоки.png")
win = pygame.mixer.Sound("D:\sounds\gate_kick.mp3")
FPS = 70
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ASTRO JUMP")

Win_sound = pygame.mixer.Sound("D:\sounds\Carti.mp3")
Win_sound.set_volume(0.4)
Lose_sound = pygame.mixer.Sound("D:\sounds\othing-Can-Be-Explained.mp3")
Lose_sound.set_volume(0.4)
ASTRO_LOGO = NONE_obj(470, 100, "D:\SPRITES PHOTO\ASTROJUMP.png")

restart_button = Button(50, 50, "D:\SPRITES PHOTO\BUTTON1.png")
next_level_button = Button(200, 250, "D:\SPRITES PHOTO\BUTTON2.png")
win_im = NONE_obj(500, 250, "D:\SPRITES PHOTO\WIN1.png")
lose = NONE_obj(500, 250, "D:\SPRITES PHOTO\YOUlose.png")
travis = HEAD(800, 270, "D:\SPRITES PHOTO\gtravisHEAAD.png")
ground = NONE_obj(500, 490, "D:\SPRITES PHOTO\Группа 1.png")
back = NONE_obj(500, 300, "D:\SPRITES PHOTO\8b3dac2e9bd425d952f7f837123733fd.jpg")
hero = Pers(100, 400, nn)
check = COUNTER(800, 100, pict_of_check)
clock = pygame.time.Clock()
fall = False
winer = False
speed = 3
BG_COLOR = (0, 0, 0)
end_game = False
counter_for_create = 1000
list_of_map_obj = []
music = 0
cc = 0
Number_of_elem_in_game = 1
nned = False
counter = 0
level2 = False
a = 1
level1 = True
# ---------------------     2 СЦЕНА    ----------------------------

coming_car = MILITARYCAR(-100, 385, "D:\SPRITES PHOTO\CAR_OF_WAR.png")
new_back_sound = pygame.mixer.Sound("D:\sounds\Mobb Deep.mp3")
new_back_sound.set_volume(0.5)
counter_sound = 0
list_of_bullet = []
number_of_bullet = 0
new_back = NONE_obj(500, 250, "D:\SPRITES PHOTO\BACK.png")
Ready_for_attac = True
fire_sound = pygame.mixer.Sound("D:\sounds\laser-blast.mp3")
hit_sound = pygame.mixer.Sound("D:\sounds\hit.mp3")
marsik_enemy = Enemy(1150, 250, "D:\SPRITES PHOTO\marsik_fly.png")
list_of_enemy_health = ["D:\SPRITES PHOTO\qenemy_health1.png",
                        "D:\SPRITES PHOTO\qenemy_health2.png",
                        "D:\SPRITES PHOTO\qenemy_health3.png", ]

marsik_health = Enemy_health(862, 50, list_of_enemy_health)

while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
    if level1:
        screen.fill(BG_COLOR)
        screen.blit(back.image, back.rect)
        screen.blit(ground.image, ground.rect)
        screen.blit(travis.image, travis.rect)
        screen.blit(hero.image, hero.rect)
        screen.blit(ASTRO_LOGO.image, ASTRO_LOGO.rect)
        travis.pump(hero, back, ground)
        if not hero.enter and a == 1:
            hero.move(2, 3, girl_walk_right, girl_walk_left, stay_girl)
        elif hero.enter:
            ASTRO_LOGO.rect.y += 1000
            if not fall and not winer:
                screen.blit(check.image, check.rect)
                if hero.rect.y == 357:
                    hero.rect.y = 354
                if cc <= Number_of_elem_in_game:
                    for i in range(Number_of_elem_in_game):
                        type_of_obj = random.randint(0, 1)
                        random_pict = random.randint(0, 1)
                        random_y = random.randint(0, 1)
                        if type_of_obj == 0:
                            if random_y == 0:
                                subject = Hiters(counter_for_create, 400, pict_of_trash[random_pict])
                                counter_for_create += 500
                                list_of_map_obj.append(subject)
                                cc += 1
                            else:
                                subject = Hiters(counter_for_create, 300, pict_of_trash[random_pict])
                                counter_for_create += 500
                                list_of_map_obj.append(subject)
                                cc += 1
                        else:
                            if random_y == 0:
                                subject = Block(counter_for_create, 400, "D:\SPRITES PHOTO\Planet1.png")
                                counter_for_create += 500
                                list_of_map_obj.append(subject)
                                cc += 1
                            else:
                                subject = Block(counter_for_create, 300, "D:\SPRITES PHOTO\Planet1.png")
                                counter_for_create += 500
                                list_of_map_obj.append(subject)
                                cc += 1

                    CAR = Eater(counter_for_create + 100, 385, "D:\SPRITES PHOTO\Жигули1.png", hero)
                    list_of_map_obj.append(CAR)
                    cc += 1
                hero.remover(3, girl_walk_right)
                for elem in list_of_map_obj:
                    if type(elem) == Hiters:
                        screen.blit(elem.image, elem.rect)
                        elem.moving(hero, speed)
                        if elem.lost:
                            fall = True

                    elif type(elem) == Eater:
                        screen.blit(elem.image, elem.rect)
                        elem.moving()
                        if elem.rect.x < 500:
                            if check.counter >= 1:
                                elem.winnig("D:\SPRITES PHOTO\Машинистка.png")
                                nned = True
                            else:
                                elem.lose(girl_fall_to_win)
                                if elem.fall:
                                    fall = True

                        elif nned:
                            if elem.rect.x > 1050:
                                winer = True

                    else:
                        screen.blit(elem.image, elem.rect)
                        elem.moving(hero, check, win, speed)

            elif winer:
                screen.blit(back.image, back.rect)
                screen.blit(check.image, check.rect)
                screen.blit(win_im.image, win_im.rect)
                astro_thunder.stop()
                screen.blit(next_level_button.image, next_level_button.rect)
                next_level_button.next_lev()
                if next_level_button.next_level:
                    level2 = True
                    level1 = False
                    Win_sound.stop()
                if music < 1:
                    Win_sound.play()
                    music += 1

            elif fall:
                screen.blit(back.image, back.rect)
                screen.blit(check.image, check.rect)
                screen.blit(lose.image, lose.rect)
                astro_thunder.stop()
                screen.blit(restart_button.image, restart_button.rect)
                restart_button.restart()
                hero.rect.x = 100
                hero.rect.y = 354
                counter = 0
                if music < 1:
                    Lose_sound.play()
                    music += 1
                if restart_button.estart:
                    list_of_map_obj.clear()
                    cc = 0
                    counter_for_create = 1000
                    Lose_sound.stop()
                    astro_thunder.play()
                    fall = False
                    winer = False
                    check.clear()
                    check.image = pygame.image.load(pict_of_check[0])
                    screen.blit(check.image, check.rect)
                    restart_button.estart = False
                    music = 0

    elif level2:
        screen.fill(BG_COLOR)
        screen.blit(new_back.image, new_back.rect)
        screen.blit(coming_car.image, coming_car.rect)
        screen.blit(marsik_enemy.image, marsik_enemy.rect)
        if marsik_enemy.ready:
            screen.blit(marsik_health.image, marsik_health.rect)
            marsik_health.move(marsik_enemy)

        marsik_enemy.moving()
        coming_car.come()
        coming_car.moving(3)

        keys = pygame.key.get_pressed()
        # ------    определить хитбокс   ------
        """
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
        
        """
        # -------------------------------------------
        if len(list_of_bullet) >= 1:
            screen.blit(list_of_bullet[number_of_bullet - 1].image, list_of_bullet[number_of_bullet - 1].rect)
            list_of_bullet[number_of_bullet - 1].moving(5, marsik_enemy, marsik_health)
            if list_of_bullet[number_of_bullet - 1].ready:
                Ready_for_attac = True
        if keys[pygame.K_UP]:
            if Ready_for_attac:
                bullet = Bullet(257, coming_car.rect.y + 64, "D:\SPRITES PHOTO\q2bullet.png")
                now_bullet = Bullet
                list_of_bullet.append(bullet)
                number_of_bullet += 1
                fire_sound.play()
                Ready_for_attac = False
        if counter_sound < 1:
            new_back_sound.play()
            counter_sound += 1
    clock.tick(FPS)

    pygame.display.flip()
pygame.quit()