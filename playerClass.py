import pygame
from projectiles import DefaultProjectile, FireballProjectile

class Player(object):
    def __init__ (self, x,y, lifes, screenHeight, screenWidth, resourceHandler, surfaceLevel = None, showHitboxes = False):
        pygame.init()
        self.x = x
        self.y = y
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.resourceHandler = resourceHandler
        self.surfaceLevel = surfaceLevel
        self.showHitboxes = showHitboxes

        self.lifes = lifes
        # player is immune for a short period of time after taking damage
        self.immun_counter = 0
        # during the immune time the player flashes
        self.show_player = True

        self.speed = 5
        self.movingUpwards = False
        self.movingDownwards = True
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y+11, 26,52)
        self.dead = False
        # -1 implies not on any platform, but might start on a platform
        self.onPlatform = -1
        self.shoot_loop = 0

        self.lose_life_sound = pygame.mixer.Sound('resources/sounds/loseLife.wav')

        self.hitbox = (self.x + 18, self.y+13, 24,50)
        self.y_to_bottom_hitbox = 13 + self.hitbox[3]
        self.x_to_border_hitbox_left = 18
        self.x_to_border_hitbox_right = 18 + self.hitbox[2]

        # POWER-UPS

        # weapon power ups
        self.weapon = 'default'
        self.shotsLeft = None
        self.fireballIm  = pygame.image.load('resources/images/projectiles/fireball_projectile.png')

        # damage power-ups
        self.damageMultiplier = 1
        self.damagePowerUpCounter = 0
        self.damagex2Im = pygame.image.load('resources/images/powerups/damagex2.png')
        self.damagex2Im = pygame.transform.scale(self.damagex2Im, (40,40))

        # shoot direction power ups
        self.shootBothDirections = False
        self.shootDirectionPowerUpCounter = 0
        self.shootBothWaysIm =  pygame.image.load('resources/images/powerups/shootBothDirections.png')
        self.shootBothWaysIm = pygame.transform.scale(self.shootBothWaysIm, (50,40))

        # shoot direction power ups
        self.shootThreeDirections = False
        self.shootThreeDirectionPowerUpCounter = 0
        self.shootThreeDirIm =  pygame.image.load('resources/images/powerups/shootThreeDirections.png')

        # load images for character
        self.walkRightIm = [pygame.image.load('resources/images/player/R1.png'),
                            pygame.image.load('resources/images/player/R2.png'),
                            pygame.image.load('resources/images/player/R3.png'),
                            pygame.image.load('resources/images/player/R4.png'),
                            pygame.image.load('resources/images/player/R5.png'),
                            pygame.image.load('resources/images/player/R6.png'),
                            pygame.image.load('resources/images/player/R7.png'),
                            pygame.image.load('resources/images/player/R8.png'),
                            pygame.image.load('resources/images/player/R9.png')]
        self.walkLeftIm = [pygame.transform.flip(self.walkRightIm[0], True, False),
                           #pygame.image.load('resources/images/L1.png'),
                           pygame.image.load('resources/images/player/L2.png'),
                           pygame.image.load('resources/images/player/L3.png'),
                           pygame.image.load('resources/images/player/L4.png'),
                           pygame.image.load('resources/images/player/L5.png'),
                           pygame.image.load('resources/images/player/L6.png'),
                           pygame.image.load('resources/images/player/L7.png'),
                           pygame.image.load('resources/images/player/L8.png'),
                           pygame.image.load('resources/images/player/L9.png')]

        # heart
        self.heart = pygame.image.load('resources/images/powerups/heart.png')
        self.heart = pygame.transform.scale(self.heart, (32,35))



    def draw(self, win):

        #draw hearts
        y = 20
        x = 750
        for i in range(self.lifes):
            win.blit(self.heart, (x, y))
            x -= 35

        # draw power-ups
        y = 60        # y position of rectangle
        x = 682      # x position of rectangle
        width = 100    # width of rectangle
        height = 50    # height of rectangle

        if self.weapon is not 'default':
            pygame.draw.rect(win, (255,0,0), (x,y,width,height),2)
            win.blit(self.fireballIm, (x+4, y-6), (0,0,64,64))
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(str(self.shotsLeft), 3, (255,0,0))
            win.blit(text, (x+80-(text.get_width()//2), y+25-(text.get_height()//2)))
            y += height + 10

        if self.damageMultiplier != 1:
            pygame.draw.rect(win, (255,0,0), (x,y,width,height),2)
            win.blit(self.damagex2Im, (x+5, y+5))
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(str(self.damagePowerUpCounter // 27), 3, (255,0,0))
            win.blit(text, (x+80-(text.get_width()//2), y+25-(text.get_height()//2)))
            y += height + 10

        if self.shootBothDirections:
            pygame.draw.rect(win, (255,0,0), (x,y,width,height),2)
            win.blit(self.shootBothWaysIm, (x+5, y+5))
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(str(self.shootDirectionPowerUpCounter // 27), 3, (255,0,0))
            win.blit(text, (x+80-(text.get_width()//2), y+25-(text.get_height()//2)))

        elif self.shootThreeDirections:
            pygame.draw.rect(win, (255,0,0), (x,y,width,height),2)
            win.blit(self.shootThreeDirIm, (x+5, y+5))
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(str(self.shootThreeDirectionPowerUpCounter // 27), 3, (255,0,0))
            win.blit(text, (x+80-(text.get_width()//2), y+25-(text.get_height()//2)))


        # when player takes damage the character flickers for one seocond under
        # which the player is immune to further damage

        if self.show_player:
            # draw player
            if self.walkCount + 1 >=27:
                self.walkCount = 0

            if not self.standing:
                if self.left:
                    win.blit(self.walkLeftIm[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.walkRightIm[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1

            # player is idle
            else:
                if self.right:
                    win.blit(self.walkRightIm[0], (self.x, self.y))
                else:
                    win.blit(self.walkLeftIm[0], (self.x, self.y))


        if self.showHitboxes:
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)

        # if no input next frame, then player should be idle
        self.standing = True


    def walkLeft(self,platforms):
        self.x = max(self.x-self.speed,0 - self.x_to_border_hitbox_left)
        self.left = True
        self.right = False
        self.standing = False

        # was the player on a platform last frame?
        if self.onPlatform != -1:
            postOnPlatform = self.checkPlatforms(platforms)
            # if we have left the platform, start moving downwards
            if postOnPlatform == -1:
                self.movingDownwards = True


    def walkRight(self,platforms):
        self.x = min(self.x + self.speed, self.screenWidth-self.x_to_border_hitbox_right)
        self.right = True
        self.left = False
        self.standing = False

        if self.onPlatform != -1:
            postOnPlatform = self.checkPlatforms(platforms)
            if postOnPlatform == -1:
                self.movingDownwards = True


    def jump(self):
        if not self.movingUpwards and not self.movingDownwards:
            self.movingUpwards = True
            self.jumpCount = 10
            self.onPlatform = -1
            self.walkCount = 0

    def fire(self):
        # at least a number of frames (depending on weapon) between shoots
        if self.shoot_loop == 0:
            if self.left:
                shot_direction = -1
            else:
                shot_direction = 1

            projectiles = [self.createProjectile((shot_direction,0))]

            # create projectile in opposite direction of player
            if self.shootBothDirections or self.shootThreeDirections:
                projectiles.append(self.createProjectile((-1*shot_direction,0)))

            # create projectile moving straight upwards
            if self.shootThreeDirections:
                projectiles.append(self.createProjectile((0,-1)))

            if self.weapon == 'default':
                self.shoot_loop = 10

            if self.weapon == 'fireball':
                self.shotsLeft -= 1
                self.shoot_loop = 20
                # if out of projectiles back to default weapon
                if self.shotsLeft == 0:
                    self.weapon = 'default'
                    self.shotsLeft = None
                    self.shoot_loop = 10

            return projectiles
        return -1

    def createProjectile(self, direction):

        if self.weapon == 'default':
            return DefaultProjectile((self.x + 32), \
                            (self.y+32), 12, 12, direction, 8, \
                                1*self.damageMultiplier,5, self.screenWidth,
                                showHitbox = True, color=(0,0,0))

        elif self.weapon == 'fireball':
            return FireballProjectile((self.x), \
                            (self.y + 10), 20, 15, direction, 8, \
                              1*self.damageMultiplier,1, self.screenWidth,
                              showHitbox = self.showHitboxes, resourceHandler = self.resourceHandler)

    """
    Functions called when player picks up power-ups
    """
    def weaponPowerUp(self, weapon, shots):
        if self.weapon == weapon:
            self.shotsLeft += shots
        else:
            self.weapon    = weapon
            self.shotsLeft = shots

    def damagePowerUp(self, damageMultiplier, time):
        self.damageMultiplier = 2
        self.damagePowerUpCounter += time

    def shootDirectionPowerUp(self, time):
        self.shootBothDirections = True
        self.shootDirectionPowerUpCounter += time

    def shootThreeDirectionPowerUp(self,time):
        self.shootThreeDirections = True
        self.shootThreeDirectionPowerUpCounter += time


    """
    Updates variables that need to be updated every frame, even if no keypresse occur
    """
    def updateEveryFrame(self, platforms):

        if self.shoot_loop > 0:
            self.shoot_loop -= 1

        # if player has taken damage, immun and blinking for a period of time
        if self.immun_counter > 0:
            self.immun_counter -= 1
            if self.immun_counter % 3 == 0:
                self.show_player = not self.show_player
        else:
            self.show_player = True

        # reduce counter of damage power up
        if self.damageMultiplier > 1:
            self.damagePowerUpCounter -= 1
            if self.damagePowerUpCounter == 0:
                self.damageMultiplier = 1

        # reduce counter of shoot both directions power up
        if self.shootBothDirections:
            self.shootDirectionPowerUpCounter -= 1
            if self.shootDirectionPowerUpCounter == 0:
                self.shootBothDirections = False

        # reduce counter of shoot three directions power up
        if self.shootThreeDirections:
            self.shootThreeDirectionPowerUpCounter -= 1
            if self.shootThreeDirectionPowerUpCounter == 0:
                self.shootThreeDirections = False

        if self.movingUpwards:
            self.y = round(self.y - (self.jumpCount ** 2) * 0.5)
            if self.jumpCount > 0:
                self.jumpCount -= 1
            else:
                self.movingUpwards = False
                self.movingDownwards = True

        elif self.movingDownwards:

            self.y = round(self.y + (self.jumpCount ** 2) * 0.5)
            if self.jumpCount < 10:
                self.jumpCount += 1

            # if level has a surface at bottom
            if self.surfaceLevel is not None:
                if self.y > self.surfaceLevel - self.y_to_bottom_hitbox:
                    self.y = self.surfaceLevel - self.y_to_bottom_hitbox
                    self.movingDownwards = False

            # if level has no surface at bottom we can fall of the map and loose a life
            else:
                if self.y > self.screenHeight:
                    if self.hit(falling_off = True) == "game_over":
                        return "game_over"
                    else:
                        self.x = 60
                        self.y = 230

            self.onPlatform = self.checkPlatforms(platforms)

            if self.onPlatform > -1:
                self.movingDownwards = False
                self.jumpCount = 0
                self.y = platforms[self.onPlatform].y - 59

        self.hitbox = (self.x + 18, self.y+13, 24,50)


    """
    Checks if the player is currently standing on a platform. Takes a list of all
    platforms as a parameter and returns the index of the platform which the players is
    standing on. If the player is standing on no platform returns -1.
    """
    def checkPlatforms(self,platforms):
        for (i,platform) in enumerate(platforms):

            # when jumpCount is high the player risk passing through the platform if
            # the cutoff in terms of the y-axis is not increased as the jumpcount increases
            y_cut_off = 5 + (self.jumpCount ** 2 / 2)

            if self.hitbox[0] < platform.x + platform.width - 2 \
               and self.hitbox[0] + self.hitbox[2] > platform.x + 2 and \
               abs(self.hitbox[1]+self.hitbox[3]-platform.y) < y_cut_off:

               return i
        return -1

    """
    Called when an enemy or an enemy projectile hits the player
    """
    def hit(self, falling_off = False):

        # we can loose a life by falling off the map even if we are immune
        if self.immun_counter > 0 and not falling_off:
            return

        self.lifes -= 1
        if self.lifes == 0:
            self.lose_life_sound.play()
            return 'game_over'
        else:
            # if hit is immun for one second
            self.immun_counter = 27 * 2
            self.lose_life_sound.play()
            return
