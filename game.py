import pygame
from pygame.locals import *
from classes import linhas
from codigos.leitura import get_recorde, set_recorde

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.event.set_allowed([QUIT, KEYDOWN])

# Musica do jogo
pygame.mixer.music.load('arquivos/in_the_silent_darkness-126664.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
hit = pygame.mixer.Sound('arquivos/mixkit-electronic-retro-block-hit-2185.wav')

# Variaveis gerais
size = width, height = 480, 480
cinza = 105, 105, 105
amarelo = 255, 255, 0
branco = 255, 255, 255
preto = 0, 0, 0

relogio = pygame.time.Clock()
tela = pygame.display.set_mode(size)
pygame.display.set_caption('Dont Crash')
from classes import carro

# Fontes e textos exibidos na tela
fonte = pygame.font.SysFont('arial', 25, True, True)
fonte2 = pygame.font.SysFont('arial', 20, True, True)
game_over = fonte.render('Fim de Jogo', True, preto)
press_r = fonte2.render('Pressione r', True, preto)

# Geração do cenario
linha = pygame.rect.Rect((30, 0, 20, height))
linha2 = pygame.rect.Rect((width-50, 0, 20, height))
linhas_classe = linhas.Linhas()
linhas_sprites = linhas_classe.linhas
sprites = pygame.sprite.Group()

# Carro do personagem
personagem = carro.Carro(0)
personagem.rect.center = 240, 480-16
sprites.add(personagem)

# Sprite group dos carros inimigos
inimigos = carro.Inimigos(5)
inimigos_sprites = inimigos.grupo


def run():
    """Executa o jogo"""
    pontos = last = 0
    velocidade, velocidade_max = 7, 12
    v_inicial = velocidade
    crescimento = 0.002
    recorde = get_recorde()
    r_txt = fonte2.render(f'Recorde: {recorde}', True, preto)
    while 1:
        relogio.tick(30)
        tela.fill(cinza)
        pygame.draw.rect(tela, amarelo, linha)
        pygame.draw.rect(tela, amarelo, linha2)
        linhas_sprites.draw(tela)
        sprites.draw(tela)
        inimigos_sprites.draw(tela)

        p_texto = fonte2.render(f'Pontuação: {int(pontos)}', True, preto)
        tela.blit(p_texto, (0, 0))
        tela.blit(r_txt, (0, p_texto.get_height()))
        if velocidade == 0:
            tela.blit(game_over, ((width//2)-game_over.get_width()//2,
                                  (height//2)))
            tela.blit(press_r, ((width//2)-press_r.get_width()//2, (height//2)+game_over.get_height()))

        for e in pygame.event.get():
            if e.type == QUIT:
                # Sair do jogo
                pygame.quit()
                return 0
            elif e.type == KEYDOWN and velocidade != 0:
                # Movimentação do jogador
                if pygame.key.get_pressed()[K_d]:
                    personagem.rect.centerx += personagem.vel
                elif pygame.key.get_pressed()[K_a]:
                    personagem.rect.centerx -= personagem.vel
                # Limitação do carro na tela
                if personagem.rect.topleft[0] < 50:
                    personagem.rect.topleft = 50, personagem.rect.topleft[1]
                elif personagem.rect.topright[0] > 430:
                    personagem.rect.topright = 430, personagem.rect.topright[1]
            elif e.type == KEYDOWN and velocidade == 0:
                # Reinicia o jogo
                if pygame.key.get_pressed()[K_r]:
                    velocidade, pontos = v_inicial, 0
                    for sprite in inimigos_sprites.sprites():
                        sprite.rect.center = 240, 240
                pygame.mixer.music.play(-1)
                r_txt = fonte2.render(f'Recorde: {get_recorde()}', True, preto)
        if pygame.sprite.spritecollide(personagem, inimigos_sprites, False):
            # Game Over
            velocidade = 0
            pygame.mixer.music.stop()
            hit.play()
            set_recorde(int(pontos))

        linhas_classe.update(velocidade)
        inimigos.update(velocidade)
        if velocidade != 0:
            # Acelera o jogo
            velocidade = min(velocidade+crescimento, velocidade_max)
            pontos += velocidade/10
        if int(pontos) % 500 == 0 and int(pontos) != last:
            # Adiciona novos inimigos no jogo
            last = int(pontos)
            if len(inimigos.pos)-2 > len(inimigos.grupo):
                item = carro.Carro(1)
                item.rect.center = width//2, height//2
                inimigos.grupo.add(item)
        pygame.display.flip()
