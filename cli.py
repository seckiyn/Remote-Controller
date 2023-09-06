import sys
import os
import readline
import netifaces
import socket
import atexit
from collections import namedtuple
from typing import List, Tuple
from kumanda import *
from time import sleep
from os.path import join


"""TODO:
    - Add a way to execute commands like !<COMMAND> [ARGS]*
        - ADD HELP
        - ADD SAVE MACRO
        - ADD REMOVE HISTORY
        - ADD NOT TO SAVE IT TO HISTORY
"""
PATH = os.path.dirname(os.path.abspath(__file__))
MACROFILE = path(".macros")
HISTORY_PATH = path(".history")
def path(*filename):
    return os.path.join(PATH, *filename)

remote = Kumanda('192.168.2.84')
SLEEP_TIME = 1

class Cli:
    def __init__(self, ip=None, port=None, file=None, rl=None):
        self.rl = rl
        if port == None: port = 8085
        self.kumanda_keycode: dict = self.get_keycode()
        self.TIMEOUT = 0.01
        self.ip = ip
        self.port = port
        self.file = file
        if ip == None and not file:
            self.kumanda, ip, port = self.connect_to_remote_auto()
        elif file:
            if not os.path.exists(path(file)):
                print("File doesn't exists")
                self.kumanda = self.init_remote_and_save_to_file()
            else:
                with open(path(file)) as f:
                    ip_port = f.read()
                    ip, port = ip_port.strip().split(":")
                    port = int(port)
                    self.ip = ip
                    self.port = port
                    self.kumanda = self.connect_to_remote(ip, port)
        else:
            self.kumanda = self.connect_to_remote(ip, port)
    def __repr__(self):
        string = "Kumanda("
        string += "Ip: " + str(self.ip) + ", "
        string += "Port: " + str(self.port) + ", "
        string += "Filename: " + str(self.file)
        string += ")"
        return string


    def init_remote_and_save_to_file(self):
        kumanda, ip, port = self.connect_to_remote_auto()
        with open(path(self.file), "w") as file:
            file.write(f"{ip}:{port}")
        return kumanda
        

    def connect_to_remote(self, ip, port=8085):
        return Kumanda(ip, port)
    def connect_to_remote_auto(self) -> Kumanda:
        ips = self.check_ports_local(self.port)
        if not ips:
            raise Exception("There are no machines found")
            
        if len(ips) != 1:
            assert False, "More than one ip not implemented yet"
        ip = ips[0]
        self.ip = ip
        kumanda = self.connect_to_remote(ip)
        return kumanda, ip, self.port

    def check_ports_local(self, port=80) -> list:
        open_port_list = list()
        local = self.get_local()
        *ip_range, spec = local.split(".")
        non_ip = ".".join(ip_range)
        for specific in range(256):
            new_ip = f"{non_ip}.{specific}"
            print("Checking:", new_ip)
            result = self.is_port_in_use(new_ip, port)
            print(f"Result: {result}")
            if result:
                open_port_list.append(new_ip)
        return open_port_list
    def is_port_in_use(self, ip: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(self.TIMEOUT)
            return s.connect_ex((ip, port)) == 0
    def get_local(self) -> str:
        iface = netifaces.gateways()["default"][netifaces.AF_INET][1]
        ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]["addr"]
        return ip

    def handle_input(self, inp: str) -> List[Tuple[str, str]]:
        nested_input = inp.split(";")
        Command = namedtuple("Command", ("name", "times"))
        list_of_commands = list()
        for command in nested_input:
            # handle times
            if ":" not in command:
                command_name = command.strip()
                command_times = 1
            else:
                command_name, command_times = map(str.strip, command.split(":"))
                command_times = int(command_times)

            if self.handle_special_input(command_name): continue
            if command_name not in self.kumanda_keycode: raise Exception(f"There's no command called {command_name}")
            com = Command(command_name, command_times)
            list_of_commands.append(com)
        return list_of_commands
    def handle_special_input(self, inp):
        if inp == "exit":
            print("If you want to use `exit` key use `exitt`\n" +
                   "if you want to exit from program use `quit` or `!exit`")
            return True
        if inp == "quit":
            sys.exit()
        if inp == "!exit":
            sys.exit()
            return True
        if inp == "help":
            print("Help")
            return True
        if inp == "keys":
            print(list(self.kumanda_keycode.keys()))
            return True
        # inputs with arguments
        splitted_inp = inp.split()
        if len(splitted_inp) == 1:
            return False

        if "addmacro" in splitted_inp:
            name, *args = splitted_inp
            return self.addmacro(args)

        if "macro" in splitted_inp:
            name, *args = splitted_inp
            return self.macro(args)

        if "wait" in splitted_inp:
            name, *args = splitted_inp
            return self.wait(args)
    def wait(self, args):
        to_wait = int(args[0])
        print("Waiting {} seconds".format(to_wait))
        sleep(to_wait)
        return True


    def check_macro(self, macro_name):
        to_check = list()
        with open(MACROFILE) as file:
            for line in file.readlines():
                macron = line.split("{")[0].strip()
                to_check.append(macron)
        # print(to_check)

        return macro_name in to_check



    def macro(self, args):
        macro_name = args[0]
        my_macro = None
        with open(MACROFILE) as file:
            for line in file.readlines():
                # print(line)
                if line.startswith(macro_name):
                    splitted_macro = line.split("{")
                    raw_macro = splitted_macro[1]
                    my_macro = raw_macro.strip()
                    my_macro = my_macro[:-1]
                    # print(my_macro)

        if not my_macro:
            print(f"Can't find the macro {macro_name}")
        self.handle_input(my_macro)

        return True

    def addmacro(self, args):
        if len(args) != 1:
            print("Exhaustive arguments for macro", "addmacro <macroname>")
            return True
        macro_name = args[0]
        print(f"{macro_name=}")
        with open(MACROFILE, "a") as file:
            """
            last = get_last_from_history()
            """
            last = self.rl.get_last()
            print("Last: ", last)
            if self.check_macro(macro_name):
                print(f"{macro_name} already added")
                return True
            to_write = macro_name + "{" + str(last.strip()) + "}"
            file.write(to_write+"\n")
        return True




    def handle_command(self, command):
        '''
            Will take a command and return a function
        '''
        # print(command)
        command, times = command
        if command in kumanda_keycode:
            for _ in range(times):
                # print(command)
                self.kumanda.send_key_command_by_name(command)
                sleep(SLEEP_TIME)

    def start(self):
        while True:
            inp = input(f"{self.ip}:{self.port}>")
            commands = self.handle_input(inp)
            # print(commands)
            for command in commands:
                mcommand = self.handle_command(command)
    def get_keycode(self):
        # print(path("keycodes.json"))
        with open(path("keycodes.json")) as f:
            return json.loads(f.read())

def print_help(script_name):
    my_help = f"""\
    {script_name} [OPTIONS]
    --file <filename>: Use ip port from file or if --auto save it to file
    --auto: Connect automatically
    --ip <IP>: Use IP to connect remote
    --port <PORT>: Use port to connect remote"""
    print(my_help)


class ReadLine:
    def __init__(self):
        self.length = None
        self.history_path = HISTORY_PATH
        self.init_readline()

    def init_readline(self):
        print("Initializing history")
        if os.path.exists(self.history_path):
            readline.read_history_file(self.history_path)
            self.length = readline.get_current_history_length()
        else:
            open(self.history_path, "wb").close()
            self.length = 0
        atexit.register(self.save)
    def debug(self):
        print(f"{self.history_path=}\n{self.length=}")
        while inp:=input("deneme: "): print("History?: ", inp)
    def save(self):
        new_h_len = readline.get_history_length()
        readline.set_history_length(1000)
        readline.write_history_file(self.history_path)
    def get_last(self):
        self.save()
        item = open(self.history_path).readlines()[-2]
        return item


def parse_args(rl=None):
    script_name, *args = sys.argv
    ip = None
    port = 8085
    file = None
    remote = None

    if "--help" in args or not args:
        print_help(script_name)
        sys.exit()
    if "--auto" in args or "-a" in args:
        ip = None
    if "--ip" in args:
        pos = args.index("--ip")
        pos += 1
        ip = args[pos]
    if "--port" in args:
        pos = args.index("--port")
        pos += 1
        port = int(args[pos])
    if "--file" in args:
        pos = args.index("--file")
        pos += 1
        file = args[pos]
    if "--filename" in args:
        pos = args.index("--filename")
        pos += 1
        file = args[pos]

    kumanda = Cli(ip, port, file, rl=rl)
    print(kumanda)
    return kumanda



if __name__ == '__main__':
    readLine = ReadLine()
    atexit.register(readLine.save)
    # readLine.debug()
    remote: Cli = parse_args(readLine)
    remote.start()
