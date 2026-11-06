# Erika Enterprise vs embOS Benchmark for Cortex M0

<a id="Benchmark_Purpose"></a>

## Benchmark Purpose

The purpose of this benchmark is to provide a measure of the performance of Erika Enterprise
in comparison with embOS provided by Segger. We used the binary version of embOS available on the Segger home page (see below).

The comparison is done for the following kernel mechanisms:

- ISR1 latency: the time elapsed from the activation of an Interrupt Service Routine of type 1 (ISR1), to the first ISR instruction.
- ISR1 exit: the time elapsed from the last instruction of an ISR1 to the subsequent instruction of the interrupted task.
- ISR2 latency: the time elapsed from the activation of an Interrupt Service Routine of type 2 (ISR2), to the first ISR2 instruction.
- ISR2 exit: the time elapsed from the last instruction of an ISR2 to the subsequent instruction of the interrupted task.
- New task from an ISR2: the time elapsed from the last instruction of an ISR2 to the first instruction of the new task.
- New task with preemption: the time elapsed from the first instruction necessary to active a new task to the first instruction of the new task.
- New task without preemption: the time elapsed from the first instruction necessary to active a new task to the last instruction necessary to active the new task.
- Terminate task (not activated from an ISR): the time elapsed from the last task instruction to the next instruction of the task preempted by the task just terminated.
- Terminate task (activated from an ISR): the time elapsed from the last task instruction to the next instruction of the task preempted by the task just terminated.

<a id="Benchmark_Location_for_Erika_Enterprise"></a>

## Benchmark Location for Erika Enterprise

The benchmark project for Erika is located in [examples/cortex\_mx/lpc12xxx/benchmark/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lpc12xx/benchmark/) folder.

The benchmark project folder is organized as follows:
root directory contains "readme.txt", with all the information you can find in this page, plus the "makefile" and the following subfolders;

- **benchmark**: it contains the source files of the benchmark application;
- **output**: it will contain, after the compilation process, all the files of the project.
- **Keil\_Debug\_BM\_Project**: it contains the configuration files for the Keil IDE.
- **results**: it contains the file with the benchmark results (the result of the test is already committed on the SVN repository)

<a id="Benchmark_Location_for_embOS"></a>

## Benchmark Location for embOS

The benchmark project for embOS is located in [examples/cortex\_mx/lpc12xxx/benchmark\_embOS/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lpc12xx/benchmark_embOS/) folder.

The benchmark project folder is organized as follows:
root directory contains "readme.txt", with all the information you can find in this page, plus the "makefile" and the following subfolders;

- **benchmark**: it contains the source files of the benchmark application;
- **output**: it will contain, after the compilation process, all the files of the project.
- **Keil\_Debug\_BM\_Project**: it contains the configuration files for the Keil IDE.
- **results**: it contains the file with the benchmark results (the result of the test is already committed on SVN repository)
- **embOS**: it just contains the folders tree where to put the embOS files.

The readme.txt file contains the instructions on how to get and use all the necessary embOS files to
run the benchmark. Please note that the embOS source code has not been inserted in the ERIKA Enterprise SVN.

<a id="How_to_Run_the_Benchmark"></a>

## How to Run the Benchmark

Follow the instruction below to compile and run the benchmark:

1. Open the cygwin shell and go in the benchmark directory.
2. If you want to compile and execute the benchmark with the simulator provided with the Keil IDE, type the following two commands:

```
export Debugger=Simul
make
```

If you want to compile and run the benchmark with the target board, just type the make command.
If you want to compile and run the benchmark with the target board and get the output from the
UART type the following two commands:

```
export OUTPUT_PORT=uart
make
```

After the execution of the benchmark, the obtained results are stored in the file
BM\_NXP\_LPC1227.log. The instructions above are valid both for Erika and for embOS.

For Erika Enterprise, the folder results already contains BM\_NXP\_LPC1227\_HW.log and BM\_NXP\_LPC1227\_SIM.log.

For embOS, the folder results already contains BM\_NXP\_LPC1227\_ULINK2.log and BM\_NXP\_LPC1227\_Simul.log.

These files report respectively the results obtained with the LPCXpresso board connected to the ULINK2 debugger and with the Keil simulator.

<a id="Bechmark_Results_Table_for_Erika_Enterprise"></a>

## Bechmark Results Table for Erika Enterprise

The results are obtained working with a clock frequency of 24 MHz. The results are obtained with **SVN revision number 2473**.

| Test Name | Samples | Mean | Minimun | Maximum |
| --- | --- | --- | --- | --- |
| ISR1 Latency | 50 | 79 ticks (3.291 usec) | 79 ticks (3.291 usec) | 79 ticks (3.291 usec) |
| ISR1 exit | 50 | 66 ticks (2.750 usec) | 66 ticks (2.750 usec) | 66 ticks (2.750 usec) |
| ISR2 Latency | 50 | 113 ticks (4.708 usec) | 113 ticks (4.708 usec) | 113 ticks (4.708 usec) |
| ISR2 Exit | 50 | 229 ticks (9.541 usec) | 229 ticks (9.541 usec) | 229 ticks (9.541 usec) |
| New task from ISR | 50 | 424 ticks (17.666 usec) | 424 ticks (17.666 usec) | 424 ticks (17.666 usec) |
| New task with preemption | 50 | 361 ticks (15.041 usec) | 361 ticks (15.041 usec) | 361 ticks (15.041 usec) |
| New task without preemption | 50 | 187 ticks (7.791 usec) | 187 ticks (7.791 usec) | 187 ticks (7.791 usec) |
| Task (not activated from IRQ) exit | 50 | 315 ticks (13.125 usec) | 315 ticks (13.125 usec) | 315 ticks (13.125 usec) |
| Task (activated from IRQ) exit | 50 | 798 ticks (33.250 usec) | 798 ticks (33.250 usec) | 798 ticks (33.250 usec) |

<a id="Bechmark_Results_Table_for_embOS"></a>

## Bechmark Results Table for embOS

The results are obtained working with a clock frequency of 24 MHz. The results are obtained with embOS\_CortexM\_Keil\_Trial\_V386e.

| Test Name | Samples | Mean | Minimun | Maximum |
| --- | --- | --- | --- | --- |
| ISR1 Latency | 50 | 79 ticks (3.291 usec) | 79 ticks (3.291 usec) | 79 ticks (3.291 usec) |
| ISR1 exit | 50 | 64 ticks (2.666 usec) | 64 ticks (2.666 usec) | 64 ticks (2.666 usec) |
| ISR2 Latency | 50 | 103 ticks (4.291 usec) | 103 ticks (4.291 usec) | 103 ticks (4.291 usec) |
| ISR2 Exit | 50 | 98 ticks (4.083 usec) | 98 ticks (4.083 usec) | 98 ticks (4.083 usec) |
| New task from ISR | 50 | 311 ticks (12.958 usec) | 311 ticks (12.958 usec) | 311 ticks (12.958 usec) |
| New task with preemption | 50 | 509 ticks (21.208 usec) | 509 ticks (21.208 usec) | 509 ticks (21.208 usec) |
| New task without preemption | 50 | 294 ticks (12.250 usec) | 287 ticks (11.958 usec) | 295 ticks (12.291 usec) |
| Task (not activated from IRQ) exit | 50 | 396 ticks (16.500 usec) | 396 ticks (16.500 usec) | 396 ticks (16.500 usec) |
| Task (activated from IRQ) exit | 50 | 789 ticks (32.875 usec) | 789 ticks (32.875 usec) | 789 ticks (32.875 usec) |

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Erika_Enterprise_vs_embOS_Benchmark_for_Cortex_M0) · [Archived source revision 4874](http://erika.tuxfamily.org/wiki/index.php?oldid=4874)
- Last source edit: 2012-08-01T10:15:59Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Gfranchi, Pj.
- [Original MediaWiki source](../source/wikitext/2339.mediawiki) · [Original editing history](../source/history/batch-004.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
