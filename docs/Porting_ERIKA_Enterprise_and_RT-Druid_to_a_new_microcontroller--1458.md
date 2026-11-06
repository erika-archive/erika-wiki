# Porting ERIKA Enterprise and RT-Druid to a new microcontroller

This is a set of wiki page where we documented the effort of porting ERIKA Enterprise to a new microcontroller. The idea is that this documentation will be useful to anyone willing to port the ERIKA Enterprise kernel to a new microcontroller.

<a id="How_to"></a>

### How to

The work is composed by a set of steps. Each step has a separate wiki page, to document each phase.
These sample pages refer to the Erika Enterprise porting on a Freescale HCS12X microcontroller
using the Cosmic compiler CXS12X.

A set of files to speed up the porting to new microcontrollers has been developed since; you can find some documentation in the page [Common files for the HAL](Common_files_for_the_HAL--1530.md "Common files for the HAL"). The files include most of the code required for Monostack, and the resulting architecture of the HAL is simpler than for previously ported architectures. For an example on how to use them, see the [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)") or the [Lattice Mico32](Lattice_Mico32--1632.md "Lattice Mico32") porting; use them as a reference for your new porting.

Note that the pathnames of the files cited in the following pages are the ones used to compile the files.
Some of these files do not have yet an OIL file description.
In order to let them compile and work, you will have to change the pathnames
in the makefile and in the linker scripts.

1. Installing the compiler
2. [Porting ERIKA: writing the makefiles and first compilation](Porting_ERIKA_writing_the_makefiles_and_first_compilation--1459.md "Porting ERIKA: writing the makefiles and first compilation")
3. [MONOSTACK - writing the monostack part of a CPU layer](MONOSTACK_-_writing_the_monostack_part_of_a_CPU_layer--1462.md "MONOSTACK - writing the monostack part of a CPU layer")
   1. [Writing a mono-stack application without interrupts](Writing_a_mono-stack_application_without_interrupts--1460.md "Writing a mono-stack application without interrupts")
   2. [Writing a mono-stack with interrupt not nested](Writing_a_mono-stack_with_interrupt_not_nested--1461.md "Writing a mono-stack with interrupt not nested")
   3. [Writing a mono-stack with nested interrupts](Writing_a_mono-stack_with_nested_interrupts--1470.md "Writing a mono-stack with nested interrupts")
   4. [Implementing TerminateTask](Implementing_TerminateTask--1471.md "Implementing TerminateTask")
4. [MULTISTACK - writing the multistack part of a CPU layer](MULTISTACK_-_writing_the_multistack_part_of_a_CPU_layer--1463.md "MULTISTACK - writing the multistack part of a CPU layer")
   1. [Writing a multi-stack application that runs on a single stack](Writing_a_multi-stack_application_that_runs_on_a_single_stack--1522.md "Writing a multi-stack application that runs on a single stack")
   2. [Writing a multi-stack application that runs on multiple stacks](Writing_a_multi-stack_application_that_runs_on_multiple_stacks--1523.md "Writing a multi-stack application that runs on multiple stacks")
   3. [Writing a multi-stack application that runs on multiple stacks with interrupt not nested](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_interrupt_not_nested--1524.md "Writing a multi-stack application that runs on multiple stacks with interrupt not nested")
   4. [Writing a multi-stack application that runs on multiple stacks with nested interrupts](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_nested_interrupts--1525.md "Writing a multi-stack application that runs on multiple stacks with nested interrupts")
   5. [Writing a multi-stack application that runs on multiple stacks with nested interrupts and separate interrupt stacks](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_nested_interrupts_and_--1526.md "Writing a multi-stack application that runs on multiple stacks with nested interrupts and separate interrupt stacks")
   6. [Writing a multi-stack application that runs on multiple stacks with semaphores](Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_semaphores--1527.md "Writing a multi-stack application that runs on multiple stacks with semaphores")
5. [Running the MODISTARC regression tests](Running_the_MODISTARC_regression_tests--1529.md "Running the MODISTARC regression tests")

<a id="See_also"></a>

### See also

- [RT-Druid configuration](RT-Druid_configuration--2158.md "RT-Druid configuration") - instructions to configure RT-Druid to work with an external repository
- [Common files for the HAL](Common_files_for_the_HAL--1530.md "Common files for the HAL")
- [Erika Makefiles](Erika_Makefiles--1601.md "Erika Makefiles")
- Pages in the category [ERIKA internals](../categories/Category_ERIKA_internals--2129.md "Category:ERIKA internals")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Porting_ERIKA_Enterprise_and_RT-Druid_to_a_new_microcontroller) · [Archived source revision 5945](http://erika.tuxfamily.org/wiki/index.php?oldid=5945)
- Last source edit: 2014-12-10T15:16:01Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, Erikadds, Dibbe, Pj.
- [Original MediaWiki source](../source/wikitext/1458.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
