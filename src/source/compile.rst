Compile and Flash CH55x with SDCC
=================================

Running a Program
-----------------

To run the program, you will need to use a bash terminal. Follow these steps to clone the examples repository, navigate to the appropriate directory, and compile the project.

1. **Clone the Examples Repository**

   Begin by cloning the examples repository which contains the main code. Open your bash terminal and execute the following command:

   .. code-block:: bash

      git clone https://github.com/UNIT-Electronics/CH55x_SDCC_Examples

2. **Navigate to the Example Path**

   Once the repository is cloned, navigate to the path where the example programs are located. Use the following command to change the directory:

   .. code-block:: bash

      cd ~/CH55x_SDCC_Examples/Software/examples/Blink/

3. **Connect the Device**

   Connect your CH55x device to your computer. Ensure that you press and hold the BOOT button while connecting the device. This is essential for the device to enter programming mode.

4. **Compile the Project**

   To compile the project and generate the necessary files, execute the following command in your terminal:

   .. code-block:: bash

      make all

   This command will compile the project, resulting in the generation of files with various extensions necessary for flashing the microcontroller.

.. _files:

.. figure:: /_static/files.png
   :width: 80%
   :align: center
   :alt: sections of the code

   Compilation output files

Flashing the Program 
--------------------

Once the project is compiled, you need to flash the program onto the CH55x device. Follow these steps:

1. **Connect the Device**

   Ensure your CH55x device is connected and the BOOT button is pressed, as done during the compilation step.

2. **Flash the Program**

   Execute the following command to flash the compiled program onto the microcontroller:

   .. code-block:: bash

      make flash

   If the flashing process is successful, the code will generate a blinking effect on the connected LED, indicating that the program is running correctly.

.. _led:

.. figure:: /_static/led.png
   :width: 80%
   :align: center
   :alt: LED blinking

   LED blinking effect

Software Development Prototype
==============================

Loadupch
--------

The Loadupch is a software development prototype designed to facilitate the uploading of code to the CH552 microcontroller. It is a user-friendly tool that provides a graphical interface, making it easier for users to upload their code. The Loadupch tool is compatible with both Windows and Linux operating systems.

.. _loadupch:

.. figure:: /_static/loadupch.png
   :width: 50%
   :align: center
   :alt: Loadupch tool

   Loadupch tool interface

Installing Loadupch
~~~~~~~~~~~~~~~~~~~

.. warning::

   The Loadupch tool is currently under development and may contain bugs. Use it at your own risk.

To install the Loadupch tool, you can use `pypi`. Follow these steps:

1. **Install Loadupch**

   Use the following command to install the Loadupch tool via pip:

   .. code-block:: bash

      pip install loadupch

2. **Run Loadupch**

   After installation, you can run the Loadupch tool with the following command:

   .. code-block:: bash

      python -m loadupch

   This will launch the graphical interface of the Loadupch tool, allowing you to upload code to your CH552 microcontroller easily.

.. tip::

   If you need to uninstall the Loadupch tool for any reason, use the following command:

   .. code-block:: bash

      pip uninstall loadupch
