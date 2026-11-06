# Renesas RL78

ERIKA Enterprise Manual for Renesas RL78 targets

<a id="Introduction"></a>

## Introduction

This manual describes the porting details of the ERIKA Enterprise kernel(s) for the Renesas families of microcontrollers which supports 8/16-bit CISC RL78 cores (aka RL78).

Due to customer restrictions, this porting is not yet public. If you want to get more information about the RL78 porting, please contact [info@evidence.eu.com](mailto:info@evidence.eu.com).

<a id="ERIKA_Enterprise_and_RT-Druid_for_RL78"></a>

### ERIKA Enterprise and RT-Druid for RL78

Embedded applications often require tight control on the temporal behavior of each single activity in the system. Real-time complex system systems such as Wireless Sensor Networks are nowadays deployed in academic and industrial environments. The very limited set of resources available in the popular hardware platforms, and the diversified domains of WSN applications, require the adoption of an Operating System responding to the following pre-requisites:

- minimum footprint to fit the limited RAM capacity (of the order of few KB);
- tunable scheduling algorithm to handle the execution of the tasks;
- an application interface acting on the kernel layer and well decoupled from OS service implementation.

ERIKA Enterprise and RT-Druid represent the answer of Evidence Srl for the development of scalable real-time applications for RL78.

ERIKA Enterprise provides RL78 developers the following features:

- Traditional RTOS features:
  - Support for four conformance classes to match different application requirements;
  - Support for preemptive and non-preemptive multitasking;
  - Support for fixed priority scheduling;
  - Support for stack sharing techniques, and one-shot task model to reduce the overall stack usage;
  - Support for shared resources;
  - Support for periodic activations using Alarms;
  - Support for centralized Error Handling;
  - Support for hook functions before and after each context switch.

- RT-Druid development environment
  - Development environment based on the Eclipse IDE;
  - Support for the OIL language for the specification of the RTOS configuration;
  - Graphical configuration plugin to easily generate the OIL configuration file and to easily configure the RTOS parameters;
  - Full integration with the Cygwin development environment to provide a Unix-style scripting environment;
  - Apache ANT scripting support for code generation.

- RL78 integration features
  - Installation setup which integrates the [C Compiler Package for RL78 Family](https://www.renesas.com/en-us/products/software-tools/tools/compiler-assembler/compiler-package-for-rl78-family.html) and Renesas [e2studio](https://www.renesas.com/en-us/products/software-tools/tools/ide/e2studio.html) IDE together with ERIKA Enterprise and RT-Druid;
  - Support for Renesas [CA78K0R](http://tool-support.renesas.com/autoupdate/support/eng/cs_plus/CA78K0R_List.html) Compiler;
  - Support for Renesas [E1](https://www.renesas.com/en-sg/products/software-tools/tools/emulator/e1.html) debugger/emulator;
  - Support for the following families Renesas RL78 MCUs:
    - [RL78/F13](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rl78/rl78f1x/rl78f13.html)
    - [RL78/F14](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rl78/rl78f1x/rl78f14.html)
    - [RL78/G14](https://www.renesas.com/en-us/products/microcontrollers-microprocessors/rl78/rl78g1x/rl78g14.html)
  - Support for following boards
    - [QB-R5F10BMG-TB](https://www.renesas.com/en-eu/products/software-tools/boards-and-kits/cpu-mpu-boards/qb-r5f10bmg-tb.html) (RL78/F13)
    - [QB-R5F10PPJ-TB](https://www.renesas.com/en-us/products/software-tools/boards-and-kits/cpu-mpu-boards/qb-r5f10ppj-tb.html) (RL78/F14)
    - [YRPBRL78G14](https://www.renesas.com/en-us/products/software-tools/boards-and-kits/renesas-promotion-boards/yrpbrl78g14-for-rl78-g14.html) (RL78/G14)
  - List of functions:
    - Full support for Renesas [e2studio](https://www.renesas.com/en-us/products/software-tools/tools/ide/e2studio.html) IDE
    - Full support for [Lauterbach](http://www.lauterbach.com/bdm78k0r.html) JTAG Debugger
    - Full support for ORTI

<a id="Integration_with_other_tools_for_RL78"></a>

### Integration with other tools for RL78

ERIKA Enterprise and RT-Druid aims to the best integration with the existing tools for development available from the RL78 microcontrollers.
RT-Druid will be used to quickly configure the application, setting temporal parameters of real-time tasks, memory requirements, stack allocation and many other parameters. Moreover, RT-Druid generates the application template, and leaves the developer the task to implement the logic of each single task.
While programming the application, the developer can exploit the power and flexibility offered by the primitives of the ERIKA Enterprise real-time kernel.
ERIKA Enterprise also supports the compiling environments provided by Renesas, providing also direct support for the programming and JTAG solutions of Renesas.

<a id="Content_of_this_document"></a>

### Content of this document

The purpose of this document is to describe all the information needed to create, develop and modify an Erika Enterprise application for the RL78 family of microcontrollers.

In particular, the document describes:

- The design flow which should be used to generate an Erika Enterprise application;
- The configuration of the development environment;
- The options which are available to configure the system.

As a final note, all the settings which are explained in this document apply both to Erika Enterprise if not otherwise stated.

<a id="Erika_Enterprise_for_RL78"></a>

## Erika Enterprise for RL78

<a id="The_RT-Druid_and_Erika_Enterprise_design_flow"></a>

### The RT-Druid and Erika Enterprise design flow

The typical development environment provided by Renesas for the software development for the Renesas microcontrollers is composed by the Renesas e2studio. Renesas e2studio is a development environment for Microsoft Windows which integrates a source code editor, an instruction set simulator and a debugger.

In addition to the traditional development flow, Evidence Srl provides a design and configuration environment named RT-Druid, based on [Eclipse](http://www.eclipse.org). Eclipse is an open framework initially developed by IBM, which allows the possibility of integrating various development tools in a common environment.

For that reason, when developing an application for Erika Enterprise the user is supposed to write the source code inside the RT-Druid IDE.

Application compilation is also done inside the Eclipse Framework. In fact, the RTDruid code generator is able to generate the Erika Enterprise configuration files together with a set of configuration files (typically, a makefile plus a set of .c files) which are then used to compile the source code.

The choice of the Cygwin environment has been done to simplify the building process of an application: in fact, Cygwin provides a set of traditional Unix tools like make, awk, sed, which are really useful to implement a command line application building framework. Moreover, these tools are typically available for free on the Linux platform, easing in this way the porting of the application to a free development environment such as Linux.

<a id="Building_an_application_from_command_line"></a>

#### Building an application from command line

The RT-Druid plugins provide three ways to develop an application:

1. A graphical interface to simplify the development of an application, based on Eclipse.
2. A scripting interface based on [Apache ANT](http://ant.apache.org), which is the default scripting environment used in the Eclipse Framework.
3. A standalone code generator, that does not use Eclipse.

Using ANT or the standalone version, the developer can automatically generate from scripts the configuration data and the makefiles which are then used to compile the application. This removes the need of opening the graphical environment to compile an application, providing a way to implement automatic compilation scripts and regression tests.

Please refer to the RT-Druid reference manual for information about ANT scripting.

<a id="Setting_up_the_compiling_environment_for_RL78"></a>

### Setting up the compiling environment for RL78

Erika Enterprise has been designed to be compiled using the [C Compiler Package for RL78 Family](https://www.renesas.com/en-us/products/software-tools/tools/compiler-assembler/compiler-package-for-rl78-family.html). The RL78 porting of ERIKA Enterprise in particular can be compiled using the [C Compiler Package for RL78 Family](https://www.renesas.com/en-us/products/software-tools/tools/compiler-assembler/compiler-package-for-rl78-family.html).

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Renesas_RL78) · [Archived source revision 6110](http://erika.tuxfamily.org/wiki/index.php?oldid=6110)
- Last source edit: 2018-06-04T15:16:53Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Giuseppe Serano, Pj.
- [Original MediaWiki source](../source/wikitext/2539.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
