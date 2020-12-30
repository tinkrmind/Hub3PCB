# PiUPDI
Testing UPDI programming on AVR chips using RPi

## Resources:
* Guide: https://www.omzlo.com/articles/baremetal-programming-on-the-tinyavr-0-micro-controllers

## Results:

Ensure pyupdi is working : 
```
> pyupdi -d tiny817 -c COM46 -i
Device info: {'family': 'tinyAVR', 'nvm': 'P:0', 'ocd': 'D:0', 'osc': '3', 'device_id': '1E9320', 'device_rev': '0.1'}
```

Generate the .elf file from main.c :
```
C:\PROJECTS\Annunciator\UPDI\avr8-gnu-toolchain-3.6.2.1778-win32.any.x86\avr8-gnu-toolchain-win32_x86\bin\avr-gcc -mmcu=attiny817 -B C:\PROJECTS\Annunciator\UPDI\Atmel.ATtiny_DFP.1.8.332\gcc\dev\attiny817\ -O3 -I C:\PROJECTS\Annunciator\UPDI\Atmel.ATtiny_DFP.1.8.332\include\ -DF_CPU=20000000L -o attiny817-test.elf main.c
```

Generate the .hex file : 
```
> avr-objcopy -O ihex -R .eeprom attiny817-test.elf attiny817-test.hex
```

Program :
```
> pyupdi -d tiny817 -c COM46 -f attiny817-test.hex                            
Device info: {'family': 'tinyAVR', 'nvm': 'P:0', 'ocd': 'D:0', 'osc': '3', 'device_id': '1E9320', 'device_rev': '0.1'}  Programming successful                      
```
