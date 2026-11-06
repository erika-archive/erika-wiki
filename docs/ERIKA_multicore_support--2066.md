# ERIKA multicore support

ERIKA can run on multiple cores with static assignment of tasks and shared memory. One copy of the operating system runs on each core, with independent schedulers. It is possible to activate tasks and notify events remotely on a different core. Also mechanisms to share resources and variables are present.

<a id="Overview"></a>

### Overview

Today's embedded systems are continuously being extended to support
additional and more complex functionality. In many domains
(automotive, telecommunications, home automation), availability of powerful
hardware at low prices and cost/time market pressure are pushing for
integration of functionality on system-on-chip devices capable of
processing large amount of data in a short time.

Multicore systems are being considered as an economically viable
alternative to support this increasing computational demand. In this
context, Evidence proposes OS-level solutions and tools for embedded
multicore-on-a-chip.

The RT-Druid/ERIKA pair has been designed to handle multicore
development and programming by hiding the use of multicore
synchronization primitives. With multicore hiding, it is
possible to seamlessly migrate application code from a single
processor to a multicore system without changing a single line of the
source code.

ERIKA hides the multiple processor structure by providing an automatic
mapping of the RTOS API calls to the single processor or the multiple
processor implementation, according to the target of the call. This
mapping is obtained by exploiting an enhanced remote notification
mechanism based on multicore interrupts. Remote notification is
used to provide an implementation to kernel primitives acting on tasks
(resources) allocated to remote processors. Moreover, the notification
mechanism is hidden inside the implementation of the ERIKA primitives,
maintaining the same interface to the developer both for single and
for multicore systems.

The additional overhead caused by the remote execution of calls is
mainly due to the "send" of the remote notification from one side, and
to the interprocessor interrupt that is raised on the receiving
side. However, this overhead does
not have a great impact on typical applications where remote
activations are not as frequent as local activations.

<a id="Supported_architectures"></a>

### Supported architectures

Multicore architectures currently supported are:

- [Altera Nios II](Altera_Nios_II--1473.md "Altera Nios II")
- [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)")

<a id="Using_a_multicore_system"></a>

### Using a multicore system

Software written for a multicore ERIKA system differs very little from a single-core ERIKA application. The configuration specifies that the system is multicore and how code and OS objects are allocated to cores. The code uses the same APIs in the same manner as on single-core system. Only shared variable should be declared in a different way, and initialization code inside `main()` may differ. The ERIKA build system produces one executable image per core, each one containing an instance of the OS; shared data are present only in the first image.

<a id="OIL_configuration"></a>

#### OIL configuration

A multicore system is specified in an OIL file by declaring more than one instance of CPU\_DATA inside the OS section (only on supported architectures). Each CPU\_DATA section must specify a different ID value, and the *master* core must be declared with the MASTER\_CPU. The *master* core is the one hosting shared variables, and may have other features depending on the architecture. Core IDs can be any string. For example (for [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)")):

```
MASTER_CPU = "master";
CPU_DATA = PPCE200ZX {
	MODEL = E200Z6;
	ID = "master";
	APP_SRC = "master.c";
};
CPU_DATA = PPCE200ZX {
	MODEL = E200Z0;
	ID = "slave";
	APP_SRC = "slave.c";
};
```

The ID value must be used to allocate tasks, ISRs, counters, alarms to cores. For example:

```
TASK MainTask {
	CPU_ID = "master";
	PRIORITY = 1;
	AUTOSTART = FALSE;
	STACK = SHARED;
	ACTIVATION = 1;
	SCHEDULE = FULL;
};
TASK OtherTask {
	CPU_ID = "slave";
	PRIORITY = 3;
	AUTOSTART = FALSE;
	STACK = SHARED;
	ACTIVATION = 1;
	SCHEDULE = FULL;
};
```

A few options in the OS section are used to limit the scope of the communication between cores (and limit resource usage).

**USEREMOTETASK**

List of the tasks that can be acted upon remotely (via `ActivateTask()`, `SetEvent()`...). It can assume the value ALWAYS to enable remote support for all tasks. If this option is not present, all tasks are local.

**USEREMOTEEVENT**

When set to ALWAYS, it enables the support for remote `SetEvent()`. If this option is not present, no event can be set remotely.

<a id="Known_bugs"></a>

##### Known bugs

Due to a limitation in the code of the current version of RT-Druid, only one `OS` section should be present in an OIL file. If an `OS` section does not contains any CPU\_DATA elements, RT-Druid may create an additional CPU named "default\_cpu", and ultimately the project building will fail. This example is not currently supported:

```
OS EE {
       MASTER_CPU = "master";
       CPU_DATA = E200ZX {
               ID = "master";
               ...
       };
       CPU_DATA = E200ZX {
               ID = "secondary";
               ...
       };
       ...
};
...
OS EE {
       /* PROBLEM: an implicit "default_cpu" CPU_DATA section is created */
       KERNEL_TYPE = ECC1;
};
```

<a id="Application_programming"></a>

#### Application programming

Depending on the architecture, specific multi-core features may be supported. Standard APIs are not changed in syntax nor in semantics, except for a few details reported here. When `ActivateTask()` is called with a remote task, no error is returned if the maximum number of activations has been reached (this is different from what Autosar specifies, but it is more efficient). `StartOS()` is synchronized with a barrier shared among cores; the operating system starts when `StartOS()` has been called on all cores.

Variables to be shared must be declared and defined by using appropriate macros. For [Altera Nios II](Altera_Nios_II--1473.md "Altera Nios II") there is a specific set of macros. Here only the more recent macros (used since the [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)") multicore support) are described. This is an example of the definition of three variables:

```
int EE_SHARED_UDATA x[10];
volatile int EE_SHARED_IDATA y = 3;
const char EE_SHARED_CDATA msg[5] = "Ciao";
```

and this is an example of the declaration of the same variables (usually found inside a header file):

```
extern int EE_SHARED_UDATA x[10];
extern volatile int EE_SHARED_IDATA y;
extern const char EE_SHARED_CDATA msg[5];
```

The macro EE\_SHARED\_UDATA is used for uninitialized data (BSS), EE\_SHARED\_IDATA for initialized data, and EE\_SHARED\_CDATA for constant data. Additional modifiers, such as volatile, can be added.

Shared variables must be defined inside the code for the *master* core. The build system extracts the addresses of shared variables from the executable file of the first core, and generates reference symbols for the linker scripts of the other cores.

<a id="Generated_files"></a>

#### Generated files

For each core, RT-Druid creates one directory inside the output directory (normally called Debug or output). Each core directory contains the usual set of files (makefile, eecfg.h, and eecfg.c) plus possibly others. Two make files are generated in the output directory: makefile, which invokes the core-specific make files and contains also the rules to link everything together, and common.mk, which contains the options (EEOPTs and other variables) common to all cores. Also, a file common.c is produced that contains the shared OS variables and is compiled on the *master* core.

<a id="History"></a>

### History

Multicore support for ERIKA Enterprise started in year 2001, with a prototype dual-core ARM7 developed by Parades, Magneti Marelli and ST Microelectronics, named *Janus*. This version was completed in september 2002, but has never been available to the public (the chip never went in production).

In 2005, the multicore support has been ported to the [Altera Nios II](Altera_Nios_II--1473.md "Altera Nios II") softcore. The basic features of Janus were retained, plus a set of other features such as:

- RT-Druid support for code generation through OIL
- support for up to 32 cores
- cache disabling
- customized multicore interrupts and queuing spin-locks

In 2011, the multicore support has been ported to the [PPC e200](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)") microcontroller family, namely the MPC5668 Fado.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=ERIKA_multicore_support) · [Archived source revision 3254](http://erika.tuxfamily.org/wiki/index.php?oldid=3254)
- Last source edit: 2011-09-19T14:36:04Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Dibbe, Paolo.gai.
- [Original MediaWiki source](../source/wikitext/2066.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
