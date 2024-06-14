CH55x with SDCC and Windows
===================================
This section provides a step-by-step guide to setting up the SDCC compiler on Windows operating systems. It also includes instructions for installing the necessary tools and configuring the environment variables. Additionally, it covers the installation of the pyusb library and updating the driver using Zadig.

Compiler Installation 
---------------

Follow the steps below to install the necessary tools:

- **Installing Git for Windows**  
  Download and install `Git for Windows <https://git-scm.com/download>`_ from the official Git website.

- **Installing SDCC**  
  Download and install the latest version of SDCC. You can find the latest version on the `SDCC downloads page <https://sourceforge.net/projects/sdcc/>`_.

- **Installing MinGW**  
  Install MinGW, which is a set of tools for software development on Windows. You can download the installer from the `official MinGW website <https://sourceforge.net/projects/mingw/>`_.

- **Installing Zadig**  
  Download the latest version of `Zadig <https://zadig.akeo.ie/>`_. You can download it from the official website.

.. tip::  
    It is recommended to install the tools in the order listed above.

.. caution::  
    Remember to restart your computer after installing the tools.

Environment Variable Configuration
----------------------------------

Remember that for Windows operating systems, an extra step is necessary, which is to open the environment variable -> Edit environment variable::

    C:\MinGW\bin


Install pyusb
---------------

Verify the installation with `python --version`.

If not installed, download and install:

- `Python <https://www.python.org/downloads/>`_

Use pip to install pyusb::

    pip install pyusb

Locate the file
---------------
After installing MinGW, you will need to locate the `mingw32-make.exe` file. This file is typically found in the `C:\MinGW\bin` directory. Once located, rename the file to `make.exe`.

.. _make_file:
.. figure:: /_static/make_file.png
   :align: center
   :alt: Locating the mingw32-make.exe file.
   :width: 80%

   Locating the `mingw32-make.exe` file

Rename it
---------
After locating `mingw32-make.exe`, rename it to `make.exe`. This change is necessary for compatibility with many build scripts that expect the command to be named `make`.

.. _rename:
.. figure:: /_static/rename.png
   :align: center
   :alt: Renaming mingw32-make.exe to make.exe.
   :width: 80%
   
   Renaming `mingw32-make.exe` to `make.exe`

.. warning::  
    If you encounter any issues, create a copy of the file and then rename the copy to `make.exe`.

Add the path to the environment variable
----------------------------------------
Next, you need to add the path to the MinGW bin directory to your system's environment variables. This allows the `make` command to be recognized from any command prompt.

1. Open the Start Search, type in "env", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. In the Environment Variables window, under "System variables", select the "Path" variable and click "Edit".
4. In the Edit Environment Variable window, click "New" and add the path `C:\MinGW\bin`.

.. _var_env:
.. figure:: /_static/var_env.png
   :align: center
   :alt: Adding MinGW bin directory to environment variables.
   :width: 70%
   
   Adding MinGW bin directory to environment variables

Verify the installation
-----------------------
To verify that the `make` command is correctly set up, open a new command prompt and type::

    make --version

You should see the version information for `make`, indicating that it is correctly installed and recognized by the system.


Update driver
---------------


The current loading tool can utilize the default driver and coexist with the official WCHISPTool. In case the driver encounters issues, it is advisable to switch the driver version to libusb-win32 using `Zadig <https://zadig.akeo.ie/>`_.




.. _driver:

.. figure:: /_static/driver.png
   :align: center
   :alt: GitHub build status reporting for pull requests.
   :width: 100%
   
   driver


.. warning::
    The use of Zadig is at your own risk. if you are not familiar with the tool, it is recommended to seek assistance from someone who is. In the case of changing the driver any device  , it is important to have the original driver available to revert the changes.