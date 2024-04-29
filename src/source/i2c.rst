I2C (Inter-Integrated Circuit) 
==============================
Description
-----------
I2C is a serial communication protocol, so data is transferred bit by bit along a single wire (the SDA line). The SCL line is used to synchronize the data transfer. The I2C protocol is a master-slave protocol, which means that the communication is always initiated by the master device. A master device can communicate with one or multiple slave devices. The master device generates the clock signal and initiates the data transfer. The slave devices are addressed by the master device, and they respond to the master device based on the address they are assigned. The I2C protocol supports multiple devices on the same bus, and each device has a unique address. This allows multiple devices to communicate with each other using the same bus.

.. note::
    The microcontroller use bit banging to communicate with the I2C devices. 

All pin configurations are defined in the config.h file. The I2C pins are defined as follows::
    
        #define I2C_SCL_PIN  P32
        #define I2C_SDA_PIN  P15

OLED Display SD1306
-------------------
The OLED display is a 128x64 pixel monochrome display that uses the I2C protocol for communication. The display has a built-in controller that handles the display refresh and data transfer. The display is controlled by the microcontroller using the I2C protocol. The display has a resolution of 128x64 pixels, which allows it to display text, graphics, and images. The display is monochrome, which means that it can only display one color (white) on a black background. The display has a built-in controller that handles the display refresh and data transfer. The display is controlled by the microcontroller using the I2C protocol. The display has a resolution of 128x64 pixels, which allows it to display text, graphics, and images. The display is monochrome, which means that it can only display one color (white) on a black background::
             
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
