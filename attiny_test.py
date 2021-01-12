import attiny
from smbus import SMBus

i2cbus = SMBus(1)

i2caddress = attiny.TWI_SLAVE_ADDRESS

def readFlags():
    i2cbus.read_byte_data(i2caddress, attiny.FLAGS)

print(readFlags)