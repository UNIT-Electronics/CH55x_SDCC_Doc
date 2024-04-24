Analog to Digital Converter (ADC) 
===
The CH552 has a single 8-bit ADC which can be used to read analog voltages and convert them to a digital value.
You can construct such and ADC using the following code:

Code
---
.. code-block:: c
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