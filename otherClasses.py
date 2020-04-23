import pygame
from abc import ABC, abstractmethod
from resourceHandler import ResourceHandler

"""
Class for platforms, which the player can jump up to
"""
class Platform (object):
    def __init__ (self, x,y,width,height,level):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if level == 1 or level == 3:
            self.block = pygame.image.load('resources/images/block_light.png')
            self.block = pygame.transform.scale(self.block, (self.width,self.height))
        elif level == 2:
            self.block = pygame.image.load('resources/images/block_dark.png')
            self.block = pygame.transform.scale(self.block, (self.width,self.height))

    def draw(self,win):
        win.blit(self.block,(self.x, self.y))

"""
Class for speical objects such as power-ups and extra lifes
"""
class SpecialObject (ABC):
    def __init__ (self, x,y, width,height, velocity, surfaceLevel, showHitbox = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surfaceLevel = surfaceLevel
        self.showHitbox = showHitbox
        self.hitbox = (self.x, self.y, self.width,self.height)
        self.velocity = velocity
        self.counter = 27*5
        self.flashing = False
        self.flashing_show = None
        self.inAir = True
        self.remove = False

    @abstractmethod
    def draw(self,win):
        pass

    def shouldDraw(self):
        if not self.flashing:
            return True
        else:
            return self.flashing_show

    @abstractmethod
    def effect(self,player, model, view):
        pass

    def update(self):

        # if object has been picked up
        if self.remove:
            return False

        self.y += self.velocity

        # remove if no surface on level and out of the screen
        if self.surfaceLevel is None and self.y > 480:
            return False

        # if we end up on the surface
        if self.surfaceLevel is not None and self.y > self.surfaceLevel - self.height:
            self.inAir = False
            self.y = self.surfaceLevel - self.height
            self.counter -= 1
            if self.counter <= 0:
                return False

            # if less than two seconds left start flashing the special object
            if self.counter < 27*2:
                self.flashing = True
                if self.counter % 5 == 0:
                    self.flashing_show = not self.flashing_show


        self.hitbox = (self.x, self.y, self.width,self.height)

        return True

class Life(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    heart = pygame.image.load('resources/images/powerups/heart.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/extralife.wav')

    def draw(self,win):
        if self.shouldDraw():
            heart =  pygame.transform.scale(self.heart, (self.width, self.height))
            win.blit(heart,(self.x, self.y))

    def effect(self,player,model,view):
        if player.lifes <= 10:
            player.lifes += 1
        self.pickup_sound.play()


class Treasure(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    treasure =  pygame.image.load('resources/images/powerups/treasure.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/treasureSound.wav')

    def draw(self,win):
        if self.shouldDraw():
            treasure =  pygame.transform.scale(self.treasure, (self.width, self.height))
            win.blit(treasure,(self.x, self.y))
            if self.showHitbox:
                pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def effect(self,player, model, view):
        if self.inAir:
            model.score += 10
        else:
            model.score += 5
        self.pickup_sound.play()


class Fireball(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    fireball =  pygame.image.load('resources/images/powerups/fireballPowerup.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/powerup.wav')


    def draw(self,win):
        if self.shouldDraw():
            win.blit(self.fireball,(self.x, self.y))
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def effect(self, player, model,view):
        player.weaponPowerUp('fireball', 5)
        self.pickup_sound.play()


class DamageX2(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    damagex2 =  pygame.image.load('resources/images/powerups/damagex2.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/powerup.wav')

    def draw(self,win):
        if self.shouldDraw():
            damagex2 =  pygame.transform.scale(self.damagex2, (self.width, self.height))
            win.blit(damagex2,(self.x, self.y))
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def effect(self, player, model, view):
        player.damagePowerUp(2,27*10)
        self.pickup_sound.play()


class ShootBothWays(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    shootBothWaysIm =  pygame.image.load('resources/images/powerups/shootBothDirections.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/powerup.wav')

    def draw(self,win):
        if self.shouldDraw():
            shootBothWaysIm =  pygame.transform.scale(self.shootBothWaysIm, (self.width, self.height))
            win.blit(shootBothWaysIm,(self.x, self.y))
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def effect(self, player, model, view):
        player.shootDirectionPowerUp(27*10)
        self.pickup_sound.play()


class ShootThreeWays(SpecialObject):

    pygame.init()
    surfaceLevel = 410+57-40
    shootThreeWaysIm =  pygame.image.load('resources/images/powerups/shootThreeDirections.png')
    pickup_sound = pygame.mixer.Sound('resources/sounds/powerup.wav')

    def draw(self,win):
        if self.shouldDraw():
            shootThreeWaysIm =  pygame.transform.scale(self.shootThreeWaysIm, (self.width, self.height))
            win.blit(shootThreeWaysIm,(self.x, self.y))
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def effect(self, player, model, view):
        player.shootThreeDirectionPowerUp(27*10)
        self.pickup_sound.play()
