import pygame


class Player():
    def __init__(self, screen):
        self.screen = screen
        self.position = (247, 258)
    
    def draw_player(self, images):
        # Load images
        self.image = pygame.image.load(
            r"images/hand"+str(images)+".png")
        # Draw hand in screen
        self.screen.blit(self.image, self.position)
        
        
class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.position = (247, 258)
    
    def draw_enemy(self, num_img):
        # Load images
        self.image = pygame.image.load(
            r"images/hand"+str(num_img)+".png")
        self.image = pygame.transform.rotate(self.image, 180)
        # Draw hand in screen
        self.screen.blit(self.image, self.position)