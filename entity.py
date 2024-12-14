class player:
    def __init__(self,x,y):
        self_x=x
        self_y=y
        self.image = pygame.image.load("player.png")
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
        
