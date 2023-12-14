from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
import random

def gameplay(difficulty, start):
    def scrolling(bg_bottome, bg_bottomd, bg_tope, bg_topd, roll_speed, teclado):
        # Movimenta ambos os Sprites verticalmente 
        if teclado.key_pressed("s"):
            bg_bottome.y -= roll_speed * janela.delta_time()
            bg_bottomd.y -= roll_speed * janela.delta_time()
            bg_tope.y -= roll_speed * janela.delta_time()
            bg_topd.y -= roll_speed * janela.delta_time()
            

        if teclado.key_pressed("w"):
            bg_bottome.y += roll_speed * janela.delta_time()
            bg_bottomd.y += roll_speed * janela.delta_time()
            bg_tope.y += roll_speed * janela.delta_time()
            bg_topd.y += roll_speed * janela.delta_time()
            

        # Movimenta ambos os Sprites verticalmente 
        if teclado.key_pressed("d"):
            bg_bottome.x -= roll_speed * janela.delta_time()
            bg_bottomd.x -= roll_speed * janela.delta_time()
            bg_tope.x -= roll_speed * janela.delta_time()
            bg_topd.x -= roll_speed * janela.delta_time()


        if teclado.key_pressed("a"):
            bg_bottomd.x += roll_speed * janela.delta_time()
            bg_bottome.x += roll_speed * janela.delta_time()
            bg_topd.x += roll_speed * janela.delta_time()
            bg_tope.x += roll_speed * janela.delta_time()
            
    
        # Se a imagem do topo já tiver sido completamente exibida,
        # retorna ambas imagens às suas posições iniciais
        if bg_tope.y >= 0 or bg_topd.y >= 0:
            bg_bottome.y = 0
            bg_bottomd.y = 0
            bg_tope.y = -bg_tope.height
            bg_topd.y = -bg_topd.height
    
        if bg_bottome.y < 0 or bg_bottomd.y < 0:
            bg_bottome.y = bg_bottome.height
            bg_bottomd.y = bg_bottomd.height
            bg_tope.y = 0
            bg_topd.y = 0


        if bg_bottome.x >= 0 or bg_tope.x >= 0:
            bg_bottome.x = -bg_bottome.width
            bg_tope.x = -bg_tope.width
            bg_bottomd.x = 0
            bg_topd.x = 0
    
        if bg_topd.x < 0 or bg_bottomd.x < 0:
            bg_tope.x = 0
            bg_bottome.x = 0
            bg_topd.x = bg_topd.width
            bg_bottomd.x = bg_bottomd.width
    
        # Renderiza as duas imagens de fundo
        bg_bottome.draw()
        bg_bottomd.draw()
        bg_tope.draw()
        bg_topd.draw()

    def load():
        ranking = open("ranking.txt", "r")
        listaranking = ranking.readlines()
        for i in range(0, len(listaranking)):
            listaranking[i] = listaranking[i].split()
        return listaranking

    def adiciona(nome, pontos, tempo):
        res = ""
        listaranking = load()
        listaranking.append([nome, pontos, tempo])
        ranking = open("ranking.txt", "w")
        for i in range(0, len(listaranking)):
            for j in range(0, len(listaranking)):
                if int(listaranking[i][1]) > int(listaranking[j][1]):
                    res=listaranking[i]
                    listaranking[i] = listaranking[j]
                    listaranking[j] = res
        for i in range(0, len(listaranking)):
            listaranking[i] = str(listaranking[i][0]) + " " + str(listaranking[i][1]) + " " + "{}:{}".format(int(listaranking[i][2]//60), int(listaranking[i][2]%60)) + "\n"
        ranking.writelines(listaranking)
        ranking.close()

    def spawn_mob(listacoordenadas): #spawn de mobs aleatórios, com suas posições definidas pra fora do mapa
        #listamob = [Sprite("png/zumbiframes.png", 2), Sprite("png/esqueletoframes.png", 2), Sprite("png/policialframes.png", 2)]
        listamob = [Sprite("png/zumbiframes.png", 2), Sprite("png/esqueletoframes.png", 2), Sprite("png/policialframes.png", 2)]
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
                    if Collision.collided(m, t):
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
    janela.set_title("Vampiro Carioca")
    telanum = 0
    fundo = GameImage("png/fundo_jogo_4.png")

    fundoBAIXOE = GameImage("png/fundo_jogo_4.png")
    fundoBAIXOD = GameImage("png/fundo_jogo_4.png")
    fundoTOPOE = GameImage("png/fundo_jogo_4.png")
    fundoTOPOD = GameImage("png/fundo_jogo_4.png")
  
    fundoBAIXOE.y = 0
    fundoBAIXOD.y = 0
    fundoTOPOE.y = - fundoTOPOE.height
    fundoTOPOD.y = - fundoTOPOD.height

    fundoBAIXOE.x = 0
    fundoBAIXOD.x = - fundoBAIXOD.width
    fundoTOPOE.x = 0
    fundoTOPOD.x = - fundoBAIXOE.width

    player = Sprite("png/playerframes.png", 2)
    player.set_sequence(0, 1, False) #direita
    player.set_total_duration(500)
    player.set_position(janela.width/2 - player.width/2, janela.height/2-player.height/2)
    vidas = 3
    timerinvencivel = 0
    timerpisca = 0

    moeda = Sprite("png/moeda.png")
    moedaspawn = False
    timermsg = 10
    sorteio = 0
                
    velplayer = 150
    velmob = 50 + 2.50*difficulty
    cooldown_shot = 0.6 + difficulty/10


    matMob = []
    timerMob = 0
    timervelocidade = 0
    timermoeda = 0
    timermeta = 300


    matTirosEsq = []
    matTirosDir = []
    velTiro = 150+30/difficulty
    timerhit = 0
    pontos = 0

    listacoordenadas = [[-25, -25], [-25, janela.height/2], [-25, janela.height + 25], [janela.width/2, janela.height + 25],  
                        [janela.width + 25, -25], [janela.width + 25, janela.height/2], [janela.width + 25, janela.height + 25], 
                        [janela.width/2, - 25]]

    while True:

        if start == 1:
            timervelocidade = 0
            timermoeda = 0
            timerMob = 0
            timerhit = 0
            timerinvencivel = 0
            timermeta = 300
            start = 0
        
        if vidas == 0:
            start = 0
            temposob = 300 - timermeta
            telanum = 0
            nome = input("Nome: ")
            adiciona(nome, pontos, temposob)
            janela.clear()
            return telanum            
        if teclado.key_pressed("esc"): #CASO ESTEJA NA TELA DO JOGO E APERTAR ESC, VOLTAR PRO MENU
            start = 0
            telanum == 0
            janela.clear()
            janela.set_background_color((255, 255, 255))
            return telanum
            
        #CONTADORES
        timervelocidade += janela.delta_time()
        timermoeda += janela.delta_time()
        timerMob += janela.delta_time()
        timerhit += janela.delta_time()
        timerinvencivel += janela.delta_time()
        timermeta -= janela.delta_time()

        #INCREMENTADOR DE VELOCIDADE
        if timervelocidade > 20 - difficulty:
            velmob = velmob + 10
            timervelocidade = 0
            pontos += 200

        if timermoeda > 15:
            timermoeda = 0
            i = random.randint(150, janela.width - 150)
            j = random.randint(150, janela.height - 150)
            moeda.set_position(i, j)
            moedaspawn = True
        
        if Collision.collided_perfect(player, moeda) and moedaspawn == True:
            sorteio = random.randint(0,5)
            if sorteio == 0:
                vidas += 1
            elif sorteio == 1 or sorteio == 4:
                cooldown_shot = 0.90 * cooldown_shot
            elif sorteio == 2  or sorteio == 5:
                velplayer = 1.15 * velplayer
            elif sorteio == 3:
                velTiro = 1.1 * velTiro
            moedaspawn = False
            timermsg = 0
        
        if timermsg < 1.5:
            timermsg += janela.delta_time()
            if sorteio == 0:
                janela.draw_text("MAIS UMA VIDA!",janela.width/2-100,janela.height/8-30,30,(255,255,255))
            elif sorteio == 1 or sorteio == 4:
                janela.draw_text("+10% VELOCIDADE DE RECARGA!",janela.width/2-150,janela.height/8-30,30,(255,255,255))
            elif sorteio == 2 or sorteio == 5:
                janela.draw_text("+15% VELOCIDADE MOVIMENTO!",janela.width/2-270,janela.height/8-30,30,(255, 255, 255))
            elif sorteio == 3:
                janela.draw_text("+10% VELOCIDADE DA BALA!",janela.width/2-220,janela.height/8-30,30,(255, 255, 255))


        #MOVIMENTAÇÃO E SPAWN DOS TIROS
        if teclado.key_pressed("w"):
            if matMob != []:
                for z in matMob:
                        z.move_y(janela.delta_time() * velplayer)
            if matTirosDir != []:
                for td in matTirosDir:
                    td.move_y(janela.delta_time() * velplayer)
            if matTirosEsq != []:
                for te in matTirosEsq:
                    te.move_y(janela.delta_time() * velplayer)

        if teclado.key_pressed("s"):
            if matMob != []:
                for z in matMob:
                        z.move_y(janela.delta_time() * -velplayer)
            if matTirosDir != []:
                for td in matTirosDir:
                    td.move_y(janela.delta_time() * -velplayer)
            if matTirosEsq != []:
                for te in matTirosEsq:
                    te.move_y(janela.delta_time() * -velplayer)
        if teclado.key_pressed("a"):
            if matMob != []:
                for z in matMob:
                        z.move_x(janela.delta_time() * velplayer)
            if matTirosDir != []:
                for td in matTirosDir:
                    td.move_x(janela.delta_time() * velplayer)

        if teclado.key_pressed("d"):
            if matMob != []:
                for z in matMob:
                    z.move_x(janela.delta_time() * -velplayer)
            if matTirosEsq != []:
                    for te in matTirosEsq:
                        te.move_x(janela.delta_time() * -velplayer)


        if matMob != []:
            for z in matMob:
                if z.x >= player.x: #mob indo pra esquerda
                    z.move_x(janela.delta_time() * -velmob)
                    z.set_curr_frame(0)
                else: #mod indo pra direita
                    z.move_x(janela.delta_time() * velmob)
                    z.set_curr_frame(1)
                if z.y >= player.y:
                    z.move_y(janela.delta_time() * -velmob)
                else:
                    z.move_y(janela.delta_time() * velmob)

        if mouse.get_position()[0] > player.x:
            player.set_curr_frame(1)
        elif mouse.get_position()[0] < player.x:
            player.set_curr_frame(0)

        if (teclado.key_pressed("space") or mouse.is_button_pressed(1)) and timerhit > cooldown_shot:
                tiro = Sprite("png/tiro.png")
                tiro.set_position(player.x, player.y+player.height/2)
                if mouse.get_position()[0] > player.x:
                    tiro.set_position(player.x+player.width, player.y+player.height/2)
                    matTirosDir.append(tiro)
                elif mouse.get_position()[0] < player.x:
                    tiro.set_position(player.x, player.y+player.height/2)
                    matTirosEsq.append(tiro)
                timerhit = 0

        #SPAWN E MOVIMENTAÇÃO MOBS
        if timerMob > 2-difficulty/10:
            matMob.append(spawn_mob(listacoordenadas))
            timerMob = 0

        if matMob != []:
            for z in matMob:
                z.draw()

        if matMob != []:
            for z in matMob:
                if Collision.collided(z, player) and timerinvencivel > 3:
                    vidas -= 1
                    timerinvencivel = 0

        #INVENCIBILIDADE
        if timerinvencivel < 3-difficulty/10:
            timerpisca += janela.delta_time()
            if timerpisca < 0.2:
                player.draw()
            if timerpisca > 0.4:
                timerpisca = 0
        else:
            player.draw()

        if moedaspawn == True:
            if teclado.key_pressed("w"):
                    moeda.move_y(janela.delta_time() * velplayer)
            if teclado.key_pressed("s"):
                    moeda.move_y(janela.delta_time() * -velplayer)
            if teclado.key_pressed("a"):
                    moeda.move_x(janela.delta_time() * velplayer)
            if teclado.key_pressed("d"):
                    moeda.move_x(janela.delta_time() * -velplayer)
            moeda.draw()

        #MOVIMENTAÇÃO E COLISÃO DOS TIROS DO PLAYER
        mov_tiros(matTirosEsq, -velTiro)
        mov_tiros(matTirosDir, velTiro)
        pontos += colision_tiro_mob(matMob, matTirosEsq)
        pontos += colision_tiro_mob(matMob, matTirosDir)

        #DESENHA UMAS INFORMAÇÕES AÍ
        #janela.draw_text(str(velmob) + " PIXEL/SEG",0,20,16,(255,255,255)) 
        janela.draw_text(str(pontos) + " PONTOS",10,40,25,(255,255,255))
        janela.draw_text(str(vidas) + " VIDAS",10,80,25,(255,255,255))
        janela.draw_text("SOBREVIVA: " + "{}:{}".format(int(timermeta//60), int(timermeta%60)),10,120,25,(255,255,255))

        janela.draw_text(str(timerMob) + " timermob",10,200,25,(255,255,255))
        janela.draw_text(str(timervelocidade) + " timervelocidade",10,225,25,(255,255,255))
        janela.draw_text(str(timermeta) + " timermeta",10,250,25,(255,255,255))

        
        janela.update()
        scrolling(fundoBAIXOE, fundoBAIXOD, fundoTOPOE, fundoTOPOD, velplayer, teclado)
        
