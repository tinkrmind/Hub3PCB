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
    print(t)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME, t)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME+1, t>>8)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME+2, t>>16)
    i2cbus.write_byte_data(i2caddress, attiny.UNIX_TIME+3, t>>24)

def readVbat():
    Vbat = i2cbus.read_i2c_block_data(i2caddress,attiny.ADC_VBATT,attiny.ADC_VBATT_LENGTH) 
    return (Vbat[0]+(Vbat[1]<<8))

def readIB():
    ib = i2cbus.read_i2c_block_data(i2caddress,attiny.ADC_IB,attiny.ADC_IB_LENGTH) 
    return (ib[0]+(ib[1]<<8))

def readVin():
    VIN = i2cbus.read_i2c_block_data(i2caddress,attiny.ADC_VIN,attiny.ADC_VIN_LENGTH) 
    return (VIN[0]+(VIN[1]<<8))

def readFanSpeed():
    return i2cbus.read_byte_data(i2caddress,attiny.FAN_SPEED) 
    
def writeFanSpeed(speed):
    #fan speed in %
    i2cbus.write_byte_data(i2caddress,attiny.FAN_SPEED, speed) 

print(readFlags())
print(readTime())
writeTime()
print(readTime())
print(readVbat())
print(readIB())
print(readVin())
print(readFanSpeed())
writeFanSpeed(50)
print(readFanSpeed())
