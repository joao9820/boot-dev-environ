import pyautogui, time, os
import ctypes
from dotenv import load_dotenv

load_dotenv()

pyautogui.PAUSE = 1

project = os.environ.get('APP')

alert = "Deseja iniciar o ambiente de desenvolvimento"

if(project):
  alert += " " + project

alert += "?"

accept = pyautogui.confirm(text=alert, title="Auto boot Development System", buttons=['OK', 'Cancelar'])

if accept != 'OK':
  exit()

def off_capslock():
  capsOn = ctypes.WinDLL("User32.dll").GetKeyState(0x14)

  if(capsOn):
    pyautogui.press('capslock')

def start_project(path: str, comand: str):

  # Executar
  pyautogui.press('win')
  pyautogui.write(os.environ.get('TERMINAL'))
  pyautogui.press('enter')

  # shell
  # print(path)

  #Não é possível utilizar / no pyautogui
  pyautogui.typewrite('cd ' + path)
  pyautogui.press('enter')
  pyautogui.write('code .')
  pyautogui.press('enter')

  # espera abrir o vs code
  time.sleep(3)

  pyautogui.hotkey('ctrl', "'")

  # espera abrir o terminal
  time.sleep(3)

  # iniciar servidor
  pyautogui.write(comand)
  pyautogui.press('enter')


""" def start_insomnia():
  pyautogui.press('win')
  pyautogui.write('insomnia')
  pyautogui.press('enter') """

off_capslock()

start_project(os.environ.get('PATH-BACKEND'), os.environ.get('START-SERVER-BACKEND'))

# Verificar quando precisa clicar no botão do vscode que o projeto é confiável
start_project(os.environ.get('PATH-FRONTEND'), os.environ.get('START-SERVER-FRONTEND'))





