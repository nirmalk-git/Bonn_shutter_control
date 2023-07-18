import serial
import time as time


class shutter:
    # class attributes
    """
        A class for the Bonn Shutter

        ...

        Attributes
        -------------------
        port_name : str
            The name of port to which the Bonn shutter is connected to.
            For a windows machine it is a COM* port
            For a Linux machine it is /ttyUSB*
        Baud_rate : int
            the baud rate of serial data communication
        Bits_per_byte : int
            Number of data bits in byte data
        Stop_bits : int
            number of stop bits indicating end of a byte word.

        Methods
        -------------------

        """
    def __init__(self, port_name):
        self.port_name = port_name
        self.Baud_rate = 19200
        self.Bits_per_byte = 8
        self.Stop_bits = 1
        self.serialPort = serial.Serial(
            port=self.port_name,
            baudrate=self.Baud_rate,
            bytesize=self.Bits_per_byte,
            timeout=2,
            stopbits=serial.STOPBITS_ONE,
        )

    def start_interactive_session(self):
        """
        parameters: none
            Start an interactive session with the Bonn shutter. Checks if connection is established between
            Bonn shutter and pc.
        """
        print("Starting interactive session - - - -")
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            pass
        self.serialPort.write(b"ia 1 <CR> \r\n")
        time.sleep(5)
        self.serialPort.write(b"s?" + b"<CR> \r\n")
        time.sleep(2)
        data = []
        while True:
            if self.serialPort.readline() != b'':
                data.append(self.serialPort.readline())
            else:
                # print(len(data))
                # print('printing data after this', data)
                if len(data) < 4:
                    print("Bonn shutter connection not established.")
                else:
                    print("Bonn shutter connection established.")
                break

    def print_shutter_status(self):
        """
        parameters: None
            Print the status of the shutter, whether open or close,
            if close which blade is on the frame.


        """
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            self.serialPort.write(b"ss" + b"<CR> \r\n")
            while True:
                if self.serialPort.readline() != b'':
                    data = []
                    data.append(self.serialPort.readline())
                    print(data)
                else:
                    break

    # Opening the ports
    # The input is the initialised serial port
    def get_full_status(self):
        """
        parameters: None
            Prints the full status of the shutter.
        """
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            self.serialPort.write(b"ss" + b"<CR> \r\n")
            while True:
                if self.serialPort.readline() != b'':
                    data = []
                    data.append(self.serialPort.readline())
                    print(data)
                else:
                    break

    def open_shutter(self):
        """
        parameters: none
            Opens the shutter if closed.
        """
        print("opening shutter")
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            pass
        self.serialPort.write(b"os <CR> \r\n")
        time.sleep(2)
        return

    # Closing the port
    # input is the initialized serial port
    def close_shutter(self):
        """
        parameters: none
            Closes the shutter if open.
        """
        print("closing shutter")
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            pass
        self.serialPort.write(b"cs <CR> \r\n")
        time.sleep(2)
        return

    # Resetting everything to the factory default value
    def reset_fd(self):
        """
        parameters: none
            Reset shutter value to factory reset
        """
        # Reset everything to factory default
        print("Resetting everything to factory default value")
        if not self.serialPort.isOpen():
            self.serialPort.open()
        else:
            pass
        self.serialPort.write(b"fd <CR> \r\n")
        time.sleep(2)

    # set the exposure time
    def set_exposure_time(self, exp_time):
        """
        Parameters
        ----------
        exp_time : float
            The Bonn shutter opening time in milliseconds.
        """
        # exp_time is the shutter open time
        print("Setting exposure time as", exp_time, "ms")
        if not self.serialPort.isOpen():
            self.serialPort.open()
        if exp_time <= 1000:
            self.serialPort.write(b"ex " + str(exp_time).encode("Ascii") + b"<CR> \r\n")
            time.sleep(2)
        else:
            self.open_shutter()
            time.sleep((exp_time / 1000))
            self.close_shutter()

    # set the acceleration of the blade
    def set_acceleration(self, acc):
        """
        Parameters
        ----------
        acc : int
            The value of acceleration. Can be between 1 and 9.
            1 being the lowest and 9 being the highest acceleration.
        """
        # exp_time is the shutter open time
        print("Setting acceleration to m/s2", acc)
        if not self.serialPort.isOpen():
            self.serialPort.open()
        if acc < 10 or acc >= 1:
            self.serialPort.write(b"ac " + str(acc).encode("Ascii") + b"<CR> \r\n")
        else:
            print("Acceleration has to be between 1 and 10 ")



