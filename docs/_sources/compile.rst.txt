Compile and Flash CH55x with SDCC
===================================

Running a Program
---------------
To run the program, use a bash terminal.

Clone the examples with the main code::

    git clone https://github.com/UNIT-Electronics/CH55x_SDCC_Examples


Navigate to the path::

    cd ~/CH55x_SDCC_Examples/Software/examples/Blink/


Connect a device with the BOOT button pressed.

Execute the command::

    make all


This will compile the project and generate files with the following extensions:

.. _files:

.. figure:: /_static/files.png
   :width: 80%
   :align: center
   :alt: sections of the code
   
   command line



Flashing the Program 
---------------

Connect a device and press the BOOT button, then write the command::

    make flash


If the project is successful, the code will generate a blinking effect as shown below:

.. _led:

.. figure:: /_static/led.png
   :width: 80%
   :align: center
   
   LED blinking


Software Development prototype
----------------

Loadupch 
~~~~~~~~~~~~~~~~~~~~~~

The Loadupch is a software development prototype that allows users to upload code to the CH552 microcontroller. It is a simple and easy-to-use tool that provides a graphical interface for uploading code to the microcontroller. The Loadupch tool is available for Windows and Linux operating systems.

.. _loadupch:

.. figure:: /_static/loadupch.png
   :width: 60%
   :align: center
   :alt: Loadupch tool

   Loadupch tool

Installing Loadupch
~~~~~~~~~~~~~~~~~~~~~~

.. Warning::
   The Loadupch tool is still under development and may contain bugs. Use it at your own risk.

Use pypi to install the `Loadupch tool <https://pypi.org/project/loadupch/>`_::

    pip install loadupch

run the Loadupch tool::

    python -m loadupch

.. tip::
    To uninstall the Loadupch tool, use the following command::

        pip uninstall loadupch

