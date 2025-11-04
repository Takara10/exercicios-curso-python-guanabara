# 1. Importa a biblioteca
import pygame

# 2. Inicia o pygame
pygame.init()

# 3. Carrega o arquivo de música
#    (O pygame vai procurar por 'musica.mp3' na mesma pasta do seu script)
pygame.mixer.music.load('musica.mp3')

# 4. Dá o "play" na música
pygame.mixer.music.play()

# 5. Mantém o programa rodando enquanto a música toca
#    O input() aqui serve para o programa não fechar imediatamente.
#    Pressione ENTER quando quiser parar.
input('Pressione ENTER para parar a música...')
