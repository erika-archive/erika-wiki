# QP framework

<a id="Introduction"></a>

## Introduction

This tutorial describes how to use the **QP** framework with **ERIKA Enterprise** to develop real-time embedded applications.

**QP** (Quantum Platform) is a family of software frameworks that can be utilized to develop embedded applications based on the [event-driven](http://en.wikipedia.org/wiki/Event-driven_programming|) [active objects](http://en.wikipedia.org/wiki/Actor_model|) programming model. **QP** supports manual coding of [active objects](http://en.wikipedia.org/wiki/Actor_model) through [UML state machines](http://en.wikipedia.org/wiki/UML_state_machine) in [C (programming language)](http://en.wikipedia.org/wiki/C_(programming_language)) or [C++](http://en.wikipedia.org/wiki/C%2B%2B) as well as fully automatic code generation by means of the graphical modeling tool [**QM**.](http://www.state-machine.com/qm)

**ERIKA Enterprise** is an open-source [OSEK/ VDX](http://www.osek-vdx.org/) Real Time Operating System (RTOS). **ERIKA** supports single and multi-processor platforms and provides hard real-time computing through a set of schedulers and resource management mechanisms.

<a id="Prerequisites"></a>

## Prerequisites

We presume that the reader is familiar with **ERIKA Enterprise** and **RT-Druid** and these tools are already installed and working in his/her machine. The application examples described below have been developed for the following hardware platform: [STM32F4xx](http://www.st.com/internet/mcu/subclass/1521.jsp) (Cortex M4) architecture and the [STM32F407 Discovery Board](http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/PF252419). Further information regarding the support of **ERIKA** for this platform can be retrieved at this link: [http://erika.tuxfamily.org/wiki/index.php?title=ARM\_Cortex\_MX](ARM_Cortex_MX--2226.md). It is also assumed that the reader has already installed the tools needed to compile and run the demo applications, as explained in the following tutorial: [STM32-Integrated Debugging in Eclipse using GNU toolchain](Tutorial_STM32_-_Integrated_Debugging_in_Eclipse_using_GNU_toolchain--2459.md). Note that, to get ready to work with **ERIKA** a virtual machine with all the necessary tools already installed is available at this link: <http://www.erika-enterprise.com/#VM>.

<a id="Porting_to_ERIKA_Enterprise"></a>

## Porting to ERIKA Enterprise

The porting has been developed following the indications contained in the Samek's book: [Practical UML Statecharts in C/C++, Second Edition: Event-Driven Programming for Embedded Systems](http://www.state-machine.com/psicc2/index.php).

The source files of the **QP** framework are located in the `contrib` directory inside the **ERIKA** source tree. Currently, the supported version of the framework is the 5.2.1: <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/qpc_v521/>. The source files mainly involved in the porting are `qf_ports.c`, located in <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/qpc_v521/src/ports/erika/>, and  `qf_ports.h` located in <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/contrib/qpc_v521/inc/ports/erika/>.

The main technical choices taken during the development of the porting, along with possible alternative solutions, are summarized in the following.

- Each active object runs in a separate **ERIKA** task.
- The native type `QEQueue` is used to implement the event queue for active objects. `QEQueue` is provided by the **QP** framework. An alternative solution could be to use the communication mechanisms provided by the **OSEK COM** layer available with **ERIKA**.
- Critical sections are protected by unconditionally disabling and enabling the processor interrupts through the following **ERIKA** routines: `DisableAllInterrupts()` and  `EnableAllInterrupts()`. An alternative solution could be to use the **Resource** mechanism provided by **ERIKA**. **Resources** are binary semaphores handled by the [Immediate Priority Ceiling](http://en.wikipedia.org/wiki/Priority_ceiling_protocol) protocol.
- The blocking mechanism for event queues is implemented through an **Event** variable. **Events** is a technique provided by **ERIKA** to implement synchronization mechanisms.

<a id="Demo_applications"></a>

## Demo applications

A set of demo examples, derived from those already available in the **QP** framework, have been developed to show how to create applications with **ERIKA** and **QP**. These demos can be found in the `examples` folder in the **ERIKA** repository: <http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/STM32F4xx/>. The sub-folders containing the demos are: `STM32_qpc_blinky`, `STM32_qpc_dpp`, `STM32_qpc_lcd` and `STM32_qpc_dpp_usart`.

The demo contained in `STM32_qpc_blinky` implements a state machine that blinks the leds on the STM32F407 Discovery board. The demo in `STM32_qpc_dpp` implements the [Dining Philosophers Problem](http://www.state-machine.com/resources/AN_DPP.pdf) (**DPP**) example using six concurrent active objects. The behavior of each object is implemented through a state machine. The demo can be paused and resumed by pressing the user button available on the STM32F407 Discovery board. The blue led of the board is turned on to indicate that a philosopher is eating and off otherwise. When the demo is paused the red led is turned on.

`STM32_qpc_lcd` and `STM32_qpc_dpp_usart` implement the same **DPP** example using respectively the LCD and the USART port to display information on the demo state, i.e paused or running, and the philosophers's state, i.e. eating, hungry or thinking.

The demo examples are composed by a set of source files. The following group of files are only related to the **QP** framework, that is, they do not depend neither on the underlying kernel nor on the hardware platform.

- `main.c` contains the instructions to create active objects and to set and start the **QP** framework and its data structures, e.g. active object event queues and pools.
- One or more source files that encode the active objects behaviour. For instance, the behaviour of the active objects of the **DPP** demo is defined in a couple of source files: `philo.c` and `table.c`

Other than the files listed above, which are independent both from the kernel and from the hardware, each demo contains two or more files whose code depends both on the kernel and on the hardware platform:

- `conf.oil` is used to configure **ERIKA** objects, such as tasks, resources, alarms etc.. The configuration is specified in **OIL** [(OSEK Implementation Language)](Tutorial_RT-Druid_and_OIL_basics--1658.md) language.
- `bsp.c` contains the source code concerning the hardware platform, interrupt service routines (ISRs), **ERIKA** tasks and the functions of the **QP** framework that must be defined by the application developer.

For instance, in the **DPP** example the `conf.oil` file is structured as follows. The first part below defines:

- (6, 7) the CPU model: Cortex M4;
- (8), (9), (10), (11) the list of application source files;
- (14) the compiler (GNU, i.e. gcc);
- (16), (17), (18), (19), (20) the use of the multi-stack support with the definition of the size of the stack for ISRs (Interrupt Service Routines);
- (23) the use of the system tick;
- (25), (26), (27) the microcontroller model: STM32F4xx.

```
/*Uncomment the following EE_OPTs when using KEIL*/
//EE_OPT = "__KEIL_USE_AXF_EXT__";
//EE_OPT = "__MICROLIB";
        
(6) CPU_DATA = CORTEX_MX {
(7)    MODEL = M4;
(8)    APP_SRC = "main.c";
(9)    APP_SRC = "bsp.c";
(10)    APP_SRC = "philo.c";
(11)    APP_SRC = "table.c";
(12)    
(13)    //COMPILER_TYPE = KEIL;
(14)    COMPILER_TYPE = GNU;
(15)            
(16)    MULTI_STACK = TRUE {
(17)        IRQ_STACK = TRUE {
(18)            SYS_SIZE=512;
(19)        };
(20)    };
(21) };
(22)
(23) EE_OPT = "__USE_SYSTICK__";
(24)        
(25) MCU_DATA = STM32 {
(26)     MODEL = STM32F4xx;
(27) };
```

The following lines of code define:

- (3), (4) the use of the **QP** framework (version 5.2.1);
- from (6) to (22) the use of the drivers that handle some of the microcontroller's peripherals (e.g GPIO) and some of the board's devices (buttons and leds);
- from (25) to (35) some configurations for the kernel. In particular, at line (35), the attribute KERNEL\_TYPE is set to ECC2. Since application tasks must use an **Event** variable when the application is developed using the **QP** framework, kernel type ECC2 is a mandatory setting, see below for further details.

```
(1) EE_OPT = "__ADD_LIBS__";
(2)         
(3) LIB = ENABLE { NAME = "QPC_V521"; };
(4) EE_OPT = "__LIB_QPC_V521__";
(5)         
(6) LIB = ENABLE { NAME = "ST_CMSIS"; };
(7)         
(8) LIB = ENABLE { NAME = "STM32F4XX_SPD"; 
(9)     STM32F4XX_SPD = ENABLE {
(10)        USEGPIO = TRUE;
(11)         USEEXTI = TRUE;
(12)         USESYSCFG = TRUE; 
(13)         USEMISC = TRUE;
(14)         };
(15)     };
(16)         
(17) LIB = ENABLE { NAME = "STM32F4_DISCOVERY";
(18)     STM32F4_DISCOVERY = ENABLE {
(19)     USELEDS = TRUE;
(20)     USEBUTTONS = TRUE;
(21)     };
(22) };
(23)         
(24)         
(25) STATUS = EXTENDED;
(26) STARTUPHOOK = FALSE; 
(27) ERRORHOOK = FALSE;
(28) SHUTDOWNHOOK = FALSE;
(29) PRETASKHOOK = FALSE;
(30) POSTTASKHOOK = FALSE;
(31) USEGETSERVICEID = FALSE;
(32) USEPARAMETERACCESS = FALSE;
(33) USERESSCHEDULER = TRUE;
(34) 
(35) KERNEL_TYPE = ECC2;
        
```

The following configuration code, from line 1 to line 65, defines the application tasks. Note that, each task defines its private stack, all tasks are activated at the system start up (AUTOSTART = TRUE), namely after that the `StartOS()` function is called, which in turn is called by `QF_run()`, see file `qf_port.c`. The code at line 67 defines the **Event** variable `QFEvent`, which is used for the blocking mechanism of **QP** event queues. The code from line 69 to line 73 enables the system tick interrupt and defines the related ISR.

```
    
(1) TASK Philo0Task {
(2)     PRIORITY = 0x01;
(3)     AUTOSTART = TRUE; { /* NOTE: AUTOSTART should be always TRUE*/}
(4)    STACK = PRIVATE {
(5)     SYS_SIZE = 512;
(6)     };
(7)     ACTIVATION = 1;    /* only one pending activation */
(8)     SCHEDULE = FULL;
(9)     EVENT = QFEvent;
(10) };
(11)
(12) TASK Philo1Task {
(13)     PRIORITY = 0x02;
(14)     AUTOSTART = TRUE;  /* NOTE: AUTOSTART should be always TRUE*/
(15)     STACK = PRIVATE {
(16)         SYS_SIZE = 512;
(17)     };
(18)     ACTIVATION = 1;    /* only one pending activation */
(19)     SCHEDULE = FULL;
(20)     EVENT = QFEvent;
(21) };
(22)     
(23) TASK Philo2Task {
(24)     PRIORITY = 0x03;
(25)     AUTOSTART = TRUE;  /* NOTE: AUTOSTART should be always TRUE*/
(26)     STACK = PRIVATE {
(27)         SYS_SIZE = 512;
(28)     };
(29)     ACTIVATION = 1;    /* only one pending activation */
(30)     SCHEDULE = FULL;
(31)     EVENT = QFEvent;
(32) };
(33) 
(34) TASK Philo3Task {
(35)    PRIORITY = 0x04;
(36)     AUTOSTART = TRUE;  /* NOTE: AUTOSTART should be always TRUE*/
(37)     STACK = PRIVATE {
(38)         SYS_SIZE = 512;
(39)     };
(40)     ACTIVATION = 1;    /* only one pending activation */
(41)     SCHEDULE = FULL;
(42)     EVENT = QFEvent;
(43) };
(44)     
(45) TASK Philo4Task {
(46)     PRIORITY = 0x05;
(47)     AUTOSTART = TRUE;  /* NOTE: AUTOSTART should be always TRUE*/
(48)     STACK = PRIVATE {
(49)         SYS_SIZE = 512;
(50)     };
(51)     ACTIVATION = 1;    /* only one pending activation */
(52)     SCHEDULE = FULL;
(53)     EVENT = QFEvent;
(54) };
(55)     
(56) TASK TableTask {
(57)     PRIORITY = 0x06;
(58)     AUTOSTART = TRUE;  /* NOTE: AUTOSTART should be always TRUE*/
(59)     STACK = PRIVATE {
(60)         SYS_SIZE = 512;
(61)     };
(62)     ACTIVATION = 1;    /* only one pending activation */
(63)     SCHEDULE = FULL;
(64)     EVENT = QFEvent;
(65) };
(66)     
(67) EVENT QFEvent { MASK = AUTO; };
(68)     
(69) ISR systick_handler {
(70)     CATEGORY = 2;
(71)     ENTRY = "SYSTICK";
(72)     PRIORITY = 1;
(73) };
```

As far as the **OIL** configuration file is concerned, any application developed with **QP** and **ERIKA** must observe the following rules:

- For each **QP** active object a corresponding **ERIKA** task must be created. The task must have the priority attribute (PRIORITY) equal to the active object priority.
- Each task must declare `QFEvent` through its event attribute (EVENT = QFEvent).
- Each task must use a private stack.
- Each task must set its AUTOSTART attribute equal to TRUE.
- All tasks must be extended tasks, hence, KERNEL\_TYPE attribute must be set to Extended Conformance Class 2 (ECC2).

It is worth noting that, it is not necessary that the name of a task corresponds to the name of the related active object. The only requirement is that for each active object it must exist at least a task with the same priority number, and the number of tasks must match the number of active objects.

For further information on how to create **OIL** configuration files see the [RT-Druid Reference Manual](../assets/linked/rtdruid_refman_1_5.0--f652278e8166b38c.pdf).

The body of each task must be defined in one of the application source files. In the demo examples available with **ERIKA** the task bodies are defined in the file `bsp.c`. All tasks are coded using the same scheme as it follows:

```
TASK(TaskName)
{

    task_function(pdata[TaskName]);
    
    TerminateTask();
}
```

Each task has to call the `task_function()` routine and passing as argument the element of the array `pdata` indexed by the task name, namely `TaskName`. `task_function()` is defined in `qf_port.c` and `pdata` is an array where each element is a data structure that defines the associated active object. Notice that, when `task_function()` is called it executes the code of the active object associated with task `TaskName`. Each task must be terminated by a call to `TerminateTask()`. Note that, as long as the application is running, a call to `task_function()` never ends. For this reason each task must have a private stack.

Other than task bodies, file `bsp.c` provides the following **QP** functions that must be defined by the application developer:

- `QF_onStartup()`,
- `QF_onCleanup()`,
- `Q_onAssert()`,
- `QF_onIdle()`.

Some other functions concerning to the tracing tool [**QP Spy**](http://www.state-machine.com/qp/qspy/) are also defined in `bsp.c`.

<a id="QP_Modeler"></a>

## QP Modeler

[**QM**](http://www.state-machine.com/qm/) is a graphical modeling tool for the development of embedded applications based on the **QP** framework. It is freeware and usable to to develop real-time embedded applications using **UML** state machines and **ERIKA** Enterprise.

We suggest the following steps be used in creating your application through **QM**.

1. Design a graphical model of the application using **QM**.
2. Generate the source code from the graphical model using **QM**.
3. Handwrite file `bsp.c` with the code needed to handle the hardware, to define the **QP** functions that must be coded by the application developer, and to define tasks and other **ERIKA** related stuffs, such as ISRs. Of course, instead of just creating `bsp.c` the source code can be divided into more files.
4. Handwrite the **ERIKA** configuration file, usually named `conf.oil`.

For instance, taking as an example the **DPP** demo, inside the folder there is a file named `dpp.qm`. This file contains the graphical model of the demo. By opening `dpp.qm` with **QM** it is possible both to see the graphical model and to generate the relative source code. **QM** generates four files: `main.c`, `philo.c`, `table.c` and `dpp.h`. Note that, these files contain the code only related to the **QP** framework and independent from both **ERIKA** and from the hardware platform. As already stated above, the source files that depend on the kernel and on the hardware, that is `bsp.c` and `conf.oil`, must be handwritten by the application developer.

Note that, to work with the version 5.2.1 of the **QP** framework the developer must use the version 3.0.0 of **QM**. Otherwise, **QM** can generate a source code inconsistent with the version of **QP** currently supported by **ERIKA**.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=QP_framework) · [Archived source revision 5777](http://erika.tuxfamily.org/wiki/index.php?oldid=5777)
- Last source edit: 2014-09-01T16:47:31Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Gfranchi.
- [Original MediaWiki source](../source/wikitext/2480.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
