from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
import random

def spawn_mob(listacoordenadas): #spawn de mobs aleatórios, com suas posições definidas pra fora do mapa
    listamob = [Sprite("png/zumbi.png"), Sprite("png/esqueleto.png"), Sprite("png/policial.png")]
    i = random.randint(0, 2)
    mob = listamob[i]
    coordenadas = random.choice(listacoordenadas)
    mob.set_position(coordenadas[0], coordenadas[1])
    return mob

def colision_tiro_mob(listamob, listatiro): #testa a colisão do tiro do player com os mobs
    pontostemp = 0
    if listamob != [] and listatiro != []:
        for m in listamob:
            for t in listatiro:
                if Collision.collided_perfect(m, t):
                    listamob.remove(m)
                    listatiro.remove(t)
                    pontostemp += 50
                if t.x > janela.width or t.x < 0:
                    listatiro.remove(t)
    return pontostemp

def mov_tiros(listatiros, velTiro):
    if listatiros != []:
        for t in listatiros:
            t.draw()
    if listatiros != []:
        for t in listatiros:
            t.move_x(velTiro * janela.delta_time())

janela = Window(1080, 720)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
fundo = GameImage("png/fundo_jogo_3.png")
janela.set_title("Vampiro Carioca")


player = Sprite("png/player.png")
player.set_position(460, 460)
vidas = 3
timerinvencivel = 0
timerpisca = 0
            
        
velplayer = 200
velmob = 50


matMob = []
timerMob = 0
timervelocidade = 0


matTirosEsq = []
matTirosDir = []
velTiro = 200
timerhit = 0
pontos = 0

listacoordenadas = [[-25, -25], [-25, janela.height/2], [-25, janela.height + 25], [janela.width/2, janela.height + 25],  
                    [janela.width + 25, -25], [janela.width + 25, janela.height/2], [janela.width + 25, janela.height + 25], 
                    [janela.width/2, - 25]]

while True:

    #CONTADORES
    timervelocidade += janela.delta_time()
    timerMob += janela.delta_time()
    timerhit += janela.delta_time()
    timerinvencivel += janela.delta_time()
    timerpisca += janela.delta_time()

    #INCREMENTADOR DE VELOCIDADE
    if timervelocidade > 20:
        velmob = velmob + 20
        timervelocidade = 0

    #MOVIMENTAÇÃO E SPAWN DOS TIROS
    if teclado.key_pressed("w"):
        if player.y - 1 > 0: 
            player.move_y(janela.delta_time() * -velplayer)
    if teclado.key_pressed("s"):
        if player.y + 1 < janela.height - player.height: 
            player.move_y(janela.delta_time() * velplayer)
    if teclado.key_pressed("a"):
        if player.x - 1 > 0: 
            player.move_x(janela.delta_time() * -velplayer)
    if teclado.key_pressed("d"):
        if player.x + 1 < janela.width - player.width: 
            player.move_x(janela.delta_time() * velplayer)
    if (teclado.key_pressed("space") or mouse.is_button_pressed(1)) and timerhit > 0.5:
            tiro = Sprite("png/tiro.png")
            tiro.set_position(player.x, player.y+player.height/2)
            if mouse.get_position()[0] > player.x:
            #if teclado.key_pressed("d"):
                tiro.set_position(player.x+player.width, player.y+player.height/2)
                matTirosDir.append(tiro)
            #elif teclado.key_pressed("a"):
            elif mouse.get_position()[0] < player.x:
                tiro.set_position(player.x, player.y+player.height/2)
                matTirosEsq.append(tiro)
            #else:
                #matTirosDir.append(tiro)
            timerhit = 0

    #SPAWN E MOVIMENTAÇÃO MOBS
    if timerMob > 1:
        matMob.append(spawn_mob(listacoordenadas))
        timerMob = 0

    if matMob != []:
        for z in matMob:
            z.draw()

    if matMob != []:
        for z in matMob:
            if z.x > player.x:
                z.move_x(janela.delta_time() * -velmob)
            else:
                z.move_x(janela.delta_time() * velmob)
            if z.y > player.y:
                z.move_y(janela.delta_time() * -velmob)
            else:
                z.move_y(janela.delta_time() * velmob)

    if matMob != []:
        for z in matMob:
            if Collision.collided_perfect(z, player) and timerinvencivel > 3:
                vidas -= 1
                timerinvencivel = 0

    #INVENCIBILIDADE
    if timerinvencivel < 3:
        if timerpisca < 0.2:
            player.draw()
        if timerpisca > 0.4:
            timerpisca = 0
    else:
        player.draw()

    if vidas == 0:
        exit()

    #MOVIMENTAÇÃO E COLISÃO DOS TIROS DO PLAYER
    mov_tiros(matTirosEsq, -velTiro)
    mov_tiros(matTirosDir, velTiro)
    pontos += colision_tiro_mob(matMob, matTirosEsq)
    pontos += colision_tiro_mob(matMob, matTirosDir)

    #DESENHA UMAS INFORMAÇÕES AÍ
    janela.draw_text(str(velmob) + " PIXEL/SEG",0,20,16,(255,255,255))
    janela.draw_text(str(pontos) + " PONTOS",0,40,16,(255,255,255))
    janela.draw_text(str(vidas) + " VIDAS",0,60,16,(255,255,255))

    janela.update()
    fundo.draw()
