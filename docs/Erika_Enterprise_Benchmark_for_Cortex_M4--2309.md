# Erika Enterprise Benchmark for Cortex M4

<a id="Benchmark_Purpose"></a>

## Benchmark Purpose

The purpose of this benchmark is to provide a measure of the performance of Erika Enterprise
with the following kernel mechanisms:

- ISR1 latency: the time elapsed from the activation of an Interrupt Service Routine of type 1 (ISR1), to the first ISR instruction.
- ISR1 exit: the time elapsed from the last instruction of an ISR1 to the subsequent instruction of the interrupted task.
- ISR2 latency: the time elapsed from the activation of an Interrupt Service Routine of type 2 (ISR2), to the first ISR2 instruction.
- ISR2 exit: the time elapsed from the last instruction of an ISR2 to the subsequent instruction of the interrupted task.
- New task from an ISR2: the time elapsed from the last instruction of an ISR2 to the first instruction of the new task.
- New task with preemption: the time elapsed from the first instruction necessary to active a new task to the first instruction of the new task.
- New task without preemption: the time elapsed from the first instruction necessary to active a new task to the last instruction necessary to active the new task.
- Terminate task (not activated from an ISR): the time elapsed from the last task instruction to the next instruction of the task preempted by the task just terminated.
- Terminate task (activated from an ISR): the time elapsed from the last task instruction to the next instruction of the task preempted by the task just terminated.

<a id="Benchmark_Location"></a>

## Benchmark Location

The benchmark project is located in [examples/cortex\_mx/lm4f232xxxx/benchmark/](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/cortex_mx/lm4f232xxxx/benchmark/) folder.

The benchmark project folder is organized as follows:
root directory contains "readme.txt", with all the information you can find in this page, plus the "makefile" and the following subfolders;

- **benchmark**: it contains the source files;
- **output**: it will contain, after the compilation process, all the files of the project.
- **Keil\_Debug\_BM\_Project**: it contains the configuration files for the Keil IDE.
- **results**: it contains the file with the benchmark results (the result of test is alredy commited on repository)

<a id="How_to_Run_the_Benchmark"></a>

## How to Run the Benchmark

Follow the instruction below to compile and run the benchmark:

1. Open the cygwin shell and go in the benchmark directory.
2. If you want to compile and run the benchmark with the target board, type the following two commands:

```
export Debugger=ICDI
make
```

If you want to compile and execute the benchmark with the simulator provided with the Keil IDE, just type the make command.

After the execution of the benchmark, the obtained results are stored in the file
BM\_TI\_Stellaris\_LM4F232H5QD.log. This file can be found in the results folder.

<a id="Bechmark_Results_Table"></a>

## Bechmark Results Table

The result are obtained working with the LM4F232H5QD internal oscillator (clock frequency of 16 MHz). The result are obtained with **SVN revision number 2366** corresponding
to the tag **osek\_ti\_kslm4f232**.

| Test Name | Samples | Mean | Minimun | Maximum |
| --- | --- | --- | --- | --- |
| ISR1 Latency | 50 | 59 ticks (3.687 usec) | 59 ticks (3.687 usec) | 59 ticks (3.687 usec) |
| ISR1 exit | 50 | 48 ticks (3.000 usec) | 48 ticks (3.000 usec) | 48 ticks (3.000 usec) |
| ISR2 Latency | 50 | 104 ticks (6.500 usec) | 104 ticks (6.500 usec) | 104 ticks (6.500 usec) |
| ISR2 Exit | 50 | 138 ticks (8.625 usec) | 138 ticks (8.625 usec) | 138 ticks (8.625 usec) |
| New task from ISR | 50 | 345 ticks (21.562 usec) | 345 ticks (21.562 usec) | 345 ticks (21.562 usec) |
| New task with preemption | 50 | 314 ticks (19.625 usec) | 314 ticks (19.625 usec) | 314 ticks (19.625 usec) |
| New task without preemption | 50 | 164 ticks (10.250 usec) | 164 ticks (10.250 usec) | 164 ticks (10.250 usec) |
| Task (not activated from IRQ) exit | 50 | 275 ticks (17.187 usec) | 275 ticks (17.187 usec) | 275 ticks (17.187 usec) |
| Task (activated from IRQ) exit | 50 | 689 ticks (43.062 usec) | 689 ticks (43.062 usec) | 689 ticks (43.062 usec) |

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Erika_Enterprise_Benchmark_for_Cortex_M4) · [Archived source revision 4795](http://erika.tuxfamily.org/wiki/index.php?oldid=4795)
- Last source edit: 2012-07-09T16:18:58Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Eguidieri, Pj.
- [Original MediaWiki source](../source/wikitext/2309.mediawiki) · [Original editing history](../source/history/batch-004.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
