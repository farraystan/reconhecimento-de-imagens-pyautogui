import pyautogui
import time

# Aguardando um tempo para você abrir a janela necessária
time.sleep(3)

# Tente localizar a imagem
try:
    location = pyautogui.locateOnScreen(r'')
    if location:
        # Clica no centro da imagem encontrada
        pyautogui.click(pyautogui.center(location))
    else:
        print("Imagem não encontrada.")
except pyautogui.ImageNotFoundException:
    print("Erro: A imagem não foi encontrada.")
