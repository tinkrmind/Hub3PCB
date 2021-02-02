import attiny
from smbus2 import SMBus

i2cbus = SMBus(1)

i2caddress = attiny.TWI_SLAVE_ADDRESS

def readFlags():
    return i2cbus.read_byte_data(i2caddress, attiny.FLAGS)

def readTime():
    return i2cbus.read_i2c_block_data(i2caddress,attiny.UNIX_TIME,attiny.UNIX_TIME_LENGTH) 


print(readFlags())
