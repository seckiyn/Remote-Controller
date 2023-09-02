import requests
import json
import os
TIMEOUT = 10


kumanda_keycode: dict = None

PATH = os.path.dirname(os.path.abspath(__file__))
def path(*filename):
    return os.path.join(PATH, *filename)


with open(path("keycodes.json")) as f:
    kumanda_keycode = json.loads(f.read())


class Kumanda:
    def __init__(self, host, port="8085"):
        self._host = host
        self._port = port

    def send_get_request(self, path, log_errors=True):
        try:
            request_str = f"http://{self._host}:{self._port}{path}"
            print(f"Sending request: {request_str}")
            response = requests.get(request_str,headers={},timeout=TIMEOUT)
        except Exception as rollas:
            print(rollas.message, rollas.args)
            return False
        return response.content.decode('utf-8')

    def get_key_by_name(self, key_name: str) -> str:
        return kumanda_keycode[key_name]

    def send_key_command_by_name(self, key_name: str) -> None:
        if key_name not in kumanda_keycode:
            raise ValueError('key code not valid')

        key_id, key_symbol = self.get_key_by_name(key_name).split(":")
        request_string = f"/sendrcpackage?keyid={key_id}&keysymbol={key_symbol}"
        response = self.send_get_request(request_string)
        if response and "Set rc key is handled for" in response:
            return True
        else:
            return False



def test():
    kumanda = Kumanda("127.0.0.1")
    print(kumanda.get_key_by_name("mute"))
    spoof = lambda *args, **kwargs: "Set rc key is handled for"
    kumanda.send_get_request = spoof
    print(kumanda.send_key_command_by_name("mute"))


if __name__ == "__main__": test()
