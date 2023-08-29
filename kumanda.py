import requests
TIMEOUT = 10

kumanda_keycode = dict(
    power = "-2544:-4081",
    mute = "-2539:-4018",
    volume_up = "-2475:-4020",
    volume_down = "-2476:-4019",
    channel_up = "-2464:-4026",
    channel_down = "-2465:-4025",
    menu= "-2547:-4078",
    exitt= "-2534:-3998",
    back= "-2542:-3979",
    left= "-2495:-4096",
    right= "-2494:-4095",
    top= "-2493:-4094",
    bottom= "-2492:-4093",
    ok= "-2490:13",
    tools= "-2506:-4079",
    source= "-2541:-3992",
    guide= "-2536:-4069",
    fav= "-2557:-4071",
    txt= "-2543:-3990",
    zero= "-2533:48",
    one= "-2532:49",
    two= "-2531:50",
    three= "-2530:51",
    four= "-2529:52",
    five= "-2528:53",
    six= "-2527:54",
    seven= "-2526:55",
    eight= "-2525:56",
    nine= "-2524:57",
    rec= "-2535:-4010",
    play= "-2548:-4015",
    pause= "-2480:-4086",
    stop= "-2545:-4014",
    prev= "-2538:-4005",
    forward= "-2555:-4023",
    nextt="-2546:4004",
    language= "-2549:-3984",
    subtitle="-2507:4064",
    red="-2523:4030",
    green="-2522:-4029",
    yellow="-2521:-4028",
    blue= "-2520:4027"
    )



class Kumanda:
    def __init__(self, host, port="8085"):
        self._host = host
        self._port = port

    def send_get_request(self, path, log_errors=True):
        try:
            response = requests.get('http://' + self._host + ':' + self._port + path,headers={},timeout=TIMEOUT)
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
        response = self.send_get_request("/sendrcpackage?keyid={key_id}&keysymbol={key_symbol}")
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
