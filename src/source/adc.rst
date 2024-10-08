Analog to Digital Converter (ADC)
==================================

The CH552 has four ADC channels, which can be used to read analog values from sensors. The ADC channels are multiplexed with the GPIO pins, so you can use any GPIO pin as an ADC input. 
the distribution of the ADC channels is as follows.

.. list-table:: Pin Mapping
   :widths: 10 20
   :header-rows: 1
   :align: center

   * - PIN
     - ADC Channel
   * - A0
     - P1.1
   * - A1
     - P1.4
   * - A2
     - P1.5
   * - A3
     - P3.2


The ADC has a resolution of 8 bits, which means it can read values from 0 to 255. The ADC can be configured to read values from 0 to 5V, or from 0 to 3.3V, depending on the VCC voltage::

    #include "src/config.h" // user configurations
    #include "src/system.h" // system functions
    #include "src/gpio.h"   // for GPIO
    #include "src/delay.h"  // for delays

    void main(void)
    {
        CLK_config();
        DLY_ms(5);

        ADC_input(PIN_ADC);

        ADC_enable();
        while (1)
        {
            int data = ADC_read(); // Assuming ADC_read() returns an int
        }
    }


