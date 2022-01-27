from pynput.mouse import Listener
import pyautogui

def on_move(x, y):
	print("Movendo o mouse")
	
def on_click(x, y, button, pressed):
	print(x, y, button)

def on_scrolll(x, y, dx, dy):
	print('Mouse Scrolled')



with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	listener.join()
