import socketio

API_KEY = input("API Key: ")


sio = socketio.Client()


@sio.event
def connected(data):
    sio.emit('subscribe', ['trade:bitmex:XBTUSD'])


@sio.event
def trade(data):
    print(data)


sio.connect(f'https://markets.profitview.net?api_key={API_KEY}')