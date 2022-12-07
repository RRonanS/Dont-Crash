import pygame.sprite

branco = 255, 255, 255


class Linha(pygame.sprite.Sprite):
    """Sprite de uma linha branca"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surf = pygame.surface.Surface((15, 25))
        surf.fill(branco)
        self.image = surf
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = 240, 240


class Linhas:
    """Armazena as linhas utilizadas no jogo"""
    def __init__(self):
        espacamento = 15
        self.linhas = pygame.sprite.Group()
        for i in range(40, 520, espacamento+25):
            item = Linha()
            item.rect.centery = i
            self.linhas.add(item)

    def update(self, vel):
        """Move as linhas na tela"""
        for sprite in self.linhas.sprites():
            sprite.rect.centery += vel
            if sprite.rect.topleft[1] >= 480:
                sprite.rect.centery = 0
