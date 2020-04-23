
import pygame


"""
Loads resources which are used several times
"""
class ResourceHandler():

    def __init__(self):

        self.zombie_width = 50
        self.zombie_height = 60

        self.zombie_idle_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/idle1.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle2.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle3.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle4.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle5.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle6.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle7.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle8.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle9.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle10.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle11.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle12.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle13.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle14.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/idle15.png'), (self.zombie_width, self.zombie_height))]

        self.zombie_walk_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/walk1.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk2.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk3.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk4.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk5.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk6.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk7.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk8.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk9.png'), (self.zombie_width, self.zombie_height)),
                                   pygame.transform.scale(pygame.image.load('resources/images/zombie/walk10.png'), (self.zombie_width, self.zombie_height))]


        self.zombie_dead_right = [  pygame.transform.scale(pygame.image.load('resources/images/zombie/dead1.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead2.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead3.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead4.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead5.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead6.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead7.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead8.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead9.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead10.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead11.png'), (self.zombie_width, self.zombie_height)),
                                    pygame.transform.scale(pygame.image.load('resources/images/zombie/dead12.png'), (self.zombie_width, self.zombie_height))]


        self.zombie_boss_width = 100
        self.zombie_boss_height = 120

        self.zombie_boss_idle_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/idle1.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle2.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle3.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle4.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle5.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle6.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle7.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle8.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle9.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle10.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle11.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle12.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle13.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle14.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/idle15.png'), (self.zombie_boss_width, self.zombie_boss_height))]

        self.zombie_boss_walk_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/walk1.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk2.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk3.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk4.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk5.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk6.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk7.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk8.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk9.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/walk10.png'), (self.zombie_boss_width, self.zombie_boss_height))]

        self.zombie_boss_dead_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/dead1.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead2.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead3.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead4.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead7.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead5.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead6.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead8.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead9.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead10.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead11.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                        pygame.transform.scale(pygame.image.load('resources/images/zombie/dead12.png'), (self.zombie_boss_width, self.zombie_boss_height))]

        self.zombie_boss_attack_right = [ pygame.transform.scale(pygame.image.load('resources/images/zombie/attack1.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack2.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack3.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack4.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack7.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack5.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack6.png'), (self.zombie_boss_width, self.zombie_boss_height)),
                                          pygame.transform.scale(pygame.image.load('resources/images/zombie/attack8.png'), (self.zombie_boss_width, self.zombie_boss_height))]


        self.flying_eye_flight_right = pygame.image.load('resources/images/FlyingEye/Flight.png').convert_alpha()
        self.flying_eye_flight_right = pygame.transform.scale(self.flying_eye_flight_right, (1800,225))
        self.flying_eye_flight_left = pygame.transform.flip(self.flying_eye_flight_right, True, False)
        self.flying_eye_death_right = pygame.image.load('resources/images/FlyingEye/Death.png').convert_alpha()
        self.flying_eye_death_right = pygame.transform.scale(self.flying_eye_death_right, (900,225))
        self.flying_eye_death_left = pygame.transform.flip(self.flying_eye_death_right, True, False)

        self.flying_eye_boss_flight_right = pygame.image.load('resources/images/FlyingEye/Flight.png').convert_alpha()
        self.flying_eye_boss_flight_right = pygame.transform.scale(self.flying_eye_boss_flight_right, (3600,450))
        self.flying_eye_boss_flight_left = pygame.transform.flip(self.flying_eye_boss_flight_right, True, False)
        self.flying_eye_boss_death_right = pygame.image.load('resources/images/FlyingEye/Death.png').convert_alpha()
        self.flying_eye_boss_death_right = pygame.transform.scale(self.flying_eye_boss_death_right, (1800,450))
        self.flying_eye_boss_death_left = pygame.transform.flip(self.flying_eye_boss_death_right, True, False)
        self.flying_eye_boss_attack_right = pygame.image.load('resources/images/FlyingEye/Attack2.png').convert_alpha()
        self.flying_eye_boss_attack_right = pygame.transform.scale(self.flying_eye_boss_attack_right, (3600,450))
        self.flying_eye_boss_attack_left = pygame.transform.flip(self.flying_eye_boss_attack_right, True, False)



        self.mushroom_idle_right = pygame.image.load('resources/images/Mushroom/Idle.png').convert_alpha()
        self.mushroom_idle_right = pygame.transform.scale(self.mushroom_idle_right, (900,225))
        self.mushroom_idle_left = pygame.transform.flip(self.mushroom_idle_right, True, False)
        self.mushroom_walk_right = pygame.image.load('resources/images/Mushroom/Run.png').convert_alpha()
        self.mushroom_walk_right = pygame.transform.scale(self.mushroom_walk_right, (1800,225))
        self.mushroom_walk_left = pygame.transform.flip(self.mushroom_walk_right, True, False)
        self.mushroom_death_right =  pygame.image.load('resources/images/Mushroom/Death.png').convert_alpha()
        self.mushroom_death_right = pygame.transform.scale(self.mushroom_death_right, (900,225))
        self.mushroom_death_left = pygame.transform.flip(self.mushroom_death_right, True, False)
        self.mushroom_attack_right = pygame.image.load('resources/images/Mushroom/Attack.png').convert_alpha()
        self.mushroom_attack_right = pygame.transform.scale(self.mushroom_attack_right, (1800,225))
        self.mushroom_attack_left = pygame.transform.flip(self.mushroom_attack_right, True, False)

        self.mushroom_boss_idle_right = pygame.image.load('resources/images/Mushroom/Idle.png').convert_alpha()
        self.mushroom_boss_idle_right = pygame.transform.scale(self.mushroom_boss_idle_right, (1200,300))
        self.mushroom_boss_idle_left = pygame.transform.flip(self.mushroom_boss_idle_right, True, False)
        self.mushroom_boss_walk_right = pygame.image.load('resources/images/Mushroom/Run.png').convert_alpha()
        self.mushroom_boss_death_right =  pygame.image.load('resources/images/Mushroom/Death.png').convert_alpha()
        self.mushroom_boss_death_right = pygame.transform.scale(self.mushroom_boss_death_right, (1200,300))
        self.mushroom_boss_death_left = pygame.transform.flip(self.mushroom_boss_death_right, True, False)
        self.mushroom_boss_attack_right = pygame.image.load('resources/images/Mushroom/Attack.png').convert_alpha()
        self.mushroom_boss_attack_right = pygame.transform.scale(self.mushroom_boss_attack_right, (2400,300))
        self.mushroom_boss_attack_left = pygame.transform.flip(self.mushroom_boss_attack_right, True, False)
        self.mushroom_boss_attack2_right = pygame.image.load('resources/images/Mushroom/take_hit.png').convert_alpha()
        self.mushroom_boss_attack2_right = pygame.transform.scale(self.mushroom_boss_attack_right, (1200,300))
        self.mushroom_boss_attack2_left = pygame.transform.flip(self.mushroom_boss_attack_right, True, False)


        self.goblin_idle_right = pygame.image.load('resources/images/Goblin/Idle.png')
        self.goblin_idle_right = pygame.transform.scale(self.goblin_idle_right, (900,225))
        self.goblin_idle_left = pygame.transform.flip(self.goblin_idle_right, True, False)
        self.goblin_walk_right = pygame.image.load('resources/images/Goblin/Run.png')
        self.goblin_walk_right = pygame.transform.scale(self.goblin_walk_right, (1800,225))
        self.goblin_walk_left = pygame.transform.flip(self.goblin_walk_right, True, False)
        self.goblin_death_right =  pygame.image.load('resources/images/Goblin/Death.png').convert_alpha()
        self.goblin_death_right = pygame.transform.scale(self.goblin_death_right, (900,225))
        self.goblin_death_left = pygame.transform.flip(self.goblin_death_right, True, False)
        self.goblin_attack_right = pygame.image.load('resources/images/Goblin/Attack.png').convert_alpha()
        self.goblin_attack_right = pygame.transform.scale(self.goblin_attack_right, (1800,225))
        self.goblin_attack_left = pygame.transform.flip(self.goblin_attack_right, True, False)

        self.fireball_projectile    = pygame.image.load('resources/images/projectiles/fireball_projectile.png').convert_alpha()
        self.sunburn_projectile     = pygame.image.load('resources/images/projectiles/sunburn_projectile.png').convert_alpha()
        self.sunburn_projectile     = pygame.transform.scale(self.sunburn_projectile, (400,400))
        self.vortex_projectile      = pygame.image.load('resources/images/projectiles/vortex_projectile.png').convert_alpha()
        self.vortex_projectile      = pygame.transform.scale(self.vortex_projectile, (600,600))
        self.felspell_projectile    = pygame.image.load('resources/images/projectiles/felspell_projectile.png').convert_alpha()
        self.felspell_projectile    = pygame.transform.scale(self.felspell_projectile, (750,750))
        self.freezing_projectile    = pygame.image.load('resources/images/projectiles/freezing_projectile.png').convert_alpha()
        self.freezing_projectile    = pygame.transform.scale(self.freezing_projectile, (500,500))
