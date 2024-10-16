Cocket Nova Developmet Board CH552 Guide
========================================

This is an excellent guide for beginner programmers, focused on using the SDCC compiler in both Windows and Linux environments.
Here, you can find excellent references and examples along with comprehensive documentation focusing on developing technology for embedded systems. 
This course covers everything from installation and setting up the compiler to managing project dependencies and developing code. 
It's a valuable resource that will guide you through the development process using high-quality technology, ensuring long-lasting and robust projects.

Why Use the SDCC Compiler?
----------------------------

The Small Device C Compiler (SDCC) is a highly regarded tool in the field of embedded systems development. Here are several reasons why you might choose to use the SDCC compiler for your projects:

1. **Free and Open-Source**: SDCC is freely available and open-source, which means you can use it without licensing fees and contribute to its development if you wish.

2. **Wide Microcontroller Support**: It supports a broad range of microcontrollers, including popular ones like the CH552, making it a versatile choice for various projects.

3. **Ease of Use**: SDCC is known for its user-friendly interface and straightforward setup, which helps developers get started quickly.

4. **Active Community and Documentation**: With an active community and extensive documentation, you can find support and resources to help you solve any issues you encounter.

5. **Compatibility**: SDCC is compatible with many other tools and environments, allowing for seamless integration into existing workflows.

Understanding Programming Languages in Embedded Systems
-------------------------------------------------------

To develop effective embedded systems, it's crucial to understand the different types of programming languages used:

Machine Language
~~~~~~~~~~~~~~~~~

Machine language, also known as machine code, is the most fundamental level of programming. Instructions are written in binary bit patterns, which are combinations of 1s and 0s. These patterns correspond to HIGH and LOW voltage levels that the microcontroller or microprocessor can directly interpret. This language is the most difficult for humans to use due to its complexity and lack of readability.

Assembly Language
~~~~~~~~~~~~~~~~~~

Assembly language is a step above machine language, providing a more human-readable format. It uses mnemonics and hexadecimal codes to represent machine language instructions. For instance, the 8051 microcontroller assembly language includes a combination of English-like words called mnemonics and hexadecimal numbers. Despite being more readable than machine language, it still requires an in-depth understanding of the microcontroller’s architecture.

High-level Language
~~~~~~~~~~~~~~~~~~~~

High-level languages simplify programming by abstracting away the intricate details of the microcontroller’s architecture. These languages use familiar words and statements, making them easier to learn and use. Examples of high-level languages include BASIC, C, Pascal, C++, and Java. Programs written in high-level languages are translated into machine code by a compiler, bridging the gap between human-friendly code and machine-understandable instructions.

By understanding these `different levels of programming languages <https://gmostofabd.github.io/8051-Assembly-Programming/>`_ , you can choose the most appropriate one for your project, balancing ease of use with the level of control you need over the hardware.



Requirements
----------------

- `Python <https://www.python.org/downloads/>`_  (Package Installation and Environments) 
- Utilization of Operating System Controllers
- Understanding of Basic Electronics

.. tip::
   This  guide is tailored for individuals with a basic understanding of programming and electronics. It's ideal for those interested in diving into embedded systems and programming microcontrollers.


PinOut
------

The CH552 microcontroller development board has a total of 16 pins, each with a specific function. The following is a list of the pins and their respective functions:

.. _PinOut:

.. figure:: /_static/PinOut_CH552.jpg
   :width: 80%
   :align: center
   :alt: PinOut CH552

   Cocket Nova CH552 PinOut