import pygame.sprite
from random import randint

# Carregamento das sprites dos carros
pngs = pygame.image.load('arquivos/cars.png')
lista = [pygame.transform.scale(pngs.subsurface((0, 0, 16, 31)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((18, 0, 21, 32)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((42, 0, 20, 32)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((62, 0, 20, 32)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((82, 0, 20, 32)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((107, 0, 22, 36)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((132, 0, 17, 35)).convert_alpha(), (32, 32)),
         pygame.transform.scale(pngs.subsurface((157, 0, 18, 33)).convert_alpha(), (32, 32))]


class Carro(pygame.sprite.Sprite):
    """Sprite do carro, sem update"""
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = lista[id]
        self.vel = 30
        self.rect = self.image.get_rect()

    def flip(self):
        """Gira a imagem em 180 graus"""
        self.image = pygame.transform.flip(self.image, False, True)


class Inimigos:
    """Classe para gerar e armazenar diversos carrosr"""
    def __init__(self, num):
        self.pos = {x: True for x in range(50, 430, 32)}
        self.poskeys = [x for x in self.pos.keys()]
        self.grupo = pygame.sprite.Group()
        for i in range(num):
            item = Carro(randint(1, len(lista)-1))
            item.flip()
            item.rect.center = 240, 240
            self.grupo.add(item)

    def update(self, vel):
        """Faz com que os carros se movam pelo jogo"""
        for sprite in self.grupo.sprites():
            sprite.rect.centery += vel
            if sprite.rect.topleft[1] >= 480:
                while True:
                    x = randint(0, len(self.poskeys)-1)
                    if self.poskeys[x] in self.pos:
                        if self.pos[self.poskeys[x]]:
                            self.pos[self.poskeys[x]] = False
                            break
                if sprite.rect.centerx in self.pos:
                    self.pos[sprite.rect.centerx] = True
                item = Carro(randint(1, len(lista)-1))
                item.flip()
                sprite.kill()
                sprite = item
                sprite.rect.centerx = self.poskeys[x]
                sprite.rect.centery = -randint(0, 4)*5
                self.grupo.add(sprite)
