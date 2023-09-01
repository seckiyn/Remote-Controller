import sys
import os
import readline
import netifaces
import socket
from collections import namedtuple
from typing import List, Tuple
from kumanda import *
from time import sleep

remote = Kumanda('192.168.2.84')
SLEEP_TIME = 1

class Cli:
    def __init__(self, ip=None, port=None, file=None):
        if port == None: port = 8085
        self.kumanda_keycode: dict = self.get_keycode()
        self.TIMEOUT = 0.01
        self.ip = ip
        self.port = port
        self.file = file
        if ip == None and not file:
            self.kumanda = self.connect_to_remote_auto()
        elif file:
            if not os.path.exists(file):
                print("File doesn't exists")
                self.kumanda = self.init_remote_and_save_to_file()
            else:
                with open(file) as f:
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
        with open(self.file, "w") as file:
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
        if inp == "quit":
            if input("Do you want to quit?[y/n]: ") == "y":
                sys.exit()
            return True
        if inp == "help":
            print("Help")
            return True
        if inp == "keys":
            print(list(self.kumanda_keycode.keys()))
            return True


    def handle_command(self, command):
        '''
            Will take a command and return a function
        '''
        print(command)
        command, times = command
        if command in kumanda_keycode:
            for _ in range(times):
                print(command)
                self.kumanda.send_key_command_by_name(command)
                sleep(SLEEP_TIME)

    def start(self):
        while True:
            inp = input(f"{self.ip}:{self.port}>")
            commands = self.handle_input(inp)
            print(commands)
            for command in commands:
                mcommand = self.handle_command(command)
    def get_keycode(self):
        with open("./keycodes.json") as f:
            return json.loads(f.read())



def parse_args():
    script_name, *args = sys.argv
    ip = None
    port = 8085
    file = None
    remote = None
    args = ["--auto", "--ip", "192.168.1.1", "--filename", "ipport.md"]

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

    kumanda = Cli(ip, port, file)
    print(kumanda)
    return kumanda



if __name__ == '__main__':
    remote = parse_args()
    remote.start()
