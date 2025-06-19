 # Desenvolvedor
Nome: Julio Cesar de Almeida Prado 
RA: 1137708

# Descrição do Jogo
  É um jogo em Python com interface gráfica, onde o jogador controla o personagem Manoel Gomes e precisa desviar de objetos (canetas voadoras e mísseis) para acumular pontos. O jogo possui um sistema de ranking baseado em pontuação e uma interface gráfica interativa com animações, som ambiente e efeitos sonoros.

# Bibliotecas Utilizadas
Pygame
Responsável por toda a renderização gráfica, reprodução de sons, controle de eventos do teclado/mouse e lógica principal do jogo.
Funções utilizadas:
pygame.init, pygame.display, pygame.mixer, pygame.font, pygame.event, entre outras.
Recursos gráficos e de som: imagens, músicas de fundo e efeitos sonoros.
random
Utilizada para gerar posições aleatórias dos objetos (como nuvens, mísseis e canetas pretas) no jogo.
os
Incluída no código, mas não está sendo usada ativamente no main.py. Pode ser removida se não houver uso futuro.
tkinter.simpledialog
Utilizada para abrir uma caixa de diálogo para o jogador inserir seu nome antes de iniciar o jogo.
cx_Freeze (em setup.py)
Utilizada para empacotar e criar executáveis do jogo. O setup especifica a inclusão dos pacotes necessários (pygame) e da pasta de recursos (recursos), como imagens e sons.

# Tecnologias Utilizadas
Python 3.13 (compatível com Python 3.11)
pygame
pyttsx3 (síntese de voz)
Speech_recognition (reconhecimento de voz)
json (armazenamento de dados)
datetime (registro de dados/hora)
cx_Freeze (empacotamento para continuação)
Git (controle de versão)
# Funcionalidades
Tela de menu com som de comunicação
Entrada do nome do jogador via teclado
Comando de voz para iniciar (diga "jogar" após iniciar TAB)
Voz personalizada com o nome do jogador
Sistema de pontuação com log em log.dat
Dificuldade progressiva
Elementos decorativos: sol pulsante e caça
Tecla uasada para pausar o jogo
Efeitos sonoros de mísseis, explosão e comunicação
Tela de Game Over com exibição dos últimos registros

# Observações
Para executar no Windows:
Utilize python main.py (com Python 3.11+ e bibliotecas instaladas);