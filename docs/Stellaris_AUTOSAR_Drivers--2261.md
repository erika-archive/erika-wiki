# Stellaris AUTOSAR Drivers

<a id="AUTOSAR_Drivers"></a>

## AUTOSAR Drivers

To enable AUTOSAR Drivers for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AUTOSAR_R4_0__";
```

AUTOSAR Drivers need to be configured by C header compiler file (Compiler\_Cfg.h). These file (for now) needs to be manually written.  
Template of these file can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header compiler file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header compiler file is stored.

**Note:** Each AUTOSAR Driver must be enabled individually.

<a id="AUTOSAR_MCU_Driver"></a>

#### AUTOSAR MCU Driver

To enable AUTOSAR MCU Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_MCU_DRIVER__";
```

The AUTOSAR MCU Driver needs to be configured by C header and source files (Mcu\_Cfg.h and Mcu\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Mcu_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

Usage examples of the AUTOSAR MCU Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_PORT_Driver"></a>

#### AUTOSAR PORT Driver

To enable AUTOSAR PORT Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_PORT_DRIVER__";
```

The AUTOSAR PORT Driver needs to be configured by C header and source files (Port\_Cfg.h and Port\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Port_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

Usage examples of the AUTOSAR PORT Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_DIO_Driver"></a>

#### AUTOSAR DIO Driver

To enable AUTOSAR DIO Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_DIO_DRIVER__";
```

The AUTOSAR DIO Driver needs to be configured by C header and source files (Dio\_Cfg.h and Dio\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Dio_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

Usage examples of the AUTOSAR DIO Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_SCI_Driver"></a>

#### AUTOSAR SCI Driver

To enable AUTOSAR SCI Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_SCI_DRIVER__";
```

The AUTOSAR SCI Driver needs to be configured by C header and source files (Sci\_Cfg.h and Sci\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Sci_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

To use the SCI driver in interrupt mode, an ISR object must be added to OSEK/VDX configuration for every SCI Channel:

```
 ISR Sci_Channel_<Channel Number>_ISR {
   CATEGORY = 2;
   ENTRY = "UART_<Channel Number>";
   PRIORITY = <ISR Priority>;
 };
```

Where `<Channel Number>` is the "channel number" as stated in the SCI Driver Channel Identifier of the channel and `<ISR Priority>` is a number indicating the level of priority (0: Lowest).

Usage examples of the AUTOSAR SCI Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_GPT_Driver"></a>

#### AUTOSAR GPT Driver

To enable AUTOSAR GPT Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_GPT_DRIVER__";
```

The AUTOSAR GPT Driver needs to be configured by C header and source files (Gpt\_Cfg.h and Gpt\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Gpt_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

The Stellaris General-Purpose Timer Module (GPTM) contains six 16/32-bit GPTM blocks and six 32/64-bit Wide GPTM blocks.

Each 16/32-bit GPTM block provides two 16-bit timers (referred to as Timer A and Timer B) that can be configured to operate independently (with optional 8-bit prescaler) or concatenated to operate as one 32-bit timer (without prescaler).

Channel Identifiers for 16/32-bit GPTM blocks operating indipendently are the followings:

```
 GPT_CHANNEL_0_A /* block 0 timer A */
 GPT_CHANNEL_0_B /* block 0 timer B */
 GPT_CHANNEL_1_A /* block 1 timer A */
 GPT_CHANNEL_1_B /  block 1 timer B */
 ...
 GPT_CHANNEL_5_A /* block 5 timer A */
 GPT_CHANNEL_5_B /* block 5 timer B */
```

If a timer value can't be translated on 16-bit, the driver enables the 8-bit prescaler extending the timer counter size to 24-bit.

Channel Identifiers for 16/32-bit GPTM blocks concatenated are the followings:

```
 GPT_CHANNEL_J_0 /* block 0 [timer B]:[timer A] */
 GPT_CHANNEL_J_1 /* block 1 [timer B]:[timer A] */
 ...
 GPT_CHANNEL_J_5 /* block 5 [timer B]:[timer A] */
```

The timer counter size is fixed to 32-bit.

Each 32/64-bit Wide GPTM block provides two 32-bit timers (referred to as Timer A and Timer B) that can be configured to operate independently (with optional 16-bit prescaler) or concatenated to operate as one 64-bit timer (without prescaler).

Channel Identifiers for 32/64-bit GPTM blocks operating indipendently are the followings:

```
 GPT_CHANNEL_W_0_A /* block 0 timer A */
 GPT_CHANNEL_W_0_B /* block 0 timer B */
 GPT_CHANNEL_W_1_A /* block 1 timer A */
 GPT_CHANNEL_W_1_B /  block 1 timer B */
 ...
 GPT_CHANNEL_W_5_A /* block 5 timer A */
 GPT_CHANNEL_W_5_B /* block 5 timer B */
```

If a timer value can't be represented on 32-bit, the driver enables the 16-bit prescaler extending the timer counter size to 48-bit.

Channel Identifiers for 32/64-bit GPTM blocks concatenated are the followings:

```
 GPT_CHANNEL_J_W_0 /* block 0 [timer B]:[timer A] */
 GPT_CHANNEL_J_W_1 /* block 1 [timer B]:[timer A] */
 ...
 GPT_CHANNEL_J_W_5 /* block 5 [timer B]:[timer A] */
```

The timer counter size is fixed to 64-bit.

To use the GPT driver in interrupt mode, an ISR object must be added to OSEK/VDX configuration for every GPT Channel:

```
 ISR Gpt_Channel_<Channel>_ISR {
   CATEGORY = 2;
   ENTRY = "[WIDE_]TIMER_<Channel>";
   PRIORITY = <ISR Priority>;
 };
```

Where `<Channel>` is the "channel identifier" part as stated in the GPT Driver Channel Identifier of the channel and `<ISR Priority>` is a number indicating the level of priority (0: Lowest).

Examples:

```
 /* GPT_CHANNEL_0_B: 16-bit GPTM block 0 timer B */
 ISR Gpt_Channel_0_B_ISR {
   CATEGORY = 2;
   ENTRY = "TIMER_0_B";
   PRIORITY = 4;
 };
 ...
 /* GPT_CHANNEL_J_1: 32-bit GPTM conactenated GPTM block 1 [timer B]:[timer A] */
 ISR Gpt_Channel_J_1_ISR {
   CATEGORY = 2;
   ENTRY = "TIMER_1_A"; /* Concatenated GPTM blocks ALWAYS refers timer A ENTRY */
   PRIORITY = 3;
 };
 ...
 /* GPT_CHANNEL_W_4_A: 32-bit WIDE GPTM block 4 timer A */
 ISR Gpt_Channel_0_B_ISR {
   CATEGORY = 2;
   ENTRY = "WIDE_TIMER_4_A"; /* WIDE GPTM block */
   PRIORITY = 6;
 };
 ...
 /* GPT_CHANNEL_J_W_3: 64-bit conactenated WIDE GPTM block 3 [timer B]:[timer A] */
 ISR Gpt_Channel_J_W_3_ISR {
   CATEGORY = 2;
   ENTRY = "WIDE_TIMER_3_A"; /* Concatenated WIDE GPTM blocks ALWAYS refers timer A ENTRY */
   PRIORITY = 7;
 };
```

Usage examples of the AUTOSAR GPT Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_DMA_Driver"></a>

#### AUTOSAR DMA Driver

To enable AUTOSAR DMA Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_DMA_DRIVER__";
```

The AUTOSAR DMA Driver needs to be configured by C header and source files (Dma\_Cfg.h and Dma\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Dma_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

To use the DMA driver in interrupt mode, an ISR object must be added to OSEK/VDX configuration for Software DMA Channel Transfer End and another ISR must be added to OSEK/VDX configuration for DMA Transfer Error:

```
 ISR Dma_SoftwareTransferEnd_ISR {
   CATEGORY = 2;
   ENTRY = "UDMA_SOFT_TRANSF";
   PRIORITY = <ISR Priority>;
 }
```

```
 ISR Dma_TransferError_ISR {
   CATEGORY = 2;
   ENTRY = "UDMA_ERR";
   PRIORITY = <ISR Priority>;
 };
```

Where `<ISR Priority>` is a number indicating the level of priority (0: Lowest).

Usage examples of the AUTOSAR DMA Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_SPI_Driver"></a>

#### AUTOSAR SPI Driver

To enable AUTOSAR SPI Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_SPI_DRIVER__";
```

The AUTOSAR SPI Driver needs to be configured by C header and source files (Spi\_Cfg.h and Spi\_Cfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Spi_Cfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

To use the AUTOSAR SPI driver, the AUTOSAR DMA driver must be enabled and configured too. Moreover an ISR object must be added to OSEK/VDX configuration for every TI Stellaris SSI harware unit configured and :

```
 ISR Spi_HwUnit_<Hardware Unit Number>_ISR {
   CATEGORY = 2;
   ENTRY = "SSI_<Hardware Unit Number>";
   PRIORITY = <ISR Priority>;
 }
```

Where `<Hardware Unit Number>` is the TI Stellaris SSI hardware unit number (from 0 to 3) and `<ISR Priority>` is a number indicating the level of priority (0: Lowest).

Usage examples of the AUTOSAR SPI Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_WDG_Driver"></a>

#### AUTOSAR WDG Driver

Texas Instruments Stellaris LM4F232 MCU provides two watchdog peripherals: one clocked by Precision Internal Oscillator (PIOsc) with a fixed frequency of 16MHz and the other clocked System Clock (SysClk) which frequency is configurable by AUTOSAR MCU Driver.

Each watchdog is driven by a separate driver.

<a id="AUTOSAR_PIOSC_WDG_Driver"></a>

##### AUTOSAR PIOSC WDG Driver

To enable AUTOSAR PIOSC WDG Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_WDG_PIOSC_DRIVER__";
```

The AUTOSAR PIOSC WDG Driver needs to be configured by C header and source files (Wdg\_PIOscCfg.h and Wdg\_PIOscCfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Wdg_PIOscCfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

To use the AUTOSAR PIOSC WDG driver, almost another pheriperal must be configured and initialized to be clocked by PIOsc (eg. Adc, Spi, Sci, ...). Moreover an ISR object must be added to OSEK/VDX configuration:

```
 ISR Wdg_PIOsc_ISR {
   CATEGORY = 2;
   ENTRY = "WATCHDOG_TIMER";
   PRIORITY = <ISR Priority>;
 }
```

Where `<ISR Priority>` is a number indicating the level of priority (0: Lowest); if the driver is configured to fire "Standard" Interrupts, or:

```
 ISR Wdg_PIOsc_ISR {
   CATEGORY = 2;
   ENTRY = "NMI";
 }
```

If the driver is configured to fire Non-Maskable Interrupts with a fixed priority higher than "standard".

Usage examples of the AUTOSAR PIOSC WDG Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="AUTOSAR_SYSCLK_WDG_Driver"></a>

##### AUTOSAR SYSCLK WDG Driver

To enable AUTOSAR SYSCLK WDG Driver for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following `EE_OPT` attribute is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__AS_WDG_SYSCLK_DRIVER__";
```

The AUTOSAR PIOSC WDG Driver needs to be configured by C header and source files (Wdg\_SysClkCfg.h and Wdg\_SysClkCfg.c). These files (for now) need to be manually written.  
Templates of these files can be found in [contrib/as/arch/stellaris/config/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/config/).

The configuration C header file inclusion is done by `CFLAGS` attribute in the `OS` object of the OSEK/VDX configuration:

```
 CFLAGS = "-I<PATH>";
```

Where `<PATH>` is the absolute or relative directory path which configuration C header file is stored.

Instead the configurations C source file is added to the compilation process by `APP_SRC` attribute in the `CPU_DATA` object of the OSEK/VDX configuration:

```
 APP_SRC = "<PATH>/Wdg_SysClkCfg.c";
```

Where `<PATH>` is the absolute or relative directory path which configuration C source file is stored.

To use the AUTOSAR SYSCLK WDG driver an ISR object must be added to OSEK/VDX configuration:

```
 ISR Wdg_SysClk_ISR {
   CATEGORY = 2;
   ENTRY = "WATCHDOG_TIMER";
   PRIORITY = <ISR Priority>;
 }
```

Where `<ISR Priority>` is a number indicating the level of priority (0: Lowest); if the driver is configured to fire "Standard" Interrupts, or:

```
 ISR Wdg_SysClk_ISR {
   CATEGORY = 2;
   ENTRY = "NMI";
 }
```

If the driver is configured to fire Non-Maskable Interrupts with a fixed priority higher than "standard".

Usage examples of the AUTOSAR SYSCLK WDG Driver can be found at [examples/cortex\_mx/lm4f232xxxx/as](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/as)

<a id="Stand-alone_Library"></a>

#### Stand-alone Library

To build a stand-alone library (libas.a) containing enabled AUTOSAR Drivers for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain, the following code is needed in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__ADD_LIBS__";
 LIB = ENABLE {
   NAME = "AUTOSAR";
 };
```

It's possible to include into library the drivers configurations by the following `EE_OPT` attribute in the `OS` object of the OSEK/VDX configuration:

```
 EE_OPT = "__NO_APP__";
```

<a id="Keil_uVision_Integration"></a>

#### Keil uVision Integration

To integrate AUTOSAR Drivers for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain in a ARM KEIL uVision application project, it nees:

- To add a previously builded libas.a (containing drivers configurations) to a Target Sources Group of ARM KEIL uVision Project.
- To add AUTOSAR Drivers include path ([contrib/as/include/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/include/)) to ARM KEIL uVision C/C++ compiler include paths.
- To add AUTOSAR Drivers for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain [contrib/as/arch/stellaris/keil/include/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/as/arch/stellaris/keil/include/) to Keil uVision C/C++ compiler include paths.
- To add AUTOSAR Drivers configurations for Texas Instruments Stellaris LM4F232H5QD Evaluation Board with ARM KEIL compiler toolchain include path to ARM KEIL uVision C/C++ compiler include paths.

<a id="See_also"></a>

## See also

- [ARM Cortex MX#Building stand-alone libee.a using RT-Druid Eclipse](ARM_Cortex_MX--2226.md#Building_stand-alone_libee.a_using_RT-Druid_Eclipse "ARM Cortex MX")
- [ARM Cortex MX#Building ERIKA based application using KEIL uVision](ARM_Cortex_MX--2226.md#Building_ERIKA_based_application_using_KEIL_uVision "ARM Cortex MX")
- [AUTOSAR - Automotive Open System Architecture - Web site](http://www.autosar.org/)
- [Texas Instruments - Stellaris LM4F232 USB+CAN Evaluation Kits - Web site](http://www.ti.com/tool/ek-lm4f232?DCMP=cortexm4f&HQS=ek-lm4f232)
- [Keil Embedded Development Tools Web site](http://www.keil.com/)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Stellaris_AUTOSAR_Drivers) · [Archived source revision 4952](http://erika.tuxfamily.org/wiki/index.php?oldid=4952)
- Last source edit: 2012-11-20T15:48:50Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Outlawch.
- [Original MediaWiki source](../source/wikitext/2261.mediawiki) · [Original editing history](../source/history/batch-010.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
