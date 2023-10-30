

from gps import *

if __name__ == "__main__":
    print("called ")
    session = gps()
    session.read()
    session.send('?DEVICES;')
    code = session.read()
    print("got code {}".format(code))
    response = session.data
    print("got response {}".format(response))
    devices = response['devices']
    if len(devices) == 0:
        raise Exception("no gps device")
    session.send('?WATCH={"enable":true,"json":true,"nmea":true}')
    while(True):
        try:
            data = session.next()
            print(f"{data}")
        except KeyError:
            # this happens when elevation is not included, we don't care
            pass
