import machine,gc,neopixel,network
from config import *

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, password)
station.isconnected()
station.ifconfig()

# ------ if you get a output like : 0.0.0.0:80 , stop program and run it again ------#
print('enter this ip and port to your browser : '+str(station.ifconfig()[0])+':'+str(p))#----#
# ---------------------------------------------------------------------------------- #

np = neopixel.NeoPixel(machine.Pin(WS2812B_pin), matrix)
def clear(x=np):
    for i in range(x.n):
        x[i] = (0,0,0)
    x.write()
def show(color,x=np):
    clear()
    for i in range(x.n):
        x[i] = color
    x.write()

try:
  import usocket as socket
except:
  import socket

def web_page():
    html = """<html><style>* {margin: 0;padding: 0;box-sizing: border-box;} body {height: 100vh;overflow: hidden;display: flex;flex-direction: column;align-items: center;justify-content: center;background: #333;}.noselect {-webkit-touch-callout: none;-webkit-user-select: none;-khtml-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;-webkit-tap-highlight-color: transparent;}button {width: 150px;height: 50px;cursor: pointer;background: #333;margin: 10px;border: none;border-radius: 10px;box-shadow: -5px -5px 15px #444, 5px 5px 15px #222, inset 5px 5px 10px #444, inset -5px -5px 10px #222;color: #222;font-size: 16px;}button:hover {box-shadow: -5px -5px 15px #444, 5px 5px 15px #222, inset 5px 5px 10px #222, inset -5px -5px 10px #444;font-size: 15px;transition: 500ms;}button:focus {outline: none;}.red:hover {color: #f07171;text-shadow: 0px 0px 10px #f07171;}.green:hover {color: #93f071;text-shadow: 0px 0px 10px #93f071;}.blue:hover {color: #71b7f0;text-shadow: 0px 0px 10px #71b7f0;}.purple:hover {color: #b971f0;text-shadow: 0px 0px 10px #b971f0;}.white:hover {color: #ffffff;text-shadow: 0px 0px 10px #ffffff;}</style><script>function buttons(type){var location = window.location.href.split('?')[0];if (location.charAt(location.length - 1) != '/'){var location = location+'/';}window.location.href = location+'?color='+type;}</script><body><div><button class="noselect red" onclick="buttons('red')">Turn on red</button><button class="noselect green" onclick="buttons('green')">Turn on green</button></div><div><button class="noselect blue" onclick="buttons('blue')">Turn on blue</button><button class="noselect purple" onclick="buttons('purple')">Turn on purple</button></div>    <div><button class="noselect white" onclick="buttons('None')">clear</button></div></body></html>"""
    return html

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('', p))
  s.listen(Persons_to_connect)
except OSError:
  machine.reset()

while True:
  try:
    if gc.mem_free() < 102000:
        gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    try:
        request = str(conn.recv(1024).decode()).split()[1].split('=')[1]
        if request == 'green':
            show((0,255,0))
        elif request == 'red':
            show((255,0,0))
        elif request == 'blue':
            show((0,0,255))
        elif request == 'purple':
            show((255,0,255))
        elif request == 'None':
            clear()
    except:
        pass
    conn.settimeout(None)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError:
    conn.close()

