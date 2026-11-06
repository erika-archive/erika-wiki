# Renesas RX200 and RX130

<a id="Renesas_RX200_Series_support"></a>

## Renesas RX200 Series support

ERIKA Enterprise supports Renesas RX200 series microcontrollers, in particular the [RX210](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rx/rx200/rx210.html) and [RX130](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rx/rx200/rx210.html) Groups.
The support for RT-Druid is now available.

Due to customer restrictions, the [RX130](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rx/rx200/rx210.html) porting is not yet public. If you want to get more information about the [RX130](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rx/rx200/rx210.html) porting, please contact [info@evidence.eu.com](mailto:info@evidence.eu.com).

The Renesas RX200 support includes:

1. support for [C/C++ Compiler Package for RX Family](https://www.renesas.com/en-eu/products/software-tools/tools/compiler-assembler/compiler-package-for-rx-family.html);
2. support for single and multi stack configurations;
3. ISR Type 1 and Type 2 supported;
4. support for Renesas [E1](https://www.renesas.com/en-sg/products/software-tools/tools/emulator/e1.html) debugger/emulator;

- Supported IDEs:
  - Renesas [High-performance Embedded Workshop](https://www.renesas.com/en-us/products/software-tools/tools/ide/hew.html);
  - Renesas [e2studio](https://www.renesas.com/en-us/products/software-tools/tools/ide/e2studio.html) IDE;

- Mode of operation:
  - Mono-stack: The Monostack configuration of the ERIKA Kernel models the fact that all tasks and ISRs in the system share the same stack.
  - Multi-stack HAL: Every task can have its private stack, or it can share it with other tasks.

<a id="MCUs"></a>

#### MCUs

- The MCU currently supported is the following:
  - R5F52108xxxx
  - R5F51308xxxx

<a id="Boards"></a>

#### Boards

- The board currently supported is the following:
  - [Renesas Starter Kit for RX210](https://www.renesas.com/en-eu/products/software-tools/boards-and-kits/renesas-starter-kits/renesas-starter-kit-for-rx210.html) (part number R0K505210S000BE)
  - [Renesas Starter Kit for RX130-512KB](https://www.renesas.com/en-us/products/software-tools/boards-and-kits/renesas-starter-kits/renesas-starter-kit-for-rx130-512kb.html) (part number RTK5051308C00000BE)

- List of functions:
  - [Renesas Starter Kit for RX210](https://www.renesas.com/en-eu/products/software-tools/boards-and-kits/renesas-starter-kits/renesas-starter-kit-for-rx210.html) is supported by Erika RTOS. Currently only leds, buttons and the LCD module are supported.

<a id="Download_and_install"></a>

## Download and install

RT-Druid and Erika Enterprise RTOS (version 1.6.1) can be freely downloaded from the following web address:

- <http://erika.tuxfamily.org/erika-for-multiple-devices.html>

Once downloaded, extract all the files contained in it and copy the folder named *eclipse* in your preferred directory on your PC (a recommended path is: C:\\Evidence\\).
Now, launch the program by double-clicking on the executable *eclipse.exe*inside the *C:\Evidence\eclipse* folder and choose the path of your workspace.
The workspace is the default working directory in which the projects will be created.

If you want to download only a selected revision of the kernel, open the Cygwin shell and get an anonymous SVN checkout typing this command:

```
 svn co svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee -r number_of_revision
```

Note:
Cygwin can be downloaded from this web site: <http://www.cygwin.com/>
To use SVN, the Cygwin SVN package must to be installed using the Cygwin Setup utility.

The Renesas RX200 plug-in for Eclipse is part of the official distribution of RT-Druid.

- The procedure to update Erika and RT-Druid plugins is described at [Tutorial: Update ERIKA and RT-Druid](Tutorial_Update_ERIKA_and_RT-Druid--2049.md "Tutorial: Update ERIKA and RT-Druid").

<a id="Target_Configuration_and_Programming"></a>

## Target Configuration and Programming

ERIKA is configured through  [RT-Druid and an OIL file](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")

<a id="Compiler_Path"></a>

### Compiler Path

It is possible to choose the path of the compiler in three different ways:

- environment var:
  - CCRX compiler: the CCRX\_ROOT variable is able to override the path compiler set in RT-Druid during the build progress.
- configuration file:
  - see [RT-Druid configuration#Compiler paths](RT-Druid_configuration--2158.md#Compiler_paths "RT-Druid configuration")
- gui:
  - inside eclipse preferences, it is possible to set the paths of above compilers.

<a id="CPU"></a>

### CPU

`CPU_DATA` must be set to `RX200`.  
The exact model is specified with the `MODEL` item (supported values are `M0` for Cortex M0 and `M4` for Cortex M4).  
The compiler is specificed with the `COMPILER_TYPE` item (currently the only supported value is `CCRX<code>).  
Example of a CPU_DATA section:`

CPU\_DATA = RX200 {

```
  APP_SRC = "code.c";
  COMPILER_TYPE = CCRX;
  MULTI_STACK = TRUE {
      IRQ_STACK = TRUE {
           SYS_SIZE=512;
      };
  };
```

};

<a id="MCU"></a>

### MCU

<code>MCU\_DATA must be set to `RENESAS`   
The only item supported is `MODEL`. The model currently supported is the RF5210x  
Example of a MCU\_DATA section:

```
MCU_DATA = RENESAS {
   MODEL = R5F5210x;
};
```

<a id="Interrupt_Handling"></a>

### Interrupt Handling

Renesas MCU R5F5210x is configured to have a flexible Interrupt Vector Table specified in <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/mcu/renesas_r5f5210x/src/ee_vtable_ccrx.c>.  
Each entry is specified by the following macro:

```
 EE_<ARCH>_<ENTRY>_ISR
```

Where `<ARCH>` is the architecture depended identifier (E.g. `RX200`), and `<ENTRY>` is the fixed Interrupt Vector Table Entry identifier (E.g. `CMIA0`).

To define each ISR an `ISR` object is needed to be added in the `CPU` object of the OSEK/VDX configuration:

```
 ISR <SYMBOL> {
   CATEGORY = <ISR_TYPE>;
   ENTRY = "<ENTRY>";
 };
```

Where `<ISR_TYPE>` is the type of the ISR (1 or 2), `<SYMBOL>` is the symbol that must be the parameter of `ISR<ISR_TYPE>()` ISR signature, and `<ENTRY>` is the variable Interrupt Vector Table Entry identifier.

<a id="Libraries"></a>

## Libraries

- The software libraries currently supported are those provided with Erika:
  - [Leds and Buttons](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/board/renesas_rskrx210).
  - [Operating Frequency Setup](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/board/renesas_rskrx210).
  - [System tick](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/mcu/renesas_r5f5210x).

<a id="OIL_file_configuration"></a>

#### OIL file configuration

To enable system tick routines, the following code is needed in the `OS` object of the OSEK/VDX configuration:

```
EE_OPT = "__USE_SYSTICK__";
```

To enable board support library with Renesas RX210 starter kit, the following code is needed in the `OS` object of the OSEK/VDX configuration:

```
EE_OPT = "__RSKRX210__";
```

To use the board's leds add:

```
EE_OPT = "__USE_RSKRX120_USER_LED__";
```

To use the board's buttons add:

```
EE_OPT = "__USE_RSKRX120_BUTTONS__";
```

To use the Operating Frequency Setup routine add:

```
EE_OPT = "__USE_RSKRX210_OP_FREQ_SETUP__";
```

If you want to add an external library, such as the Renesas RPDL library, and need to tell the linker to allocate the code Section "L" into the loadable module,
the following code is needed in the `OS` object of the OSEK/VDX configuration:

```
EE_OPT = "__ADD_LIB_SECT__";
```

<a id="Examples"></a>

## Examples

- The examples and tests are available in this folder:
  - <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/rx200/porting_examples>: Porting examples.
  - <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/rx200/rskrx210_base_demo>: Base demo for the RX210 Starter Kit board that uses leds, buttons and the LCD module.

<a id="See_also"></a>

## See also

- [Tutorial: Installing ERIKA and RT-Druid, and compile your first application](Tutorial_PIC30_-_Installing_ERIKA_and_RT-Druid_and_compile_your_first_application--1637.md "Tutorial: Installing ERIKA and RT-Druid, and compile your first application")
- [Tutorial: RT-Druid and OIL basics](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")
- [Renesas RX210 architecture webpage.](http://am.renesas.com/products/mpumcu/rx/rx200/rx210/index.jsp)
- [RX210 Starter Kit](http://am.renesas.com/products/tools/introductory_evaluation_tools/renesas_starter_kits/rsk_rx210/index.jsp)
- [Renesas High-performance Embedded Workshop](http://am.renesas.com/products/tools/ide/ide_hew/index.jsp) }

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Renesas_RX200_and_RX130) · [Archived source revision 6118](http://erika.tuxfamily.org/wiki/index.php?oldid=6118)
- Last source edit: 2018-06-04T17:36:52Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Gfranchi, Pj, Giuseppe Serano.
- [Original MediaWiki source](../source/wikitext/2307.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
