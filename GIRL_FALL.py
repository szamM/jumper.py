
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
            if not(self.back):
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
            if not(self.back):
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
            if (hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (hero.rect.y in range(300, 355)):
                if self.counter < 1:
                    counter.counter += 1
                    counter.image = pygame.image.load(counter.all_pic[counter.counter])
                    win_sound.play()
                    self.rect.y += 1000
                    self.counter += 1

        elif self.y == 300:
            if (hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (hero.rect.y in range(200, 326)):
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
            if (hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (hero.rect.y in range(300, 355)):
                self.rect.y += 1000
                self.lost = True

        elif self.y == 300:
            if (hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x - 1 or hero.rect.x == self.rect.x or hero.rect.x == self.rect.x - 2 or hero.rect.x == self.rect.x + 2) and (hero.rect.y in range(200, 326)):
                self.rect.y += 1000
                self.lost = True


class Eater(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.win = False
        self.droop = False
        self.x = x
        self.y = y
        self.hero = hero
        self.anim_count = 0

    def winnig(self, list_fall):
        if hero.rect.x <= -50:
            self.droop = True
        if hero.rect.x > self.rect.x - 60:
            hero.rect.x -= 3
            hero.rect.y -= 3
            self.win = True
            self.anim_count += 1
            if self.anim_count >= 30:
                self.anim_count = 0

            if self.win:
                hero.image = list_fall[self.anim_count // 10]

    def moving(self):
        self.rect.x -= 3


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.estart = False

    def restart(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            music_counter = 0
            if (x in range(16, 84)) and (y in range(11, 80)):
                self.estart = True
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
klick_sound = pygame.mixer.Sound("D:\sounds\gate_kick.mp3")


earth_pict = pygame.image.load("D:\SPRITES PHOTO\Planet1.png")
NONE_obj(500, 430, "D:\SPRITES PHOTO\блоки.png")
win = pygame.mixer.Sound("D:\sounds\gate_kick.mp3")
FPS = 60
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
win_im = NONE_obj(500, 250, "D:\SPRITES PHOTO\WIN1.png")
lose = NONE_obj(500, 250, "D:\SPRITES PHOTO\YOUlose.png")
travis = HEAD(800, 270, "D:\SPRITES PHOTO\gtravisHEAAD.png")
ground = NONE_obj(500, 490, "D:\SPRITES PHOTO\Группа 1.png")
back = NONE_obj(500, 300, "D:\SPRITES PHOTO\8b3dac2e9bd425d952f7f837123733fd.jpg")
hero = Pers(100, 400, nn)
check = COUNTER(800, 100, pict_of_check)
clock = pygame.time.Clock()
game = False
fall = False
winer = False
speed = 3
BG_COLOR = (0, 0, 0)
end_game = False
enter = False
restart = False
counter_for_create = 1000
list_of_map_obj = []
music = 0
cc = 0
Number_of_elem_in_game = 2


while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True

    screen.fill(BG_COLOR)
    screen.blit(back.image, back.rect)
    screen.blit(ground.image, ground.rect)
    screen.blit(travis.image, travis.rect)
    screen.blit(hero.image, hero.rect)
    screen.blit(ASTRO_LOGO.image, ASTRO_LOGO.rect)
    travis.pump(hero, back, ground)
    if not hero.enter:
        hero.move(2, 3, girl_walk_right, girl_walk_left, stay_girl)
    else:
        ASTRO_LOGO.rect.y += 1000
        if not fall and not winer:
            screen.blit(check.image, check.rect)
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
            enter = True
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
                    elem.winnig(girl_fall_to_win)
                    if elem.droop:
                        winer = True
                else:
                    screen.blit(elem.image, elem.rect)
                    elem.moving(hero, check, win, speed)

        elif winer:
            screen.blit(back.image, back.rect)
            screen.blit(check.image, check.rect)
            screen.blit(win_im.image, win_im.rect)
            astro_thunder.stop()
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
    clock.tick(FPS)

    pygame.display.flip()
pygame.quit()