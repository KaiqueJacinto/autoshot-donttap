import time
import win32api, win32con

def clica(x,y):
    win32api.SetCursorPos((x,y)) # Coloca o mouse na posição desejada
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # Aperta o botão direito do mouse para baixo
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) # Solta o botão direito
    time.sleep(0.05) # Espera um pouco para não bugar o clique, esse tempo foi o mais rapido que consegui
    # Se o autoshot começar a cometer erros aumente o tempo de sleep
    '''Dependendo do modo você pode colocar 0.04 no sleep'''