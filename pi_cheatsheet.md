# Pi cheatsheet

## Show I2C devices-

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
#OR
i2cdetect -l
```

## Enabling I2C bus 4-

In /boot/config.txt:

```bash
dtparam=i2c_arm=off
dtparam=i2c_arm=on
dtoverlay=i2c4,pins_6_7
# (board pins 31, 26)
dtoverlay=i2c1,pins_2_3
# (board pins  3,  5)
```

I2C bus 4 should show up as /dev/i2c-4

## Enabling UART 5-

In /boot/config.txtL

```bash
dtoverlay=uart5
```

Serial bus should show up as /dev/ttyAMA4