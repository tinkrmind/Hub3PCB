TWI_SLAVE_ADDRESS  = 0x05

FLAGS_BOOST_OFF  = 0x80
# 	State of the BOOST_OFF pin, 1 = boost active.
 
FLAGS_CHARGE_OFF  = 0x40
# 	State of the CHARGE_OFF pin, 1 = charge active.

FLAGS_AOK  = 0x20
# 	State of the AOK input, 0 = input voltage present.
 
FLAGS_BOOST  = 0x10
# 	State of the BOOST input, 0 = boost is running.
 
FLAGS_CHG  = 0x08
# 	State of the CHG input, 0 = battry is charging.
 
FLAGS_BUTTON  = 0x01
# 	State of the POWER BUTTON, 1 = pressed.

# volatile uint8_t 	identifier
#  	reg 0, READONLY, fixed value 0x47, used for identification

 
# volatile uint8_t 	flags
#  	reg 1, READONLY, various flags, see Register Flags
 
# volatile uint32_t 	unix_time
#  	reg 2-5, READ/WRITE, UNIX timestamp
 
# volatile uint16_t 	adc_vbatt
#  	reg 6-7, READONLY, battery voltage in mV
 
# volatile uint16_t 	adc_ib
#  	reg 8-9, READONLY, battery charge/discharge current in mA
 
# volatile uint16_t 	adc_vin
#  	reg 10-11, READONLY, input voltage in mV
 
# volatile uint8_t 	fan_speed
#  	reg 12, READ/WRITE, fan speed setting in %