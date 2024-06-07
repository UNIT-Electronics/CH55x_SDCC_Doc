I2C (Inter-Integrated Circuit) 
==============================

I2C is a serial communication protocol, so data is transferred bit by bit along a single wire (the SDA line). The SCL line is used to synchronize the data transfer. The I2C protocol is a master-slave protocol, which means that the communication is always initiated by the master device. A master device can communicate with one or multiple slave devices. 

.. note::
    The microcontroller use bit banging to communicate with the I2C devices. 

All pin configurations are defined in the `config.h` file. The I2C pins are defined as follows

.. list-table:: I2C Pinout
   :widths: 20 20 20
   :header-rows: 1
   :align: center

   * - PIN
     - I2C 1
     - I2C 2
   * - SDA
     - P15
     - P31
   * - SCLK
     - P32
     - P30

SSD1306 Display
~~~~~~~~~~~~~~~

.. _figura-ssd1306-display:

.. figure:: /_static/oled.jpg
   :align: center
   :alt: ssd1306 display
   :width: 50%

   SSD1306 Display

The OLED display is a 128x64 pixel monochrome display that uses the I2C protocol for communication::
             
    void beep(void) {
    uint8_t i;
    for(i=255; i; i--) {
        PIN_low(PIN_BUZZER);
        DLY_us(125);
        PIN_high(PIN_BUZZER);
        DLY_us(125);
    }
    }

    void main(void) {
    // Setup
    CLK_config();                           // configure system clock
    DLY_ms(5);                              // wait for clock to stabilize

    OLED_init();                            // init OLED

    OLED_print("*  UNITelectronics  *");
    OLED_print("---------------------\n");
    OLED_print("Ready\n");
    beep();
    while(1) {

    }
    }
