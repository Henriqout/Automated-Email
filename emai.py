import pyautogui
import time
import os

pyautogui.PAUSE = 1

def find_and_click(image_path, confidence=0.9):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            time.sleep(1)  
        else:
            raise Exception(f"Imagem não encontrada: {image_path}")
    except Exception as e:
        print(f"Erro ao encontrar e clicar na imagem {image_path}: {e}")

def write_text(text):
    pyautogui.typewrite(text, interval=0.05)

compose_button_img = os.path.abspath('C:/Users/ASUS/Downloads/vs/Emai/Compose.png')
attach_button_img = os.path.abspath('C:/Users/ASUS/Downloads/vs/Emai/Attach.png')
send_button_img = os.path.abspath('C:/Users/ASUS/Downloads/vs/Emai/Send.png')

while True:
    try:
        find_and_click(compose_button_img)

        time.sleep(2)

        write_text('seu_destinatario@gmail.com')
        pyautogui.press('tab') 
        pyautogui.press('tab')

        write_text('Lorem Ipsum')
        pyautogui.press('tab') 

        write_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

        find_and_click(attach_button_img)

        time.sleep(2)

        write_text('teste.txt')
        pyautogui.press('enter') 

        time.sleep(3)

        find_and_click(send_button_img)

        print("Email enviado com sucesso!")

    
        time.sleep(10)  # Ajuste o intervalo conforme necessário

    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")
        break
    except Exception as e:
        print(f"Erro durante o envio do e-mail: {e}")
        time.sleep(10)  
