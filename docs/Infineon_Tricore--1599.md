# Infineon Tricore

<a id="Acknowledgements"></a>

## Acknowledgements

The porting of ERIKA Enterprise for the Infineon Tricore is a contribution developed in the context of the [PREDATOR FP7](http://www.predator-project.eu/) project, and it has been done by Jan C. Kleinsorge from TU Dortmund.

<a id="Requirements"></a>

## Requirements

ERIKA for TriCore currently supports the GCC toolchain provided by HighTec GmbH.
Currently, GCC 3.4.6 as the cross-compiler is tested, which is binary packaged with the PXROS (free of charge for educational purposes). A source distribution exists for GCC 3.3.7. Note however that this compiler version might not compile with GCC 4 or higher and has possible incompatibilities with recent GNU autotools. If possible, obtain 3.4.6.

The compiled binaries can either be run on the simulator tsim which is to be found with the aforementioned binary package, or on a supported evaluation board (see below).

<a id="Supported_devices"></a>

## Supported devices

The current port specifically supports Tricore1, core tc1.3, MCU tc1796b. It encompasses a boilerplate implementation to meet ERIKAs requirements (monostack and multistack).

- Core
  - Support for ISR1-, ISR2- and Trap-handling
  - Direct CSA manipulation

- MCU
  - WDT (locking)
  - PLL (initialization of system clocks and frequency selection)
  - STM (basic timer interrupt support and timing information)

This subset makes the code-base self-contained and allows to apply most configurations. For full support of these and other devices, it is advised to use the device definitions provided by the compiler toolchain. The definitions from HighTec feature the entire range of TriCore1 CPUs and their respective on-chip devices.

<a id="Supported_evaluation_boards"></a>

## Supported evaluation boards

The tested targets are

- TriBoard tc1796b v4.1
- Infineon tsim simulator.

<a id="How_to_compile_and_run_an_application"></a>

## How to compile and run an application

- To compile the demos, prefix the gcc and binutils binaries with 'tricore-' and place the path into the PATH variable. Calling 'make' in the demo folders will build the binaries instantly. Alternatively,

enter the correct path in the variable TRICORE1\_GCCDIR within the demo's makefiles. Note that there is currently no RTDruid support, the demos are hand-crafted.

- To run a demo in the simulator, make sure the flag \_\_TSIM\_\_ is enabled in the demo makefiles. This changes the set of start-up files and prevents the initialization of the system clock circuitry which is not supported (tested on tsim V0.03).

Otherwise, the binary can directly loaded and run.

- Useful links:
  - [http://www.hightec-rt.com](http://www.hightec-rt.com/)

<a id="Examples"></a>

## Examples

At its current state, the port comes with a few example applications

- **demo\_hello** consists of a single (background) task which outputs "Hello, world!" through the debug interface and enters an idle loop.

- **demo\_mono** demonstrates the monostack implementation. It makes use of the OSEK function TerminateTask to demonstrate how tasks can be aborted at aribtrary call depths.

- **demo\_multi**demonstrates the multistack implementation with synchronization primitives. Activation and preemption is performed through Tasks and an ISR.

- **demo\_isr** shows the interrupt-handling capabilities by using OSEK ISR1, ISR2 and trap handlers.

- **demo\_led** implements a simple control of the on-board LEDs on the TriBoard tc1769 4.1 with multiple tasks and a timer ISR.

<a id="Notes_on_the_internal_implementation"></a>

## Notes on the internal implementation

- Although the MCU folder is labelled tc179x, there is specifically only support for tc1796b. It should not be too hard to provide other ports with minor changes.

- EE\_MAX\_ISR allows to define the maximum size of the interrupt vector table. Arbitration cycles are minimized upon initialization depending on this value. This can be used to reduce the memory footprint.

- A new type 'EE\_STACK' was introduced due to TriCore's stack alignment requirements (double word).

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Infineon_Tricore) · [Archived source revision 2971](http://erika.tuxfamily.org/wiki/index.php?oldid=2971)
- Last source edit: 2011-04-07T08:59:24Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Pj, Jck, WikiSysop.
- [Original MediaWiki source](../source/wikitext/1599.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
