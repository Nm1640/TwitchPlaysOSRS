import time
import socket
import random
import keyboard
import pyautogui
import threading
import configparser
from win32gui import *
print('Modules Loaded')

config = configparser.ConfigParser()
config.read('config.ini')

token = config.get('DEFAULT', 'token')
channel = config.get('DEFAULT', 'channel')
nickname = config.get('DEFAULT', 'nickname')
server = config.get('DEFAULT', 'server')
port = config.getint('DEFAULT', 'port')
osrs_username = config.get('DEFAULT', 'osrs_username')
print()
print(f'Token: Hidden')
print(f'Channel: {channel}')
print(f'Nickname: {nickname}')
print(f'Server: {server}')
print(f'Port: {port}')
print(f'OSRS Username: {osrs_username}')
print()
print('Config Loaded')
print()
# Connect to Twitch IRC server
sock = socket.socket()
sock.connect((server, port))

# Login to Twitch IRC server
sock.send(f"PASS {token}\r\n".encode())
sock.send(f"NICK {nickname}\r\n".encode())

# Join the desired Twitch channel
sock.send(f"JOIN #{channel}\r\n".encode())
print('Connected, please click on client.')
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print()

window_coords = ()
window_width = 0
window_height = 0

running = True

admin = ['hananniee','nmflash8','adorablemma', 'bastin101', 'bat_ears', 'ben_vos', 'casey8x8', 'collin_sky', 'crbnfiber', 'defyj', 'eeyorishem', 'emmajayne', 'fyreeflye', 'imreallyadog', 'ismisk', 'lillypie1', 'nightbot', 'oddbob1150', 'purple_sadge', 'purplesage_', 'quantumturtl', 'quantumturtle', 'rewardtts', 'space_prism', 'streamelements', 'swaggyfredd2', 'tenshibeat', 'tersotacto', 'thewalruscancer', 'torchr', 'whitstream', 'wistfulbirb', 'xd4nkxm3m3x420xbl4z3x1tx']

available_inputs = ['ESC','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','RC','LC','SC','UP','DOWN','LEFT','RIGHT','SPACE']
inputs = []
decision = 'all'

def close_program():
    global running
    while running:
        if keyboard.is_pressed("q"):
            print()
            print('Shutting Down...')
            running = False

def input_reader():
    global window_coords
    global decision
    global running
    global inputs
    time.sleep(3)
    while running:
        top_left = (window_coords[0],window_coords[1])
        bottom_right = (window_coords[2],window_coords[3])
        if inputs:
            print(decision)
            if decision == 'all':
                choice = inputs[0]
                inputs.pop(0)
                split_choice = choice.split()
                if is_chess_input(split_choice[0]):
                    coords = chess_to_coords(top_left, bottom_right, split_choice[0])
                    pyautogui.moveTo(coords)
                    if len(split_choice) > 1:
                        if split_choice[1] == 'RC':
                            pyautogui.mouseDown(button='right')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='right')
                        elif split_choice[1] == 'LC':
                            pyautogui.mouseDown(button='left')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='left')
                        elif split_choice[1] == 'SC':
                            pyautogui.keyDown('shift')
                            pyautogui.mouseDown(button='left')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='left')
                            pyautogui.keyUp('shift')
                        else:
                            if split_choice[1] in available_inputs:
                                pyautogui.press(split_choice[1].lower())
                    else:
                        pyautogui.leftClick()   
                        if split_choice[0] == 'RC':
                            pyautogui.mouseDown(button='right')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='right')
                        elif split_choice[0] == 'LC':
                            pyautogui.mouseDown(button='left')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='left')
                        elif split_choice[0] == 'SC':
                            pyautogui.keyDown('shift')
                            pyautogui.mouseDown(button='left')
                            time.sleep(.5)
                            pyautogui.mouseUp(button='left')
                            pyautogui.keyUp('shift')
                else:
                    if split_choice[0] in available_inputs:
                        pyautogui.press(split_choice[0].lower())

            if decision == 'random':
                choice = random.choice(inputs)
                inputs = []
                split_choice = choice.split()
                if is_chess_input(split_choice[0]):
                    coords = chess_to_coords(top_left, bottom_right, split_choice[0])
                    pyautogui.moveTo(coords)
                    if len(split_choice) > 1:
                        if split_choice[1] == 'RC':
                            pyautogui.rightClick()
                        elif split_choice[1] == 'LC':
                            pyautogui.leftClick()
                        elif split_choice[1] == 'SC':
                            pyautogui.keyDown('shift')
                            pyautogui.leftClick()
                            pyautogui.keyUp('shift')
                        else:
                            if split_choice[1] in available_inputs:
                                pyautogui.press(split_choice[1].lower())       
                    else:
                        pyautogui.leftClick()
                elif split_choice[0] == 'RC':
                    pyautogui.rightClick()
                elif split_choice[0] == 'LC':
                    pyautogui.leftClick()
                elif split_choice[0] == 'SC':
                    pyautogui.keyDown('shift')
                    pyautogui.leftClick()
                    pyautogui.keyUp('shift')
                else:
                    if split_choice[0] in available_inputs:
                        pyautogui.press(split_choice[0].lower())
                time.sleep(random.uniform(.4, 1))

            if decision == 'democracy':
                mode = max(set(inputs.lower()), key = inputs.lower().count)
                inputs = []
                split_choice = mode.split()
                if is_chess_input(split_choice[0]):
                    coords = chess_to_coords(top_left, bottom_right, split_choice[0])
                    pyautogui.moveTo(coords)
                    if len(split_choice) > 1:
                        if split_choice[1] == 'RC':
                            pyautogui.rightClick()
                        elif split_choice[1] == 'LC':
                            pyautogui.leftClick()
                        elif split_choice[1] == 'SC':
                            pyautogui.keyDown('shift')
                            pyautogui.leftClick()
                            pyautogui.keyUp('shift')
                        else:
                            if split_choice[1] in available_inputs:
                                pyautogui.press(split_choice[1].lower())       
                    else:
                        pyautogui.leftClick()
                elif split_choice[0] == 'RC':
                    pyautogui.rightClick()
                elif split_choice[0] == 'LC':
                    pyautogui.leftClick()
                elif split_choice[0] == 'SC':
                    pyautogui.keyDown('shift')
                    pyautogui.leftClick()
                    pyautogui.keyUp('shift')
                else:
                    if split_choice[0] in available_inputs:
                        pyautogui.press(split_choice[0].lower())
                time.sleep(random.uniform(5, 15))

    print('Shutdown Successful: Input Reader.')
    
def chess_to_coords(coord1, coord2, input):
    # Create the window space.
    x1, y1 = coord1
    x2, y2 = coord2

    # Offset padding
    x1 += 10
    x2 -= 10
    y1 += 40
    y2 -= 10

    # Find width and height of the window.
    width = x2 - x1
    height = y2 - y1

    # Find the section width and height.
    section_width = width / 40
    section_height = height / 26

    # Parse the row and col from the input.
    alphabet_to_int = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    
    col = int(input[1:])
    row = alphabet_to_int[input[0].upper()]

    # Find the section region to pick a coord from.
    x_min = x1 + round((col - 1) * section_width)
    x_max = x1 + round(col * section_width)
    y_min = y1 + round((row - 1) * section_height)
    y_max = y1 + round(row * section_height)

    # Create random coords in the given section.
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    print(x, y)
    return (x, y)

def window_position():
    global window_coords
    global window_width
    global window_height
    global osrs_username
    while running:
        window_handle = FindWindow(None, f"Old School RuneScape")
        #window_handle = FindWindow(None, f"RuneLite - Cursed Nm")
        window_rect = GetWindowRect(window_handle)
        if window_coords != window_rect: # Update window coords
            window_coords = window_rect
            window_height = window_coords[3] - window_coords[1]
            window_width = window_coords[2] - window_coords[0]

            print(f'Updated Window Coords \n{window_coords} \nwindow width: {window_width} \nwindow height: {window_height}')
            print()
        time.sleep(.1)
    print('Shutdown Successful: Window Reader.')

def is_chess_input(test_input):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Remove Spaces
    no_loggout = ['y34','y35', 'z34', 'z35', 'y33', 'z33', 'z36', 'y36', 'y37', 'x37', 'x38', 'y38', 'x39', 'y39' 'y33','e38','e39','e40','f38','f39','f40','g38','g39','g40','y33','z32','y32','z31','y31','z37']
# ok nm disable 36,37,38,39 on y,z


    if test_input.lower() in no_loggout:
        return False
    stripped_input = test_input.strip(" ")                          
    # Is the input 2 - 3 Characters long
    if len(stripped_input) == 2 or len(stripped_input) == 3:       
        # Is the first character a letter
        if stripped_input[0].lower() in letters:                    
            # Are the last digit's a number
            if stripped_input[1:].isdigit():                        
                # Are the numbers 1 - 40
                if int(stripped_input[1:]) in range(1, 40 + 1):     
                    # Then it is a valid input
                    return True                                     
    return False

def read_twitch_chat():
    # Read Twitch chat messages
    global running
    global inputs
    global decision
    response = ''
    print('Atempting to connect to twitch chat.')
    while running:
        # Recieve message from twitch chat
        try:
            response = sock.recv(2048).decode()
        except ConnectionAbortedError:
            print("Connection closed by the host machine.")
            break
        except:
            if response == '':
                print('Error Connecting to server, Shutting down.')
                running = False
        # Check if it's a server ping.
        if response.startswith("PING"):
            print('Ping')
            sock.send("PONG :tmi.twitch.tv\r\n".encode())
            print('Pong')
        else:
            try:
                if response != '':
                    username = response.split("!")[0][1:]
                    message = response.split(":")[2][:-2]
                    print(f'{username} : {message}')
                    split_message = message.split()
                    if is_chess_input(split_message[0]):
                        inputs.append(message.upper())
                        continue
                    if available_inputs:
                        if split_message[0].upper() in available_inputs:
                            inputs.append(message.upper())

                    if message.startswith('!') and username.lower() in admin:
                        if message.lower() == '!all':
                            decision = 'all'
                        if message.lower() == '!random':
                            decision = 'random'
                        if message.lower() == '!democracy':
                            decision = 'democracy'
                        
            except IndexError:
                print(f'(Index Error) - {response}')
    print('Shutdown Successful: Twitch Reader.')

def main():
    global running
    global inputs

    chat_thread = threading.Thread(target=read_twitch_chat)
    position_thread = threading.Thread(target=window_position)
    input_thread = threading.Thread(target=input_reader)
    close_thread = threading.Thread(target=close_program)

    chat_thread.start()
    position_thread.start()
    input_thread.start()
    close_thread.start()

    try:
        while running:
            time.sleep(1)
    except SystemExit:
        pass
    finally:
        sock.close()
        print('Shutdown Successful: Socket closed.')

if __name__ == "__main__":
    main()