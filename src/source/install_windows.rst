Environment for CH55x with SDCC and Windows
===================================

Compiler Installation 
---------------

Follow the steps below to install the necessary tools

- Installing Git for Windows
    Download and install `Git <https://git-scm.com/downloads>`_ for Windows from the official Git website.

- Installing SDCC
    Download and install the latest version of SDCC. You can find the latest version on the SDCC downloads page.
    `here a alternative <https://sourceforge.net/projects/sdcc/>`_

- Installing MinGW
    Install MinGW, which is a set of tools for software development on Windows. You can download the installer from the official MinGW website.
    `here a alternative <https://sourceforge.net/projects/mingw/>`_ 

- Installig Zadig
    Download the latest version of `Zadig <https://zadig.akeo.ie/>`. You can download in a official website.

Configuring MAKE
---------------


Remember that for Windows operating systems, an extra step is necessary, which is to open the environment variable -> Edit environment variable::

    C:\MinGW\bin



Locate the file


.. figure:: https://raw.githubusercontent.com/Cesarbautista10/CH55x_SDCC_Examples/main/Images/make_file.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :figwidth: 80%


rename it

.. figure:: https://raw.githubusercontent.com/Cesarbautista10/CH55x_SDCC_Examples/main/Images/rename.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :figwidth: 80%


path::
    
    C:\MinGW\bin\make




.. figure:: https://raw.githubusercontent.com/Cesarbautista10/CH55x_SDCC_Examples/main/Images/var_env.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :figwidth: 80%

Install pyusb
---------------


Verify the installation with `python --version`. 

If not installed, download and install:
- [Python](https://www.python.org/downloads/)

Use pip for install py usb::

    pip install pyusb

Update driver
---------------


The current loading tool can utilize the default driver and coexist with the official WCHISPTool. In case the driver encounters issues, it is advisable to switch the driver version to libusb-win32 using Zadig.


.. figure:: https://raw.githubusercontent.com/Cesarbautista10/CH55x_SDCC_Examples/main/Images/driver.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :figwidth: 80%