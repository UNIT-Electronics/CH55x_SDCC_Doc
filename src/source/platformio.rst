PlatformIO Support for CH55x
============================

The
`unit_ch55x_docker_sdk <https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk>`_
repository is the SDK base for CH55x PlatformIO projects. It can be used as a
local PlatformIO development platform or referenced directly from GitHub.
PlatformIO uses SDCC to build the firmware and generates the ``firmware.ihx``,
``firmware.hex`` and ``firmware.bin`` output files.

This is the supported installation workflow for new Ubuntu and Windows setups.
If you use PlatformIO, you do not need to follow the manual SDCC, Make, MinGW
or Linux package installation steps from the environment setup pages. Install
PlatformIO, configure the project with ``platformio.ini`` and build with
``pio run``.

.. note::

   The previous manual SDCC and Make workflow is kept in this guide as a legacy
   reference. New support should use the PlatformIO SDK base.

Requirements
------------

Install `PlatformIO Core <https://docs.platformio.org/en/latest/core/installation/index.html>`_
or use the PlatformIO extension for Visual Studio Code. Git is required to
clone the SDK base or to use it directly from ``platformio.ini``.

If you want to work with the SDK locally, clone the SDK base repository:

.. code-block:: bash

   git clone git@github.com:UNIT-Electronics-MX/unit_ch55x_docker_sdk.git
   cd unit_ch55x_docker_sdk

Ubuntu Setup
~~~~~~~~~~~~

On Ubuntu, install PlatformIO and Git. The manual SDCC, Make and package setup
from the legacy Linux page is not required for PlatformIO projects.

Verify that PlatformIO is available:

.. code-block:: bash

   pio --version

For uploads on Ubuntu, the default uploader uses ``chprog.py`` and requires
PyUSB in the PlatformIO Python environment:

.. code-block:: bash

   ~/.platformio/penv/bin/python -m pip install pyusb

USB access may also require udev permissions:

.. code-block:: bash

   echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="4348", ATTR{idProduct}=="55e0", MODE="666"' | sudo tee /etc/udev/rules.d/99-ch55x.rules
   sudo udevadm control --reload-rules
   sudo udevadm trigger

Windows Setup
~~~~~~~~~~~~~

On Windows, install PlatformIO, Git and the CH372 driver. The manual SDCC,
MinGW and Make setup from the legacy Windows page is not required for
PlatformIO projects.

**Install CH372 Driver**

Download the latest version of the CH372 driver from the
`CH372 driver website <https://www.wch-ic.com/downloads/CH372DRV_EXE.html>`_.

Verify PlatformIO from PowerShell:

.. code-block:: powershell

   C:\Users\<user>\.platformio\penv\Scripts\platformio.exe --version

Windows upload uses ``vnproch55x`` when ``upload_protocol = auto``.

Build a PlatformIO Example
--------------------------

From the Blink example inside the SDK repository, run:

.. code-block:: bash

   cd examples/blink
   pio run

The generated firmware files are placed in the PlatformIO build directory:

.. code-block:: text

   examples/blink/.pio/build/unit_ch552/

The Blink example is available in the SDK base repository:
`examples/blink <https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk/tree/main/examples/blink>`_.

Examples that include a ``platformio.ini`` file can be built the same way:

.. code-block:: bash

   cd examples/usb/usb_uart
   pio run

Upload Firmware
---------------

Put the CH55x board in bootloader mode and run:

.. code-block:: bash

   pio run -t upload

The default ``upload_protocol = auto`` selects ``chprog.py`` on Linux and
macOS, and ``vnproch55x`` on Windows.

Windows Upload with vnproch55x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Windows, the Arduino package uses ``vnproch55x.exe`` from the
``devlabtools`` package. If PlatformIO does not download the uploader
automatically, install it manually in the SDK root:

.. note::

   Edit the paths in the following commands before running them. Replace
   ``C:\path\to\unit_ch55x_docker_sdk`` with the folder where you cloned the
   SDK, and replace ``<user>`` with your Windows user name.

.. code-block:: powershell

   $SdkRoot = "C:\path\to\unit_ch55x_docker_sdk"
   cd $SdkRoot
   Invoke-WebRequest "https://github.com/UNIT-Electronics/Uelectronics-CH552-Arduino-Package/releases/download/v0.0.6/ch55xduino-tools_mingw32-2026.06.21.tar.bz2" -OutFile "ch55xduino-tools_mingw32-2026.06.21.tar.bz2"
   tar -xjf ch55xduino-tools_mingw32-2026.06.21.tar.bz2
   Test-Path .\tools\win\vnproch55x.exe

The ``Test-Path`` command must print ``True``. The extracted layout must
contain:

.. code-block:: text

   tools/win/vnproch55x.exe
   tools/win/*.dll

After installing the uploader, build and upload from the PlatformIO project:

.. code-block:: powershell

   $PlatformioExe = "C:\Users\<user>\.platformio\penv\Scripts\platformio.exe"
   & $PlatformioExe run
   & $PlatformioExe run --target upload

PlatformIO Configuration
------------------------

For a PlatformIO project inside this repository, point ``platform`` to the SDK
root:

.. code-block:: ini

   [env:unit_ch552]
   platform = ../..
   board = unit_ch552

To pin a released SDK version from GitHub, use the release tag in
``platformio.ini``:

.. code-block:: ini

   [env:unit_ch552]
   platform = https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk.git#v0.1.1
   board = unit_ch552

To use the current SDK branch directly from GitHub:

.. code-block:: ini

   [env:unit_ch552]
   platform = https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk.git
   board = unit_ch552

For an existing Makefile-style example where ``main.c`` is located at the
project root, set the source directory globally:

.. code-block:: ini

   [platformio]
   src_dir = .

   [env:unit_ch552]
   platform = ../..
   board = unit_ch552

The default configuration can usually stay minimal:

.. code-block:: ini

   [env:unit_ch552]
   platform = ../..
   board = unit_ch552

   ; Arduino defaults to bootcfg 3 for CH552 P3.6 (D+) pull-up.
   board_upload.bootcfg = 3

You can force a specific uploader when needed:

.. code-block:: ini

   upload_protocol = chprog
   upload_protocol = vnproch55x

For serial upload:

.. code-block:: ini

   upload_protocol = vnproch55x_serial
   upload_port = COM5

Supported Boards
----------------

The following board identifiers are available:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Board ID
     - Target
   * - ``unit_ch551``
     - CH551
   * - ``unit_ch552``
     - CH552
   * - ``unit_ch554``
     - CH554
   * - ``unit_ch559``
     - CH559

Common build overrides can be added to ``platformio.ini``:

.. code-block:: ini

   board_build.f_cpu = 24000000
   build_flags =
     -D PIN_LED=P34

Create a New SDK Project
------------------------

The SDK CLI can create a new project directory:

.. code-block:: bash

   ./spkg/spkg init examples/project

For the SDK Makefile workflow, the compiled binary is generated at:

.. code-block:: text

   examples/blink/build/main.bin

You can flash that binary using ``tools/chprog.py``,
`wchusbdfu <https://github.com/DeqingSun/ch554tools>`_ or
`WCHISPTool <https://www.wch-ic.com/downloads/WCHISPTool_Setup_exe.html>`_.
