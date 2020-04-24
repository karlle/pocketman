import pygame

class View():

    def __init__(self, screenWidth, screenHeight):
        self.screenWidth  = screenWidth
        self.screenHeight = screenHeight

        # create the window in which we draw the game
        self.win = pygame.display.set_mode((screenWidth,screenHeight))

        self.backgrounds = []
        background_hills = pygame.image.load('resources/images/backgrounds/background_hills.png').convert_alpha()
        background_hills = pygame.transform.scale(background_hills,
                            (self.screenWidth, self.screenHeight))
        self.backgrounds.append(background_hills)

        background_forest = pygame.image.load('resources/images/backgrounds/background_forest.png').convert_alpha()
        background_forest = pygame.transform.scale(background_forest,
                            (self.screenWidth, self.screenHeight))
        self.backgrounds.append(background_forest)

        background_mountains = pygame.image.load('resources/images/backgrounds/background_mountains.png').convert_alpha()
        background_mountains = pygame.transform.scale(background_mountains,
                            (self.screenWidth, self.screenHeight))
        self.backgrounds.append(background_mountains)

        self.standing_player = pygame.image.load('resources/images/player/standing.png').convert_alpha()

        pygame.init()
        pygame.display.set_caption('POCKET MAN')



    """
    Plays different pieces of music based on the argument string
    """
    def playMusic(self, sound):

        if sound == 'start_screen':
            music = pygame.mixer.music.load('resources/sounds/start_screen_music.mp3')
            # play music in a loop
            pygame.mixer.music.play(-1 )

        if sound == 'level1':
            pygame.mixer.music.load('resources/sounds/music2.mp3')
            pygame.mixer.music.play(-1 )
        elif sound == 'level2':
            pygame.mixer.music.load('resources/sounds/forest_theme.mp3')
            pygame.mixer.music.play(-1)
        elif sound == 'level3':
            pygame.mixer.music.load('resources/sounds/mountain_theme.mp3')
            pygame.mixer.music.play(-1)

        elif sound == 'bossmusic1':
            pygame.mixer.music.load('resources/sounds/boss_music.mp3')
            pygame.mixer.music.play(-1)
        elif sound == 'bossmusic2':
            pygame.mixer.music.load('resources/sounds/boss_music2.mp3')
            pygame.mixer.music.play(-1)

        elif sound == 'victory':
            pygame.mixer.music.load('resources/sounds/victory.mp3')
            pygame.mixer.music.play()

        elif sound == 'end_music':
            pygame.mixer.music.load('resources/sounds/end_music.mp3')
            pygame.mixer.music.play(-1)

        elif sound == 'game_over':
            music = pygame.mixer.music.load('resources/sounds/game_over.mp3')
            pygame.mixer.music.play(-1 )


    """
    Draws the start screen
    """
    def startScreen(self, difficulty):
        self.win.blit(self.backgrounds[0],(0,0))
        font = pygame.font.SysFont('comicsans', 110)
        text = font.render('POCKET MAN', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 80))

        if difficulty == 0:
            font = pygame.font.SysFont('comicsans', 45)
            pygame.font.Font.set_underline(font, True)
            text = font.render('Easy', 50, (255,60,60))
        else:
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render('Easy', 1, (255,60,60))


        self.win.blit(text, (self.screenWidth/3-(text.get_width()/2), 200))

        if difficulty == 1:
            font = pygame.font.SysFont('comicsans', 55)
            pygame.font.Font.set_underline(font, True)
            text = font.render('Normal', 1, (255,60,60))
        else:
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render('Normal', 1, (255,60,60))


        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 200))

        if difficulty == 2:
            font = pygame.font.SysFont('comicsans', 45)
            pygame.font.Font.set_underline(font, True)
            text = font.render('Hard', 1, (255,60,60))
        else:
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render('Hard', 1, (255,60,60))


        self.win.blit(text, (self.screenWidth*2/3-(text.get_width()/2), 200))


        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Press ENTER to play!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 290))
        self.win.blit(self.standing_player, (500,400))
        pygame.display.update()


    """
    Draws the instruction screen
    """
    def instructionScreen(self):
        self.win.blit(self.backgrounds[0],(0,0))
        font = pygame.font.SysFont('comicsans', 90)
        text = font.render('How to play', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 20))

        font = pygame.font.SysFont('comicsans', 45)

        #self.win.blit(self.keys_instruction, (285,115))
        #self.win.blit(self.keys_instruction, (335,115))
        text = font.render('left, right', 1, (255,0,0))
        self.win.blit(text, (232, 120))
        text = font.render('-   move', 1, (255,0,0))
        self.win.blit(text, (389, 120))


        #self.win.blit(self.keys_instruction, (335,190))
        text = font.render('up', 1, (255,0,0))
        self.win.blit(text, (330, 195))
        text = font.render('-   jump', 1, (255,0,0))
        self.win.blit(text, (389, 195))

        #self.win.blit(self.fire_instruction, (335,265))
        text = font.render('spacebar', 1, (255,0,0))
        self.win.blit(text, (229, 270))
        text = font.render('-   fire weapon', 1, (255,0,0))
        self.win.blit(text, (389, 270))


        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Press ENTER to start first level!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 350))
        self.win.blit(self.standing_player, (500,400))
        pygame.display.update()



    """
    Draws the game over screen
    """
    def gameOver(self, level, high_scores, difficulty, high_score_name = None, high_score_index = None):

        self.win.blit(self.backgrounds[level-1],(0,0))

        font = pygame.font.SysFont('comicsans', 58)

        if high_score_index is None:
            text = font.render('Press ENTER to go to start screen!', 1, (255,0,0))
        elif len(high_score_name) == 3:
            text = font.render('Press ENTER to save score!', 1, (255,0,0))
        else:
            text = font.render('New high score! Type your name!', 1, (255,0,0))

        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 375))
        self.highScoreBoard(high_scores,high_score_name, high_score_index, difficulty)
        pygame.display.update()


    """
    Draws the high score board on the game over screen
    """
    def highScoreBoard(self, high_scores, high_score_name, high_score_index, difficulty):

        y = 50

        font = pygame.font.SysFont('comicsans', 62)
        difficulties = ['Easy','Medium','Hard']
        text = font.render('High Score - ' + str(difficulties[difficulty]), 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), y))

        y += 70

        for (i,(score,name)) in enumerate(high_scores):
            font = pygame.font.SysFont('comicsans', 42)
            text = font.render(str(i+1) + '. ' + str(score), 1, (255,0,0))
            self.win.blit(text, (self.screenWidth/2-90, y))

            # is this a new high score?
            if high_score_index is not None and high_score_index == i:
                name = []
                for i in range(3):
                    if len(high_score_name) > i:
                        name.append(high_score_name[i])
                    else:
                        name.append('_')

                if len(high_score_name) == 3:
                    name = "".join(name)
                else:
                    name = " ".join(name)

            name = name.upper()
            text = font.render(name, 1, (255,0,0))
            self.win.blit(text, (self.screenWidth/2 + 40, y))
            y += 45

    """
    Add the text paused on the screen
    """
    def paus(self):
        font = pygame.font.SysFont('comicsans', 75)
        text = font.render('Paused', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 80))
        pygame.display.update()


    """
    Adds finished level text on screen
    """
    def finishedLevel(self):
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Level Finished!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 80))
        font = pygame.font.SysFont('comicsans', 45)
        text = font.render('Press ENTER to start next level!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 150))


    """
    Adds finished game text on screen
    """
    def finishedGame(self):
        font = pygame.font.SysFont('comicsans', 75)
        text = font.render('You beat the game!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 80))
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Press ENTER to continue!', 1, (255,0,0))
        self.win.blit(text, (self.screenWidth/2-(text.get_width()/2), 150))


    """
    Updated the screen, which it done in every frame while playing a level
    """
    def redraw_game_window(self, level, player, enemies, enemy_projectiles, platforms,
            bullets, treasures, score, finished_level, difficulty):

        self.win.blit(self.backgrounds[level-1],(0,0))
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(score), 1, (255,0,0))
        self.win.blit(text, (10,10))

        for platform in platforms:
            platform.draw(self.win)
        for treasure in treasures:
            treasure.draw(self.win)
        for enemy in enemies:
            enemy.draw(self.win)
        for bullet in bullets:
            bullet.draw(self.win)

        player.draw(self.win)

        for projectile in enemy_projectiles:
            projectile.draw(self.win)

        if finished_level:
            if level == 3:
                self.finishedGame()
            else:
                self.finishedLevel()

        pygame.display.update()
