import socket

from app import create_app
from OSX import New_OSX
from main import new_row

app = create_app()
OSX = New_OSX()

from routes import *

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == '__main__':
    app.run(debug=True, host=get_ip(), port=5002)
    #