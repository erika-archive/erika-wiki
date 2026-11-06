# MULTISTACK - writing the multistack part of a CPU layer

In the Multistack HAL every thread can have its private stack, or it can share it with other threads.
This allows the Kernel Layer to use scheduling algorithms that could block threads in synchronization
primitives (as for example, a fixed priority scheduler with semaphores) or for arbitrary reasons
(as, for example, a classical round robin scheduler).

Some code required for Multistack is already available in among the [Common files for the HAL](Common_files_for_the_HAL--1530.md "Common files for the HAL"). This is used for example in the [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)") or the [Lattice Mico32](Lattice_Mico32--1632.md "Lattice Mico32") porting. Those architectures feature a HAL that is easier to write than older ports, so you are encouraged to take those ports as a reference to develop your new port.

The following steps explain how to write the MULTISTACK part of a CPU layer.

1. [Writing a multi-stack application that runs on a single stack](Writing_a_multi-stack_application_that_runs_on_a_single_stack--1522.md "Writing a multi-stack application that runs on a single stack")
2. [Writing a multi-stack application that runs on multiple stacks](Writing_a_multi-stack_application_that_runs_on_multiple_stacks--1523.md "Writing a multi-stack application that runs on multiple stacks")
3. [Writing a multi-stack application that runs on multiple stacks with interrupt not nested](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_interrupt_not_nested--1524.md "Writing a multi-stack application that runs on multiple stacks with interrupt not nested")
4. [Writing a multi-stack application that runs on multiple stacks with nested interrupts](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_nested_interrupts--1525.md "Writing a multi-stack application that runs on multiple stacks with nested interrupts")
5. [Writing a multi-stack application that runs on multiple stacks with nested interrupts and separate interrupt stacks](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_nested_interrupts_and_--1526.md "Writing a multi-stack application that runs on multiple stacks with nested interrupts and separate interrupt stacks")
6. [Writing a multi-stack application that runs on multiple stacks with semaphores](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_semaphores--1527.md "Writing a multi-stack application that runs on multiple stacks with semaphores")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=MULTISTACK_-_writing_the_multistack_part_of_a_CPU_layer) · [Archived source revision 3127](http://erika.tuxfamily.org/wiki/index.php?oldid=3127)
- Last source edit: 2011-06-08T08:42:44Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Dibbe.
- [Original MediaWiki source](../source/wikitext/1463.mediawiki) · [Original editing history](../source/history/batch-007.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
