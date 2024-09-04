#Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.



import pyautogui as auto
import time

# atrasar os comandos da biblioteca
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('firefox') # digita a palavra "Chrome" ou "Firefox"
auto.press('enter') # aperta "Enter"

# tecla de atalho para maximizar tela
#auto.hotkey('alt', '')
#auto.press('x')             

# acessa o site do "GitHub"
auto.write('youtube.com')
auto.press('enter')
# entrar na página de login do GitHub
for i in range(1):
    time.sleep(5)
    auto.write('pesquisar')
    auto.write('video aulas de python')
    auto.press('enter')

#auto.press('enter')