import MAX98372

from smbus import SMBus

i2cbus = SMBus(1)

i2caddress = 0x32

def reset():
    i2cbus.write_byte_data(i2caddress, MAX_REG_SOFTWARE_RESET, RST)

def enable(enable):
    i2cbus.write_byte_data(i2caddress, MAX_REG_GLOBAL_ENABLE, ENABLE if enable else 0)

def begin():
    # Program the device to the desired mode of operation.
    i2cbus.write_byte_data(i2caddress, MAX_REG_PCM_MODE_CONFIG, CHANSZ_16);
    i2cbus.write_byte_data(i2caddress, 0x14, 0x40);

    i2cbus.write_byte_data(i2caddress, MAX_REG_PCM_SAMPLE_RATE_SETUP, SPK_SR_44_1KHZ);


    # Program the digital audio interface inputs and outputs.


    # Program the speaker output amplifier gain and set SPK_EN (this bit must only be toggled when EN is low).

    i2cbus.write_byte_data(i2caddress, MAX_REG_SPEAKER_ENABLE, 1);

    # Program the PVDD and thermal ADC.

    i2cbus.write_byte_data(i2caddress, MAX_REG_DYNAMIC_GAIN_ENABLE, PVADC_ENABLE);

    i2cbus.write_byte_data(i2caddress, MAX_REG_LIMITER_THRESHOLD, 3);

    i2cbus.write_byte_data(i2caddress, MAX_REG_PCM_RX_ENABLE_A, 1); # channel 0

    # print(i2cbus.read_byte_data(i2caddress, 0x34))

# reset()
# begin()
# enable(1)

print(i2cbus.read_byte_data(i2caddress, MAX_REG_REV_ID))