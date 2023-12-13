from PPlay.window import *
from PPlay.sprite import *
from Play import *

telanum = 0 #VARIÁVEL DE CONTROLE DE QUAL JANELA ESTÁ ABERTA
janela = Window(1080, 720)
janela.set_title("Space Invaders")
janela.set_background_color((255, 255, 255))
cursor = Window.get_mouse() #ATIVAR MOUSE
teclado = Window.get_keyboard() #ATIVAR TECLADO


def load():
    ranking = open("ranking.txt", "r")
    listaranking = ranking.readlines()
    for i in range(0, len(listaranking)):
        listaranking[i] = listaranking[i].split()
    return listaranking

def adiciona(nome, pontos):
    res = ""
    listaranking = load()
    listaranking.append([nome, str(pontos)])
    ranking = open("ranking.txt", "w")
    for i in range(0, len(listaranking)):
        for j in range(0, len(listaranking)):
            if int(listaranking[i][1]) > int(listaranking[j][1]):
                res=listaranking[i]
                listaranking[i] = listaranking[j]
                listaranking[j] = res
    for i in range(0, len(listaranking)):
        listaranking[i] = str(listaranking[i][0]) + " " + str(listaranking[i][1]) + "\n"
    ranking.writelines(listaranking)
    ranking.close()

def tela_inicial(cursor, telanum):
    jogar = Sprite("png/jogar.png")
    dificuldade = Sprite("png/dificuldade.png")
    ranking = Sprite("png/ranking.png")
    sair = Sprite("png/sair.png")
    jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
    dificuldade.set_position(janela.width/2-jogar.width/2, 2 * janela.height/6)
    ranking.set_position(janela.width/2-jogar.width/2, 3 * janela.height/6)
    sair.set_position(janela.width/2-jogar.width/2, 4 * janela.height/6)
    janela.set_background_color((255, 255, 255))
    while True:
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()

        #TROCA DE SPRITE DO BOTÃO JOGAR DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, janela.height/6], [janela.width/2+jogar.width/2, janela.height/6+jogar.height]):
            jogar = Sprite("png/jogar-2.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                gameplay(1)
        else:
            jogar = Sprite("png/jogar.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)

        #TROCA DE SPRITE DO BOTÃO JOGAR DIFICULDADE DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 2*janela.height/6], [janela.width/2+jogar.width/2, 2*janela.height/6+jogar.height]):
            dificuldade = Sprite("png/dificuldade-2.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                tela_dificuldade(cursor, telanum)
        else:
            dificuldade = Sprite("png/dificuldade.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6) 

        #TROCA DE SPRITE DO BOTÃO RANKING DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 3*janela.height/6], [janela.width/2+jogar.width/2, 3*janela.height/6+jogar.height]):
            ranking = Sprite("png/ranking-2.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                tela_ranking()
        else:
            ranking = Sprite("png/ranking.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)

       #TROCA DE SPRITE DO BOTÃO SAIR DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 4*janela.height/6], [janela.width/2+jogar.width/2, 4*janela.height/6+jogar.height]):
            sair = Sprite("png/sair-2.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6)
            if cursor.is_button_pressed(1):
                exit()
        else:
            sair = Sprite("png/sair.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6)
        janela.update()

def tela_dificuldade(cursor, telanum):
    facil = Sprite("png/facil.png")
    medio = Sprite("png/medio.png")
    dificil = Sprite("png/dificil.png")
    facil.set_position(janela.width/2-facil.width/2, janela.height/6)
    medio.set_position(janela.width/2-medio.width/2, 3 * janela.height/6)
    dificil.set_position(janela.width/2-dificil.width/2, 5 * janela.height/6)
    janela.set_background_color((255, 255, 255))
    while True:
        facil.draw()
        medio.draw()
        dificil.draw()

        if teclado.key_pressed("esc"):
            tela_inicial(cursor, telanum)

        #TROCA DE SPRITE DO BOTÃO FÁCIL DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-facil.width/2, janela.height/6], [janela.width/2+facil.width/2, janela.height/6+facil.height]):
            facil = Sprite("png/facil-2.png")
            facil.set_position(janela.width/2-facil.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                gameplay(1)
        else:
            facil = Sprite("png/facil.png")
            facil.set_position(janela.width/2-facil.width/2, janela.height/6)

        #TROCA DE SPRITE DO BOTÃO MÉDIO DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-medio.width/2, 3*janela.height/6], [janela.width/2+medio.width/2, 3*janela.height/6+medio.height]):
            medio = Sprite("png/medio-2.png")
            medio.set_position(janela.width/2-medio.width/2, 3*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                gameplay(2)
        else:
            medio = Sprite("png/medio.png")
            medio.set_position(janela.width/2-medio.width/2, 3*janela.height/6)

        #TROCA DO BOTÃO DIFÍCIL DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-dificil.width/2, 5*janela.height/6], [janela.width/2+dificil.width/2, 5*janela.height/6+dificil.height]):
            dificil = Sprite("png/dificil-2.png")
            dificil.set_position(janela.width/2-dificil.width/2, 5*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                gameplay(3)
        else:
            dificil = Sprite("png/dificil.png")
            dificil.set_position(janela.width/2-dificil.width/2, 5*janela.height/6)
        janela.update()

def tela_ranking():
    janela.clear()
    lista = load()
    while True:
        janela.set_background_color((255, 255, 255))
        if teclado.key_pressed("esc"):
                tela_inicial(cursor, telanum)
        if len(lista) < 5:
            for i in range(0, len(lista)):
                janela.draw_text(lista[i][0][0:3:].upper() + "  " + lista[i][1], janela.width/2-120,150 + 80*i,50,(0,0,0))
        else:
            for i in range(0, 5):
                janela.draw_text(lista[i][0][0:3:].upper() + "  " + lista[i][1], janela.width/2-120,150 + 80*i,50,(0,0,0))
        janela.update()
