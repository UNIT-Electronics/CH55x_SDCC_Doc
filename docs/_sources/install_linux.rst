Environment Setup on Ubuntu
============================


.. caution::

   This project is under active development. The information provided here is subject to change.

Update the operating system::

    sudo apt update


Install `make`, `binutils` and `sdcc`::

    sudo apt install make
    sudo apt install binutils
    sudo apt install sdcc
    sudo apt install python3-usb

Linux Configuration for USB
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new file::

    sudo nano /etc/udev/rules.d/99-ch55x.rules


Add the following content::

    SUBSYSTEM=="usb", ATTR{idVendor}=="4348", ATTR{idProduct}=="55e0", MODE="0666"

update the rules::

    sudo udevadm control --reload-rules
    sudo udevadm trigger


Clone the examples with the main code::

    git clone https://github.com/UNIT-Electronics/CH55x_SDCC_Examples.git


Navigate to the path::

    cd CH55x_SDCC_Examples/Software/examples/Blink


Execute the command::

    make help


You will see::

    Use the following commands:
    make all     compile, build, and keep all files
    make hex     compile and build blink.hex
    make bin     compile and build blink.bin
    make clean   remove all build files


Connect a device with the BOOT button pressed::

    lsusb


The device will be shown with this description::

    pc@LAPTOP:~$ lsusb
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 4348:55e0 WinChipHead
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub   

Compile the code::
    
        make bin

Flash the code, remember to change the device path::

    sudo python3 ../../tools/chprog.py main.bin


Success::

    pc@LAPTOP:~$ sudo python3 ../../tools/chprog.py main.bin
    [sudo] password for pc: 
    FOUND: CH552 with bootloader v2.4.0.
    Erasing chip ...
    Flashing main.bin to CH552 ...
    SUCCESS: 374 bytes written.
    Verifying ...
    SUCCESS: 374 bytes verified.
    DONE.

.. note::

    chprog.py is a python script that allows you to flash the code to the device.





