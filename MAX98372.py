MAX_ADDR_DEFAULT= 0x32


 MAX_REG_INTERRUPT_STATUS_0      = 0x01
 MAX_REG_INTERRUPT_STATUS_1      = 0x02
 MAX_REG_INTERRUPT_STATE_0       = 0x03
 MAX_REG_INTERRUPT_STATE_2       = 0x04
 MAX_REG_INTERRUPT_FLAG_0        = 0x05
 MAX_REG_INTERRUPT_FLAG_1        = 0x06
 MAX_REG_INTERRUPT_ENABLE_0      = 0x07
 MAX_REG_INTERRUPT_ENABLE_1      = 0x08
 MAX_REG_INTERRUPT_CLEAR_0       = 0x09
 MAX_REG_INTERRUPT_CLEAR_1       = 0x0A
 MAX_REG_LIVE_STATUS             = 0x0B
 MAX_REG_STATE_1                 = 0x0C
 MAX_REG_FLAG_1                  = 0x0D
 MAX_REG_IRQ_ENABLE_1            = 0x0E
 MAX_REG_IRQ_CLEAR_1             = 0x0F

 MAX_REG_PCM_CLOCK_SETUP         = 0x10
     BSEL_32                     = 0x02    // default
     BSEL_48                     = 0x03
     BSEL_64                     = 0x04
     BSEL_96                     = 0x05
     BSEL_128                    = 0x06
     BSEL_192                    = 0x07
     BSEL_256                    = 0x08
     BSEL_384                    = 0x09
     BSEL_512                    = 0x0A

 MAX_REG_PCM_SAMPLE_RATE_SETUP   = 0x11
     SPK_SR_32KHZ                = 0x06
     SPK_SR_44_1KHZ              = 0x07
     SPK_SR_48KHZ                = 0x08    // default
     SPK_SR_88_2KHZ              = 0x0A
     SPK_SR_96KHZ                = 0x0B

 MAX_REG_PCM_MODE_CONFIG         = 0x14
     CHANSZ_8                    = 0x00
     CHANSZ_16                   = 0x40
     CHANSZ_24                   = 0x80    // default
     CHANSZ_32                   = 0xC0

     FORMAT_I2S                  = 0x00    // default
     FORMAT_LEFT_JUSTIFIED       = 0x08
     FORMAT_RIGHT_JUSTIFIED      = 0x10
     FORMAT_TDM_MODE_1           = 0x18
     FORMAT_TDM_MODE_2           = 0x20

     BCLEDGE                     = 0x04

     CHANSEL_FALLLING            = 0x00    // default
     CHANSEL_RISING              = 0x02


 MAX_REG_PCM_RX_ENABLE_A         = 0x15
 MAX_REG_PCM_RX_ENABLE_B         = 0x16
 MAX_REG_PCM_MONOMIX_CH_SRC      = 0x18
 MAX_REG_PCM_MONOMIX_CONFIG      = 0x19

 MAX_REG_DIGITAL_FILTER          = 0x1C
 MAX_REG_DAC_BQ_B0_H             = 0x1D
 MAX_REG_DAC_BQ_B0_M             = 0x1E
 MAX_REG_DAC_BQ_B0_L             = 0x1F

 MAX_REG_DAC_BQ_B1_H             = 0x20
 MAX_REG_DAC_BQ_B1_M             = 0x21
 MAX_REG_DAC_BQ_B1_L             = 0x22

 MAX_REG_DAC_BQ_B2_H             = 0x23
 MAX_REG_DAC_BQ_B2_M             = 0x24
 MAX_REG_DAC_BQ_B2_L             = 0x25

 MAX_REG_DAC_BQ_A0_H             = 0x26
 MAX_REG_DAC_BQ_A0_M             = 0x27
 MAX_REG_DAC_BQ_A0_L             = 0x28

 MAX_REG_DAC_BQ_A1_H             = 0x29
 MAX_REG_DAC_BQ_A1_M             = 0x2A
 MAX_REG_DAC_BQ_A1_L             = 0x2B

 MAX_REG_DIGITAL_VOLUME          = 0x2D    // 0 = 0dB, 126 = -64.5dB, 127 = mute
     DVOL_RAMP_BYP               = 0x80

 MAX_REG_PATH_GAIN               = 0x2E
     DPGA_CLIP_MASK              = 0xF0    // 0.5 per bit up to 6 (= 0xA0)
     SPK_GAIN_MAX_MASK           = 0x0F    // see DS page 54



 MAX_REG_DHT_ROTATION_POINT      = 0x31
 MAX_REG_DHT_ATTACK              = 0x32
 MAX_REG_DHT_RELEASE             = 0x33

 MAX_REG_PVDD_ADC_MEASUREMENT    = 0x34
 MAX_REG_THERMAL_FOLDBACK        = 0x36
 MAX_REG_THERMAL_ADC_MEASUREMENT = 0x37
 MAX_REG_THERMAL_FOLDBACK_MIN_T  = 0x38
 MAX_REG_THERMAL_FOLDBACK_FILTER = 0x39

 MAX_REG_PCM2_RXDHT_ENABLE_A     = 0x3A
 MAX_REG_PCM2_RXDHT_ENABLE_B     = 0x3B

 MAX_REG_PCM2_RXTHM_ENABLE_A     = 0x3C
 MAX_REG_PCM2_RXTHM_ENABLE_B     = 0x3D

 MAX_REG_PCM2_TX_ENABLE_A        = 0x3E
 MAX_REG_PCM2_TX_ENABLE_B        = 0x3F

 MAX_REG_PCM2_DATA_ORDER_SELECT  = 0x40

 MAX_REG_PCM2_HIZ_MANUAL_MODE    = 0x41
 MAX_REG_PCM2_TX_HIZ_ENABLE_A    = 0x42
 MAX_REG_PCM2_TX_HIZ_ENABLE_B    = 0x43

 MAX_REG_SSM_CONFIG              = 0x49
 MAX_REG_SPEAKER_ENABLE          = 0x4A
 MAX_REG_DYNAMIC_GAIN_ENABLE     = 0x4B
     PVADC_ENABLE                = 0x04
     LIMITER_ENABLE              = 0x02
     DHT_ENABLE                  = 0x01
 MAX_REG_THERMAL_FOLDBACK_ENABLE = 0x4C
 MAX_REG_RESTART_BEHAVIOUR       = 0x4D
 MAX_REG_ICC_LINK_ENABLE         = 0x4E
 MAX_REG_GLOBAL_ENABLE           = 0x50
     ENABLE                      = 0x01

 MAX_REG_SOFTWARE_RESET          = 0x51
     RST                         = 0x01

 MAX_REG_LIMITER_ATTACK_RELEASE  = 0x55

 MAX_REG_DIGITAL_FILTER_DITHER   = 0x57
 MAX_REG_LIMITER_THRESHOLD       = 0x58
 MAX_REG_LIMITER_MAN_THRESHOLD   = 0x59
 MAX_REG_ICC_PAD_CONTROL         = 0x5C
 MAX_REG_PCM2_RXALC_ENABLE_A     = 0x60
 MAX_REG_PCM2_RXALC_ENABLE_B     = 0x61
 MAX_REG_ALC_THRESHOLD           = 0x62
 MAX_REG_ALC_ATTACK              = 0x63
 MAX_REG_ALC_ATTEN_RLS           = 0x64
 MAX_REG_ALC_INFINITE_HOLD_REL   = 0x65
 MAX_REG_ALC_CONFIG              = 0x66

 MAX_REG_REV_ID                  = 0xFF



#\************************************************************************#
#\!
#    @brief Constructor for MAX98372 Class
#
#\************************************************************************#
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
