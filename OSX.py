import pyvisa

class New_OSX():
    def __init__(self):
        # print(f"In find_osx_device")
        rm = pyvisa.ResourceManager()
        instruments = rm.list_resources()
        # Scan the found instruments for an OSX device.
        # If one is found then return it, otherwise return None.
        # NOTE: IF multiple OSXs are connected to the computer
        # this will ony return the first one found.
        r = [s for s in instruments if s.startswith('USB0::')]
        for i in r:
            self.instrument = rm.open_resource(i, open_timeout=5000)
            self.instrument.timeout = 10000
            self.instrument.query_delay = 0
            self.instrument.write_termination = '\n'
            self.instrument.read_termination = '\n'
            resp = self.instrument.query('*IDN?')
            # print(resp)
            self.idn = resp.split(',')
            if self.idn[1] == 'osx' or self.idn[1] == 'OSX':
                print('OSX Created')
        self.num_channel=int(self.instrument.query("CFG:SWT0:END?"))
