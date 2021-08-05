import pyautogui
import keyboard
from cliquerapido.clique import clica
 
def achar_posicao_dos_ponteiros():
    '''
    Função destinada a encontrar as posição onde deve precisamos verificar a 
    cor e posteriormente clicar se necessário.
    '''
    pyautogui.displayMousePosition()

#achar_posicao_dos_ponteiros()
#114,180
#550,616
#cor (0,0,0)

def pega_imagem(pontoI,pontoF):
    '''
    Essa função serve para tirar uma screenshot de parte da tela,
    você precisa dos pontos finais e iniciais, que você obteve utilizando a função anterior.
    '''
    #tela = pyautogui.screenshot('teste.png',region=(pontoI[0],pontoI[1],(pontoF[0]-pontoI[0]),(pontoF[0]-pontoI[0])))
    '''Você pode descomentar a linha a cima para verificar se você esta obtendo a região correta'''
    tela = pyautogui.screenshot(region=(pontoI[0],pontoI[1],(pontoF[0]-pontoI[0]),(pontoF[0]-pontoI[0])))
    return tela

#pega_imagem((114,180),(550,616))

def main():
    pontoInicial = (114,180)
    pontoFinal   = (550,616)
    while not(keyboard.is_pressed('q')): # Desativa o autoshot com a tecla Q
        imagem = pega_imagem(pontoInicial,pontoFinal) # Pega a screenshot da região utilizando so os ponto inicial e ponto final

        altura,largura = imagem.size # Pega a altura e largura da região que foi feito o screenshot
        for x in range(50,altura,100):
            for y in range(50,largura,100):
                r,g,b = imagem.getpixel((x,y)) # Pega a cor do pixel
                if r == 0 and g == 0 and b == 0: # Verifica se a cor do pixel é preto
                    clica(pontoInicial[0]+x,pontoInicial[1]+y) # Utilizaremos a api do windows para clicar mais rapido
                    '''Você pode escolher entra uma das duas função de cliques,
                    no entanto a função usando a api do windows se mostrou mais rapida nos cliques'''
                    #pyautogui.click(pontoInicial[0]+x,pontoInicial[1]+y) # Utiliza a função de clique do pyautogui para clicar no pixel preto

main()