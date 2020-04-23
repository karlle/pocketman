import pygame
from abc import ABC, abstractmethod
from resourceHandler import ResourceHandler

"""
Abstract class for projectiles
"""
class Projectile(ABC):

    def __init__(self, x, y, width, height, direction, speed, damage,
                        damageMultiplier, screenWidth, showHitbox, color=None, resourceHandler = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        (self.x_direction, self.y_direction) = direction
        self.x_velocity = speed*self.x_direction
        self.y_velocity = speed*self.y_direction
        self.damage = damage
        self.damageMultiplier = damageMultiplier
        self.screenWidth = screenWidth
        self.showHitbox = showHitbox
        self.color = color
        self.resourceHandler = resourceHandler

        self.hitbox = self.updateHitbox()

        self.loadResources()
        self.playProjectileSound()

    @abstractmethod
    def loadResources(self):
        pass

    def playProjectileSound(self):
        self.projectile_sound.play()

    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def updateHitbox():
        pass

    """
    Moves the projectile, if the projectile leaves the screen returns False,
    otherwise True
    """
    def update(self):
        if self.x < self.screenWidth and self.x + self.width > 0 and self.y > 0 and self.y < 500:
            self.x += self.x_velocity
            self.y += self.y_velocity
            self.updateHitbox()
            return True
        return False


class DefaultProjectile(Projectile):


    def loadResources(self):
        self.radius = 6
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/default_projectile.wav')
        self.hit_enemy_sound = pygame.mixer.Sound('resources/sounds/default_projectile_hit.wav')

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        if self.showHitbox and self.hitbox is not None: #bug
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hitEnemySound(self, view):
        self.hit_enemy_sound.play()

    def remove(self):
        return True

    def updateHitbox(self):
        self.hitbox = (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)



class FireballProjectile(Projectile):


    def loadResources(self):
        self.fireball_images = self.resourceHandler.fireball_projectile
        self.im_counter = 0
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/fireball_projectile.wav')
        self.hit_enemy_sound = pygame.mixer.Sound('resources/sounds/fireball_projectile_hit.wav')


    def draw(self,win):

        if self.y_direction == -1:
            win.blit(self.fireball_images,(self.x,self.y), (64*self.im_counter,128,64,64))
        elif self.x_direction == 1:
            win.blit(self.fireball_images,(self.x,self.y), (64*self.im_counter,256,64,64))
        else:
            win.blit(self.fireball_images,(self.x,self.y), (64*self.im_counter,0,64,64))

        self.im_counter = (self.im_counter + 1) % 8

        if self.showHitbox:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def remove(self):
        return False

    def hitEnemySound(self, view):
        self.hit_enemy_sound.play()

    def updateHitbox(self):
        if self.x_direction == 1:
            self.hitbox = (self.x + 34, self.y + 23, self.width, self.height)
        elif self.x_direction == -1:
            self.hitbox = (self.x + 7, self.y + 23, self.width, self.height)
        else:
            self.hitbox = (self.x + 25, self.y + 13, self.height, self.width)


class SunburnProjectile(Projectile):


    def loadResources(self):
        self.sunburn_projectile = self.resourceHandler.sunburn_projectile
        self.num_img = 8
        self.img_counter = 0
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/sunburn_projectile.wav')

    def draw(self,win):

        win.blit(self.sunburn_projectile,(self.x,self.y), (50*self.img_counter,0,50,50))

        self.img_counter = (self.img_counter + 1) % self.num_img

        if self.showHitbox:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def remove(self):
        return True

    def updateHitbox(self):
        self.hitbox = (self.x + 16, self.y + 21, self.width, self.height)



class VortexProjectile(Projectile):


    def loadResources(self):
        self.vortex_projectile = self.resourceHandler.vortex_projectile
        self.img_counter = 0
        self.num_img = 8
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/vortex_projectile.wav')

    def draw(self,win):

        win.blit(self.vortex_projectile,(self.x,self.y), (75*self.img_counter,0,75,75))

        self.img_counter = (self.img_counter + 1) % self.num_img

        if self.showHitbox:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def remove(self):
        return True

    def updateHitbox(self):
        self.hitbox = (self.x + 16, self.y + 21, self.width, self.height)


class FelspellProjectile(Projectile):


    def loadResources(self):
        self.felspell_projectile = self.resourceHandler.felspell_projectile
        self.img_counter = 0
        self.num_img = 10
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/felspell_projectile.wav')

    def draw(self,win):

        win.blit(self.felspell_projectile,(self.x,self.y), (75*self.img_counter,0,75,75))

        self.img_counter = (self.img_counter + 1) % self.num_img

        if self.showHitbox:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def remove(self):
        return True

    def updateHitbox(self):
        self.hitbox = (self.x + 20, self.y + 18, self.width, self.height)

class FreezingProjectile(Projectile):

    def loadResources(self):
        self.freezing_projectile = self.resourceHandler.freezing_projectile
        self.num_img = 10
        self.img_counter = 0
        self.projectile_sound = pygame.mixer.Sound('resources/sounds/freezing_projectile.wav')

    def draw(self,win):

        win.blit(self.freezing_projectile,(self.x,self.y), (50*self.img_counter,0,50,50))

        self.img_counter = (self.img_counter + 1) % self.num_img

        if self.showHitbox:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)


    def remove(self):
        return True

    def updateHitbox(self):
        self.hitbox = (self.x + 16, self.y + 21, self.width, self.height)
