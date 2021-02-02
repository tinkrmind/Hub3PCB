TWI_SLAVE_ADDRESS  = 0x05

FLAGS_BOOST_OFF  = 7
#0x80
# 	State of the BOOST_OFF pin, 1 = boost active.
 
FLAGS_CHARGE_OFF  = 6
#0x40
# 	State of the CHARGE_OFF pin, 1 = charge active.

FLAGS_AOK  = 5
#0x20
# 	State of the AOK input, 0 = input voltage present.
 
FLAGS_BOOST  = 4
#0x10
# 	State of the BOOST input, 0 = boost is running.
 
FLAGS_CHG  = 3
#0x08
# 	State of the CHG input, 0 = battry is charging.
 
FLAGS_BUTTON  = 0
#0x01
# 	State of the POWER BUTTON, 1 = pressed.

ID = 0x00
# volatile uint8_t 	identifier
#  	reg 0, READONLY, fixed value 0x47, used for identification

FLAGS = 0x01
# volatile uint8_t 	flags
#  	reg 1, READONLY, various flags, see Register Flags

UNIX_TIME = 0x02
UNIX_TIME_LENGTH = 4
# volatile uint32_t 	unix_time
#  	reg 2-5, READ/WRITE, UNIX timestamp

ADC_VBATT = 0x06
ADC_VBATT_LENGTH = 2
VBATT_MULTIPLIER = 656/128
# volatile uint16_t 	adc_vbatt
#  	reg 6-7, READONLY, battery voltage in mV

ADC_IB = 0x08
ADC_IB_LENGTH = 2
IB_MULTIPLIER = 781/64
# volatile uint16_t 	adc_ib
#  	reg 8-9, READONLY, battery charge/discharge current in mA

ADC_VIN = 0x0A
ADC_VIN_LENGTH = 2
VIN_MULTIPLIER = 521/128
# volatile uint16_t 	adc_vin
#  	reg 10-11, READONLY, input voltage in mV

FAN_SPEED = 0X0C
# volatile uint8_t 	fan_speed
#  	reg 12, READ/WRITE, fan speed setting in %
