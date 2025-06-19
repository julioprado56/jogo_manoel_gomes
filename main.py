import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone = pygame.image.load("assets/icone.png")
icone = pygame.transform.scale(icone, (64, 64))
manoel = pygame.image.load("assets/manoel.png")
manoel = pygame.transform.scale(manoel, (100, 100))
fundo = pygame.image.load("assets/fundo.png")
fundo = pygame.transform.scale(fundo, (1000, 700))
fundoStart = pygame.image.load("assets/fundoStart.png")
fundoStart = pygame.transform.scale(fundoStart, (1000, 700))
fundoDead = pygame.image.load("assets/fundoDead.png")
fundoDead = pygame.transform.scale(fundoDead, (1000, 700))
canetaPreta = pygame.image.load("assets/blackpen.png")
canetaPreta = pygame.transform.scale(canetaPreta, (200, 200))
nuvem_imagem = pygame.image.load("assets/nuvem.png")
nuvem_imagem = pygame.transform.scale(nuvem_imagem, (100, 50))
pen = pygame.image.load("assets/pen.png")
pen = pygame.transform.scale(pen, (150, 250))

tamanho = (1000, 700)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Blue pen game")
pygame.display.set_icon(icone)

pensound = pygame.mixer.Sound("assets/pensound.wav")
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
fonte = pygame.font.SysFont("comicsans", 28)
fonteStart = pygame.font.SysFont("comicsans", 55)
fonteMorte = pygame.font.SysFont("arial", 120)
pygame.mixer.music.load("assets/blueSound.mp3")

branco = (255, 255, 255)
preto = (0, 0, 0)
amarelo = (255, 255, 0)

def criar_nuvens():
    return [{"x": random.randint(0, 1000), "y": random.randint(0, 100), "vel": random.randint(1, 3)} for _ in range(5)]

def mover_nuvens(nuvens):
    for nuvem in nuvens:
        nuvem["x"] += nuvem["vel"]
        if nuvem["x"] > 1000:
            nuvem["x"] = -nuvem_imagem.get_width()

def desenhar_nuvens(tela, nuvens):
    for nuvem in nuvens:
        tela.blit(nuvem_imagem, (nuvem["x"], nuvem["y"]))

def jogar(nome):
    pygame.mixer.Sound.play(pensound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 450
    posicaoYPersona = 500
    movimentoXPersona = 0
    movimentoYPersona = 0
    posicaoXMissel = 450
    posicaoYMissel = -250
    velocidadeMissel = 2
    velocidadecaneta = 1
    posicaoYcaneta = -150
    posicaoXcaneta = 300
    larguraPersona = 100
    alturaPersona = 100
    larguracaneta = 150
    alturacaneta = 150
    larguaMissel = 100
    alturaMissel = 250
    pontos = 0
    pausado = False
    nuvens = criar_nuvens()
    raio_sol = 30
    crescimento = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    movimentoXPersona = 10
                elif evento.key == pygame.K_LEFT:
                    movimentoXPersona = -10
                elif evento.key == pygame.K_SPACE:
                    pausado = not pausado
            elif evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    movimentoXPersona = 0

        tela.fill(branco)
        tela.blit(fundo, (0, 0))
        desenhar_nuvens(tela, nuvens)
        mover_nuvens(nuvens)
        pygame.draw.circle(tela, amarelo, (950, 50), raio_sol)
        raio_sol += crescimento
        if raio_sol >= 35 or raio_sol <= 25:
            crescimento = -crescimento

        if not pausado:
            posicaoXPersona += movimentoXPersona
            if posicaoXPersona < 0:
                posicaoXPersona = 0
            elif posicaoXPersona > 900:
                posicaoXPersona = 900

            tela.blit(manoel, (posicaoXPersona, posicaoYPersona))

            posicaoYMissel += velocidadeMissel
            if posicaoYMissel > 700:
                posicaoYMissel = -250
                pontos += 1
                velocidadeMissel += 2
                posicaoXMissel = random.randint(0, 950)
                pygame.mixer.Sound.play(pensound)

            tela.blit(pen, (posicaoXMissel, posicaoYMissel))

            posicaoYcaneta += velocidadecaneta
            if posicaoYcaneta > 700:
                posicaoYcaneta = -150
                pontos += 1
                velocidadecaneta += 1
                posicaoXcaneta = random.randint(0, 950)
                pygame.mixer.Sound.play(pensound)

            tela.blit(canetaPreta, (posicaoXcaneta, posicaoYcaneta))

            texto = fonte.render(f"{nome} - Pontos: {pontos}", True, branco)
            tela.blit(texto, (10, 10))

            px = range(posicaoXPersona, posicaoXPersona + larguraPersona)
            py = range(posicaoYPersona, posicaoYPersona + alturaPersona)
            mx = range(posicaoXMissel, posicaoXMissel + larguaMissel)
            my = range(posicaoYMissel, posicaoYMissel + alturaMissel)
            cx = range(posicaoXcaneta, posicaoXcaneta + larguracaneta)
            cy = range(posicaoYcaneta, posicaoYcaneta + alturacaneta)

            if (set(px).intersection(mx) and set(py).intersection(my)) or (set(px).intersection(cx) and set(py).intersection(cy)):
                dead(nome, pontos)
        else:
            textoPausa = fonte.render("JOGO PAUSADO - Aperte ESPAÇO para continuar", True, amarelo)
            tela.blit(textoPausa, (200, 320))

        pygame.display.update()
        relogio.tick(60)

def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)

    jogadas = {}
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            jogadas = eval(arquivo.read())
    except:
        pass

    jogadas[nome] = pontos
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(str(jogadas))

    nomes_ordenados = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)

        tela.fill(branco)
        tela.blit(fundoDead, (0, 0))
        buttonStart = pygame.draw.rect(tela, preto, (125, 580, 750, 100), 0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400, 590))
        textoEnter = fonte.render("Pressione ENTER para continuar...", True, branco)
        tela.blit(textoEnter, (350, 660))

        textoPontuacao = fonteStart.render(f"{nome}: {pontos} pontos", True, amarelo)
        tela.blit(textoPontuacao, (300, 100))

        tela.blit(fonte.render("Ranking:", True, branco), (430, 160))
        posicaoY = 190
        for i, (jogador, score) in enumerate(nomes_ordenados[:5]):
            textoRanking = fonte.render(f"{i+1}. {jogador} - {score}", True, branco)
            tela.blit(textoRanking, (400, posicaoY))
            posicaoY += 30

        pygame.display.update()
        relogio.tick(60)

def start():
    nome = simpledialog.askstring("Manoel Gomes", "Nome Completo:")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)

        tela.fill(branco)
        tela.blit(fundoStart, (0, 0))
        buttonStart = pygame.draw.rect(tela, preto, (125, 580, 750, 100), 0)
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (450, 600))

        pygame.display.update()
        relogio.tick(60)

start()

'/mnt/data/blue_pen_game.py'