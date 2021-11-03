from kumanda import *
from time import sleep
import sys

remote = Kumanda('192.168.2.84')
SLEEP_TIME = 1

def helpme():
    print('This is a help')

def waitme(waittime=1): # Add to wait specific time without bloating command_list
    pass
    # sleep(waittime)

commandto = {
            '1':remote.one,
            '2':remote.two,
            '3':remote.three,
            '4':remote.four,
            '5':remote.five,
            '6':remote.six,
            '7':remote.seven,
            '8':remote.eight,
            '9':remote.nine,
            '0':remote.zero,
            'power':remote.power_off,
            'mute':remote.toggle_mute,
            'volup':remote.volume_up,
            'volume up':remote.volume_up,
            'voldown':remote.volume_down,
            'volume down':remote.volume_down,
            'next':remote.channel_up,
            'channel up':remote.channel_up,
            'pre':remote.channel_down,
            'channel down':remote.channel_down,
            'menu':remote.menu,
            'exit':remote.exitt,
            'back':remote.back,
            'left':remote.left,
            'right':remote.right,
            'top':remote.top,
            'bottom':remote.bottom,
            'ok':remote.ok,
            'tools':remote.tools,
            'source':remote.source,
            'guide':remote.guide,
            'fav':remote.fav,
            'txt':remote.txt,
            'rec':remote.rec,
            'play':remote.play,
            'pause':remote.pause,
            'stop':remote.stop,
            'prevv':remote.prev,
            'nextv':remote.next,
            'lang':remote.language,
            'sub':remote.subtitle,
            'red':remote.red,
            'green':remote.green,
            'yellow':remote.yellow,
            'blue':remote.blue,
            'help':helpme,
            'quit':sys.exit,
            'wait':waitme
        }

def handle_command(command):
    '''
        Will take a command and return a function
    '''
    if command in commandto: # Check if command exists
        return commandto[command]
    else:
        print('There is no command named {}'.format(command))
        return False
def send_command(*commands):
    for i in commands:
        i()
        sleep(SLEEP_TIME)
def split_input(inp):
    '''
        will take str input like "next:3"
        and will return next and 3
    '''
    times = 1
    splitted_inp = inp.split(':')
    if len(splitted_inp) == 2: # If input contains a times value
        inp = splitted_inp[0]
        if splitted_inp[1].isdigit():
            times = int(splitted_inp[1])
        return inp, times
    elif len(splitted_inp) == 1: # If input is alone :(
        return inp, 1
    else: # If input is something else
        print('Too much to split!!!')
        return None,None

def get_input():
    command_list = []
    while True:
        nested_input = input('>>').split(';') # Get a list of inputs separated with semicolums "next:23;5;8"
        for command in nested_input: # Iterate over command list
            command, times = split_input(command) # Split and get command and how many times its gonna do
            mcommand = handle_command(command) # Take commands and makes it into corresponding command
            if mcommand: # Checks if its really a command
                for _ in range(times):
                    command_list.append(mcommand)

        if command_list:
            send_command(*command_list)
            command_list = []


if __name__ == '__main__':
    get_input()













