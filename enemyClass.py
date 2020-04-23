import pygame
import random
from abc import ABC, abstractmethod
from projectiles import DefaultProjectile, SunburnProjectile, \
                         VortexProjectile, FelspellProjectile, FreezingProjectile


"""
Abstract enemy class
"""
class Enemy (ABC):

    def __init__(self,x,y,speed, health, startDirection, screenWidth, surfaceLevel,
                        resourceHandler, showHitbox = False):

        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.direction = startDirection
        self.screenWidth = screenWidth
        self.surfaceLevel = surfaceLevel
        self.resourceHandler = resourceHandler
        self.showHitbox = showHitbox

        self.screenHeight = 480

        self.start_health = health

        self.idle = True
        self.idleCount = 0
        self.moving = False
        self.moveCount = 0
        self.attacking = False
        self.attackCount = 0
        self.dead = False
        self.deadCount = 0

        self.remove = False
        self.dead = False

        self.on_ground = False

        self.dead_sound = pygame.mixer.Sound('resources/sounds/deadEnemy.wav')

        self.loadResources()
        self.initializeOtherVars()

    @abstractmethod
    def loadResources(self):
        pass

    @abstractmethod
    def initializeOtherVars(self):
        pass

    def draw(self,win):

            # draw death animation
            if self.dead:

                # if standing towards the right direction
                if self.direction == 1:
                    # if the animation is loaded as a spritesheet
                    if self.hasSpriteSheet:
                        win.blit(self.death_right, (self.x,self.y),
                            (self.dim_of_img_in_spritesheet[0] * (self.deadCount // 9),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    # if the animation is loaded as individual images in an array
                    else:
                        win.blit(self.death_right[self.deadCount // 3], (self.x,self.y))

                # if standing towards the left direction
                else:
                    if self.hasSpriteSheet:
                        win.blit(self.death_left, (self.x,self.y),
                            (self.dim_of_img_in_spritesheet[0] * ((self.num_death_sprites - 1) - (self.deadCount // 9)),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(pygame.transform.flip(self.death_right[self.deadCount // 3],
                                True, False), (self.x,self.y))

            # draw the idle animation
            elif self.idle:

                if self.direction == 1:
                    if self.hasSpriteSheet:
                        win.blit(self.idle_right, (self.x,self.y),
                            (self.dim_of_img_in_spritesheet[0] * (self.idleCount // 3),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(self.idle_right[self.idleCount // 3], (self.x,self.y))

                else:
                    if self.hasSpriteSheet:
                        win.blit(self.idle_left, (self.x,self.y),
                            (self.dim_of_img_in_spritesheet[0] * ((self.num_idle_sprites -1 ) - (self.idleCount // 3)),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(pygame.transform.flip(self.idle_right[self.idleCount // 3],
                                True, False), (self.x,self.y))

            # draw the movement animation
            elif self.moving:

                if self.direction == 1:
                    if self.hasSpriteSheet:
                        win.blit(self.move_right, (self.x,self.y), (self.dim_of_img_in_spritesheet[0] * (self.moveCount // 3),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(self.move_right[self.moveCount // 3], (self.x,self.y))

                else:
                    if self.hasSpriteSheet:
                        win.blit(self.move_left, (self.x,self.y),
                            (self.dim_of_img_in_spritesheet[0] * ((self.num_move_sprites - 1) - (self.moveCount // 3)),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(pygame.transform.flip(self.move_right[self.moveCount // 3],
                                True, False), (self.x,self.y))

            # draw the attacking animation
            elif self.attacking:

                if self.direction == 1:
                    if self.hasSpriteSheet:
                        win.blit(self.attack_right, (self.x,self.y), (self.dim_of_img_in_spritesheet[0] * (self.attackCount // 3),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(self.attack_right[round(self.attackCount//3)], (self.x,self.y))

                else:
                    if self.hasSpriteSheet:
                        win.blit(self.attack_left, (self.x,self.y), (self.dim_of_img_in_spritesheet[0] * ((self.num_attack_sprites - 1) - (self.attackCount // 3)),0,self.dim_of_img_in_spritesheet[0],self.dim_of_img_in_spritesheet[1]))
                    else:
                        win.blit(pygame.transform.flip(self.attack_right[self.attackCount//3],
                                True, False), (self.x,self.y))

            # draw hitbar
            if not self.dead:
                pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]-20, self.healthbar_length, 10))
                pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1]-20, \
                                    self.healthbar_length - (self.one_health_length * (self.start_health-self.health)), 10))

            # draw hitbox if toggled
            if self.showHitbox:
                pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):

        # if dead
        if self.dead:


            # leave last sprite after animation finished
            if self.deadCount  < self.num_death_sprites*self.death_speed - 1:
                self.deadCount += 1
            else:
                if not self.isBoss:
                    self.remove = True

            # if died in air, fall to ground if there is a ground
            if self.surfaceLevel is not None:
                if self.y  < self.surfaceLevel - self.y_to_bottom_hitbox:
                    self.y += 2
                else:
                    self.y =  self.surfaceLevel - self.y_to_bottom_hitbox
            # if there is no ground - fall out of screen
            else:
                self.y += 2

        # if idle
        elif self.idle:
            self.y += 2

            # reset idleCount if too high, each sprite is shown n three subsequent frames
            self.idleCount += 1
            if self.idleCount > 3 * self.num_idle_sprites - 1:
                self.idleCount = 0

            # enemies are never idle if no surfaceLevel exists
            if self.y > self.surfaceLevel - self.y_to_bottom_hitbox - self.lowest_flight_height:
                self.y = self.surfaceLevel - self.y_to_bottom_hitbox - self.lowest_flight_height
                self.idle = False
                self.idleCount = 0
                self.moving = True
                self.movingCount = 0
                self.movingUpwards = True
                self.maxHeight = self.surfaceLevel - 40

        # if moving
        elif self.moving:

            if self.hasAttack:
                # should we initiate attack
                r = random.randint(0,self.attackRate)

                # attack instead
                if r == 0:
                    self.moving = False
                    self.moveCount = 0
                    self.attacking = True
                    self.attackCount = 0

            # no attack initiated
            if self.moving:

                if self.canFly:
                    if self.movingUpwards:
                        self.y -= 2

                        if self.y < 0:
                            self.movingUpwards = False
                            self.movingDownwards = True

                    elif self.movingDownwards:
                        self.y += 2
                        if self.surfaceLevel is not None:
                            if self.y > self.surfaceLevel - self.y_to_bottom_hitbox - self.lowest_flight_height:
                                self.movingUpwards = True
                                self.movingDownwards = False
                        else:
                            if self.y > self.screenHeight - self.y_to_bottom_hitbox - self.lowest_flight_height:
                                self.movingUpwards = True
                                self.movingDownwards = False



                # if facing right
                if self.direction == 1:
                    # if next step not leaves screen (with some margins)
                    if self.x + self.x_to_border_hitbox_right + self.speed < self.screenWidth - 10:
                        self.x += self.speed
                    # otherwise turn around and walk in other direction
                    else:
                        self.direction = -1
                        self.moveCount = 0

                # if facing left
                else:
                    if self.x + self.x_to_border_hitbox_left - self.speed > 10:
                        self.x -= self.speed
                    else:
                        self.direction = 1
                        moveCount = 0

                self.moveCount += 1
                # reset moveCount if too high, each sprite is shown n three subsequent frames
                if self.moveCount > 3 * self.num_move_sprites - 1:
                    self.moveCount = 0

        # attacking
        elif self.attacking:
            self.attackCount += 1
            if self.attackCount > 3 * self.num_attack_sprites - 1:
                self.attacking = False
                self.attackCount = 0
                self.moving = True
                self.moveCount = 0
                # return projectiles as effect of the attack
                return self.attackProjectiles()

        self.updateHitbox()

    @abstractmethod
    def updateHitbox(self):
        pass


    """
    Function called when the enemy is hit by a player projectile
    """
    def hit(self, projectile_direction, damage, damageMultiplier):

        if projectile_direction * self.direction > 0:
            self.health -= damage*damageMultiplier
            self.direction = -1 * self.direction
            self.moveCount = 0

        else:
            self.health -= damage

        if self.health <= 0:
            self.dead_sound.play()
            self.dead = True


class Goblin(Enemy):

    def loadResources(self):
        self.idle_right = self.resourceHandler.goblin_idle_right
        self.idle_left = self.resourceHandler.goblin_idle_left
        self.move_right = self.resourceHandler.goblin_walk_right
        self.move_left = self.resourceHandler.goblin_walk_left
        self.death_right = self.resourceHandler.goblin_death_right
        self.death_left = self.resourceHandler.goblin_death_left
        self.attack_right = self.resourceHandler.goblin_attack_right
        self.attack_left = self.resourceHandler.goblin_attack_left

        self.num_idle_sprites = 4
        self.num_move_sprites = 8
        self.num_death_sprites = 4
        self.num_attack_sprites = 8

        self.dim_of_img_in_spritesheet = (225,225)

    def initializeOtherVars(self):
        self.updateHitbox()

        self.healthbar_length = 5 * self.start_health
        self.one_health_length = 5

        self.hasSpriteSheet = True
        self.isBoss = False
        self.hasAttack = True
        self.attackRate = 150
        self.canFly = False
        self.lowest_flight_height = 0
        self.death_speed = 3

    """
    The projectiles created when the enemy attacks
    """
    def attackProjectiles(self):
        return [FreezingProjectile(self.x+110, self.y+100, 30, 30, (self.direction,0), 10, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler)]

    def updateHitbox(self):
        self.hitbox = (self.x+95, self.y+97, 32,52)
        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3]
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x


class Zombie(Enemy):


    def loadResources(self):
        self.idle_right = self.resourceHandler.zombie_idle_right
        self.move_right = self.resourceHandler.zombie_walk_right
        self.death_right = self.resourceHandler.zombie_dead_right

        self.num_idle_sprites = 15
        self.num_move_sprites = 10
        self.num_death_sprites = 12

    def initializeOtherVars(self):
        self.updateHitbox()

        self.healthbar_length = 5 * self.start_health
        self.one_health_length = 5

        self.hasSpriteSheet = False
        self.isBoss = False
        self.hasAttack = False
        self.lowest_flight_height = 0
        self.canFly = False
        self.death_speed = 3

    def updateHitbox(self):
        self.hitbox = (self.x+13, self.y+10, 23,50)
        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3]
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x



class ZombieBoss(Enemy):


    def loadResources(self):
        self.idle_right = self.resourceHandler.zombie_boss_idle_right
        self.move_right = self.resourceHandler.zombie_boss_walk_right
        self.death_right = self.resourceHandler.zombie_boss_dead_right
        self.attack_right  = self.resourceHandler.zombie_boss_attack_right

        self.num_idle_sprites = 15
        self.num_move_sprites = 10
        self.num_death_sprites = 12
        self.num_attack_sprites = 8

    def initializeOtherVars(self):
        self.updateHitbox()

        self.healthbar_length = 1 * self.start_health
        self.one_health_length = 1

        self.hasSpriteSheet = False
        self.isBoss = True
        self.hasAttack = True
        self.attackRate = 50
        self.lowest_flight_height = 0
        self.canFly = False
        self.death_speed = 3

    def attackProjectiles(self):
        projectiles = []
        projectiles.append(FelspellProjectile(self.x+25, self.y+50, 40, 40, (1,0), 10, 1, 1, self.screenWidth, showHitbox = self.showHitbox, color=(255,0,0), resourceHandler = self.resourceHandler))
        projectiles.append(FelspellProjectile(self.x+10, self.y+50, 40, 40, (-1,0), 10, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0), resourceHandler = self.resourceHandler))
        return projectiles

    def updateHitbox(self):
        self.hitbox = (self.x+20, self.y+15, 60,100)
        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3]
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x



class FlyingEye(Enemy):

    def loadResources(self):
        self.move_right = self.resourceHandler.flying_eye_flight_right
        self.move_left  = self.resourceHandler.flying_eye_flight_left
        self.death_right   = self.resourceHandler.flying_eye_death_right
        self.death_left    = self.resourceHandler.flying_eye_death_left

        self.num_move_sprites = 8
        self.num_death_sprites  = 4
        self.dim_of_img_in_spritesheet = (225,225)

    def initializeOtherVars(self):
        self.updateHitbox()

        self.healthbar_length = 5 * self.start_health
        self.one_health_length = 5

        # flying so will start flying (moving at once)
        self.canFly = True
        self.moving = True
        self.idle = False
        self.movingUpwards = False
        self.movingDownwards = True

        self.hasSpriteSheet = True
        self.isBoss = False
        self.hasAttack = False
        self.lowest_flight_height = 50
        self.death_speed = 9

    def updateHitbox(self):
        if self.direction == 1:
            self.hitbox = (self.x+90, self.y+100, 50,30)
        else:
            self.hitbox = (self.x+80, self.y+100, 50,30)

        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3]
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x

class Mushroom(Enemy):

    def loadResources(self):
        self.idle_right = self.resourceHandler.mushroom_idle_right
        self.idle_left = self.resourceHandler.mushroom_idle_left
        self.move_right = self.resourceHandler.mushroom_walk_right
        self.move_left = self.resourceHandler.mushroom_walk_left
        self.death_right = self.resourceHandler.mushroom_death_right
        self.death_left = self.resourceHandler.mushroom_death_left
        self.attack_right = self.resourceHandler.mushroom_attack_right
        self.attack_left = self.resourceHandler.mushroom_attack_left

        self.num_idle_sprites = 4
        self.num_move_sprites = 8
        self.num_death_sprites = 4
        self.num_attack_sprites = 8
        self.dim_of_img_in_spritesheet = (225,225)

    def initializeOtherVars(self):
        self.updateHitbox()

        self.healthbar_length = 5 * self.start_health
        self.one_health_length = 5

        self.hasSpriteSheet = True
        self.isBoss = False
        self.hasAttack = True
        self.attackRate = 50
        self.canFly = False
        self.lowest_flight_height = 0
        self.death_speed = 9

    def attackProjectiles(self):
        return [SunburnProjectile(self.x+110, self.y+100, 12, 12, (self.direction,0), 10, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler)]

    def updateHitbox(self):
        self.hitbox = (self.x+95, self.y+97, 32,54)
        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3]
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x

class FlyingEyeBoss(Enemy):

    def loadResources(self):
        self.move_right = self.resourceHandler.flying_eye_boss_flight_right
        self.move_left  = self.resourceHandler.flying_eye_boss_flight_left
        self.death_right   = self.resourceHandler.flying_eye_boss_death_right
        self.death_left    = self.resourceHandler.flying_eye_boss_death_left
        self.attack_right   = self.resourceHandler.flying_eye_boss_attack_right
        self.attack_left    = self.resourceHandler.flying_eye_boss_attack_left

        self.num_move_sprites = 8
        self.num_death_sprites  = 4
        self.num_attack_sprites = 8
        self.dim_of_img_in_spritesheet = (450,450)

    def initializeOtherVars(self):

        self.one_health_length = 1
        self.healthbar_length = self.one_health_length * self.start_health

        self.canFly = True
        self.movingUpwards = False
        self.movingDownwards = True
        self.moving = True
        self.idle = False
        self.lowest_flight_height = 50

        self.hasSpriteSheet = True
        self.isBoss = True
        self.hasAttack = True
        self.attackRate = 50
        self.death_speed = 9

        self.updateHitbox()

    def attackProjectiles(self):
        projectiles = []
        x_offset = 0
        if self.direction == -1:
            x_offset = 15
        projectiles.append(VortexProjectile(self.x+160-x_offset, self.y+140, 45, 40, (-1,-1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        projectiles.append(VortexProjectile(self.x+240-x_offset, self.y+140, 45, 40, (1,-1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        projectiles.append(VortexProjectile(self.x+245-x_offset, self.y+195, 45, 40, (1,1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        projectiles.append(VortexProjectile(self.x+160-x_offset, self.y+195, 45, 40, (-1,1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        return projectiles

    def updateHitbox(self):

        if self.moving:
            if self.direction == 1:
                self.hitbox = (self.x+180, self.y+200, 110,65)
            else:
                self.hitbox = (self.x+160, self.y+200, 110,65)
        elif self.attacking:
            if self.direction == 1:
                self.hitbox = (self.x+220, self.y+185, 60,45)
            else:
                self.hitbox = (self.x+180, self.y+195, 50,45)

        self.y_to_bottom_hitbox = self.hitbox[1] - self.y + self.hitbox[3] + 50
        self.x_to_border_hitbox_right = self.hitbox[0] - self.x + self.hitbox[2]
        self.x_to_border_hitbox_left = self.hitbox[0] - self.x


class FlyingEyeBoss2(FlyingEyeBoss):

    def initializeOtherVars(self):

        self.one_health_length = 1
        self.healthbar_length = self.one_health_length * self.start_health

        self.canFly = True
        self.movingUpwards = False
        self.movingDownwards = True
        self.moving = True
        self.idle = False
        self.lowest_flight_height = -50

        self.hasSpriteSheet = True
        self.isBoss = True
        self.hasAttack = True
        self.attackRate = 50
        self.death_speed = 9

        self.hard_version = False

        self.updateHitbox()

    def setHardLevel(self):
        self.hard_version = True

    def attackProjectiles(self):
        projectiles = []
        if not self.hard_version:
            projectiles.append(VortexProjectile(self.x+160, self.y+200, 45, 40, (-1,0), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
            projectiles.append(VortexProjectile(self.x+240, self.y+200, 45, 40, (1,0), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        else:
            x_offset = 0
            if self.direction == -1:
                x_offset = 15
            projectiles.append(VortexProjectile(self.x+160-x_offset, self.y+140, 45, 40, (-1,-1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
            projectiles.append(VortexProjectile(self.x+240-x_offset, self.y+140, 45, 40, (1,-1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
            projectiles.append(VortexProjectile(self.x+245-x_offset, self.y+195, 45, 40, (1,1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
            projectiles.append(VortexProjectile(self.x+160-x_offset, self.y+195, 45, 40, (-1,1), 5, 1, 1, self.screenWidth, showHitbox =self.showHitbox, color=(255,0,0),resourceHandler = self.resourceHandler))
        return projectiles
