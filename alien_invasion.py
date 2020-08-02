# pg315_Projeto_1_Espaçonave_que_atira
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()

    # Tela do jogo
    #screen = pygame.display.set_mode((500, 500))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    # Titulo do jogo
    pygame.display.set_caption('Alien Invasion')

    
    # Cria espaçonave
    ship = Ship(screen)


    # define a cor de fundo
    #bg_color = (230, 230, 230)

    # inicializa o laço principal do jogo
    while True:
        # Obeserva os eventos do mouse e teclado
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
        
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Deixa a tela mais recente possivel
        pygame.display.flip()

run_game()
