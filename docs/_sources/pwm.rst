PWM (Pulse Width Modulation)
============================

The PWM module is used to generate a PWM signal on a pin. The PWM signal is generated by changing the duty cycle of the signal. The duty cycle is the ratio of the time the signal is high to the total time of the signal. The PWM module can be used to control the brightness of an LED, the speed of a motor, or the position of a servo motor.

The board contain two PWM pins, which are PIN_PWM and PIN_PWM2. The PWM module can be used to generate a PWM signal on these pins::

    PWM 1 : P30/P15
    PWM 2 : P31/P34

Some of the functions provided by the PWM module are::

    #define MIN_COUNTER 10
    #define MAX_COUNTER 254
    #define STEP_SIZE   10

    void change_pwm(int hex_value)
    {
        PWM_write(PIN_PWM, hex_value);
    }
    void main(void) 
    {
        CLK_config();                          
        DLY_ms(5);                            
        PWM_set_freq(1);                    
        PIN_output(PIN_PWM);       
        PWM_start(PIN_PWM);      
        PWM_write(PIN_PWM, 0);
    while (1) 
    {
        for (int i = MIN_COUNTER; i < MAX_COUNTER; i+=STEP_SIZE) 
        {
            change_pwm(i);
            DLY_ms(20);
        }
        for (int i = MAX_COUNTER; i > MIN_COUNTER; i-=STEP_SIZE)
        {
            change_pwm(i);
            DLY_ms(20);
        }      
    }
    }

