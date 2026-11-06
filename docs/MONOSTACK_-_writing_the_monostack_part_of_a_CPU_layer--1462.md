# MONOSTACK - writing the monostack part of a CPU layer

The Monostack configuration of the ERIKA Kernel models the fact that all tasks and ISRs in the system share the same stack.

This stack configuration can only be used when the scheduling algorithm implemented by the kernel insures that there is not an interleaving among the various tasks in the system.

That is, the kernel must guarantee that there are no blocking primitives implemented in the system. OSEK/VDX Immediate Priority Ceiling Protocol guarantees that property.

The Monostack configuration has some nice properties, in particular due to the fact that, in the FP, EDF, and FRSH kernels, there is no need to save registers when a context switch happens because a task called a primitive.

Most the code required for Monostack is probably already available in among the [Common files for the HAL](Common_files_for_the_HAL--1530.md "Common files for the HAL"). See the [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)") or the [Lattice Mico32](Lattice_Mico32--1632.md "Lattice Mico32") porting for examples on how to use them.

1. [Writing a mono-stack application without interrupts](Writing_a_mono-stack_application_without_interrupts--1460.md "Writing a mono-stack application without interrupts")
2. [Writing a mono-stack with interrupt not nested](Writing_a_mono-stack_with_interrupt_not_nested--1461.md "Writing a mono-stack with interrupt not nested")
3. [Writing a mono-stack with nested interrupts](Writing_a_mono-stack_with_nested_interrupts--1470.md "Writing a mono-stack with nested interrupts")
4. [Implementing TerminateTask](Implementing_TerminateTask--1471.md "Implementing TerminateTask")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=MONOSTACK_-_writing_the_monostack_part_of_a_CPU_layer) · [Archived source revision 3126](http://erika.tuxfamily.org/wiki/index.php?oldid=3126)
- Last source edit: 2011-06-08T08:42:23Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Paolo.gai, Dibbe, AnnaSharp.
- [Original MediaWiki source](../source/wikitext/1462.mediawiki) · [Original editing history](../source/history/batch-007.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
