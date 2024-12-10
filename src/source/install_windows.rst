Environment Setup on Windows
===================================
This section provides a step-by-step guide to setting up the SDCC compiler on Windows operating systems. It also includes instructions for installing the necessary tools and configuring the environment variables. Additionally, it covers the installation of the pyusb library and updating the driver using Zadig.

Compiler Installation
---------------------

Follow these steps to install the necessary tools:

1. **Install Git for Windows**
   Download and install Git for Windows from the `official Git website <https://git-scm.com/download>`_.

2. **Install SDCC**
   Download and install the latest version of SDCC from the `SDCC downloads page <https://sourceforge.net/projects/sdcc/>`_.

3. **Install MinGW**
   Download and install MinGW, a set of development tools for Windows, from the `official MinGW website <https://sourceforge.net/projects/mingw/>`_.

4. **Install CH372 Driver**
   Download the latest version of the CH372 driver from the `official website <https://www.wch-ic.com/downloads/CH372DRV_EXE.html>`_.

5. **Install Zadig**
   Download and install the latest version of Zadig from the `official website <https://zadig.akeo.ie/>`_.

6. **Install Filter Wizard**
   Download the latest version of libusb-win32 from the `official website <https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.7.3/>`_. This driver is used by the Loadupch tool to communicate with the device.

7. **Install Python**
   Download and install the latest version of Python from the `official Python website <https://www.python.org/downloads/>`_.

8. **Install Editor Code**
   Download and install the latest version of your preferred text editor. Some popular choices include `Visual Studio Code <https://code.visualstudio.com/Download>`_, Sublime Text, and Notepad++.



.. tip::  
    It is recommended to install the tools in the order listed above.

.. caution::  
    Remember to restart your computer after installing the tools.

Environment Variable Configuration
----------------------------------

Remember that for Windows operating systems, an extra step is necessary, which is to open the environment variable -> Edit environment variable::

    C:\MinGW\bin



Locate the file
---------------
After installing MinGW, you will need to locate the `mingw32-make.exe` file. This file is typically found in the `C:/MinGW/bin` directory. Once located, rename the file to `make.exe`.

.. _make_file:
.. figure:: /_static/make_file.png
   :align: center
   :alt: Locating the mingw32-make.exe file.
   :width: 90%

   Locating the `mingw32-make.exe` file

Rename it
---------
After locating `mingw32-make.exe`, rename it to `make.exe`. This change is necessary for compatibility with many build scripts that expect the command to be named `make`.

.. _rename:
.. figure:: /_static/rename.png
   :align: center
   :alt: Renaming mingw32-make.exe to make.exe.
   :width: 90%
   
   Renaming `mingw32-make.exe` to `make.exe`

.. warning::  
    If you encounter any issues, create a copy of the file and then rename the copy to `make.exe`.

Add the path to the environment variable
----------------------------------------

Next, you need to add the path to the MinGW bin directory to your system's environment variables. This allows the `make` command to be recognized from any command prompt.

1. Open the Start Search, type in "env", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. In the Environment Variables window, under "System variables", select the "Path" variable and click "Edit".
4. In the Edit Environment Variable window, click "New" and add the path::

    C:\MinGW\bin

.. _var_env:
.. figure:: /_static/var_env.png
   :align: center
   :alt: Adding MinGW bin directory to environment variables.
   :width: 60%
   
   Adding MinGW bin directory to environment variables

Verify the installation
------------------------

To verify that the `make` command is correctly set up, open a new command prompt and type::

    make --version

You should see the version information for `make`, indicating that it is correctly installed and recognized by the system.

.. _verify:

.. figure:: /_static/make_version.png
   :align: center
   :alt: Verifying the installation of make.
   :width: 90%
   
   Verifying the installation of `make`

Update driver
---------------

.. warning::
    The use of Zadig is at your own risk. if you are not familiar with the tool, it is recommended to seek assistance from someone who is. In the case of changing the driver any device, it is important to have the original driver available to revert the changes.



The current loading tool can utilize the default driver and coexist with the official WCHISPTool. In case the driver encounters issues, it is advisable to switch the driver version to libusb-win32 using `Zadig <https://zadig.akeo.ie/>`_.


.. _driver:

.. figure:: /_static/driver.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :width: 100%
   
   driver


