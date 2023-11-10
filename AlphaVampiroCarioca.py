from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

janela = Window(1080, 720)
teclado = Window.get_keyboard()
fundo = GameImage("png/fundo_jogo_3.png")
janela.set_title("Vampiro Carioca")

player = Sprite("png/player.png")
esqueleto = Sprite("png/esqueleto.png")
policial = Sprite("png/policial.png")

player.set_position(460, 460)
esqueleto.set_position(460, 10)
policial.set_position(10, 460)

def spawn_zombie(listacoordenadas):
    zumbi = Sprite("png/zumbi.png")
    coordenadas = random.choice(listacoordenadas)
    zumbi.set_position(coordenadas[0], coordenadas[1])
    return zumbi

velplayer = 200
velmob = 50

matZumbi = []
contador = 0
contadorgeral = 0

listacoordenadas = [[-25, -25], [-25, janela.height/2], [-25, janela.height + 25], [janela.width/2, janela.height + 25],  
                    [janela.width + 25, -25], [janela.width + 25, janela.height/2], [janela.width + 25, janela.height + 25], 
                    [janela.width/2, - 25]]

while True:

    contadorgeral += janela.delta_time()
    contador += janela.delta_time()

    if contadorgeral > 30:
        velmob = velmob + 20
        contadorgeral = 0

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

    if contador > 1:
        matZumbi.append(spawn_zombie(listacoordenadas))
        contador = 0

    if matZumbi != []:
        for z in matZumbi:
            z.draw()

    if matZumbi != []:
        for z in matZumbi:
            if z.x > player.x:
                z.move_x(janela.delta_time() * -velmob)
            else:
                z.move_x(janela.delta_time() * velmob)

            if z.y > player.y:
                z.move_y(janela.delta_time() * -velmob)
            else:
                z.move_y(janela.delta_time() * velmob)

    janela.draw_text(str(contadorgeral) + " FPS",0,0,16,(255,255,255))
    janela.draw_text(str(velmob) + " FPS",0,20,16,(255,255,255))

    janela.update()
    fundo.draw()
    player.draw()