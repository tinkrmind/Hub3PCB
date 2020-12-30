#ifndef _MAX98372_H_
#define _MAX98372_H_

#include <Wire.h>
#include <Arduino.h>

#define MAX_ADDR_DEFAULT                0x32


#define MAX_REG_INTERRUPT_STATUS_0      0x01
#define MAX_REG_INTERRUPT_STATUS_1      0x02
#define MAX_REG_INTERRUPT_STATE_0       0x03
#define MAX_REG_INTERRUPT_STATE_2       0x04
#define MAX_REG_INTERRUPT_FLAG_0        0x05
#define MAX_REG_INTERRUPT_FLAG_1        0x06
#define MAX_REG_INTERRUPT_ENABLE_0      0x07
#define MAX_REG_INTERRUPT_ENABLE_1      0x08
#define MAX_REG_INTERRUPT_CLEAR_0       0x09
#define MAX_REG_INTERRUPT_CLEAR_1       0x0A
#define MAX_REG_LIVE_STATUS             0x0B
#define MAX_REG_STATE_1                 0x0C
#define MAX_REG_FLAG_1                  0x0D
#define MAX_REG_IRQ_ENABLE_1            0x0E
#define MAX_REG_IRQ_CLEAR_1             0x0F

#define MAX_REG_PCM_CLOCK_SETUP         0x10
    #define BSEL_32                     0x02    // default
    #define BSEL_48                     0x03
    #define BSEL_64                     0x04
    #define BSEL_96                     0x05
    #define BSEL_128                    0x06
    #define BSEL_192                    0x07
    #define BSEL_256                    0x08
    #define BSEL_384                    0x09
    #define BSEL_512                    0x0A

#define MAX_REG_PCM_SAMPLE_RATE_SETUP   0x11
    #define SPK_SR_32KHZ                0x06
    #define SPK_SR_44_1KHZ              0x07
    #define SPK_SR_48KHZ                0x08    // default
    #define SPK_SR_88_2KHZ              0x0A
    #define SPK_SR_96KHZ                0x0B

#define MAX_REG_PCM_MODE_CONFIG         0x14
    #define CHANSZ_8                    0x00
    #define CHANSZ_16                   0x40
    #define CHANSZ_24                   0x80    // default
    #define CHANSZ_32                   0xC0

    #define FORMAT_I2S                  0x00    // default
    #define FORMAT_LEFT_JUSTIFIED       0x08
    #define FORMAT_RIGHT_JUSTIFIED      0x10
    #define FORMAT_TDM_MODE_1           0x18
    #define FORMAT_TDM_MODE_2           0x20

    #define BCLEDGE                     0x04

    #define CHANSEL_FALLLING            0x00    // default
    #define CHANSEL_RISING              0x02


#define MAX_REG_PCM_RX_ENABLE_A         0x15
#define MAX_REG_PCM_RX_ENABLE_B         0x16
#define MAX_REG_PCM_MONOMIX_CH_SRC      0x18
#define MAX_REG_PCM_MONOMIX_CONFIG      0x19

#define MAX_REG_DIGITAL_FILTER          0x1C
#define MAX_REG_DAC_BQ_B0_H             0x1D
#define MAX_REG_DAC_BQ_B0_M             0x1E
#define MAX_REG_DAC_BQ_B0_L             0x1F

#define MAX_REG_DAC_BQ_B1_H             0x20
#define MAX_REG_DAC_BQ_B1_M             0x21
#define MAX_REG_DAC_BQ_B1_L             0x22

#define MAX_REG_DAC_BQ_B2_H             0x23
#define MAX_REG_DAC_BQ_B2_M             0x24
#define MAX_REG_DAC_BQ_B2_L             0x25

#define MAX_REG_DAC_BQ_A0_H             0x26
#define MAX_REG_DAC_BQ_A0_M             0x27
#define MAX_REG_DAC_BQ_A0_L             0x28

#define MAX_REG_DAC_BQ_A1_H             0x29
#define MAX_REG_DAC_BQ_A1_M             0x2A
#define MAX_REG_DAC_BQ_A1_L             0x2B

#define MAX_REG_DIGITAL_VOLUME          0x2D    // 0 = 0dB, 126 = -64.5dB, 127 = mute
    #define DVOL_RAMP_BYP               0x80

#define MAX_REG_PATH_GAIN               0x2E
    #define DPGA_CLIP_MASK              0xF0    // 0.5 per bit up to 6 (0xA0)
    #define SPK_GAIN_MAX_MASK           0x0F    // see DS page 54



#define MAX_REG_DHT_ROTATION_POINT      0x31
#define MAX_REG_DHT_ATTACK              0x32
#define MAX_REG_DHT_RELEASE             0x33

#define MAX_REG_PVDD_ADC_MEASUREMENT    0x34
#define MAX_REG_THERMAL_FOLDBACK        0x36
#define MAX_REG_THERMAL_ADC_MEASUREMENT 0x37
#define MAX_REG_THERMAL_FOLDBACK_MIN_T  0x38
#define MAX_REG_THERMAL_FOLDBACK_FILTER 0x39

#define MAX_REG_PCM2_RXDHT_ENABLE_A     0x3A
#define MAX_REG_PCM2_RXDHT_ENABLE_B     0x3B

#define MAX_REG_PCM2_RXTHM_ENABLE_A     0x3C
#define MAX_REG_PCM2_RXTHM_ENABLE_B     0x3D

#define MAX_REG_PCM2_TX_ENABLE_A        0x3E
#define MAX_REG_PCM2_TX_ENABLE_B        0x3F

#define MAX_REG_PCM2_DATA_ORDER_SELECT  0x40

#define MAX_REG_PCM2_HIZ_MANUAL_MODE    0x41
#define MAX_REG_PCM2_TX_HIZ_ENABLE_A    0x42
#define MAX_REG_PCM2_TX_HIZ_ENABLE_B    0x43

#define MAX_REG_SSM_CONFIG              0x49
#define MAX_REG_SPEAKER_ENABLE          0x4A
#define MAX_REG_DYNAMIC_GAIN_ENABLE     0x4B
    #define PVADC_ENABLE                0x04
    #define LIMITER_ENABLE              0x02
    #define DHT_ENABLE                  0x01
#define MAX_REG_THERMAL_FOLDBACK_ENABLE 0x4C
#define MAX_REG_RESTART_BEHAVIOUR       0x4D
#define MAX_REG_ICC_LINK_ENABLE         0x4E
#define MAX_REG_GLOBAL_ENABLE           0x50
    #define ENABLE                      0x01

#define MAX_REG_SOFTWARE_RESET          0x51
    #define RST                         0x01

#define MAX_REG_LIMITER_ATTACK_RELEASE  0x55

#define MAX_REG_DIGITAL_FILTER_DITHER   0x57
#define MAX_REG_LIMITER_THRESHOLD       0x58
#define MAX_REG_LIMITER_MAN_THRESHOLD   0x59
#define MAX_REG_ICC_PAD_CONTROL         0x5C
#define MAX_REG_PCM2_RXALC_ENABLE_A     0x60
#define MAX_REG_PCM2_RXALC_ENABLE_B     0x61
#define MAX_REG_ALC_THRESHOLD           0x62
#define MAX_REG_ALC_ATTACK              0x63
#define MAX_REG_ALC_ATTEN_RLS           0x64
#define MAX_REG_ALC_INFINITE_HOLD_REL   0x65
#define MAX_REG_ALC_CONFIG              0x66

#define MAX_REG_REV_ID                  0xFF



/**************************************************************************/
/*!
    @brief Constructor for MAX98372 Class
*/
/**************************************************************************/
class MAX98372 {
 public:
  MAX98372();
  bool begin(uint8_t addr = MAX_ADDR_DEFAULT);

  void reset(void);
  void enable(bool enable);

  void set_gain(float pregain, float supply_voltage);

  void set_volume(uint8_t vol, uint8_t ramp = 0 );

  byte get_revision_id(void);
  byte get_pvdd_adc(void);
  byte get_themal_adc(void);

// protected:
  void writeRegister8(uint8_t reg, uint8_t data);
  byte readRegister(byte reg);
  uint8_t _i2caddr;  ///< The I2C address we expect to find the chip
};

#endif
