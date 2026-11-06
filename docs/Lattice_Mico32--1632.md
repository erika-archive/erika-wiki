# Lattice Mico32

<a id="Lattice_Mico32_support"></a>

### Lattice Mico32 support

[Lattice Mico32](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm) is the soft processor developed by Lattice for their FPGAs. ERIKA Enterprise supports Lattice Mico32. The support for RT-Druid is now available using the nightly build. Instructions on how to get nightly builds can be found on the
[Erika web site](http://erika.tuxfamily.org/erika-for-multiple-devices.html)

The Lattice Mico32 support includes:

1. support for lm32-elf-gcc compiler.
2. support for single and multi stack configurations.
3. ISR interrupt supported.
4. support for Lattice Debugger.

- Supported compiler
  - lm32-elf-gcc cross compiler and ELF module generation for debugging. The compiler can be downloaded together with the Lattice Mico32 from the [Lattice Web site](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm).

```
 We notice that the objdump of debug symbols may fail with a segmentation fault if
 the binary file was produced using NOLOAD keyword in the linker-script.
 The webserver camera demo is an example of this problem.
```

- Mode of operation
  - Mono-stack: The Monostack configuration of the ERIKA Kernel models the fact that all tasks and ISRs in the system share the same stack.
  - Multistack HAL: Every thread can have its private stack, or it can share it with other threads.

<a id="Configuration"></a>

### Configuration

ERIKA Enterprise for Lattice Mico32 can be configured with the usual  [OIL file and RT-Druid workflow](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics"). Here the items specific for the Lattice Mico32 support are described.

<a id="EEOPTs"></a>

#### EEOPTs

**\_\_SPACE\_\_**

Optimize for space

**\_\_USE\_CUSTOM\_LINKER\_SCRIPT\_\_**

Don't use the dafault linker script. Users can direct the linker to use their own linker script by setting the `LDFLAGS` variable. Example:

```
OS EE {
   EE_OPT = "__USE_CUSTOM_LINKER_SCRIPT__";
   LDFLAGS = "-T my_linker_script.ld";
};
```

**\_\_USE\_CUSTOM\_CRT0\_\_**

Don't use Erika default crt0. Users can provide their own crt0 by adding source files in the usual way (APP\_SRC in the OIL file).

**\_\_LM32\_NOISY\_HANDLERS\_\_**

On the FPG-EYE board, exception handlers make the LEDs blink with an error code

**\_\_LM32\_VERBOSE\_HANDLERS\_\_**

On the FPG-EYE board, exception handlers make the LEDs blink with an error code and print the values of all CPU registers to the serial port (115200, 8N1) when a key is pressed

**\_\_LM32\_STANDARD\_HANDLERS\_\_**

On the FPG-EYE board, use the standard exception handlers (which call the debugger)

<a id="CPU"></a>

#### CPU

- The CPU currently supported is the following:
  - Lattice Mico32; The LatticeMico32™ is a configurable 32-bit soft processor core for Lattice Field Programmable Gate Array (FPGA) devices. By combining a 32-bit wide instruction set with 32 general-purpose registers, the LatticeMico32 provides the performance and flexibility suitable for a wide variety of markets. Some of the key features of this 32-bit processor include: RISC architecture, 32-bit data path, 32-bit instructions, 32 general-purpose registers, Up to 32 external interrupts, Optional instruction cache, Optional data cache, Dual WISHBONE memory interfaces (instruction and data).

<a id="MCU"></a>

#### MCU

- Timer support is enabled with the TIMER option:

  DEVICE = TIMER {

  NAME = "freetimer";

  };

  // Also, interrupts are supported:

  DEVICE = TIMER {

  NAME = "timer";

  OPTIONS = TIMER\_IRQ\_SUPPORT;

  };
- Uart support is enabled with the UART option:

  DEVICE = UART {

  NAME = "myuart";

  };

  // Also, interrupts are supported:

  DEVICE = UART {

  NAME = "myuart";

  OPTIONS = UART\_IRQ\_SUPPORT;

  };
- SPI support is enabled with the SPI option:

  DEVICE = SPI {

  NAME = "myspi";

  };
- I2C support is enabled with the SPI option:

  DEVICE = I2C {

  NAME = "myi2c";

  };
- GPIO support is enabled with the GPIO option:

  DEVICE = GPIO {

  NAME = "mygpio";

  };

  // Also, interrupts are supported:

  DEVICE = GPIO {

  NAME = "mygpio";

  OPTIONS = GPIO\_IRQ\_SUPPORT;

  };

<a id="Boards"></a>

#### Boards

<a id="FPG-EYE_board"></a>

##### FPG-EYE board

Item BOARD\_DATA = XP2\_CAMERA\_BOARD of EE in conf.oil.
Supported devices:

- Real-time clock. Option RTCLOCK.
- Leds. Option LEDS.
- Power transistors. Option TRANSISTORS.
- Switches and user button. Option SWITCHES.
- RS232 serial interface. Option RS232. IRQ for RS232 can be enabled with RS232\_IRQ\_SUPPORT.
- HV7131GP Camera. Option CAMERA. IRQ for the camera can be enabled with CAMERA\_IRQ\_SUPPORT.
- Real-time clock. Option RTCLOCK. IRQ for the real time clock can be enabled with RTCLOCK\_IRQ\_SUPPORT.
- External SPI master interfaces. Option EXTSPI. IRQ for the external SPIs can be enabled with EXTSPI\_IRQ\_SUPPORT.
- IEEE 802.15.4 (ZigBee) module. Option ZIGBEE. IRQ for the ZigBee module can be enabled with ZIGBEE\_IRQ\_SUPPORT. Please note that ZigBee and Ethernet are mutually exclusive.
- ENC28J60 Ethernet interface. Option ETHERNET. IRQ for the Ethernet can be enabled with ETHERNET\_IRQ\_SUPPORT. Please note that ZigBee and Ethernet are mutually exclusive.
- Everything, included the ZigBee (Ethernet is excluded). Option ALL\_ZIGBEE.
- Everything, included the Ethernet (ZigBee is excluded). Option ALL\_ETHERNET.

<a id="Lattice_Standard_XP2_Evaluation_board"></a>

##### Lattice Standard XP2 Evaluation board

- Leds. Option LEDS.
- RS232 serial interface. Option RS232. IRQ for RS232 can be enabled with RS232\_IRQ\_SUPPORT.
- HV7131GP Camera. Option CAMERA. IRQ for the camera can be enabled with CAMERA\_IRQ\_SUPPORT.

<a id="Lattice_Mico32_OIL_example"></a>

#### Lattice Mico32 OIL example

See the example [OIL file for Lattice Mico32](OIL_file_for_Lattice_Mico32--1659.md "OIL file for Lattice Mico32")

<a id="See_also"></a>

### See also

- [Tutorial: Installing ERIKA and RT-Druid, and compile your first application](Tutorial_PIC30_-_Installing_ERIKA_and_RT-Druid_and_compile_your_first_application--1637.md "Tutorial: Installing ERIKA and RT-Druid, and compile your first application")
- [Tutorial: RT-Druid and OIL basics](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")
- [Lattice Mico32 page on the Lattice Semiconductor Web site](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Lattice_Mico32) · [Archived source revision 4001](http://erika.tuxfamily.org/wiki/index.php?oldid=4001)
- Last source edit: 2011-10-31T09:19:13Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Dibbe, Erikadds, WikiSysop, Nicola.
- [Original MediaWiki source](../source/wikitext/1632.mediawiki) · [Original editing history](../source/history/batch-007.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
