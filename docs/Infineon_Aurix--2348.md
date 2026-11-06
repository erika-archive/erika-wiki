# Infineon Aurix

<a id="Infineon_Aurix_support"></a>

## Infineon Aurix support

ERIKA Enterprise supports the Infineon AURIX family microcontrollers.

Currently the TC27x and TC29x AURIX families have been fully ported.

Due to customer restrictions, this porting of TC29x AURIX family is not yet public. If you want to get more information about the TC29x AURIX family porting, please contact [info@evidence.eu.com](mailto:info@evidence.eu.com).

The support includes:

1. Support for the HIGHTEC GCC Compiler (form both single and multicore) and TASKING compiler (only for singlecore).
2. Support for single- and multi-stack configurations.
3. ISR Type 1 and Type 2.
4. ORTI support.
5. Full Lauterbach support.

- Supported compilers:
  - HIGHTEC GCC Compiler v4.6.3.1 & 4.9.2.0 (for both Single and Multicore).
  - TASKING VX-toolset for TriCore v4.0r1 (only for Singlecore).
  - WIND RIVER DIAB Compiler Rel. 5.9.2.0 (only for Singlecore).

- Mode of operation
  - Monostack: The Monostack configuration of the ERIKA Kernel models the fact that all tasks and ISRs in the system share the same stack.
  - Multistack: Every thread can have its private stack, or it can share it with other threads.
  - Multicore: It follows the same philosophy used by [ERIKA on other multicore systems](ERIKA_multicore_support--2066.md "ERIKA multicore support") and specified by [Autosar](http://www.autosar.org/): two instances of the operating systems run on the two cores, and communication between cores is performed with a few APIs and shared memory.

- **CYGWIN**
  - **Under Cygwin environment you MUST use make command version 4.2.1 or above**

<a id="MCU_.26_Board"></a>

#### MCU & Board

- The porting have been completly developed on top of:
  - TriBoard TC2x5 v2.0 equiped with a TC275TE MCU
  - TriBoard TC2x5 v2.0 equiped with a TC264DE MCU
  - TriBoard TC2x5 v2.0 equiped with a TC297TA MCU (please contact [info@evidence.eu.com](mailto:info@evidence.eu.com))

<a id="Target_Configuration_and_Programming"></a>

## Target Configuration and Programming

ERIKA Enterprise is configured through  [RT-Druid and an OIL file](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics"). Here are listed, after the information to set compiler path, the OIL fields customized for Tricore Aurix architecture.

<a id="Compiler_Path"></a>

#### Compiler Path

It is possible to choose the path of the compiler in three different ways:

- *PATH enviornment variable*: You can put compilers bin directories in PATH and the environmet can use them from here.
- *Compiler specific environment variables*:
  - **HIGHTEC GCC toolchain**: You can specify the compiler path for HIGHTEC GCC with the **TRICORE\_GCCDIR**.
  - **Altium TASKING toolchain**: You can specify the compiler path for Altium TASKING with the **TRICORE\_TASKINGDIR**.
  - **Wind River Diab toolchain**: You can specify the compiler path for Altium TASKING with the **TRICORE\_DIABDIR**.
- *RT-Druid configuration file* see [RT-Druid configuration#Compiler paths](RT-Druid_configuration--2158.md#Compiler_paths "RT-Druid configuration"):
  - **preference\_tricore\_\_path\_for\_gnu\_compiler** set HIGHTEC gcc compiler path for Tricore AURIX
  - **preference\_tricore\_\_path\_for\_tasking\_compiler** set Altium TASKING compiler path for Tricore AURIX
  - **preference\_tricore\_\_path\_for\_diab\_compiler** set Wind River Diab compiler path for Tricore AURIX

Here is an [example of RT-Druid configuration file](Common_oil.pref_example--2161.md "Common oil.pref example").

<a id="CPU"></a>

#### CPU

**CPU\_DATA** must be set to **TRICORE**.
The compiler is specificed with the **COMPILER\_TYPE** item, supported values are **GNU** (the default value) and **TASKING**.

On multicore systems, one **CPU\_DATA** instance can exist for each core. They must have different **ID**s. See [ERIKA multicore support](ERIKA_multicore_support--2066.md "ERIKA multicore support") for more details about multicore systems on Erika. Later in this page you will find a paragraph relative to specific multicore support developed for Tricore Aurix, according to **Autosar OS 4.0 Rev 3** specifications.

Tricore AURIX support CPU clock configuration with a simple PLL driver. The target clock value in MHz can be set with the *CPU\_CLOCK'* field.
We kept the algorithm to avaluate PLL parameters simple, so it implements a best effort approach to set the right value.
In any case max declared CPU clock value (i.e. 200 Mhz for TC27x & TC26x families), is guaranteed to be perfectly matched.

**N.B.** To get the real value set you can use **EE\_tc27x\_get\_clock()** API after executing **StartOS**, PLL configuration is done during OS start-up.

Moreover a new field to declare a custom linker script have been added to CPU\_DATA block: **LINKERSCRIPT = "fake.ld";**

Example of a CPU\_DATA section:

```
   CPU_DATA = TRICORE {
     CPU_CLOCK = 200.0;
     APP_SRC = "code.c";
     COMPILER_TYPE = GNU;
     MULTI_STACK = TRUE {
       IRQ_STACK = TRUE {
           SYS_SIZE = 128;
       };
     };
   };
```

<a id="MCU"></a>

#### MCU

**MCU\_DATA** supports the **TC27x**, **TC27xA**, **TC27xB**, **TC27xC** and **TC26x** values. Compiler can be specified even in **MCU\_DATA** block and will inherited by all configured CPUs (useful in multicore project configuration).

Note: due to a currupted register file of GNU compiler ( HighTec GCC Version 4.9.x.x ), the compiling of **TC27x** and **TC27xA** MCU models is broken.

```
 MCU_DATA = TRICORE {
   MODEL = TC27x;
   COMPILER_TYPE = GNU;
 };
```

<a id="BOARD"></a>

#### BOARD

There is only support form TriBoard TC2x5. This board only provide debug interface and 8 leds, so the support is limited to the LEDs configuration/driving and, because standard ERIKA demos require it, an external button (*external* means that have to be soldered by the user) mounted on pin P15.8 of (corresponding to pin 71 of PERIPHERALS (Xx02,Xx02) connector). Add the following OIL field to enable this support.

```
 BOARD_DATA = TRIBOARD_TC2X5;
```

<a id="Interrupt_Handling"></a>

#### Interrupt Handling

Due to the special implementation of the Interrupt Vector in AURIX architecture, each entry of the vector table is simply identified by it's priority value. It must be the application code that configure the service request node (*SRN'*) with the right priority, assigning in this way the right handler.

```
 ISR IsrLow {
   CATEGORY = 2;
   PRIORITY = 1;
   HANDLER = "isr_low"; 
 };
```

The mean of the fields are:

- **CATEGORY**: the type of ISR as specified by OSEK.
- **PRIORITY**: The ISR priority that represent it's position inside Interrupt Vector so it has to be considered as ISR Identifier. The **ENTRY** field, the one usually used to declare Interrupt IDs, is still available but it's superfluous because it has to be equal to PRIORITY and, in any case, priority value take the precedence.
- **HANDLER**: Declare the interrupt handler symbol. If it's not declared the the handler symbol is supposed to be equal to ISR block name (IsrLow in the example).

<a id="Trap_Handling"></a>

#### Trap Handling

With TriCore AURIX, for the first time, we support the options to register handler for TRAP/Exceptions. OSEK OIL do not provide any field for trap handling: it suppose that all the handling is done inside the Kernel. Usually that's what happens, but sometime can be useful have some mechanism to attach an handler for a particular class of TRAPs.

We decide to exetend ISR entry with the field **TRAP** that can be set to TRUE to enable TRAP handling. In this case you have to choose the TRAP class with the field LEVEL (or ENTRY). The only valid values for this configuration are:

- **TRAP\_MMU** (Actually useless because TC27x and TC26x families don't have MMU, just a place holder)
- **TRAP\_PROT** (Handler for protection traps)
- **TRAP\_INST** (Handler for instructions traps)
- **TRAP\_CONT** (Handler for context traps)
- **TRAP\_BUS** (Handler forn bus traps)
- **TRAP\_ASS** (Handler for assertion traps) (please don't be silly :))
- **TRAP\_SYS** (Handler for system calls)
- **TRAP\_NMI** (Handler for NMI trap)

OIL TRAP configuration example:

```
 ISR trap_context {
     LEVEL = "TRAP_CONT";
     HANDLER = "EE_trap_context";   //Trap handler
     TRAP = TRUE;
 };
```

To define the handler in your code, you have to use the following syntax:

```
 TRAP(EE_CLASS_TRAPCONT, EE_trap_context) {
   while(1) {
     ; /* dummy */
   }
 }
```

TRAP class identifiers are the following:

- EE\_CLASS\_TRAPMMU
- EE\_CLASS\_TRAPPROT
- EE\_CLASS\_TRAPINST
- EE\_CLASS\_TRAPCONT
- EE\_CLASS\_TRAPBUS
- EE\_CLASS\_TRAPASS
- EE\_CLASS\_TRAPSYS
- EE\_CLASS\_TRAPNMI

Inside the TRAP handler TIN (Trap Identification Number) value can be accessed with **EE\_tc\_get\_TIN()** function or, for HIGHTEC GNUC Compiler, with the local variable **tin**. For more information you can check the **$(ee)/pkg/cpu/tricore/inc/ee\_tc\_trap.h** file.

<a id="EEOPT"></a>

#### EEOPT

EEOPT is a way to specify configuration flags to the Erika build environment.
EEOPTs can be specified as strings in the OS section of the OIL file. Examples:

```
EE_OPT = "EE_DEBUG";
EE_OPT = "__ASSERT__";
```

Please notice that spelling inside the OIL file includes an underscore: EE\_OPT.

The only supported format for EEOPTs is a single name, which should be a valid C identifier (i.e., only Latin letters, digits, and underscore are allowed; the first character cannot be a digit). And any other format is not supported, and even if it works now, it may break in the future.

The following EEOPTs are specific of AURIX Architecture:

- **EE\_DEBUG**: Replace the often used DEBUG option (because it conflict with compilers DEBUG define). Enable debug compiler options, basically less optimization and debug symbols generation plus defualt TRAP handlers are implemented as busy loops instead of system reset.
- **EE\_EXECUTE\_FROM\_RAM**: When specified, a linker script is used that maps both code and data in the RAM space. Executables produced with this option can be used only together with a debugger that loads the program in memory. By default, code and constant data are mapped to Flash, data to RAM.
- **EE\_SAVE\_TEMP\_FILES**: Enable temporary files saving for the compiler, useful to debug build process and to inspect generate assembly code. It's useful only for HIGHTEC GCC compiler because for TASKING compiler is always active. For the GCC compiler it has been added the switch because the size of temporary files is **huge**.
- **EE\_ICACHE\_ENABLED**: Enable the instruction cache in start-up code.
- **EE\_DCACHE\_ENABLED**: Enable data cache in start-up code

<a id="OSEK.2FVDX_Extensions"></a>

## OSEK/VDX Extensions

This Section contains information about the OSEK/VDX Extensions (or optional features) that have been implemented for the AURIX support.

<a id="Resource_Managament_at_ISR_level"></a>

#### Resource Managament at ISR level

This feauture is automatically enabled by RT-Druid during the configuration generation step. To specify that a Resource is used by both a Task and a ISR you need to add that resource to the corrisponding ISR object as follows:

```
 TASK Task1 {
   ...
   RESOURCE = "ResourceA";
 };
 
 ISR <SYMBOL> {
   PRIORITY = <PRIORITY_LEVEL>;
   CATEGORY = <ISR_TYPE>;
   RESOURCE = "ResourceA";
 };
 
 RESOURCE ResourceA { RESOURCEPROPERTY = STANDARD; };
```

<a id="System_Timer"></a>

#### System Timer

The OSEK/VDX standard provides support for a **System Counter** (a counter that is automatically linked to a hardware timer). The System Timer is used to give a coherent timing reference across the entire application.

In ERIKA Enterprise, this special counter has been named **System Timer**. To use it, you need to set a specific attribute in a Counter definition. Please note that only one counter **for each core** can be the System Timer.

A Counter which is not a System Counter must be incremented explicitly using the Autosar primitive **IncrementCounter**.

The following is an example OIL definition for a System Counter:

```
 CPU_DATA = TRICORE{
   CPU_CLOCK = 200.0;
   ...
 };
 
 COUNTER SystemTimer {
   MINCYCLE = 1;
   MAXALLOWEDVALUE = 2147483647;
   TICKSPERBASE = 1;
   TYPE = HARDWARE {
     DEVICE = "STM_SR0";
     SYSTEM_TIMER = TRUE;
     PRIORITY = 1;
   };
   SECONDSPERTICK = 0.001;
 };
```

The meaning of the various attributes is as follows:

- **CPU\_DATA/CPU\_CLOCK** is used to declare the clock frequency (in MHZ).
- **COUNTER/TYPE** must be set to **HARDWARE**, and **SYSTEM\_TIMER** must be set to true.
- **COUNTER/TYPE/DEVICE** must be a valid device that can be used for a system timer. Currently, for TRICORE only **STM** (System Timer Module) MCU peripheral is a valid device for system timer. Both Interrupt source of this peripheral can be set to device and allowed values are **STM\_SR0** and **STM\_SR1**
- **COUNTER/TYPE/PRIORITY** By default SYSTEM\_TIMER is tied to smallest ISR priority (i.e. PRIORITY = 1;), but it can be overritten. Ovveride is necessay in multicore environment because priority 1 is used by the **Intercore Interrupt Request**.
- **COUNTER/SECONDSPERTICK** is used to declare the wanted time duration of one hardware tick in seconds.

The System Timer can be attached to ALARMs as usual, as in the following example:

```
 ALARM AlarmExample {
   COUNTER = SystemTimer;
   ACTION  = ACTIVATETASK{
      TASK = TaskExample;
   };
 };
```

<a id="CPU_MCU_.26_BOARD_API"></a>

## CPU MCU & BOARD API

In addition to **AUTOSAR OS Kernel Interface**, in ERIKA AURIX porting are implemented a bunch of utility functions that will be considered as part of **ERIKA API**. As usual they are separated in the three logical layer that compose ERIKA architecture abstraction: **CPU, MCU & BOARD**.

<a id="CPU_API"></a>

#### CPU API

CPU layer represent all the behaviour shared between all the families of AURIX MCUs. In this layer are declared the functions to temporary disable **ENDINIT** and **SAFETY\_ENDINIT** register protection (see Infineon AURIX documentation). These functions are a little bit tricky: *declaration* belong to CPU layer, because AURIX architecture documentation states that every AURIX implementation has some kind of **ENDINIT** and **SAFETY\_ENDINIT** protection, but delegate implementation details to each AURIX family, so functions *definitions* has been done inside MCU files.

- **void EE\_tc\_endint\_disable( void )**: Temporary disable ENDINT protection.
- **void EE\_tc\_endint\_enable( void )**: Re-enable ENDINT protection.

- **void EE\_tc\_safety\_endinit\_disable( void )**: Temporary disable SAFETY\_ENDINIT protection.
- **void EE\_tc\_safety\_endinit\_enable( void )**: Re-enable SAFETY\_ENDINIT protection.

<a id="MCU_API"></a>

#### MCU API

MCU layer represent the behaviour tied to an specific AURIX family of MCUs. For now only family TC27x is supported.
Most part of the utilities belong to this layer:

- **void EE\_tc2Yx\_get\_clock ( void )**: Return CPU clock frequency in HZ.
- **void EE\_tc2Yx\_configure\_clock( EE\_UREG fclock )**: Make the best effort to set CPU clock frequency to fclock value. It's the function used by **StartOS** when a **CPU\_CLOCK** is configured in **CPU\_DATA**.
- **void EE\_tc2Yx\_delay ( EE\_UREG usec )**: Implement a busy loop wait of **usec** micorseconds.
- **void EE\_tc2Yx\_stm\_set\_sr0( EE\_UINT32 usec, EE\_TYPEISR2PRIO intvec )**: Programs **STM compare register 0** to trigger an IRQ after **usec** microseconds. **intvec** is the priority tied to this source, in other words it is the Interrupt Vector Table entry that will handle STM interrupt. With intvec == 0, the correponding service request node is left unprogrammed or resetted.
- **void EE\_tc2Yx\_stm\_set\_sr0\_next\_match( EE\_UINT32 usec )**: Change **previous programmed** STM compare register 0 to trigger next IRQ after usec microseconds. To mantain fixed interrupt interval, it have to been called at the beginning of **intvec** handler.
- **void EE\_tc2Yx\_stm\_set\_sr1( EE\_UINT32 usec, EE\_TYPEISR2PRIO intvec )**: Programs **STM compare register 1** to trigger an IRQ after **usec** microseconds. **intvec** is the priority tied to this source, in other words it is the Interrupt Vector Table entry that will handle STM interrupt. With intvec == 0, the correponding service request node is left unprogrammed or resetted.
- **void EE\_tc2Yx\_stm\_set\_sr1\_next\_match( EE\_UINT32 usec )**: Change **previous programmed** STM compare register 1 to trigger next IRQ after usec microseconds. To mantain fixed interrupt interval, it have to been called at the beginning of **intvec** handler.

**SR0** and **SR1** API are both available to the user if **System Timer** is **not** configured. Otherwise only the one not used by system timer will be available.

<a id="Board_API"></a>

#### Board API

BOARD layer represent the specific board support. There is only aminimal support for TriBoard TC2x5 v2.0 equiped with a TC275TE MCU:

- **void EE\_tc2x5\_leds\_init( void )**: Initialize the 8 boards leds.
- **void EE\_tc2x5\_leds\_on( void )**: Turns all the 8 leds.
- **void EE\_tc2x5\_leds\_off( void )**: Turns off all the 8 leds.
- **void EE\_tc2x5\_turn\_led(enum EE\_tc2x5\_led\_id led\_id, enum EE\_tc2x5\_led\_status onoff)**: Turn the status of the led **led\_id** (led IDs are collected in an enum in the form: **EE\_TRIBOARD\_2X5\_LED\_{x}** with {x}=[1..8]) on (onoff == **EE\_TRIBOARD\_2X5\_LED\_ON**) or off (onoff == **EE\_TRIBOARD\_2X5\_LED\_OFF**).
- **EE\_BIT EE\_tc2x5\_read\_button( void ): read external button value**
- **void EE\_tc2x5\_button\_irq\_init( EE\_TYPEISR2PRIO intvec )**: Configure the external button has an interrupt source and tie it to **intvec** priority handler.
- **void EE\_tc2x5\_button\_irq\_clear\_request( void )**: Clear external button interrupt request.

External button have to be connected to pin P15.8 on TC275TE corrisponding to pin 71 of PERIPHERALS (Xx02,Xx02) connector of TriBoard TC2x5.

<a id="Debugger_support"></a>

## Debugger support

- [Lauterbach TRACE32 Support for Infineon Aurix](Lauterbach_TRACE32_Support_for_Infineon_Aurix--2532.md "Lauterbach TRACE32 Support for Infineon Aurix")
- [iSYSTEM winIDEA Support for Infineon Aurix](ISYSTEM_winIDEA_Support_for_Infineon_Aurix--2531.md "ISYSTEM winIDEA Support for Infineon Aurix")

<a id="Multicore_Autosar_OS_Support"></a>

## Multicore Autosar OS Support

For details please see the following page: [Erika AUTOSAR OS](Erika_AUTOSAR_OS--2476.md "Erika AUTOSAR OS")

<a id="Build_Multicore_Application_Single_ELF_with_HighTec_GCC_Compiler"></a>

#### Build Multicore Application Single ELF with HighTec GCC Compiler

The conventional ERIKA multicore build chain generate an ELF file for each core and the real application image is loaded on the device by Lauterbach, trought scripts. This approach is not straightforwardly portable on other programmer tools. Fortunately HighTec GCC Compiler has some peculiar features that have allowed us to change this approach, and for TriCore is possible to compile a Multicore Application contained in a single ELF.

To enable this new build method add the following **EEOPT=EE\_BUILD\_SINGLE\_ELF** to the project OIL file.

To export some symbols from a core an **HighTec GCC export file** is needed. An HighTec export file looks like this:

```
 EXPORT FUNCTION _START ;
 EXPORT FUNCTION ErrorHook ;
 EXPORT FUNCTION StartupHook ;
 EXPORT FUNCTION ShutdownHook ;
 
 EXPORT OBJECT EE_oo_ErrorHook_ServiceID ;
 EXPORT OBJECT EE_oo_ErrorHook_data ;
 
 ...
```

To inform the build system to use an export file for a given core change the **COMPILER\_TYPE** field of **CPU\_DATA** OIL container, in the following way:

```
 CPU_DATA = TRICORE {
   ID = "master";
   ...
   COMPILER_TYPE = GNU {
     EXPORT_FILE = "<relative path to the export file>";
   };
   ...
  };  
```

If this is done add explicitly **EEOPT=EE\_BUILD\_SINGLE\_ELF** is no more needed.

**N.B:** When used this approach an export files for the master core have to be provided always. The file can be empty if no symbols have to be exported by master core.

This build approach is showed on following RT-Druid TriCore templates:

*tricore/infineon\_TriBoard-TC2X5\_V2.0/Multicore automatic tests/Multicore System StartUp test*

*tricore/infineon\_TriBoard-TC2X5\_V2.0/Multicore automatic tests/Multicore Spinlocks test*

<a id="Additional_Notes"></a>

## Additional Notes

Since ERIKA 2.4.0 full AUTOSAR SC4 OS support for AURIX is publically released: you can find all the information about the implemented features and how to configure them at this page: [Erika AUTOSAR OS](Erika_AUTOSAR_OS--2476.md "Erika AUTOSAR OS").

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Infineon_Aurix) · [Archived source revision 6123](http://erika.tuxfamily.org/wiki/index.php?oldid=6123)
- Last source edit: 2018-06-06T08:38:47Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Eguidieri, Pj, Armin Stingl, Francesco, Giuseppe Serano.
- [Original MediaWiki source](../source/wikitext/2348.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
