# OIL file for Lattice Mico32

CPU test\_application {

OS EE {  

CFLAGS = "-g2"; //option to produce debugging information

ASFLAGS = "";

LDFLAGS = "";

CPU\_DATA = LM32 {  

APP\_SRC = "main.c";

MULTI\_STACK = FALSE;

USESTANDALONEPRINTF = TRUE; // Optional, default is FALSE;

USESMALLC = FALSE; // Optional, defautl is FALSE;

};

MCU\_DATA = LATTICE\_PLATFORM {  

MODEL = LIBRARY {  

PLATFORM\_LIB\_PATH = "../test\_sram\_lib"; // library (platform-dependent) path

PLATFORM\_NAME = "test\_base"; // platform name (is also the name of the main folder in the library path)

PLATFORM\_BLD\_CFG = "Release"; // Optional, default is ""

};

DEVICE = TIMER{  

NAME = "timer"; // sub-section to use the timer

OPTIONS = TIMER\_IRQ\_SUPPORT; // Timer IRQ code will be compiled

};

DEVICE = UART{  

NAME = "myuart"; // sub-section to use uart

OPTIONS = UART\_IRQ\_SUPPORT; // Uart IRQ code will be compiled

};

DEVICE = SPI{  

NAME = "myspi"; // sub-section to use spi

};

DEVICE = I2C{  

NAME = "myi2c"; // sub-section to use i2c

};

DEVICE = GPIO{  

NAME = "mygpio"; // sub-section to use gpio

OPTIONS = GPIO\_IRQ\_SUPPORT; // GPIO IRQ code will be compiled

};

};

BOARD\_DATA = XP2\_CAMERA\_BOARD { // section for XP2 camera board  

OPTIONS = LEDS; // Use leds driver for XP2\_CAMERA\_BOARD

OPTIONS = TRANSISTORS; // Use transistors driver for XP2\_CAMERA\_BOARD

OPTIONS = SWITCHES; // Use switches driver for XP2\_CAMERA\_BOARD

OPTIONS = LIGHTSENSOR; // Use light sensor driver for XP2\_CAMERA\_BOARD

OPTIONS = RS232; // Use uart specific driver for XP2\_CAMERA\_BOARD

OPTIONS = RS232\_IRQ\_SUPPORT; // Compile UART IRQ code

OPTIONS = CAMERA; // Use Camera hv7131gp driver for XP2\_CAMERA\_BOARD

OPTIONS = CAMERA\_IRQ\_SUPPORT; // Compile Camera IRQ code

OPTIONS = RTCLOCK; // Use RT-clcok pcf8583 driver for XP2\_CAMERA\_BOARD

OPTIONS = RTCLOCK\_IRQ\_SUPPORT; // Compile RT-clock IRQ code

OPTIONS = EXTSPI; // Use SPI specific driver for XP2\_CAMERA\_BOARD

OPTIONS = EXTSPI\_IRQ\_SUPPORT; // Compile SPI IRQ code

// ATT! ZIGBEE AND ETHERNET OPTIONS ARE MUTUALLY EXCLUSIVE!!!

OPTIONS = ZIGBEE; // Use Zigbee mrf24j40 driver for XP2\_CAMERA\_BOARD

OPTIONS = ZIGBEE\_IRQ\_SUPPORT; // Compile Zigbee IRQ code

// ATT! ZIGBEE AND ETHERNET OPTIONS ARE MUTUALLY EXCLUSIVE!!!

OPTIONS = ETHERNET; // Use Ethernet enc28j60 driver for XP2\_CAMERA\_BOARD

OPTIONS = ETHERNET\_IRQ\_SUPPORT; // Compile Ethernet IRQ code

// ATT! ZIGBEE AND ETHERNET OPTIONS ARE MUTUALLY EXCLUSIVE!!!

OPTIONS = ALL\_ZIGBEE; // Enable all Zigbee options

OPTIONS = ALL\_ETHERNET; // Enable all ethernet options

};

KERNEL\_TYPE = FP; // Scheduler choice (i.e. fixed priority scheduler)

};

ISR Timer { // Section for ISR definition   

CATEGORY = 2;

LEVEL = "TIMER\_IRQ"; // Level is the number specified in the library system\_conf.h file

HANDLER = "EE\_timer\_common\_handler"; // Handler is the name of the driver callback

};

TASK myTask { // Standard task definition  

PRIORITY = 2;

STACK = SHARED;

SCHEDULE = FULL;

};

};

More information about Mico32-specific features in OIL configuration files can be found in the [Lattice Mico32](Lattice_Mico32--1632.md "Lattice Mico32") page.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=OIL_file_for_Lattice_Mico32) · [Archived source revision 2846](http://erika.tuxfamily.org/wiki/index.php?oldid=2846)
- Last source edit: 2011-03-21T23:01:36Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Dibbe.
- [Original MediaWiki source](../source/wikitext/1659.mediawiki) · [Original editing history](../source/history/batch-008.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
