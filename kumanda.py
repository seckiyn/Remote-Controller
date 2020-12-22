import requests
from enum import Enum
TIMEOUT = 10
class Kumanda:
    class kumanda_keycode(Enum):
        power = "-2544:-4081"
        mute = "-2539:-4018"
        volume_up = "-2475:-4020"
        volume_down = "-2476:-4019"
        channel_up = "-2464:-4026"
        channel_down = "-2465:-4025"
        menü= "-2547:-4078"
        exit= "-2534:-3998"
        back= "-2542:-3979"
        left= "-2495:-4096"
        right= "-2494:-4095"
        top= "-2493:-4094"
        bottom= "-2492:-4093"
        ok= "-2490:13"
        tools= "-2506:-4079"
        source= "-2541:-3992"
        guide= "-2536:-4069"
        fav= "-2557:-4071"
        txt= "-2543:-3990"
        zero= "-2533:48"
        one= "-2532:49"
        two= "-2531:50"
        three= "-2530:51"
        four= "-2529:52"
        five= "-2528:53"
        six= "-2527:54"
        seven= "-2526:55"
        eight= "-2525:56"
        nine= "-2524:57"
        rec= "-2535:-4010"
        play= "-2548:-4015"
        pause= "-2480:-4086"
        stop= "-2545:-4014"
        prev= "-2538:-4005"
        forward= "-2555:-4023"
        next="-2546:4004"
        language= "-2549:-3984"
        subtitle="-2507:4064"
        red="-2523:4030"
        green="-2522:-4029"
        yellow="-2521:-4028"
        blue= "-2520:4027"
    def __init__(self, host, port="8085"):
        self._host = host
        self._port = port
    def _send_get_request(self, path, log_errors=True):
        try:
            response = requests.get('http://' + self._host + ':' + self._port + path,headers={},timeout=TIMEOUT)
        except Exception as rollas:
            print(rollas.message, rollas.args)
            return False
        else:
            return response.content.decode('utf-8')
    def send_key_command(self, key_command):
        if key_command not in self.kumanda_keycode:
            raise ValueError('key code not valid')

        parts = str.split(key_command.value, ":")
        response = self._send_get_request("/sendrcpackage?keyid=" + parts[0] + "&keysymbol=" + parts[1])
        if response and "Set rc key is handled for" in response:
            return True
        else:
            return False
    def toggle_mute(self):
        return self.send_key_command(self.kumanda_keycode.mute)
    def power_off(self):
        return self.send_key_command(self.kumanda_keycode.power)
    def volume_up(self):
        return self.send_key_command(self.kumanda_keycode.volume_up)
    def volume_down(self):
        return self.send_key_command(self.kumanda_keycode.volume_down)
    def channel_up(self):
        return self.send_key_command(self.kumanda_keycode.channel_up)
    def channel_down(self):
        return self.send_key_command(self.kumanda_keycode.channel_down)
    def menü(self):
        return self.send_key_command(self.kumanda_keycode.menü)
    def exitt(self):
        return self.send_key_command(self.kumanda_keycode.exit)
    def back(self):
        return self.send_key_command(self.kumanda_keycode.back)
    def left(self):
        return self.send_key_command(self.kumanda_keycode.left)
    def right(self):
        return self.send_key_command(self.kumanda_keycode.right)
    def bottom(self):
        return self.send_key_command(self.kumanda_keycode.bottom)
    def top(self):
        return self.send_key_command(self.kumanda_keycode.top)
    def ok(self):
        return self.send_key_command(self.kumanda_keycode.ok)
    def tools(self):
        return self.send_key_command(self.kumanda_keycode.tools)
    def source(self):
        return self.send_key_command(self.kumanda_keycode.source)
    def guide(self):
        return self.send_key_command(self.kumanda_keycode.guide)
    def fav(self):
        return self.send_key_command(self.kumanda_keycode.fav)
    def txt(self):
        return self.send_key_command(self.kumanda_keycode.txt)
    def zero(self):
        return self.send_key_command(self.kumanda_keycode.zero)
    def one(self):
        return self.send_key_command(self.kumanda_keycode.one)
    def two(self):
        return self.send_key_command(self.kumanda_keycode.two)
    def three(self):
        return self.send_key_command(self.kumanda_keycode.three)
    def four(self):
        return self.send_key_command(self.kumanda_keycode.four)
    def five(self):
        return self.send_key_command(self.kumanda_keycode.five)
    def six(self):
        return self.send_key_command(self.kumanda_keycode.six)
    def seven(self):
        return self.send_key_command(self.kumanda_keycode.txt)
    def eight(self):
        return self.send_key_command(self.kumanda_keycode.eight)
    def nine(self):
        return self.send_key_command(self.kumanda_keycode.nine)
    def rec(self):
        return self.send_key_command(self.kumanda_keycode.rec)
    def play(self):
        return self.send_key_command(self.kumanda_keycode.play)
    def pause(self):
        return self.send_key_command(self.kumanda_keycode.pause)
    def stop(self):
        return self.send_key_command(self.kumanda_keycode.stop)
    def prev(self):
        return self.send_key_command(self.kumanda_keycode.prev)
    def forward(self):
        return self.send_key_command(self.kumanda_keycode.forward)
    def next(self):
        return self.send_key_command(self.kumanda_keycode.next)
    def language(self):
        return self.send_key_command(self.kumanda_keycode.language)
    def subtitle(self):
        return self.send_key_command(self.kumanda_keycode.subtitle)
    def red(self):
        return self.send_key_command(self.kumanda_keycode.red)
    def green(self):
        return self.send_key_command(self.kumanda_keycode.green)
    def yellow(self):
        return self.send_key_command(self.kumanda_keycode.yellow)
    def blue(self):
        return self.send_key_command(self.kumanda_keycode.blue)
tv=Kumanda("192.168.1.102")
while(True):
    print("""
        CHOICE LIST******
        -------------------
        power             
        mute 
        volume_up
        volume_down
        channel_up
        channel_down
        exit
        zero
        one
        two
        three
        four
        five
        six
        seven
        eight
        nine
        rec
        play
        pause
        stop
        prev
        forward
        next
        language
        subtitle
        red
        green
        yellow
        blue
        quit
        """)
    choice=input("Your Choice:")
    if(choice=="quit"):
        break
    else:
        eval("tv"+"."+choice+"()")
    

