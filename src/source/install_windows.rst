Environment Setup on Windows
===================================
This section provides a step-by-step guide to setting up the SDCC compiler on Windows operating systems. 
It also includes instructions for installing the necessary tools and configuring the environment variables. 
Additionally, it covers the installation of the pyusb library and updating the driver using Zadig.

Compiler Installation
---------------------

Follow these steps to install the necessary tools and files:

1. **Download or Clone the Repository**

   You can either download the repository as a ZIP file or clone it using Git.

   a. **Clone via Git**

      Install Git for Windows from the `official Git website <https://git-scm.com/download>`_.
      Then open a command prompt and run::

          git clone https://github.com/UNIT-Electronics-MX/unit_ch55x_sdk.git

   b. **Download as ZIP**

      Download the ZIP file from the `GitHub repository <https://github.com/UNIT-Electronics-MX/unit_ch55x_sdk/archive/refs/heads/main.zip>`_
      and extract it to a desired location on your computer.

2. **Install CH372 Driver**
   Download the latest version of the CH372 driver from the `CH372 driver website <https://www.wch-ic.com/downloads/CH372DRV_EXE.html>`_.

3. **Install Python**
   Download and install the latest version of Python from the `official Python website <https://www.python.org/downloads/>`_.

4. **Install Editor Code**
   Download and install the latest version of your preferred text editor. Some popular choices include `Visual Studio Code <https://code.visualstudio.com/Download>`_, Sublime Text, and Notepad++.

5. **Install PlatformIO IDE**
   Download and install the latest version of Platformio IDE from the visual studio code extensions like in the next image:

.. _download_platformio:
.. figure:: /_static/platformIO.png
   :align: center
   :alt: Installing PlatformIO IDE.
   :width: 90%

   Installing PlatformIO IDE

   You can also install PlatformIO IDE from the `official Platformio website <https://platformio.org/install/ide?install=vscode>`_.

.. tip::  
    It is recommended to install the tools in the order listed above.

.. caution::  
    Remember to restart your computer after installing the tools.


Alternative Functionality
-------------------------

WCHISPTool
~~~~~~~~~~

The WCHISPTool is an official programming tool provided by WCH. It is a Windows-based tool that allows users to flash firmware onto CH55x microcontrollers. 
To use the WCHISPTool, follow these steps:

1. **Download the WCHISPTool**

   Download the `WCHISPTool <https://www.wch-ic.com/downloads/WCHISPTool_Setup_exe.html>`_ from the official WCH website.

2. **Install the WCHISPTool**

   Install the WCHISPTool on your Windows computer by following the on-screen instructions.

3. **Connect the Device**

   Connect your CH55x device to your computer using a USB cable. Ensure that the BOOT button is pressed while connecting the device.

4. **Flash the Program**

   Open the WCHISPTool and select the appropriate firmware file. Click the "Download" button to flash the program onto the microcontroller.

.. note::

   The WCHISPTool is a Windows-based tool and may not be compatible with other operating systems.

.. _wchisptool-interface:

.. figure:: /_static/wchisptool.png
   :width: 80%
   :align: center
   :alt: WCHISPTool interface

   WCHISPTool interface

.. warning::

   The WCHISPTool is an official tool provided by WCH and may have limitations compared to other flashing methods.

.. note::

   Requires the `ch372 <https://www.wch-ic.com/downloads/CH372DRV_EXE.html>`_ driver to be installed.


