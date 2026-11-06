# ARM Cortex RX

<a id="ARM_Cortex_RX_support"></a>

## ARM Cortex RX support

The Cortex R4 support includes:

1. support for [Texas Instruments](http://www.ti.com/) compiler toolchain
2. support for single stack configurations
3. ISR Type 1 and Type 2 supported;

- Supported IDEs:
  - [Texas Instruments Code Composer Studio](http://www.ti.com/tool/ccstudio) (Cortex R4)

- Mode of operation:
  - *Mono-stack*: The Monostack configuration of the ERIKA Kernel models the fact that all tasks and ISRs in the system share the same stack.

<a id="MCUs"></a>

#### MCUs

- The MCUs currently supported are the following:
  - [Hercules TMS570 MCUs](http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/c2000_performance/safety/tms570/overview.page?DCMP=TMS570&HQS=tms570) (Cortex R4)

<a id="Boards"></a>

#### Boards

- The boards currently supported are the following:
  - [Keil MCBTMS570](http://www.keil.com/mcbtms570/) (Cortex R4)

<a id="Download_and_install"></a>

## Download and install

<a id="RT-Druid_and_ERIKA_Enterprise_RTOS"></a>

#### RT-Druid and ERIKA Enterprise RTOS

RT-Druid and ERIKA Enterprise RTOS can be freely downloaded from the following web address:

<http://www.erika-enterprise.com/index.php/download/erika-v2.x.html>

<a id="Toolchain:_Code_Composer_Studio"></a>

#### Toolchain: Code Composer Studio

The toolchain and Debugger can be downloaded from the following web address:

<http://processors.wiki.ti.com/index.php/Download_CCS>

Note that CCSv6 is recommended.
To tell ERIKA where to find the compiler, the sysem variable *CCS\_INSTALL\_ROOT*
has to be set to the compiler path:
`CCS_INSTALL_ROOT = C:\ti\ccsv6`

<a id="Flasher:_TI_Uniflash"></a>

#### Flasher: TI Uniflash

The flashing utility can be downloaded from the following page:

<http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash>
It is recommended to use the same installation path as the toolchain (C:\ti\)

<a id="HAL_Code_Generator:_HALCoGen"></a>

#### HAL Code Generator: HALCoGen

Currently the whole MCU is configured via a GUI from Texas Instruments.

The software can be downloaded from <http://www.ti.com/tool/halcogen> .

<a id="Target_Configuration_and_Programming"></a>

## Target Configuration and Programming

ERIKA Enterprise is configured through  [RT-Druid and an OIL file](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")

<a id="CPU"></a>

### CPU

`CPU_DATA` must be set to `CORTEX_RX`.  
The exact model is specified with the `MODEL` item ( `R4` for Cortex R4).  
The compiler is specificed with the `COMPILER_TYPE` item (supported values are `CCS` for `R4`).  
Example of a CPU\_DATA section:

```
 CPU_DATA = CORTEX_RX {
   MODEL = R4;
   APP_SRC = "code.c";
   COMPILER_TYPE = CCS;
   MULTI_STACK = FALSE;
 };
```

<a id="MCU"></a>

### MCU

`MCU_DATA` must be set to `TI` for Keil MCBTMS570.  
The only item supported is `MODEL`, which can be either `TMS570` for `TI`.  
Example of a MCU\_DATA section:

```
   MCU_DATA = TI {
     MODEL = TMS570;
   };
```

<a id="Interrupt_Handling"></a>

### Interrupt Handling

TODO: Add Support of OIL-File Interrupt Handling.
Currently the Interrupts are handled via the HALCoGen tool.

<a id="EEOPT"></a>

### EEOPT

EEOPT is a way to specify configuration flags to the Erika build environment. EEOPTs can be specified as strings in the OS section of the OIL file. Board specific options are:

```
   EE_OPT = "__ALLOW_NESTED_IRQ__";    /* Allow nested interrupts                                 */
   EE_OPT = "__USE_SYSTICK__";         /* Enables Timer                                           */
   EE_OPT = "__USE_LEDS__";            /* Enables the use of the 6 Onboard LEDS                   */
   EE_OPT = "__USE_DISPLAY__";         /* Enables the use of the Onboard Display                  */
   EE_OPT = "__USE_ADC__";             /* Enables the use of the Analog-Digital Converter         */
   EE_OPT = "__USE_LIN__";             /* Enables the use of the LIN Driver                       */
   EE_OPT = "__USE_GIO__";             /* Enables the use of the General I/O Driver               */
   EE_OPT = "__USE_HET__";             /* Enables the use of the High End Timer                   */
   EE_OPT = "__USE_SPI__";             /* Enables the use of the Serial Peripheral Interface      */
   EE_OPT = "__USE_SCI__";             /* Enables the use of the Serial Communication Interface   */
   EE_OPT = "__USE_CAN__";             /* Enables the use of the CAN Interface                    */
```

<a id="CPU.2C_MCU_.26_BOARD_API"></a>

## CPU, MCU & BOARD API

<a id="MCU_Initialization"></a>

#### MCU Initialization

To initialise the needed HAL Drivers specified as EE\_OPTs, it is necessary to initialize these modules
by calling:

**void EE\_mcu\_init(void);**

<a id="LEDS"></a>

#### LEDS

Note: EE\_OPT = "\_\_USE\_LEDS\_\_"; has to be set in the OIL file.

**void EE\_LED\_On(unsigned int num);** Turn LED (0...5) on.

**void EE\_LED\_Off(unsigned int num);** Turn LED (0...5) off.

**void EE\_LED\_Out(unsigned int value);** Write out a binary value to the 6 LEDs.

**void EE\_LED\_Toggle (unsigned int num);** Toggle LED (0...5).

<a id="Display"></a>

#### Display

Note: EE\_OPT = "\_\_USE\_DISPLAY\_\_"; has to be set in the OIL file.

**void DISPLAY\_Init (void);**

**void DISPLAY\_WindowMax (void);**

**void DISPLAY\_PutPixel (unsigned int x, unsigned int y);**

**void DISPLAY\_SetTextColor (unsigned short color);**

**void DISPLAY\_SetBackColor (unsigned short color);**

**void DISPLAY\_Clear (unsigned short color);**

**void DISPLAY\_DrawChar (unsigned int x, unsigned int y, unsigned short \*c);**

**void DISPLAY\_DisplayChar (unsigned int ln, unsigned int col, unsigned char c);**

**void DISPLAY\_DisplayString (unsigned int ln, unsigned int col, char \*s);**

**void DISPLAY\_ClearLn (unsigned int ln);**

**void DISPLAY\_Bargraph (unsigned int x, unsigned int y, unsigned int w, unsigned int h, unsigned int val);**

**void DISPLAY\_Bitmap (unsigned int x, unsigned int y, unsigned int w, unsigned int h, unsigned char const \*bitmap);**

**void DISPLAY\_Bmp (unsigned int x, unsigned int y, unsigned int w, unsigned int h, unsigned char const \*bmp);**

<a id="Other_Interfaces"></a>

#### Other Interfaces

For other Interfaces, like the ADC, GIO, HET, see the files created by the HALCoGen tool.

They can be found in the  `$(EE_BASE)/contrib/ti_tms570`  folder.

<a id="Example"></a>

#### Example

```
 void main()
 {
 /* Initialize MCU */
 EE_mcu_init();
 /* LCD Display Initialization */
 DISPLAY_Clear(Black);
 DISPLAY_SetBackColor(Black);
 DISPLAY_SetTextColor(White);
 DISPLAY_DisplayString(0, 0, "Hardware: TI TMS570");
 DISPLAY_SetTextColor(Blue);
 DISPLAY_DisplayString(1, 0, "Software: Erika RTOS");
 /* Turn on first LED */
 EE_LED_On(0);
 
 ...
```

<a id="OSEK.2FVDX_Extensions"></a>

## OSEK/VDX Extensions

This Section contains information about the OSEK/VDX Extensions (or optional features) that have been implemented for the ARM Cortex RX support.

TODO: Add Resource Management at ISR level

TODO: Add System Timer support

<a id="Flashing"></a>

## Flashing

The build process creates a folder called **flasher** in the Debug folder.
To flash the device via the TI Uniflash, simply execute the **flash.bat**.
Currently the path to the Uniflash program is hardcoded to   
`C:\ti\uniflashv3\ccs_base\scripting\examples\uniflash\cmdLine\uniflash`

TODO: Change flash path according given installation.

<a id="Examples"></a>

## Examples

- The examples and tests are available in this folders:
  - [ERIKA SVN: Porting Examples](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_rx/ti_tms570/porting_examples/): TI TMS570 Development Board (Cortex R4) examples.

<a id="See_also"></a>

## See also

- [Tutorial: Installing ERIKA and RT-Druid, and compile your first application](Tutorial_PIC30_-_Installing_ERIKA_and_RT-Druid_and_compile_your_first_application--1637.md "Tutorial: Installing ERIKA and RT-Druid, and compile your first application")
- [Tutorial: RT-Druid and OIL basics](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=ARM_Cortex_RX) · [Archived source revision 6131](http://erika.tuxfamily.org/wiki/index.php?oldid=6131)
- Last source edit: 2019-01-02T08:09:03Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Chris Kreuzberger, Pj.
- [Original MediaWiki source](../source/wikitext/2486.mediawiki) · [Original editing history](../source/history/batch-001.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
