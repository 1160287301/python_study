# -*- coding:utf-8 -*-
import json

import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        time.sleep(0.05)
        ws.send('2probe')
        time.sleep(0.05)
        ws.send(5)
        time.sleep(0.05)
        ws.send(json.dumps('42["lconfig","{\"cId\":\"54490183810027\",\"liveInfo\":{\"liveId\":\"1474035735278\",\"showId\":\"1542542572690901\",\"starId\":\"404349330\"},\"data\":{\"rank\":true}}"]'))
        while True:
            time.sleep(5)
            ws.send(2)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    headers = {
        'Connection': 'Upgrade',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Upgrade': 'websocket',
        'Origin': 'https://web.immomo.com',
        'Sec-WebSocket-Version': '13',
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': 's_id=b56539b82e04726f47bd16f8884155bd; io=Bfi63DwgS4ACZMQxlCbp',
        'Sec-WebSocket-Key': 'yYAcpjHZX2wKqqJce6bhWQ==',
        'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    }
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://web-ws.immomo.com/socket.io/?EIO=3&transport=websocket&sid=Bfi63DwgS4ACZMQxlCbp",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()