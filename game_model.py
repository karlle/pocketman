import random
from playerClass import Player
from enemyClass import Zombie, ZombieBoss, FlyingEye, Mushroom, FlyingEyeBoss, Goblin, FlyingEyeBoss2
from otherClasses import Platform, Treasure, Fireball, DamageX2, ShootBothWays, Life, ShootThreeWays
from game_view import View
from resourceHandler import ResourceHandler
from os import path


class Model():

    def __init__(self, screenWidth, screenHeight, hitboxes = False):
        self.screenWidth  = screenWidth
        self.screenHeight = screenHeight
        self.hitboxes = hitboxes
        self.view = View(screenWidth, screenHeight)
        self.resourceHandler = ResourceHandler()
        self.num_levels = 3
        self.next_new_life_score_level = 100
        self.lifes = 3


        self.difficulties = 3
        # easy = 0, normal = 1, hard = 2
        self.difficulty = 1

        # per difficulty
        self.boss_life = [75, 150, 250]
        self.num_enemies = [10, 15, 25]
        self.time_between_enemies = [27*5,27*4,int(27*3.5)]

        self.start_screen = False
        self.game_over = False
        self.in_level = False
        self.level_finished = False
        self.paused = False

        self.new_high_score_index = None
        self.new_high_score_name = []

        # the following counters are used to prevent that
        # single key presses are registered more than once (in subsequent frames)
        self.high_score_name_counter = 0
        self.start_screen_counter = 0
        self.game_over_counter = 0
        self.pause_counter = 0
        self.difficulty_counter = 0
        self.instruction_screen_counter = 0

        self.end_music_started = False

        self.startScreen()


    """
    Prepares the start screen
    """
    def startScreen(self):
        self.start_screen = True
        self.game_over = False
        self.view.playMusic('start_screen')
        self.curr_level = 0
        self.view.startScreen(self.difficulty)

    """
    Prepares the instruction screen
    """
    def instructionScreen(self):
        self.instruction_screen = True
        self.start_screen = False
        self.instruction_screen_counter = 5
        self.view.instructionScreen()


    """
    Pause the game, can only pause when in an actual level and after a shorter
    cooldown (10 frames)
    """
    def paus(self):
        if self.in_level and not self.level_finished and self.pause_counter == 0:
            if not self.paused:
                self.paused = True
                self.view.paus()
            else:
                self.paused = False
            self.pause_counter = 10


    """
    The player has pressed the return button, it is used between levels, to
    start the next level etc.
    """
    def enter(self):
        # do nothing if we are in a level and have not finished it
        if self.in_level and not self.level_finished:
            return

        # start new game if on start screen, if start screen counter is zero
        if self.start_screen and self.start_screen_counter == 0:
            self.instructionScreen()

        if self.instruction_screen and self.instruction_screen_counter == 0:
            self.newGame()

        # go to start screen if on high score screen and no new high score
        elif  self.game_over and self.game_over_counter == 0 and \
                                self.new_high_score_index is None:
            self.start_screen_counter = 8
            self.startScreen()

        # if on high score screen with new high score and a choosen name
        # save high score and start new game
        elif  self.game_over and self.new_high_score_index is not None and \
                            len(self.new_high_score_name) == 3:
            self.writeHighScore()
            self.start_screen_counter = 8
            self.startScreen()

        # if we have finished a level, move to the next one
        elif self.level_finished:
            self.nextLevel()


    """
    Start a new game, starting level 1
    """
    def newGame(self):
        self.instruction_screen = False
        self.score = 0
        self.lifes = 3
        self.curr_level = 1
        self.next_new_life_score_level = 100
        self.initializeLevel(self.curr_level)


    """
    Starts the next level. If current level is the last one - goes to high
    score screen (game over screen)
    """
    def nextLevel(self):

        if self.curr_level == self.num_levels:
            self.game_over_counter = 8
            self.gameOver()
        else:
            # recreate player object between levels, so saves number of lifes
            self.lifes = self.player.lifes
            self.curr_level += 1
            self.initializeLevel(self.curr_level)


    """
    Initializes the specificed level
    """
    def initializeLevel(self, level):
        self.enemies = []
        self.platforms = []
        self.projectiles = []
        self.enemy_clock = 0
        self.powerups = []
        self.enemies_killed = 0
        self.enemy_projectiles = []
        self.boss = False
        self.boss_dead = False
        self.boss_dead_counter = 0
        self.level_finished = False
        self.game_over = False
        self.new_high_score_index = None
        self.new_high_score_name = []
        self.end_music_started = False

        if level == 1:

            self.surfaceLevel = 470
            x1 = random.randrange(self.screenWidth-150)
            x2 = random.randrange(self.screenWidth-150)
            self.enemies.append(Goblin (x1,55,5,8,1,self.screenWidth, self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.enemies.append(Zombie (x2,55,6,8,-1,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.platforms.append(Platform(150,300, 50,50,self.curr_level))
            self.platforms.append(Platform(570, 300,50,50,self.curr_level))
            self.view.playMusic('level1')
            self.boss_music = 'bossmusic1'
            self.boss_type = ZombieBoss
            x_start_position = 300
            y_start_position = 400
            self.player = Player(x_start_position,y_start_position, self.lifes,
                self.screenHeight, self.screenWidth, self.resourceHandler, surfaceLevel = self.surfaceLevel,
                                showHitboxes =  self.hitboxes)


        elif level == 2:

            self.surfaceLevel = 460
            self.platforms.append(Platform(150,300, 50,50,self.curr_level))
            self.platforms.append(Platform(255, 240,50,50, self.curr_level))
            self.platforms.append(Platform(570, 300,50,50,self.curr_level))
            self.platforms.append(Platform(465, 240,50,50,self.curr_level))
            x1 = random.randrange(self.screenWidth-150)
            x2 = random.randrange(self.screenWidth-150)
            self.enemies.append(Mushroom (x1,55,3,10,1,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.enemies.append(FlyingEye (x2,55,5,2,-1,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.view.playMusic('level2')
            self.boss_music = 'bossmusic2'
            self.boss_type = FlyingEyeBoss
            x_start_position = 300
            y_start_position = 400
            self.player = Player(x_start_position,y_start_position, self.lifes,
                self.screenHeight, self.screenWidth, self.resourceHandler, surfaceLevel = self.surfaceLevel,
                                showHitboxes =  self.hitboxes)


        elif level == 3:

            self.surfaceLevel = None
            self.platforms.append(Platform(60,360, 50,50,self.curr_level))
            self.platforms.append(Platform(100,200, 50,50,self.curr_level))
            self.platforms.append(Platform(40,50, 50,50,self.curr_level))
            self.platforms.append(Platform(155,420, 50,50,self.curr_level))
            self.platforms.append(Platform(165,300, 50,50,self.curr_level))
            self.platforms.append(Platform(245,370, 50,50,self.curr_level))
            self.platforms.append(Platform(270, 240,50,50, self.curr_level))
            self.platforms.append(Platform(375, 180,50,50, self.curr_level))
            self.platforms.append(Platform(480, 240,50,50,self.curr_level))
            self.platforms.append(Platform(585, 300,50,50,self.curr_level))
            self.platforms.append(Platform(690,360, 50,50,self.curr_level))
            self.platforms.append(Platform(650,200, 50,50,self.curr_level))
            self.platforms.append(Platform(600,50, 50,50,self.curr_level))
            self.platforms.append(Platform(480,50, 50,50,self.curr_level))
            self.platforms.append(Platform(500,370, 50,50,self.curr_level))
            x1 = random.randrange(self.screenWidth-150)
            x2 = random.randrange(self.screenWidth-150)
            self.enemies.append(FlyingEye (x1,55,4,3,1,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.enemies.append(FlyingEye (x2,55,4,3,-1,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            self.view.playMusic('level3')
            self.boss_music = 'bossmusic2'
            self.boss_type = FlyingEyeBoss
            x_start_position = 60
            y_start_position = 230
            self.player = Player(x_start_position,y_start_position, self.lifes,
                self.screenHeight, self.screenWidth, self.resourceHandler, surfaceLevel = self.surfaceLevel,
                                showHitboxes =  self.hitboxes)

        self.in_level = True


    """
    Method called when player runs out of lifes, or when the playe
    has beat the game
    """
    def gameOver(self):

        self.game_over = True
        if self.player.lifes == 0:
            self.view.playMusic('game_over')
        elif not self.end_music_started:
            self.view.playMusic('end_music')
            self.end_music_started = True

        self.in_level = False
        self.level_finished = False

        self.high_scores = self.loadHighScores()

        if self.score > 0 and (len(self.high_scores) < 5 or \
                    self.score > self.high_scores[-1][0]):

            # set name of new score to a in order to make it come after any
            # other entry with the same score. Score tuples are sorted on score, but
            # if the score is equal they are sorted on name
            self.high_scores.append((self.score, 'a'))
            self.high_scores.sort(reverse=True)

            # if more than 5 high scores pop lowest score
            if len(self.high_scores) > 5:
                self.high_scores.pop()

            # get index of new score in sorted list
            self.new_high_score_index = self.high_scores.index((self.score,'a'))

        self.view.gameOver(self.curr_level, self.high_scores, self.difficulty,
                        high_score_name = self.new_high_score_name,
                        high_score_index = self.new_high_score_index)


    """
    Loads high scores from text file
    """
    def loadHighScores(self):
        difficulties = ['easy','medium','hard']
        with open('highscore-' + str(difficulties[self.difficulty]) + '.txt', 'r') as f:
            lines = f.readlines()
            high_scores = []
            for line in lines:
                (score, name) = line.split()
                high_scores.append((int(score),name))

            return high_scores


    """
    Used for writing the players name when he gets a new high score
    """
    def addCharToName(self, i):

        if self.new_high_score_index is not None and \
           len(self.new_high_score_name) < 3 and \
           self.high_score_name_counter == 0:

            chars = 'abcdefghijklmnopqrstuvwxyz'
            self.new_high_score_name.append(chars[i])
            self.high_score_name_counter = 5

            self.view.gameOver(self.curr_level, self.high_scores, self.difficulty,
                            high_score_name = self.new_high_score_name,
                            high_score_index = self.new_high_score_index)

    """
    Removes the last choosen character from the players name when he gets
    a new high score
    """
    def removeCharFromName(self):
        if self.new_high_score_index is not None and \
           len(self.new_high_score_name) > 0 and \
           self.high_score_name_counter == 0:

            self.new_high_score_name.pop()
            self.high_score_name_counter = 5
            self.view.gameOver(self.curr_level, self.high_scores, self.difficulty,
                            high_score_name = self.new_high_score_name,
                            high_score_index = self.new_high_score_index)

    """
    Writes the new high score to the high score text file
    """
    def writeHighScore(self):
        # inser correct name in high score list
        self.high_scores[self.new_high_score_index] = (self.score, "".join(self.new_high_score_name))
        # format high score list as strings
        high_scores_format = []
        for hs in self.high_scores:
            high_scores_format.append(str(hs[0]) + " " + hs[1] + "\n")

        # write to the file
        difficulties = ['easy','medium','hard']
        with open('highscore-' + str(difficulties[self.difficulty]) + '.txt', 'w') as f:
            f.writelines(high_scores_format)



    """
    Methods for controlling the player, if not in a level (or start screen)
    or if the game is paused they do nothing. walkLeft/right are also used
    for choosing the difficulty on the start screen.
    """

    def walkLeft(self):
        #choosing difficulty on start screen
        if self.start_screen and self.difficulty_counter == 0:
            self.difficulty = max(0,self.difficulty -1)
            self.difficulty_counter = 5
            self.view.startScreen(self.difficulty)

        if self.in_level and not self.paused:
            self.player.walkLeft(self.platforms)

    def walkRight(self):
        #choosing difficulty on start screen
        if self.start_screen and self.difficulty_counter == 0:
            self.difficulty = min(2,self.difficulty + 1)
            self.difficulty_counter = 5
            self.view.startScreen(self.difficulty)

        if self.in_level and not self.paused:
            self.player.walkRight(self.platforms)


    def jump(self):
        if self.in_level and not self.paused:
            self.player.jump()

    def fire(self):
        if self.in_level and not self.paused:
            # can't fire more than 5 projectiles at the same time (9 if shootThreeDirections
            # power up is active
            if len(self.projectiles) < 5 or self.player.shootThreeDirections and len(self.projectiles) < 9:
                projectiles = self.player.fire()
                if projectiles != -1:
                    for projectile in projectiles:
                        self.projectiles.append(projectile)


    """
    The main update function which is run for every frame of the game
    """
    def update(self):

        if self.difficulty_counter > 0:
            self.difficulty_counter -= 1

        if self.start_screen_counter > 0:
            self.start_screen_counter -= 1

        if self.instruction_screen_counter > 0:
            self.instruction_screen_counter -= 1

        if self.game_over_counter > 0:
            self.game_over_counter -= 1

        if self.high_score_name_counter > 0:
            self.high_score_name_counter -= 1

        # dealing with paused game state
        if self.pause_counter > 0:
            self.pause_counter -= 1

        # if paused or not in a level just return
        if self.paused or not self.in_level:
            return

        # give extra life for every 100 points
        if self.score >= self.next_new_life_score_level:
            x = random.randrange(self.screenWidth-100)
            self.powerups.append(Life(x,55, 32,35, 2, self.surfaceLevel))
            self.next_new_life_score_level += 100

        if self.boss_dead:
            self.boss_dead_counter += 1

            if self.boss_dead_counter == 27*6:
                self.view.playMusic('endmusic')
                self.end_music_started = True

        # remove projectiles which are off screen
        for projectile in self.projectiles:
            if not projectile.update():
                self.projectiles.pop(self.projectiles.index(projectile))

        # update enemies
        for enemy in self.enemies:
            if enemy.remove:
                self.enemies.pop(self.enemies.index(enemy))

            projectiles = enemy.move()
            if projectiles is not None:
                for projectile in projectiles:
                    self.enemy_projectiles.append(projectile)

        # update enemy projectiles
        for projectile in self.enemy_projectiles:
            if not projectile.update():
                self.enemy_projectiles.pop(self.enemy_projectiles.index(projectile))

        # update power-ups
        for powerup in self.powerups:
            if not powerup.update():
                self.powerups.pop(self.powerups.index(powerup))

        # update player
        if self.player.updateEveryFrame(self.platforms) == "game_over":
            self.gameOver()
            return

        # add new enemies
        self.enemy_clock += 1

        if not self.boss_dead:
            if (self.enemy_clock == self.time_between_enemies[self.difficulty] \
                        and self.enemies_killed < self.num_enemies[self.difficulty]) or \
                            (self.enemy_clock == 27*8 and self.boss):
                self.addNewEnemy()
                self.enemy_clock = 0

            elif not self.boss and self.enemy_clock == 27*8:
                self.view.playMusic(self.boss_music)
                self.addNewEnemy(boss=True)
                self.enemy_clock = 0
                self.boss = True


        # do enemies hit player
        for enemy in self.enemies:
            if not enemy.dead:
                if self.compareHitboxes(self.player.hitbox, enemy.hitbox):
                    hit = self.player.hit()
                    if hit == 'game_over':
                        self.gameOver()
                        return

        # do player get power up
        for powerup in self.powerups:
            if self.compareHitboxes(self.player.hitbox, powerup.hitbox):
                powerup.effect(self.player, self, self.view)
                powerup.remove = True

        # do enemy projectiles hit player
        for projectile in self.enemy_projectiles:
            if self.compareHitboxes(self.player.hitbox, projectile.hitbox):

                # can cause a bug so in try/except block
                if projectile.remove():
                    try:
                        self.enemy_projectiles.pop(self.enemy_projectiles.index(projectile))
                    except:
                        pass

                hit = self.player.hit()
                if hit == 'game_over':
                    self.gameOver()
                    return
                elif hit == 'lost_life':
                    self.view.playMusic('lost_life')

        # do projectlies hit enemies
        for projectile in self.projectiles:
            for enemy in self.enemies:
                if not enemy.dead:
                    if self.compareHitboxes(enemy.hitbox, projectile.hitbox):
                        projectile.hitEnemySound(self.view)
                        enemy.hit(projectile.x_direction, projectile.damage, projectile.damageMultiplier)
                        if enemy.dead:
                            if isinstance(enemy, self.boss_type):
                                self.score += 100
                                # kill all other current enemies
                                for e in self.enemies:
                                    e.dead = True
                                self.view.playMusic('victory')
                                self.boss_dead = True
                                self.level_finished = True

                            else:
                                self.score += 1
                                self.enemies_killed += 1

                                # add treasure/power-up
                                x = random.randrange(self.screenWidth-100)
                                if self.boss:
                                    r = random.randint(1,4)
                                else:
                                    r = random.randint(1,6)
                                if r == 1:
                                    self.powerups.append(Fireball(x,55, 41,40, 2, self.surfaceLevel))
                                elif r == 2:
                                    self.powerups.append(DamageX2(x,55, 41,40, 2, self.surfaceLevel))
                                elif r==3:
                                    if self.curr_level == 1:
                                        self.powerups.append(ShootBothWays(x,55, 41,40, 2, self.surfaceLevel))
                                    elif self.curr_level == 2 or self.curr_level == 3:
                                        self.powerups.append(ShootThreeWays(x,55, 41,40, 2, self.surfaceLevel))
                                else:
                                    self.powerups.append(Treasure(x,55, 41,40, 2, self.surfaceLevel))


                        # bug sometimes crashes so put in try/except
                        if projectile.remove():
                            try:
                                self.projectiles.pop(self.projectiles.index(projectile))
                            except:
                                pass


        self.view.redraw_game_window(self.curr_level, self.player, self.enemies, self.enemy_projectiles, self.platforms, \
                                            self.projectiles, self.powerups, self.score, self.boss_dead, self.difficulty)



    """
    Returns true if the two hitboxes overlap, otherwise returns false
    """
    def compareHitboxes(self, hitbox1, hitbox2):

        #bug
        if hitbox1 is None or hitbox2 is None:
            return False

        if  hitbox1[0] < hitbox2[0] + hitbox2[2] and \
                hitbox1[0] + hitbox1[2] > hitbox2[0] and \
                hitbox1[1] < hitbox2[1] + hitbox2[3] and \
                hitbox1[1] + hitbox1[3] > hitbox2[1]:
                return True
        else:
                return False


    """
    Adds a new enemy
    """
    def addNewEnemy(self, boss=False):

        while True:
            x = random.randrange(self.screenWidth-150)
            # don't add new enemies to close to the player
            if abs(self.player.x - x) > 220:
                break

        dir = random.randrange(2)
        if dir == 0:
            dir = -1

        # adding the boss
        if boss:
            if self.curr_level == 1:
                self.enemies.append(ZombieBoss(x,55,3,self.boss_life[self.difficulty],dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            elif self.curr_level == 2:
                self.enemies.append(FlyingEyeBoss(x,0,3,self.boss_life[self.difficulty],dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
            elif self.curr_level == 3:
                boss = FlyingEyeBoss2(x,0,3,self.boss_life[self.difficulty]//2,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes)
                if self.difficulty == 2:
                    boss.setHardLevel()
                self.enemies.append(boss)


        # adding normal enemies
        else:

            if self.curr_level == 1:
                enemy = random.randrange(2)
                if enemy == 0:
                    self.enemies.append(Zombie(x,55,6,8,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
                else:
                    self.enemies.append(Goblin(x,55,5,8,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))

            if self.curr_level == 2:
                enemy = random.randrange(3)
                if enemy == 0:
                    self.enemies.append(Mushroom (x,55,3,10,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
                elif enemy == 1:
                    self.enemies.append(FlyingEye (x,55,5,2,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
                else:
                    self.enemies.append(Zombie(x,55,5,8,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))

            if self.curr_level == 3:
                y  = random.randrange(50, self.screenHeight-100)
                self.enemies.append(FlyingEye (x,y,4,3,dir,self.screenWidth,  self.surfaceLevel, self.resourceHandler, self.hitboxes))
