Compile and Flash CH55x with SDCC
===================================

Running a Program
---------------
To run the program, use a bash terminal.

Clone the examples with the main code::

    git clone https://github.com/Cesarbautista10/CH55x_SDCC_Examples.git


Navigate to the path::

    cd ~/CH55x_SDCC_Examples/Software/examples/0.\ Blink/


Connect a device with the BOOT button pressed.

Execute the command::

    make all


This will compile the project and generate files with the following extensions:


.. figure:: /_static/files.png
   :width: 80%
   :align: center
   :alt: GitHub authorization page

Flashing the Program 
---------------

Connect a device and press the BOOT button, then write the command::

    make flash


If the project is successful, the code will generate a blinking effect as shown below:


.. figure:: /_static/led.gif
   :width: 80%
   :align: center
   :alt: GitHub authorization page


