import attiny
from smbus2 import SMBus

i2cbus = SMBus(1)

i2caddress = attiny.TWI_SLAVE_ADDRESS

def readFlags():
    return i2cbus.read_byte_data(i2caddress, attiny.FLAGS)

def readTime():
    time = i2cbus.read_i2c_block_data(i2caddress,attiny.UNIX_TIME,attiny.UNIX_TIME_LENGTH) 
    return time[0]+(time[1]<<8)+(time[2]<<16)+(time[3]<<24)

def writeTime():
    import time
    t = int(time.time())
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME, t)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME, t>>8)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME, t>>16)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME, t>>24)


print(readFlags())
