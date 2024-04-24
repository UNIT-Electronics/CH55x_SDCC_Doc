Environment for CH55x with SDCC and Ubuntu 23.10
===================================
Ubuntu 23.10 Installer Environment
---------------

Update the operating system::

    sudo apt update


Install `make` and `binutils`::

    sudo apt install make
    sudo apt install binutils

Clone the examples with the main code::

    git clone https://github.com/Cesarbautista10/CH55x_SDCC_Examples.git


Navigate to the path::

    cd ~/CH55x_SDCC_Examples/Software/examples/0.\ Blink/


Execute the command::

    make help


You will see::

    Use the following commands:
    make all     compile, build, and keep all files
    make hex     compile and build blink.hex
    make bin     compile and build blink.bin
    make flash   compile, build, and upload blink.bin to the device
    make clean   remove all build files


Connect a device with the BOOT button pressed::

    lsusb


The device will be shown with this description::

    Descriptor


Install pyusb
---------------

Verify the installation with `python --version`. If not installed, run::

    sudo apt install python3-pip


Then verify the installation::

    python3 -m pip show pyusb

Error with pip
---------------

If you encounter this error, we recommend installing the Python environment::


    sudo apt install python3-venv


Create an environment::

    python3 -m venv .venv

Activate the environment::

    source .venv/bin/activate

And install `pyusb`::

    pip install pyusb


