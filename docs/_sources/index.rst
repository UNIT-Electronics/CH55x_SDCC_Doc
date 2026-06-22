Cocket Nova Getting Started Guide
===================================


.. note::

   This project is under active development.


The Coket Nova guide is an instructional manual for utilizing the compiler SDCC. It serves various purposes, allowing users to explore different features and obtain new projects and 
configurations.
The Cocket Nova CH552 boards are incredibly easy to use. The projects focus on innovation and 
present various alternatives for usage.

Choose one development workflow:

- Use :doc:`platformio` for the supported Ubuntu and Windows setup. This option
  does not require installing SDCC, Make or the manual toolchain described in
  the Linux and Windows setup pages. It uses the
  `unit_ch55x_docker_sdk <https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk>`_
  repository as the SDK base.
- Use :doc:`install_linux` or :doc:`install_windows` only for the legacy manual
  SDCC and Make workflow. That previous workflow is kept as reference while
  support moves to the PlatformIO SDK base.

.. _ch552:

.. figure:: /_static/CH552_Sq.png
   :align: center
   :alt: ch552 img
   :width: 80%
   
   Cocket Nova CH552 Desing graphic




.. tip::
   The supported SDK examples are available in the
   `unit_ch55x_docker_sdk examples <https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk/tree/main/examples>`_
   directory. The Blink example is available at
   `examples/blink <https://github.com/UNIT-Electronics-MX/unit_ch55x_docker_sdk/tree/main/examples/blink>`_.




.. toctree::
   :maxdepth: 2
   :caption: Contents

   
   about
   platformio
   install_linux
   install_windows
   compile
   generalboardcontrol
   adc
   i2c
   interrupts
   pwm
   ws2812
   cdc
   report
