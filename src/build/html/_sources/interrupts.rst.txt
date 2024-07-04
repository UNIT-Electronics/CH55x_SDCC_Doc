Interrupts
===========

The CH552 microcontroller supports 14 sets of interrupt signal sources. These include 6 sets of interrupts 
(INT0, T0, INT1, T1, UART0, and T2), which are compatible with the standard MCS51, and 8 sets of extended 
interrupts (SPI0, TKEY, USB, ADC, UART1, PWMX, GPIO, and WDOG). The GPIO interrupt can be chosen from 7 I/O 
pins.

.. list-table:: Default priority sequence of interrupt sources
   :widths: 20 20 10 30 20
   :header-rows: 1

   * -  Interrupt src.
     -  Entry addr.
     -  Interrupt #
     -  Description
     -  Default prio. seq.
   * - INT_NO_INT0
     - 0x0003
     - 0
     - External interrupt 0
     - High priority
   * - INT_NO_TMR0
     - 0x000B
     - 1
     - Timer 0 interrupt
     - ↓
   * - INT_NO_INT1
     - 0x0013
     - 2
     - External interrupt 1
     - ↓
   * - INT_NO_TMR1
     - 0x001B
     - 3
     - Timer 1 interrupt
     - ↓
   * - INT_NO_UART0
     - 0x0023
     - 4
     - UART0 interrupt
     - ↓
   * - INT_NO_TMR2
     - 0x002B
     - 5
     - Timer 2 interrupt
     - ↓
   * - INT_NO_SPI0
     - 0x0033
     - 6
     - SPI0 interrupt
     - ↓
   * - INT_NO_TKEY
     - 0x003B
     - 7
     - Touch key timer interrupt
     - ↓
   * - INT_NO_USB
     - 0x0043
     - 8
     - USB interrupt
     - ↓
   * - INT_NO_ADC
     - 0x004B
     - 9
     - ADC interrupt
     - ↓
   * - INT_NO_UART1
     - 0x0053
     - 10
     - UART1 interrupt
     - ↓
   * - INT_NO_PWMX
     - 0x005B
     - 11
     - PWM1/PWM2 interrupt
     - ↓
   * - INT_NO_GPIO
     - 0x0063
     - 12
     - GPIO Interrupt
     - ↓
   * - INT_NO_WDOG
     - 0x006B
     - 13
     - Watchdog timer interrupt
     - Low priority


The interrupt priority is determined by the interrupt number. 

Timer 0/1  Interrupts
---------------------

Timer0 and Timer1 are 16-bit timers/counters controlled by TCON and TMOD. TCON is responsible for timer/counter
T0 and T1 startup control, overflow interrupt, and external interrupt control. Each timer consists of dual
8-bit registers forming a 16-bit timing unit. Timer 0's high byte counter is TH0, and its low byte counter 
is TL0. Similarly, Timer 1's high byte counter is TH1, and its low byte counter is TL1. Timer 1 can also 
serve as the baud rate generator for UART0.
code example:: 

    void timer0_interrupt(void) __interrupt(INT_NO_TMR0)	/* Timer0 interrupt service routine (ISR) */
    {
        PIN_toggle(PIN_BUZZER);
        TH0 = 0xFF;      	/* 50ms timer value */
        TL0 = 0x00;      
    }


    int main(void)
    {
        CLK_config();  
        DLY_ms(5);
        PIN_output(PIN_BUZZER);
        EA  = 1;         	/* Enable global interrupt */
        ET0 = 1;         	/* Enable timer0 interrupt */
        
        TH0 = 0xFF;		/* 50ms timer value */
        TL0 = 0x00;      
        TMOD = 0x01;		/* Timer0 mode1 */
        TR0 = 1;  	      	/* Start timer0 */
        while(1);
    }

External Interrupts
-------------------

INT0 and INT1 are external interrupt input pins. When an external interrupt occurs, the corresponding 
interrupt service routine is executed. The external interrupt can be triggered by the falling edge,
rising edge, or both edges of the external interrupt input signal. The trigger mode is determined by the 
external interrupt input pin.

code example::
     
    void ext0_interrupt(void) __interrupt(INT_NO_INT0)
    {
        PIN_toggle(PIN_LED);  
    }

    int main(void)
    {
        CLK_config();  
        DLY_ms(5);
        PIN_output_OD(PIN_INT);  
        PIN_output(PIN_LED);
        
        EA  = 1;     /* Enable global interrupt */
        EX0 = 1;    // Enable INT0
        IT0 = 1;    // INT0 is edge triggered

        while(1)
        {
            // Do nothing
        }
        
    }